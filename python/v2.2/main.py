
from ast import Nonlocal
from datetime import datetime
from random import randint, random
import time
import tracemalloc
import config as sql
todos_estado = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
                "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SE", "SP", "TO"]
estado_atual = todos_estado[25]


def transactions(cursor, init, final, step):
    global estado_atual
    transaction = []
    lista = []
    lista_tempo = []
    lista_memoria = []
    
    for n in range(init, final, step):
        lista.append(n)
    tracemalloc.start()
    tempo_inicial = (time.time())
    while(lista != []):
        transaction.append(lista.pop())
        lista_memoria.append(tracemalloc.get_traced_memory()[0])
        tempo_final = (time.time()) - tempo_inicial
        lista_tempo.append(tempo_final)
    maior_memoria = max(lista_memoria)

    tracemalloc.stop()
    orderedTranscation = [num for num in reversed(transaction)]
    tempo_inical_insercao = (datetime.now())
    while(orderedTranscation != []):
        transac = orderedTranscation.pop()
        tempo = lista_tempo.pop()
        memoria = lista_memoria.pop()
        etn = etnia()
        idad = idade()
        sex = sexo()
        risco = grupo_risco()
        febr = febre()
        coriz = coriza()
        toss = tosse()
        dor = dor_muscular()
        variant = variante()
        classe = classe_social()

        print("Inserido o valor no banco de dados: transaction = {}, tempo = {}, memoria = {}, etnia = {}, idade = {}, sexo = {}, grupo de risco = {}, febre = {}, coriza = {}. tosse = {}, dor muscular = {}, variante = {}, classe social = {} ".format(
            transac, tempo, memoria, etn, idad, sex, risco, febr, coriz, toss, dor, variant, classe))
        sql.insert(cursor,
                   transac,
                   tempo,
                   memoria,
                   etn,
                   idad,
                   sex,
                   risco,
                   febr,
                   coriz,
                   dor,
                   toss,
                   variant,
                   classe,
                   estado_atual
                   )
    tempo_total_insercao = (datetime.now()) - tempo_inical_insercao
    print("tempo inicial de inserção:" + str(tempo_inical_insercao))
    print("tempo final de inserção:" + str(datetime.now()))
    print("Tempo de total inserção: {}".format(tempo_total_insercao))
    sql.insert_info(cursor, estado_atual, len(transaction),
                    tempo_inical_insercao, tempo_total_insercao, maior_memoria)


def cenario(cursor):
    global estado_atual
    global todos_estado
    valor = int(input(
        "Escolha um cenário \n 1. [100_000,600_000,100_000] \n 2. [1_000,6_000,100] \n 3. [100,600,10] \n 4. [10,60,10] \n 5. [1_000_000,6_000_000,1_000_000] \n 6. Personalizado \n 7. Alterar Estado de inserção \n 8. Banco \n 9. Sair \n"))
    if valor == 1:
        return transactions(cursor, 100_000, 600_000, 100_000)
    if valor == 2:
        return transactions(cursor, 1_000, 6_000, 100)
    if valor == 3:
        return transactions(cursor, 100, 600, 100)
    if valor == 4:
        return transactions(cursor, 10, 60, 10)
    if valor == 5:
        return transactions(cursor, 1_000_000, 6_000_000, 1_000_000)
    if valor == 6:
        dado_inicial = int(input("Digite o valor inicial: "))
        dado_final = int(input("Digite o valor final: "))
        dado_passo = int(input("Digite o valor do passo: "))
        return transactions(cursor, dado_inicial, dado_final, dado_passo)
    if valor == 7:
        print("Estados: 0. AC \n 1. AL \n 2. AP \n 3. AM \n 4. BA \n 5. CE \n 6. DF \n 7. ES \n 8. GO \n 9. MA \n 10. MT \n 11. MS \n 12. MG \n 13. PA \n 14. PB \n 15. PR \n 16. PE \n 17. PI \n 18. RJ \n 19. RN \n 20. RS \n 21. RO \n 22. RR \n 23. SC \n 24. SE \n 25. SP \n 26. TO \n")
        posicao_estado = int(input("Digite o número do Estado : "))
        estado_atual = todos_estado[posicao_estado]
        return
    if valor == 8:
        select(cursor)
        return
    if valor == 9:
        return False
    print("Opção inválida")


def select(cursor):
    valor = int(input("Escolha um cenário \n 1. Seleciona todos os valores da tabela dados \n 2. Seleciona todos os valores da tabela dados_info \n 3. Truncate tudo \n 4. Quantidade de dados \n 5. Sair \n"))
    if valor == 1:
        sql.select_dados(cursor)
    if valor == 2:
        sql.select_dados_info(cursor)
    if valor == 3:
        sql.truncate_dados(cursor)
        sql.truncate_infos(cursor)
    if valor == 4:
        sql.count_dados(cursor)
        sql.count_infos(cursor)
    if valor == 5:
        return


def etnia():
    valor = randint(0, 100)
    etnia = ""
    if valor < 43:
        etnia = "Branca"
    elif valor < 90:
        etnia = "Pardos"
    elif valor < 99:
        etnia = "Preta"
    else:
        etnia = "Amarela ou Indigena"
    return etnia


def idade():
    valor_idade = randint(0, 1000)
    idade = ""
    if valor_idade < 210:
        idade = "Menor de 0 a 14 anos"
    elif valor_idade < 450:
        idade = "15 a 29 anos"
    elif valor_idade < 864:
        idade = "30 a 59 anos"
    else:
        idade = "Maior de 60 anos"
    return idade


def sexo():
    valor_sexo = randint(0, 100)
    sexo = ""
    if valor_sexo < 50:
        sexo = "M"
    else:
        sexo = "F"
    return sexo


def grupo_risco():
    valor_grupo = randint(0, 100)
    grupo_risco = False
    if valor_grupo < 55:
        grupo_risco = True
    return grupo_risco


def febre():
    valor_febre = randint(0, 100)
    febre = False
    if valor_febre < 82:
        febre = True
    return febre


def coriza():
    valor_coriza = randint(0, 100)
    coriza = False
    if valor_coriza < 85:
        coriza = True
    return coriza


def tosse():
    valor_tosse = randint(0, 100)
    tosse = False
    if valor_tosse < 90:
        tosse = True
    return tosse


def dor_muscular():
    valor_dor_muscular = randint(0, 100)
    dor_muscular = False
    if valor_dor_muscular < 90:
        dor_muscular = True
    return dor_muscular


def classe_social():
    valor_social = randint(0, 100)
    classe_social = ""
    if valor_social < 6:
        classe_social = "Alta"
    elif valor_social < 53:
        classe_social = "Média"
    else:
        classe_social = "Baixa"
    return classe_social


def variante():
    valor_variante = randint(0, 100)
    variante = ""
    if valor_variante < 50:
        variante = "Omicron"
    elif valor_variante < 80:
        variante = "Delta"
    else:
        variante = "Alpha"
    return variante


def main():
    cnx, cursor = sql.conn()
    while(cenario(cursor) != False):
        cnx.commit()
        pass
    sql.desconect(cnx, cursor)


if __name__ == "__main__":
    main()
