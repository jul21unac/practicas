from random import randrange
from random import choice
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as f

from Rectangulo import Rectangulo
from lib.logger import Log4J

def generateRectangle(cantidad, ciudades):
    return [Rectangulo(randrange(18, 80),f'Nombre_{x}',choice(ciudades)) for x in range(cantidad)]

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Agg Demo") \
        .master("local[2]") \
        .getOrCreate()

    logger = Log4J(spark)
