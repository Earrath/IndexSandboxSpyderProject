import pyodbc             
import pandas     as pd                       #IMPORT Pandas
from   sqlalchemy import create_engine    #IMPORT Sql Retriever
from datetime import datetime
import numpy as np
import random
import time                              #Check Running times

#Database Connection Parameters
server = 'DESKTOP-J9GGR42'  
database = 'indexSandbox'
driver = 'ODBC Driver 17 for SQL Server'  
# Connection URL
conn_url = f'mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes'
#SQL Engine
engine = create_engine(conn_url)

#Calendar Table SQL Retrieval
rebalanceDatesSQL = "select * from indexSandbox..portfolioDates where portfolioID=1"  

# Retrieve data into a DataFrame
rebalanceDates = pd.read_sql_query(rebalanceDatesSQL, engine)



   
for index, row in rebalanceDates.iterrows():
    current_date = row['date'] 
    sp_call = f"EXEC indexSandbox..rebalanceTool @date = '{current_date.strftime('%Y-%m-%d')}', @portfolioID = 1, @updateFlag = 1, @debug = 0"
    with engine.begin() as conn:  
        conn.execute(sp_call)
        
        


