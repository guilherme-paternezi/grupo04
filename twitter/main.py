import requests
import io
def main():
    
    url = 'https://api.twitter.com/2/tweets/search/recent?query=("CoronaVirus") -is:retweet lang:pt&max_results=100&tweet.fields=author_id&expansions=author_id'
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAAD2qcwEAAAAAqlZiIVJif5pZ9y0pVvVzVVvewXs%3DkFaTRG4M3rNNdrj5Uim979KKOtJRyhFZofDtJXgIZKm31sJ70j'
    headers = {'Authorization': 'Bearer ' + bearer_token}
    response = requests.get(url, headers=headers)
    dados = response.json()
    saida = ""
    for dado in dados["data"]:
        saida += str(dado["text"]) + "\n"

    f = open("./tweets.txt", "w")
    with io.open("tweets.txt", "w", encoding="utf-8") as f:
        f.write(saida)

main()