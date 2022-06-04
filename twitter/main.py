import requests
import io
import tokeniza as tk
import os
from utils.utils import bearer_token

QUIT  = '3'

def main():
    option = 0
    query = ''
    while option != QUIT:
        option = int(input('>>> Selecione uma opção \n 1 - Buscar por \"Corona Virus\" com limite máximo de 100 tweets:  \n 2 - Buscar passando parâmetros: \n 3 - Sair \n'))
        if option == 1:
            url = 'https://api.twitter.com/2/tweets/search/recent?query=("Corona Virus") -is:retweet lang:pt&max_results=100&tweet.fields=author_id,created_at,geo,id,source&user.fields=id,location&expansions=author_id,geo.place_id'
        elif option == 2:
            query = input('>>> Buscar no twitter por: ')
            qtdTweets = int(input('>>> Quantidade máxima de tweets (máxima 100 e mínimo de 10): '))
            if qtdTweets > 100 or qtdTweets < 10:
                print('\nDigite um valor entre 10 e 100!\n')
                continue
            url = 'https://api.twitter.com/2/tweets/search/recent?query=("{}") -is:retweet lang:pt&max_results={}&place.fields=&tweet.fields=author_id,created_at,geo,id,source&user.fields=id,location&expansions=author_id,geo.place_id'.format(query, qtdTweets)
        elif option == 3:
            break
        else:
            print("\nOpção inválida, por favor selecione uma opção válida!")
        
        headers = {'Authorization': 'Bearer ' + bearer_token}
        response = requests.get(url, headers=headers)
        dados = response.json()
        
        tweetsWoTreated = ''
        tweetsTreated = ''

        def existLocation():
            location = None
            for user in dados['includes']['users']:
                    if user['id'] == dado['author_id'] and 'location' in user:
                        location = user['location'] 
                        return location

        
        if (dados['meta']['result_count']) > 0:
            index = 0
            header = 'Tweet;Date;Location;Source;' + '\n'
            tweetsTreated += header
            for dado in dados['data']:
                tweetsWoTreated += str(dado['text']) + '\n'
                tweetsTreated += tk.tokeniza(str(dado['text'])) + ';'
                tweetsTreated += dado['created_at'] + ';'
                location = existLocation()
                if location == None:
                    tweetsTreated += 'LOCALIZACAO NAO INFORMADA' + ';'
                else:
                    tweetsTreated += existLocation() + ';'
                tweetsTreated += dado['source'] + ';' + '\n'
                index += 1
                

            
            dir = './{}Tweets'.format('coronaVirus' if query == '' else query)  
            if not os.path.isdir(dir):
                os.mkdir(dir)

            nameOption = 'coronaVirus' if query == '' else query

            f = open('./{}Tweets/{}.csv'.format(nameOption, nameOption), 'w')
            with io.open('./{}Tweets/{}.csv'.format(nameOption, nameOption), 'w', encoding='utf-8') as f:
                f.write(tweetsTreated)

            f = open('./{}Tweets/{}WoTreatment.txt'.format(nameOption, nameOption), 'w')
            with io.open('./{}Tweets/{}WoTreatment.txt'.format(nameOption, nameOption), 'w', encoding='utf-8') as f:
                f.write(tweetsWoTreated)
        else:
            print('\nNenhum tweet com esse tema foi encontrado!\n')
    

main()