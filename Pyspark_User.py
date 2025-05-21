from random import randrange

from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from User import User
from lib.logger import Log4J
import secrets
import string

from dateutil.relativedelta import relativedelta
from datetime import datetime

def generate_User(quantity):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(randrange(8,20)))
    return [User(''.join(secrets.choice(alphabet) for i in range(randrange(8,20))), str(randrange(2024,2026))+'0521'  )  for x in range(quantity)]


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Agg Demo") \
        .master("local[2]") \
        .getOrCreate()

    logger = Log4J(spark)

    list_user = generate_User(100)

    userDF = spark.sparkContext.parallelize([(r.__str__(), r.ultimo_login, r.password) for r in list_user]
                                            ).toDF(["user", "ultimo_login", "pass"])

    userDF = userDF.withColumn("ultimo_login",f.to_date(f.col("ultimo_login"), "yyyyMMdd"))

    new_months = datetime.now() - relativedelta(months=6)
    str_date = new_months.strftime('%Y%m%d')

    user_last_login = userDF.filter(f.col("ultimo_login") < new_months)

    user_last_login.show()
