from random import randrange
from random import choice
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as f

from pyspark.sql.functions import coalesce, expr

from Persona import Persona
from lib.utils import get_spark_app_config, load_survey_json_df, load_survey_parquet_df, load_survey_no_schema, \
    load_survey_no_schema_semi_col
from lib.utils import load_survey_df

from lib.logger import Log4J

def generatePeople(cantidad, ciudades):
    return [Persona(randrange(18, 80),f'Nombre_{x}',choice(ciudades)) for x in range(cantidad)]

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Agg Demo") \
        .master("local[2]") \
        .getOrCreate()

    logger = Log4J(spark)

    list_Ciudades = ["Madrid", "Bilbao","Barcelona", "Asturias"]
    listPersonas = generatePeople(100,list_Ciudades)

    peopleDF = spark.sparkContext.parallelize([[p.nombre,p.edad,p.ciudad] for p in listPersonas]).toDF(['edad','nombre','ciudad'])

    peopleDFoversixtyDF = peopleDF.where("edad >60")

    peopleAVGCityAge = peopleDF.groupBy("ciudad").agg(f.round(f.avg("edad"),2).alias("Promedio"))

    peopleDFoversixtyDF.show()
    peopleAVGCityAge.show()

