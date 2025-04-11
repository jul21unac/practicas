from random import randrange
from random import choice
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as f
from Persona import Persona
from lib.logger import Log4J

def generatePeople(cantidad, ciudades):
    return [Persona(f'Nombre_{x}',randrange(18, 80),choice(ciudades)) for x in range(cantidad)]

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Agg Demo") \
        .master("local[2]") \
        .getOrCreate()

    logger = Log4J(spark)

    list_Ciudades = ["Madrid", "Bilbao","Barcelona", "Asturias"]
    listPersonas = generatePeople(100,list_Ciudades)

    peopleDF = spark.sparkContext.parallelize([[p.nombre,p.edad,p.ciudad] for p in listPersonas]).toDF(['nombre','edad','ciudad'])

    peopleDFoversixtyDF = peopleDF.where("edad >60")

    peopleAVGCityAge = peopleDF.groupBy("ciudad").agg(f.round(f.avg("edad"),2).alias("Promedio"))

    peopleDFoversixtyDF.show()
    peopleAVGCityAge.show()

