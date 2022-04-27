from datetime import datetime
import time
import tracemalloc
import config as sql
import dados_view_model as dvm
todos_estado = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
                "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SE", "SP", "TO"]
estado_atual = todos_estado[25]


def transactions(cursor, init, final, step):
    global estado_atual
    transaction = []
    lista = []
    lista_tempo = []
    lista_memoria = []
    # Criação dos valores do Range
    for n in range(init, final, step):
        lista.append(n)
    tracemalloc.start()
    tempo_inicial = (time.time())
    # Inserção dos valores, pegando o tempo e o espaço ocupado na memória.
    while(lista != []):
        transaction.append(lista.pop())
        lista_memoria.append(tracemalloc.get_traced_memory()[0])
        tempo_final = (time.time()) - tempo_inicial
        lista_tempo.append(tempo_final)
    maior_memoria = max(lista_memoria)

    tracemalloc.stop()
    orderedTranscation = [num for num in reversed(transaction)]
    # Inserção no Banco
    tempo_inical_insercao = (datetime.now())
    while(orderedTranscation != []):
        dados_view_Model = dvm.dados_view_model(orderedTranscation.pop(), lista_tempo.pop(), lista_memoria.pop(),estado_atual)
        dados_view_Model.mostrar_dados_da_View_model()
        sql.insert(cursor,dados_view_Model)
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
    print("Opção inválida")
def main():
    cnx, cursor = sql.conn()
    while(cenario(cursor) != False):
        cnx.commit()
        pass
    sql.desconect(cnx, cursor)


if __name__ == "__main__":
    main()
