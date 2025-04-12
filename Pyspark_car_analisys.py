from Coche import Coche
from random import choice, randrange

from pyspark.sql import SparkSession

from lib.logger import Log4J


def generateAutomotiveFleet(cantidad, lista_modelo, lista_marca ):
    return [Coche( choice(lista_marca), choice(lista_modelo) , randrange(1980, 2025),
                   randrange(50000,100000), randrange(20000, 80000) ) for x in cantidad]

if __name__ = "__main__":
    spark = SparkSession.builder.appName("Agg Demo").master("Local[2]").getOrCreate()

    logger = Log4J(spark)

