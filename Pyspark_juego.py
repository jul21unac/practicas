from random import randrange

from pyspark.sql import SparkSession
from pyspark.sql import functions as f

from Juego import Juego
from User import User
from lib.logger import Log4J
import secrets
import string

from dateutil.relativedelta import relativedelta
from datetime import datetime

def generate_Game(quantity):
    list_juego = []
    for x in range(quantity):
        a = Juego()
        a.jugar()
        list_juego.append(a)
    return list_juego


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Agg Demo") \
        .master("local[2]") \
        .getOrCreate()

    logger = Log4J(spark)

    list_games = generate_Game(1000)

    GameDF = spark.sparkContext.parallelize([(r.ganador.nombre, r.damage, r.turnos) for r in list_games]
                                            ).toDF(["Ganador", "Damage", "Turno"])

    GameDF.show()

    countPlayer = GameDF.where("Ganador = 'player'").count()
    calcGame = GameDF.where("Ganador = 'player'").count()/10



    print(countPlayer)
    print(calcGame)

    GameDF.select(f.avg(f.col("Turno"))).show()