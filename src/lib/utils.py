import configparser

from pyspark import SparkConf

def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")

    for (key , val ) in config.items("SPARK_APP_CONFIG"):
        spark_conf.set(key,val)

    return spark_conf

def load_survey_df(spark, data_file, schema_df):
    return spark.read.option("header","true") \
               .schema(schema_df)  \
                .format("csv") \
        .option("mode", "FAILFAST") \
        .option("dateFormat", "M/d/y") \
        .load(data_file)

def load_survey_json_df(spark, data_file, schema_ddl):
    return spark.read \
                .format("json") \
                .schema(schema_ddl) \
                .option("dateFormat", "M/d/y") \
                .load(data_file)

def load_survey_parquet_df(spark, data_file):
    return spark.read \
                .format("parquet") \
                .load(data_file)

def load_survey_no_schema(spark, data_file):
    return spark.read.option("header","true") \
               .option("inferSchema","true") \
                .format("csv") \
        .load(data_file)

def load_survey_no_schema_semi_col(spark, data_file):
    return spark.read.option("header","true") \
               .option("inferSchema","true") \
                .option("delimiter", ";") \
                .format("csv") \
        .load(data_file)