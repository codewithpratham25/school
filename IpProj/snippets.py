import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy
import mysql.connector

usern = 'prath'
userhost = 'localhost'
uport = '3306'
username = 'root'
passw = 'mysql'
db = 'test101'
        
myDB = mysql.connector.connect(
    host = userhost,
    user = username,
    password = passw,
    database = db
)
        
myCursor = myDB.cursor()
query = f'CREATE TABLE {usern}(Owner text(50), StoreName text(50), StoreCat text(50))'
prin = myCursor.execute(query)
print(prin)
