from Coche import Coche
from random import choice, randrange

from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from lib.logger import Log4J


def generateAutomotiveFleet(cantidad, lista_modelo, lista_marca ):
    return [Coche( choice(lista_marca), choice(lista_modelo) , randrange(1980, 2025),
                   randrange(50000,100000), randrange(20000, 80000) ) for x in range(cantidad)]

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Agg Demo").master("local[2]").getOrCreate()

    logger = Log4J(spark)

    lista_modelo =["modelo_1","modelo_2","modelo_3","modelo_4","modelo_5","modelo_5"]

    lista_marca = ["Volvo","Toyota","Hiundai","Ferrari","Renault","Fiat"]

    cars = generateAutomotiveFleet(200, lista_modelo,lista_marca)

    carsDF = spark.sparkContext.parallelize([ l.marca, l.modelo, l.precio , l.anio, l.kilometraje ] for l in cars)\
              .toDF(["Marca", "Modelo", "Precio", "Anio", "Kilometro"])

    carsDF.show(10)

    carsPrecioAVgMAx = carsDF.groupBy("Marca").agg(f.round(f.avg("Precio"),2).alias("AVG_price"),\
                                                   f.max("Kilometro").alias("MaxKm"))

    carsPrecioAVgMAx.show()
