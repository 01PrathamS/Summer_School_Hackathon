## I'm using the Aiven MySQL hosted Database for this project.

db_user = ""
db_password = ""
db_host =  ""
db_name = ""

# Construct the connection URI with the port included

from sqlalchemy import create_engine
import pandas as pd

def db_connect():
    engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:24644/{db_name}")
    return engine


