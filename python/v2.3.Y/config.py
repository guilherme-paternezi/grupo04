import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime
import dados_view_model as dvm


def conn():
    try:
        cnx = mysql.connector.connect(
            host='3.233.235.81', database='algas', user='grupo04', password='urubu100')
        print("Conectado ao servidor MySQL versão ")
        cursor = cnx.cursor()
        return cnx, cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def desconect(cnx, cursor):
    cnx.commit()
    cursor.close()
    cnx.close()


def insert(cursor, dados_view_model):
    cursor.execute("""
        INSERT INTO dados (entrada,tempo,memoria,etnia,idade,sexo,grupo_risco,febre,coriza,dor_muscular,tosse,variante,classe_social,fk_estado,data_insercao)
        VALUES (%d, %.20f,%d,'%s','%s','%s',%s,%s,%s,%s,%s,'%s','%s','%s','%s')
        """ % (dados_view_model.transaction,
        dados_view_model.tempo,
        dados_view_model.memoria,
        dados_view_model.etnia,
        dados_view_model.idade,
        dados_view_model.sexo,
        dados_view_model.grupo_risco,
        dados_view_model.febre,
        dados_view_model.coriza,
        dados_view_model.dor_muscular,
        dados_view_model.tosse,
        dados_view_model.variante,
        dados_view_model.classe_social,
        dados_view_model.estado_atual,
        datetime.now()))


def insert_info(cursor, estado_atual, numero_casos, data_inicio_insercao, tempo_total_insercao, maior_memoria):
    cursor.execute("""
        INSERT INTO infos (fk_estado, numero_casos, data_inicio_insercao, tempo_execucao, maior_memoria)
        VALUES ('%s', %d,'%s','%s', %d)
        """ % (estado_atual, numero_casos, data_inicio_insercao, tempo_total_insercao, maior_memoria))


def select_dados(cursor):
    cursor.execute("""
    SELECT * FROM dados
    """)
    myResult = cursor.fetchall()
    for x in myResult:
        print(x)


def select_dados_info(cursor):
    cursor.execute("""
    SELECT * FROM infos
    """)
    for (idInfo, estado, numero_casos, data_inicio_insercao, tempo_execucao, maior_memoria) in cursor:
        print("idInfo: %d, Estado: %s, Numero de casos: %d, Data inicio inserção: %s, Tempo total de execução: %s , Pico de memória: %d KiloByte" % (
            idInfo, estado, numero_casos, data_inicio_insercao, tempo_execucao, maior_memoria))


def truncate_dados(cursor):
    cursor.execute("""
    TRUNCATE dados
    """)


def truncate_infos(cursor):
    cursor.execute("""
    TRUNCATE infos
    """)


def count_dados(cursor):
    cursor.execute("""
    SELECT COUNT(*) FROM dados
    """)
    for (count) in cursor:
        print("Número de transações: %d" % (count))


def count_infos(cursor):
    cursor.execute("""
    SELECT COUNT(*) FROM infos
    """)
    for (count) in cursor:
        print("Número de informações: %d" % (count))
