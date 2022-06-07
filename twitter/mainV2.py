import requests
import io
import tokeniza as tk
import os
import time 
from utils.utils import bearer_token

QUIT  = '2'

def getRequest(query, option, url):
            headers = {'Authorization': 'Bearer ' + bearer_token}
            response = requests.get(url, headers=headers)
            dados = response.json()

            print(dados)
            
            tweetsWoTreated = ''
            tweetsTreated = ''
            nameOption = 'coronaVirus' if query == '' or option == 1 else query

            def existLocation():
                location = None
                for user in dados['includes']['users']:
                        if user['id'] == dado['author_id'] and 'location' in user:
                            location = user['location'] 
                            return location
            
            if (dados['meta']['result_count']) > 0:
                index = 0
                if not os.path.exists('./{}Tweets/{}.csv'.format(nameOption, nameOption)):
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
                        tweetsTreated += tk.tokeniza(existLocation()) + ';'
                    tweetsTreated += dado['source'] + ';' + '\n'
                    index += 1
                    
                dir = './{}Tweets'.format('coronaVirus' if query == '' else query)  
                if not os.path.isdir(dir):
                    os.mkdir(dir)

                f = open('./{}Tweets/{}.csv'.format(nameOption, nameOption), 'a')
                with io.open('./{}Tweets/{}.csv'.format(nameOption, nameOption), 'a', encoding='utf-8') as f:
                    f.write(tweetsTreated)

                f = open('./{}Tweets/{}WoTreatment.txt'.format(nameOption, nameOption), 'a')
                with io.open('./{}Tweets/{}WoTreatment.txt'.format(nameOption, nameOption), 'a', encoding='utf-8') as f:
                    f.write(tweetsWoTreated)
            else:
                print('\nNenhum tweet com esse tema foi encontrado!\n')

def main():
    option = 0
    query = ''
    while option != QUIT:
        option = int(input('>>> Selecione uma opção \n 1 - Pesquisar por variações de corona virus \n 2 - Sair \n'))
        if option == 1:
            variacoesCovid = open('./utils/corona-search.txt', 'r', encoding='utf-8')
            for variacao in variacoesCovid:
                url = 'https://api.twitter.com/2/tweets/search/recent?query=("{}") -is:retweet lang:pt&max_results=100&tweet.fields=author_id,created_at,geo,id,source&user.fields=id,location&expansions=author_id,geo.place_id'.format(variacao)
                print(url)
                getRequest(query, option, url)
                time.sleep(60)
        elif option == 2:
            break
        else:
            print("\nOpção inválida, por favor selecione uma opção válida!")
        
        

main()