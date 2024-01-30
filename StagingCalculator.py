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
runDate = '2020-11-02'
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

#Parameterize portfolioDetails

#CalendarID
calendarID              = portfolioDetails.loc[0, 'calendarID'] 
portfolioName           = portfolioDetails.loc[0, 'portfolioName'] 
portfolioDescription    = portfolioDetails.loc[0, 'portfolioDescription'] 


#Retrieve relevant dates for the portfolio based on on runDate
portfolioRunDatesSQL =f"""
SELECT	dbo.GetPrevious_Date({calendarID}, '{runDate}')	       AS previousDate,
		dbo.GetEOM_Date({calendarID}, '{runDate}')			   AS EOMDate,
		dbo.GetPrevious_EOM_Date({calendarID}, '{runDate}')    AS previousEOM,
		dbo.GetNext_Date({calendarID}, '{runDate}')		       AS nextDate,
		dbo.GetBOM_Date({calendarID}, '{runDate}')		       AS BOMDate
"""
portfolioRunDates = pd.read_sql_query(portfolioRunDatesSQL, engine)
#Parameterize dates
portfolioDate              = portfolioRunDates.loc[0, 'BOMDate'] 

#Calendar Table SQL Retrieval
#Begin End Dates
beginDateCalendar = runDate
endDateCalendar = '01-30-2024'
calendarSQLTable = 'calendars'
calendarSQL = f"SELECT * FROM {database}..{calendarSQLTable} where calendarID={calendarID} and date <='{endDateCalendar}'"  

calendarRaw = pd.read_sql_query(calendarSQL, engine)

#Retrieve Holiday Dates and weekends, might be useful for future inputs retrieval.
holidaysWeekendsMask = ((calendarRaw['daytype']== 1) | (calendarRaw['daytype'] == 2))
holidaysWeekendsDates = calendarRaw.loc[holidaysWeekendsMask]
#calendarRawHolidayDates = calendarRaw
#Final Calendar without holiday dates.
calendarDates = calendarRaw.loc[calendarRaw['daytype']==0,:]





# Retrieve portfolio data into a DataFrame
#Retrieve prices for date.
constituentsDataSQLTable= 'portfolioItems'
constituentsDataSQL = f"SELECT * FROM {database}..{constituentsDataSQLTable} where portfolioDate='{portfolioDate}' and portfolioID={portfolioID}"  
# Retrieve data into a DataFrame
constituentsData = pd.read_sql_query(constituentsDataSQL, engine)

#Populate Prices





#Retrieve prices for date.
pricesSQLTable = 'bondPrices'
pricesSQL = f"SELECT * FROM {database}..{pricesSQLTable} where priceDate='{runDate}'"  
# Retrieve data into a DataFrame
prices = pd.read_sql_query(pricesSQL, engine)







#Checking Performance
endTime= time.time()
elapsedTime = endTime - initalTime
print(f"Elapsed time: {elapsedTime} seconds")