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
runDate = '2020-11-03'
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
portfolioDate               = portfolioRunDates.loc[0, 'BOMDate'] 
profileDate                 = portfolioRunDates.loc[0, 'previousEOM'] 

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


print(f"Calculator running for portfolio {portfolioID} - {portfolioName} on {runDate}. Portfolio Date: {portfolioDate}.")


# Retrieve portfolio data into a DataFrame

constituentsDataSQLTable= 'portfolioItems'
constituentsDataSQL = f"SELECT * FROM {database}..{constituentsDataSQLTable} where portfolioDate='{portfolioDate}' and portfolioID={portfolioID}"  
# Retrieve data into a DataFrame
constituentsData = pd.read_sql_query(constituentsDataSQL, engine)

#Send notification error that query didn't return results.(Data frame empty) / Send notification of success
if constituentsData.empty:
    print(f"No constituent data found.SQL:{constituentsDataSQL}")
else:
    print(f"Constituent monthly static data loaded into staging DF. portfolioID={portfolioID} PortfolioDate= {portfolioDate}.")



#Populate Prices
#Retrieve prices for date.
pricesSQLTable = 'bondPrices'
pricesSQL = f"SELECT * FROM {database}..{pricesSQLTable} where priceDate='{runDate}'"  
# Retrieve data into a DataFrame
prices = pd.read_sql_query(pricesSQL, engine)

#Send notification error that query didn't return results.(Data frame empty) / Send notification of success
if prices.empty:
    print(f"No pricing data found for the date.\nSQL:{pricesSQL}")
else:
    # Process your DataFrame
    print(f"Prices loaded for {runDate}.")


#Retrieve profile prices for date.
profilePricesSQLTable = 'bondPrices'
profilePricesSQL = f"SELECT * FROM {database}..{pricesSQLTable} where priceDate='{profileDate}'"  
# Retrieve data into a DataFrame
profilePrices = pd.read_sql_query(profilePricesSQL, engine)

#Send notification error that query didn't return results.(Data frame empty) / Send notification of success
if profilePrices.empty:
    print(f"No pricing data found for the date.\nSQL:{profilePricesSQL}")
else:
    # Process your DataFrame
    print(f"Profile prices loaded for {runDate}.")


#Join Prices and Staging Dataframe
constituentsStaging = pd.merge(constituentsData,prices , on='bondID', how='left')
constituentsStaging.rename(columns={'priceDate': 'todayPriceDate','closeBid': 'todayCloseBid', 'closeAsk': 'todayCloseAsk','closeMid': 'todayCloseMid'}, inplace=True)
constituentsStaging = pd.merge(constituentsStaging,profilePrices , on='bondID', how='left')
constituentsStaging.rename(columns={'priceDate': 'profilePriceDate','closeBid': 'profileCloseBid', 'closeAsk': 'profileCloseAsk','closeMid': 'profileCloseMid'}, inplace=True)


#Check Nulls
# print(constituentsStaging.isna().sum())
#Constituents Data aggregations / Checks
constituentsAggregations = {
    'todayCloseBid'      : 'mean',
    'marketValue'   : 'sum',
    'bondID'        : 'count',
}
constituentsDataAggs= constituentsStaging.agg(constituentsAggregations)
#Transpose
constituentsDataAggs = constituentsDataAggs.to_frame().T
#Map Number of constituents
numberOfConstituents = constituentsDataAggs.loc[0,'bondID']



#Price Returns
constituentsStaging['priceReturn']= (((constituentsStaging['todayCloseBid']-constituentsStaging['profileCloseBid'])/constituentsStaging['profileCloseBid'])*100)














#Checking Performance
endTime= time.time()
elapsedTime = endTime - initalTime
print(f"Process run time: {elapsedTime} seconds")