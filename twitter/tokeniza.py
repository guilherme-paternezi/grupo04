from utils.utils import stop_words, listProfanities, remove_emoji,removeAcento, risadas, url

profanities = listProfanities('./utils/profanidades-ptBr-engEua.txt')

def tokeniza(exp):
    tokens = exp.split()
    tweetTreated = ''
    for token in tokens:
        if token.lower() in stop_words:
            continue
        if token.lower() in profanities:
            continue
        if token.lower().count(risadas[0]) > 3:
            continue
        if token.lower().count(risadas[1]) > 3:
            continue
        if token.lower().count(risadas[2]) > 3:
            continue
        if token.lower().count(url[0]) > 0 or token.lower().count(url[1]) > 0:
            continue

        token = ''.join(char for char in token if char.isalnum())

        tweetTreated += token + " "
        
    return removeAcento(remove_emoji(tweetTreated))
