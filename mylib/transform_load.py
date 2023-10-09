"""
Transforms and Loads data into Azure Databricks
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv

def load(dataset="data/dem_candidates.csv", dataset2="data/rep_incumbents.csv"):
    """Transforms and Loads data into the local databricks database"""
    df = pd.read_table(dataset, delimiter=",", skiprows=1, error_bad_lines=False)
    df2 = pd.read_table(dataset2, delimiter=",", skiprows=1, error_bad_lines=False)
    
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        
        # Create DemCandidatesDB table if not exists
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS DemCandidatesDB (
                id int,
                name string,
                age int,
                occupation string,
                education string
            )
            """
        )
        
        # Insert data into DemCandidatesDB
        for _, row in df.iterrows():
            values = tuple(row)
            c.execute(f"INSERT INTO DemCandidatesDB VALUES {values}")
        
        # Create RepIncumbentsDB table if not exists
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS RepIncumbentsDB (
                id int,
                name string,
                age int,
                occupation string,
                education string
            )
            """
        )
        
        # Insert data into RepIncumbentsDB
        for _, row in df2.iterrows():
            values = tuple(row)
            c.execute(f"INSERT INTO RepIncumbentsDB VALUES {values}")
        
        c.close()

    return "success"
