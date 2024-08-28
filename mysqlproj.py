import mysql.connector
import pandas as pd
import numpy as np
import pymysql
import sqlalchemy

print("Hello, This is Python Program which uses MySQL and Pandas Dataframe to Store and Display the Data.")
perm = str(input("Please Enter Y to Continue and N to abort: "))
print("Please select one of the options below to continue: \n1. Data Entry 2. Data Retrieval and Export")
program = int(input("Enter the Choice: "))
if perm == "y" or perm == "Y":
    if program == 1:
        uhost = 'localhost'
        uport = int(input("Enter the Port Number (By deafult 3306): "))
        username = str(input("Enter your MySQl server username: "))
        passw = str(input("Enter your MySQl server password: "))
        
        myDB = mysql.connector.connect(
            host = uhost,
            user = username,
            password = passw
        )
        
        myCursor = myDB.cursor()
        print('\nDatabase Connected! ')
        chance = int(input("How many Queries do you want to execute: "))
        print('\nSelect the Commands that you want to use (Enter from 1 to 3 )')
        for i in range(chance):    
            print('\n1. create database \n2. create table \n3. insert values')
            choice = int(input('Enter the choice: '))
            
            if choice == 1:
                db = str(input("Enter the Database Name you want to create: "))
                myCursor.execute(f'CREATE DATABASE {db}')
            
            if choice == 2:
                tb = str(input("Enter the Create table Query: "))
                myDB = mysql.connector.connect(
                    host = uhost,
                    user = username,
                    password = passw,
                    database = db
                )
        
                myCursor = myDB.cursor()
                myCursor.execute(tb)
                
            if choice == 3:
                rows = int(input("Enter the no of Rows you want to add: "))
                for j in range(rows):
                    insert = str(input('Enter the MySql query to Enter the data: '))
                    myDB = mysql.connector.connect(
                        host = uhost,
                        user = username,
                        password = passw,
                        database = db
                    )
        
                    myCursor = myDB.cursor()
                    myCursor.execute(insert)
                    myDB.commit()
        
    if program == 2:
        uhost = 'localhost'
        uport = int(input("Enter the Port Number (By deafult 3306): "))
        username = str(input("Enter your MySQl server username: "))
        passw = str(input("Enter your MySQl server password: "))
        db = str(input("Enter the Name of Database you want to retrieve: "))
        tb = str(input("Enter the Name of Table you want to retrieve: "))
        driver = 'mysql+pymysql'
        engine = sqlalchemy.create_engine(f'{driver}://{username}:{passw}@{uhost}:{uport}/{db}')
        df = pd.read_sql_query(f'SELECT * FROM {tb}', engine)
        print(df)
        perm = str(input('\nDo you want to Export the Data(Y or N): '))
        if perm == "y" or perm == "Y":
            df.to_csv('D:/Python/export.csv',sep=',',header=False)
        if perm == 'n' or perm == "N":
            exit
        
if perm == 'n' or perm == 'N':
    print("Program Aborted! ")
                
            
            
        

    