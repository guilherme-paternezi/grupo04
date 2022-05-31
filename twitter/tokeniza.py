from utils.utils import stop_words

def tokeniza(tweet):
    tokens = tweet.split()
    teste = ''
    for item in tokens:
        teste += item
        print(item)
    return tokens