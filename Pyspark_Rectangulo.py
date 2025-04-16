from random import randrange
from random import choice
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as f

from Rectangulo import Rectangulo
from lib.logger import Log4J

def generateRectangle(cantidad, colorList):
    return [Rectangulo(randrange(1, 10),randrange(1, 20),choice(colorList) ) for x in range(cantidad)]

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Agg Demo") \
        .master("local[2]") \
        .getOrCreate()

    logger = Log4J(spark)

    listColor = ["Blue", "White", "Red", "Yellow", "Black"]

    listRectangle = generateRectangle(50,listColor)

    rectangleDF = spark.sparkContext.parallelize([(r.__str__(), r.area(),r.perimetro(), r.color) for r in listRectangle]).toDF(["rectangle","area","perimetro", "color"])

    rectanglehiguerhundred=rectangleDF.where('area >100')

    rectanglehiguerhundred.show()

    print(rectanglehiguerhundred.count())