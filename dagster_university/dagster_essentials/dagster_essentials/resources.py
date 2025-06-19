from dagster_duckdb import DuckDBResource
import dagster as dg

"""
This code snippet imports a resource called DuckDBResource from Dagster’s dagster_duckdb integration library.
Next, it creates an instance of that resource and stores it in database_resource.
"""
database_resource = DuckDBResource(
    database=dg.EnvVar("DUCKDB_DATABASE")
)
