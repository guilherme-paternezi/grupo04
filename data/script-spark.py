# iniciar spark
from pyspark.sql.functions import col, sum
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import col
from pyspark import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf()
conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.2.0')
conf.set('spark.hadoop.fs.s3a.aws.credentials.provider',
         'com.amazonaws.auth.InstanceProfileCredentialsProvider')
spark = SparkSession.builder.config(conf=conf).getOrCreate()


# carregar tabela ( atenção ao caminho)
a = spark.read.option('delimiter', ';').option(
    'header', 'true').csv('s3a://murilo-3cco/vendas_anuais.csv')


# exibir a tabela

a.show()


# exercitando funções pyspark

a.select(col('id_cliente')).show()

# fazendo select no bucket

a.select(col('id_cliente').cast(IntegerType())).show()

# fazendo calculos
a.select(sum(col('id_cliente').cast(IntegerType())).alias('soma')).show()


# select via id

a.select(col('id_cliente')).first()
