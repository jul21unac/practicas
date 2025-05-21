from random import randrange
from random import choice

from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as f

from Figura import Cuadrado, Circulo, Triangulo
from Rectangulo import Rectangulo
from lib.logger import Log4J

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator, RegressionEvaluator


def generateCuadrado(cantidad):
    return [Cuadrado(randrange(1,20)) for x in range(cantidad)]
def generateCirculo(cantidad):
    return [Circulo(randrange(1,20)) for x in range(cantidad)]

def generateTrienagulo(cantidad):
    return [Triangulo(randrange(1,20), randrange(1,20)) for x in range(cantidad)]


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Agg Demo") \
        .master("local[2]") \
        .getOrCreate()

    logger = Log4J(spark)

    listCuadrado = generateCuadrado(50)

    listCirculo = generateCirculo(50)

    listTriangulo = generateTrienagulo(50)


    CirculoDF = spark.sparkContext.parallelize([( r.perimetro(), r.area()) for r in listCirculo]).toDF(["perimetro","area"])

    assembler = VectorAssembler() \
        .setInputCols(["perimetro"]) \
        .setOutputCol("features")
    assembler_df = assembler.transform(CirculoDF)
    a = assembler_df.toPandas().head()
    print(a.to_string())

    finalised_data = assembler_df.select('features', 'area')
    train, test = finalised_data.randomSplit([0.7, 0.3])

    # Entrenar modelo de regresión lineal
    lr = LinearRegression(
        featuresCol="features",
        labelCol="area",
        predictionCol="prediction"
    )

    lr_model = lr.fit(train)

    # Evaluar el modelo
    predictions = lr_model.transform(test)
    evaluator = RegressionEvaluator(
        labelCol="area",
        predictionCol="prediction",
        metricName="rmse"
    )

    rmse = evaluator.evaluate(predictions)
    print(f"Root Mean Squared Error (RMSE): {rmse}")

    # Mostrar algunas predicciones
    predictions.select("perimetro", "area", "prediction").show(10)
    '''predictions.head(10)'''
    CirculoDF.head(10)
    predictions.head(10)
    # Coeficientes del modelo
    print(f"Intercepto: {lr_model.intercept}")
    print(f"Coeficiente: {lr_model.coefficients[0]}")


