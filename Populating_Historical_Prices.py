# -*- coding: utf-8 -*-


import pyodbc             
import pandas     as pd                       #IMPORT Pandas
from   sqlalchemy import create_engine        #IMPORT Sql Retriever
from datetime import datetime
import numpy as np
import random
import time                                   #Check Running times

#Database Connection Parameters
server = 'DESKTOP-J9GGR42'  
database = 'indexSandbox'
driver = 'ODBC Driver 17 for SQL Server'  
# Connection URL
conn_url = f'mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes'
#SQL Engine
engine = create_engine(conn_url)



table = 'bondsinstruments'