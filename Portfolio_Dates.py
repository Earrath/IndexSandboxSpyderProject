import pyodbc             
import pandas     as pd                       #IMPORT Pandas
from   sqlalchemy import create_engine    #IMPORT Sql Retriever
from datetime import datetime
import numpy as np
import random
import time                              #Check Running times




#Parameters
calendarID = 1
portfolioID = 1


#Database Connection Parameters
server = 'DESKTOP-J9GGR42'  
database = 'indexSandbox'
driver = 'ODBC Driver 17 for SQL Server'  
# Connection URL
conn_url = f'mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes'
#SQL Engine
engine = create_engine(conn_url)

#Calendar Table SQL Retrieval
calendarSQLTable = 'calendars'
calendarSQL = f"SELECT * FROM {database}..{calendarSQLTable} where CalendarID={calendarID}"  

# Retrieve data into a DataFrame
calendarDf = pd.read_sql_query(calendarSQL, engine)

# DatesRemoved (Debug)
calendarHolsWknds= calendarDf.loc[calendarDf['daytype']!=0]

# Remove Holiday Dates
calendarDf= calendarDf.loc[calendarDf['daytype']==0]



# Group by year and month, and select the minimum date
firstDayOfMonth = calendarDf.groupby(['year', 'month']).agg('min').reset_index()

firstDatesHistorical= firstDayOfMonth[['date']].copy()
firstDatesHistorical['portfolioID']= portfolioID



# Insert DataFrame into SQL Server
firstDatesHistorical.to_sql('portfoliodates', con=engine, if_exists='append', index=False)


print(calendarDf.dtypes)







