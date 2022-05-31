from utils.utils import stop_words, listProfanities

PROFANITIES = listProfanities('./utils/profanidades-ptBr-engEua.txt')

def tokeniza(exp):
    tokens = exp.split()
    tweetTreated = ''
    for token in tokens:
        if token.lower() in stop_words:
            continue
        if token.lower() in PROFANITIES:
            continue
        tweetTreated += token + " "
    return tweetTreated