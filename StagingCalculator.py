# -*- coding: utf-8 -*-


import pyodbc             
import pandas     as pd                   #IMPORT Pandas
from   sqlalchemy import create_engine    #IMPORT Sql Retriever
from datetime import datetime
import numpy as np
import random
import time                              #Check Running times


#Checking Performance
initalTime = time.time()

#Parameters
runDate = '1990-01-01'
portfolioID = 1


#Database Connection Parameters
server = 'DESKTOP-J9GGR42'  
database = 'indexSandbox'
driver = 'ODBC Driver 17 for SQL Server'  
# Connection URL
conn_url = f'mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes'
#SQL Engine
engine = create_engine(conn_url)

#Retrieve Portfolio Details

portfolioDetailsSQLTable = 'lkup_portfolio_details'
portfolioDetailsSQL = f"SELECT * FROM {database}..{portfolioDetailsSQLTable} where portfolioID={portfolioID}"
portfolioDetails = pd.read_sql_query(portfolioDetailsSQL, engine)



#Retrieve prices for date.
pricesSQLTable = 'bondPrices'
pricesSQL = f"SELECT * FROM {database}..{pricesSQLTable} where priceDate='{runDate}'"  

# Retrieve data into a DataFrame
prices = pd.read_sql_query(pricesSQL, engine)



#Calendar Table SQL Retrieval


#Check if date is valid for calculator







#Checking Performance
endTime= time.time()
elapsedTime = endTime - initalTime
print(f"Elapsed time: {elapsedTime} seconds")