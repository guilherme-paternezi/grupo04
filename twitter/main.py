import requests
import io
import tokeniza as tk

QUIT  = '3'

def main():
    opcao = 0
    while opcao != QUIT:
        opcao = int(input('>>> Selecione uma opção \n 1 - Buscar por \"Corona Virus\" com limite máximo de 100 tweets:  \n 2 - Buscar passando parâmetros: \n 3 - Sair \n'))
        if opcao == 1:
            url = 'https://api.twitter.com/2/tweets/search/recent?query=("Corona Virus") -is:retweet lang:pt&max_results=100&tweet.fields=author_id&expansions=author_id'
        elif opcao == 2:
            query = input('>>> Buscar no twitter por: ')
            qtdTweets = input('>>> Máxima quantidade de tweets: ')
            url = 'https://api.twitter.com/2/tweets/search/recent?query=("{}") -is:retweet lang:pt&max_results={}&tweet.fields=author_id&expansions=author_id'.format(query, qtdTweets)
        elif opcao == 3:
            break
        else:
            print("\nOpção inválida, por favor selecione uma opção válida!")
        
        bearer_token = 'AAAAAAAAAAAAAAAAAAAAAD2qcwEAAAAAqlZiIVJif5pZ9y0pVvVzVVvewXs%3DkFaTRG4M3rNNdrj5Uim979KKOtJRyhFZofDtJXgIZKm31sJ70j'
        headers = {'Authorization': 'Bearer ' + bearer_token}
        response = requests.get(url, headers=headers)
        dados = response.json()
        
        tweetsTratados = ""
        for dado in dados["data"]:
            tweetsTratados += str(dado["text"]) + "\n"
            # tweetsTratados += tk.tokeniza(str(dado["text"])) + "\n"

        f = open("./tweets.txt", "w")
        with io.open("tweets.txt", "w", encoding="utf-8") as f:
            f.write(tweetsTratados)
    

main()