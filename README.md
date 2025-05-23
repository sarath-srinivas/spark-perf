## Local Spark Setup
  1. Install `uv` from [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)
  2. Clone this repo
     ```console
     #> git clone https://github.com/sarath-srinivas/spark-perf
     #> cd spark-perf
     ```
  3. Sync deps
     ```console
     #> uv sync
     ```

## Setup Spark UI
  1. Add these configs in sparksession.
     ```python
     spark = SparkSession.builder\
                .config('spark.eventLog.enabled', 'true')\
                .config('spark.eventLog.dir', logdir)\
                .config('spark.history.fs.logDirectory', logdir)\
                .getOrCreate()
     ```
  2. Run spark history server
     ```
     #> uv run ./.venv/lib/python3.12/site-packages/pyspark/sbin/start-history-server.sh --properties-file ./spark_history.conf
     ```
     (chnage the python3.12 to whatever is in your uv venv)

  3. Run your spark scripts
  4. Go to [http://localhost:18080](http://localhost:18080)
     
## Set up tpch dataset

  1. Download sf30 variant from [https://duckdb.org/docs/1.2/extensions/tpch.html#pre-generated-data-sets] 
  (https://duckdb.org/docs/1.2/extensions/tpch.html#pre-generated-data-sets)

  2. Install duckdb cli from [https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=direct](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=direct)

  3. Convert dataset to parquet
```console
#> duckdb /path/to/tpchsf30.db
#duckdb> SHOW TABLES;
#duckdb> COPY (SELECT * FROM lineitem) TO 'lineitem' (FORMAT parquet, FILE_SIZE_BYTES 536870912);
```


## Repartition dataset by a column(s) using duckdb

```console
#> duckdb /path/to/tpchsf30.db
#duckdb> COPY (SELECT * FROM lineitem) TO 'lineitem_shipmode' (FORMAT parquet,  PARTITION_BY (l_shipmode));
```


