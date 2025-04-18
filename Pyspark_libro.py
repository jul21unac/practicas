from random import randrange
from random import choice
from pyspark.sql import SparkSession, Window , window
from pyspark.sql import functions as f

from Libro import Libro


def generate_books(quantity):


    for x in range(quantity):
        Libro("Titulo"+str(x),"Autor"+str(x), randrange(2000,2025) ,choice(["Ficcion","no-ficcion"]) )

    return Libro.libros

if __name__ == "__main__":

    lis_libr = generate_books(100)

    spark = SparkSession.builder.appName("Agg Demo").master("local[2]").getOrCreate()


    lib_df = spark.sparkContext.parallelize(([ l.titulo, l.autor,l.anio, l.genero ] for l in lis_libr )).\
        toDF(["Titulo","Autor","Anio","Genero"])

    genero_user = input("What book do you want Ficcion or no-ficcion").upper()

    lib_fav_gen = lib_df.groupBy("Genero").count()

    lib_fav_gen.show()



    lib_las_5_year = lib_df.where( (f.upper(lib_df.Genero) == genero_user) &  lib_df.Anio.between(2020,2025))

    lib_las_5_year.show()


