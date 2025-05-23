## Download tpch Dataset

Download sf30 variant
!(https://duckdb.org/docs/1.2/extensions/tpch.html#pre-generated-data-sets)[https://duckdb.org/docs/1.2/extensions/tpch.html#pre-generated-data-sets]

## Install duckdb cli

!(https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=direct)[https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=direct]

## Convert dataset to parquet

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


