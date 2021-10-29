# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:20:52 2021

@author: jesus.tagua
"""


###OPTION 1:
    
    
import psycopg2
import pandas as pd
from datetime import date

today = date.today()

import datetime as DT
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)

#purchases data
try:
    conn = psycopg2.connect(database="your_db_name",
                            user="your_user",
                            password="your_pass",
                            host="192.168.4.86",
                            port="5432")
    cur = conn.cursor()
    #example
    postgreSQL_select_Query ="""SELECT purchase_date, sum(plan_price_usd), cryptocurrency, transaction_currency, buyer_id, user_id from analysis_data.purchases group by purchase_date,cryptocurrency, transaction_currency, user_id, buyer_id;"""
    cur.execute(postgreSQL_select_Query)
    Data_purchases = cur.fetchall() #list of tuples
    df_purchases = pd.DataFrame(Data_purchases, columns =['Date', 'USD','Cryptocurrency','transaction_currency','user_id','user_id_real']) #user_id=buyer_id
    df_purchases["Date"] = pd.to_datetime(df_purchases["Date"])
except:
    print ("no connection to db")
    
df_purchases.describe()
df_purchases.head()
df_purchases.info()


### OPTION 2:

    
# SQLAlchemy URIs
# A URI (or connection string), is simply a string containing the information needed to connect to something like a database. Here's an example:

# postgres+psycopg2://myuser:mypassword@hackersdb.example.com:5432/mydatabase

# The first part of our string is postgres+psycop2, which is a combination of our target database type and our connector. If you're connecting to MySQL, replace this with mysql+pymysql

# [DB_FLAVOR]+[DB_PYTHON_LIBRARY]://[USERNAME]:[PASSWORD]@[DB_HOST]:[PORT]/[DB_NAME]

import pandas
import sqlalchemy
    
# Create the engine to connect to the PostgreSQL database
engine = sqlalchemy.create_engine('postgresql://your_user:your_pass@192.168.4.86:5432/(database="your_db_name",')
     
# Read data from SQL table
sql_data = pandas.read_sql_table('analysis_data',engine)