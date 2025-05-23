from pyspark.sql.session import SparkSession
import os

logdir = 'file:///home/sarath/projects/spark_perf/eventlogs'
data_dir = "/mnt/d"

spark = SparkSession.builder\
                .config('spark.eventLog.enabled', 'true')\
                .config('spark.eventLog.dir', logdir)\
                .config('spark.history.fs.logDirectory', logdir)\
                .getOrCreate()


lineitem = spark.read.format('parquet').load(os.path.join(data_dir, 'lineitem'))
lineitem.show()

