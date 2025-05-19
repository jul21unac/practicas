from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from Inventory import Inventory  # Tus clases originales
from Product import Product
import json

from lib.logger import Log4J

# 1. Configuración inicial de Spark
spark = SparkSession.builder.appName("InventoryAlerts").getOrCreate()
ssc = StreamingContext(spark.sparkContext, batchDuration=5)  # Micro-batches cada 5 seg
logger = Log4J(spark)
# 2. Cargar datos iniciales (como lo hacías antes)
productos_iniciales = [
    ("jabon", 2.2, 15, 5),
    ("cafe", 3.3, 20, 10),
    ("azucar", 4.4, 10, 3),
    ("chocolate", 3.4, 8, 2)
]
for nombre, precio, cantidad, umbral in productos_iniciales:
    Inventory.agregar_producto(Product(nombre, precio, cantidad, umbral))

# 3. Crear un DStream que simule tus eventos (usando un socket)
eventos_stream = ssc.socketTextStream("localhost", 9999)

logger.info("comienzo")
# 4. Procesamiento en tiempo real
def procesar_evento(evento):

    try:
        data = json.loads(evento)
        if data["tipo"] == "r":
            Inventory.restock(data["nombre"], data["cantidad"])
        else:
            Inventory.vender(data["nombre"], data["cantidad"])

        # Verificar alertas
        alertas = [p for p in Inventory._productos if p.quantity < p.umbral_minimo]
        for producto in alertas:
            #logger.error("Alerta producto " + producto.name+ " " +str(producto.quantity) + str(producto.umbral_minimo) )
            print(f" ALERTA: {producto.name} (Stock: {producto.quantity}, Umbral: {producto.umbral_minimo})")
    except Exception as e:
        print(f"Error procesando evento: {str(e)}")


# Aplicar la función a cada evento en el stream
eventos_stream.foreachRDD(lambda rdd: rdd.foreach(procesar_evento))

# 5. Iniciar el streaming
ssc.start()
ssc.awaitTermination()