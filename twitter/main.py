import requests
import io
import tokeniza as tk

QUIT  = '3'

def main():
    option = 0
    query = ''
    while option != QUIT:
        option = int(input('>>> Selecione uma opção \n 1 - Buscar por \"Corona Virus\" com limite máximo de 100 tweets:  \n 2 - Buscar passando parâmetros: \n 3 - Sair \n'))
        if option == 1:
            url = 'https://api.twitter.com/2/tweets/search/recent?query=("Corona Virus") -is:retweet lang:pt&max_results=100&tweet.fields=author_id&expansions=author_id'
        elif option == 2:
            query = input('>>> Buscar no twitter por: ')
            qtdTweets = int(input('>>> Quantidade máxima de tweets (máxima 100): '))
            if qtdTweets > 100 or qtdTweets < 1:
                print('\nDigite um valor entre 1 e 100!\n')
                continue
            url = 'https://api.twitter.com/2/tweets/search/recent?query=("{}") -is:retweet lang:pt&max_results={}&tweet.fields=author_id&expansions=author_id'.format(query, qtdTweets)
        elif option == 3:
            break
        else:
            print("\nOpção inválida, por favor selecione uma opção válida!")
        
        bearer_token = 'AAAAAAAAAAAAAAAAAAAAAD2qcwEAAAAAqlZiIVJif5pZ9y0pVvVzVVvewXs%3DkFaTRG4M3rNNdrj5Uim979KKOtJRyhFZofDtJXgIZKm31sJ70j'
        headers = {'Authorization': 'Bearer ' + bearer_token}
        response = requests.get(url, headers=headers)
        dados = response.json()
        
        tweetsWoTreated = ''
        tweetsTreated = ''

        if (dados['meta']['result_count']) > 0:
            for dado in dados['data']:
                tweetsWoTreated += str(dado['text']) + '\n'
                tweetsTreated += tk.tokeniza(str(dado['text'])) + '\n'

            f = open('./tweets/{}.txt'.format('coronaVirus' if query == '' else query), 'w')
            with io.open('{}.txt'.format('coronaVirus' if query == '' else query), 'w', encoding='utf-8') as f:
                f.write(tweetsTreated)

            f = open('./tweets/{}WoTreatment.txt'.format('coronaVirus' if query == '' else query), 'w')
            with io.open('{}WoTreatment.txt'.format('coronaVirus' if query == '' else query), 'w', encoding='utf-8') as f:
                f.write(tweetsWoTreated)
        else:
            print('\nNenhum tweet com esse tema foi encontrado!\n')
    

main()