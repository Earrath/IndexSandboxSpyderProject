import pyodbc             
import pandas     as pd                       #IMPORT Pandas
from   sqlalchemy import create_engine    #IMPORT Sql Retriever
from datetime import datetime
import numpy as np
import random
import time                              #Check Running times

#Time Code Start
initalTime = time.time()

#Dates Logic to create calendar.
startDate = '1990-01-01'
endDate   = datetime.today().strftime('%Y-%m-%d')


# Generate calendar
baseCalendar = pd.date_range(start=startDate, end=endDate, freq='D')
baseCalendar = pd.DataFrame(baseCalendar, columns=['Date'])


#US Holiday File Path generation
usHolPath     = 'C:\\Users\\Gianf\\Documents\\Data_Science\\Databases\\IndexSandbox\\USHolidayDates\\'
usHolFileName = 'US_Holiday_Dates_2004_2021.csv' 
print(f'ID file located in {usHolPath} . Filename:{usHolFileName}') 

#Load US Holiday Dates 2004_2021
usHolidayDates = pd.read_csv(usHolPath+usHolFileName)

#Show Duplicates for debug
usHolidayDupes = usHolidayDates[usHolidayDates.duplicated(subset=['Date'])]
#Remove Duplicates
usHolidayDates = usHolidayDates[~usHolidayDates.duplicated(subset=['Date'])]


#Datatypes conversions
usHolidayDates['Date'] = pd.to_datetime(usHolidayDates['Date'])
usHolidayDates['Holiday'] = usHolidayDates['Holiday'].astype('string')
usHolidayDates['WeekDay'] = usHolidayDates['WeekDay'].astype('string')


#GroupsByForDataCheck to debug analyse
holidaysDistribution     = usHolidayDates.groupby('Holiday').size()
yearHolidaysDistribution = usHolidayDates.groupby('Year').size()


#Join Dataframes.
usHolidayCalendar = pd.merge(baseCalendar, usHolidayDates, on='Date', how='left')
#Check for extradates.
extraDates = baseCalendar[~baseCalendar['Date'].isin(usHolidayCalendar['Date'])]

#Amend dates that doesn't have data.
# Get 'WeekDay'/'Month'/'Day'/'Year'
usHolidayCalendar['WeekDay'] = usHolidayCalendar['Date'].dt.day_name()
usHolidayCalendar['Month'] = usHolidayCalendar['Date'].dt.month
usHolidayCalendar['Day'] = usHolidayCalendar['Date'].dt.day
usHolidayCalendar['Year'] = usHolidayCalendar['Date'].dt.year


#Create column to identify what kind of day is and set it.
usHolidayCalendar['dayType'] = 0
usHolidayCalendarWeekends = usHolidayCalendar['WeekDay'].isin(['Saturday', 'Sunday'])
usHolidayCalendar.loc[usHolidayCalendarWeekends,'dayType'] = 1 
usHolidayCalendarHolDate = (usHolidayCalendar['Holiday'].notna()) & (usHolidayCalendar['Holiday'] !='')
usHolidayCalendar.loc[usHolidayCalendarHolDate,'dayType'] = 2 

#Calendar ID
usHolidayCalendar['calendarId'] = '1'


#print(usHolidayDates.loc[:,:])    #row,column
#print(usHolidayDates.loc[:,['Holiday','Year']])
#print(usHolidayDates.loc[((usHolidayDates['Holiday']=='Western Easter') & (usHolidayDates['Year']==2014)),['Holiday','Year']])




#Database Connection
server = 'DESKTOP-J9GGR42'  # e.g., 'localhost\sqlexpress'
database = 'indexSandbox'
driver = 'ODBC Driver 17 for SQL Server'  # May vary based on your installed ODBC driver

# Connection URL
conn_url = f'mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes'

# Creating the engine
engine = create_engine(conn_url)




# Insert DataFrame into SQL Server
usHolidayCalendar.to_sql('Calendars', con=engine, if_exists='append', index=False)







print(usHolidayCalendar.dtypes)
print(baseCalendar.dtypes)
#idsWestern = (ids['Holiday']=='Western Easter')







endTime= time.time()
elapsedTime = endTime - initalTime
print(f"Elapsed time: {elapsedTime} seconds")

