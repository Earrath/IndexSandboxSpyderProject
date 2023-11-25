import pyodbc             
import pandas     as pd                       #IMPORT Pandas
from   sqlalchemy import create_engine    #IMPORT Sql Retriever
from datetime import datetime
import numpy as np
import random
import time                              #Check Running times




#Parameters
calendarID = 1



#Database Connection Parameters
server = 'DESKTOP-J9GGR42'  # e.g., 'localhost\sqlexpress'
database = 'indexSandbox'
driver = 'ODBC Driver 17 for SQL Server'  # May vary based on your installed ODBC driver
# Connection URL
conn_url = f'mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes'
#SQL Engine
engine = create_engine(conn_url)

#Calendar Table SQL Retrieval
calendarSQLTable = 'Calendar'
calendarSQL = f"SELECT * FROM {database}..{calendarSQLTable} where CalendarID={calendarID}"  # Replace with your query and table name

# Retrieve data into a DataFrame
calendarDf = pd.read_sql_query(calendarSQL, engine)





