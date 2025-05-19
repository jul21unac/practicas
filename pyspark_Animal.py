from random import randrange
from random import choice
from pyspark.sql import SparkSession, Window , window
from pyspark.sql import functions as f

from Gato import Gato
from Perro import Perro
from Rectangulo import Rectangulo
from lib.logger import Log4J


def generate_animals(cantidad):
    l_lista_ani = []
    l_animals = ["G","P"]
    l_peso = ["liviano","mediano","pesado"]
    l_razas_perros = ["Labrador Retriever", "Pastor Alemán", "Golden Retriever", "Bulldog Francés",
                      "Beagle", "Poodle", "Rottweiler", "Yorkshire Terrier", "Boxer", "Dachshund",
                      "Siberian Husky", "Doberman Pinscher", "Great Dane", "Shih Tzu", "Chihuahua",
                      "Border Collie", "Pomeranian", "Corgi", "Australian Shepherd", "Boston Terrier",
                      "Pug", "Havanese", "Maltese", "Bichon Frise", "Shetland Sheepdog", "Cocker Spaniel",
                      "Pembroke Welsh Corgi", "Bernese Mountain Dog", "Cavalier King Charles Spaniel", "Basset Hound",
                      "English Springer Spaniel", "Pointer", "Weimaraner", "Collie", "Rhodesian Ridgeback", "Akita"]

    l_razas_gatos = ["Persa", "Siamés", "Maine Coon", "Bengalí", "Ragdoll", "British Shorthair", "Abisinio",
                     "Sphynx", "Scottish Fold", "Birmano", "Azul Ruso", "Noruego del Bosque", "Siberiano",
                     "Oriental", "Exótico", "Devon Rex", "Cornish Rex", "Himalayo", "Americano de Pelo Duro",
                     "Bombay", "Manx", "Burmés", "Tonkinés", "Angora Turco", "Somalí", "Chartreux", "Selkirk Rex",
                     "LaPerm", "Peterbald", "Singapura", "Snowshoe", "Balines", "Javanés", "Ocicat", "Savannah",
                     "Korat", "Burmilla", "American Bobtail", "Munchkin", "European Shorthair", "Toyger", "Pixiebob",
                     "Selkirk Rex", "Chausie", "Egyptian Mau", "Havana Brown", "Japanese Bobtail", "Lykoi", "Minskin",
                     "Napoleón", "Oriental Longhair", "Serengeti", "Sokoke", "Thai", "Ukrainian Levkoy", "Van Turco"]

    for i in range(cantidad):
        ani = choice(l_animals)

        if ani =="P":

            dog = Perro("Perro_"+str(i), randrange(3,110), choice(l_razas_perros))
            l_lista_ani.append(dog)
        else:
            cat = Gato("Gato_"+str(i), randrange(2,12), choice(l_razas_gatos))
            l_lista_ani.append(cat)

    return l_lista_ani

def classify_df(df):
    l_dic_rangos = {
                        "Perro" : {

                            "Pequeño" : (3,10),
                            "Mediano" : (11,45),
                            "Grande"  : (46,110)
                        },
                        "Gato" : {
                            "Pequeño" :(2,5),
                            "Mediano" :(6,7),
                            "Grande"  :(8,12)
                        }
    }
    for animal , categorias in l_dic_rangos.items():
        for categoria,(min_peso, max_peso) in categorias.items():

            df =df.withColumn("Clasificacion",f.when(
                    (f.col("Animal") == animal) &
                    (f.col("Peso") >= min_peso) &
                    (f.col("Peso") <= max_peso),
                categoria
                ).otherwise(f.col("Clasificacion"))
                                     )
    return df

if __name__ == "__main__" :



    list_a = generate_animals(10000)

    spark = SparkSession.builder.appName("Agg DEMO").master("local[2]").getOrCreate()

    animal_DF = (spark.sparkContext.parallelize([(x.nombre, type(x).__name__, x.raza, x.peso ) for x in list_a ])
                 .toDF(["Nombre","Animal","Raza","Peso"]))

    animal_DF = animal_DF.withColumn("Clasificacion",f.lit(None))

    '''
    f.when((animal_DF.Animal == "Perro") & (animal_DF.Peso >= 3) & (animal_DF.Peso <= 10), "Pequeño"). \
        when((animal_DF.Animal == "Perro") & (animal_DF.Peso > 10) & (animal_DF.Peso <= 45), "Mediano"). \
        when((animal_DF.Animal == "Perro") & (animal_DF.Peso > 45) & (animal_DF.Peso <= 110), "Grande"). \
        when(
        (animal_DF.Animal == "Gato") & (animal_DF.Peso >= 2) & (animal_DF.Peso <= 5),
        "Pequeño"). \
        when(
        (animal_DF.Animal == "Gato") & (animal_DF.Peso > 5) & (animal_DF.Peso <= 7),
        "Mediano"). \
        when(
        (animal_DF.Animal == "Gato") & (animal_DF.Peso > 7) & (animal_DF.Peso <= 12),
        "Grande")
    '''
    animal_clasification = classify_df(animal_DF)


    animal_staditics =  animal_clasification.groupBy("Animal", "Clasificacion").count()

    animal_staditics.show()

    animal_max = animal_clasification.groupBy("Animal","Raza").count()

    w = Window.partitionBy("Animal").orderBy(f.desc("count"))
    #animal_max.sort(animal_max.Animal.desc())

    animal_rank = animal_max.withColumn("Rank", f.row_number().over(w))

    animal_rank.where("Rank =1").show()