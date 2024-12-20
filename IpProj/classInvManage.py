import numpy as np
import pandas as pd
import pymysql as py
import sqlalchemy
from matplotlib import pyplot as plt

# import csv
stock = pd.read_csv('A:/codewithpratham/school/IpProj/IpProj.csv')

# main code
class InvAccManage():
        global createAcc
        def createAcc(usern,passw):
            usern = usern
            passw = passw
            serDict = {'Username':pd.Series(usern),'Password':pd.Series(passw)}
            userDF = pd.DataFrame(serDict)
            engine = sqlalchemy.create_engine(f'mysql+pymysql://root:mysql@localhost:3306/invmanagement')
            userDF.to_sql('userandpass',engine,if_exists='append',index=False)
        global login
        def login(usern,passw):
            usern = usern
            passw = passw
            engine = sqlalchemy.create_engine(f'mysql+pymysql://root:mysql@localhost:3306/invmanagement')
            userDf = pd.read_sql_query('SELECT * FROM userandpass',engine)
            cond = (usern == (userDf[['Username']][(userDf['Password'] == passw)]))
            if cond.values == True:
                mainmenu()
            else:
                print('Invalid Credentials!!')
                createAcc(usern=usern,passw=passw)
        def prgInittiate():
            print('Hello User! Welcome to Inventory Management v1.1.')
            print('This is a Command Line based application to Manage Inventory.')
            print('Pls Enter: \n1. to Login\n2. to Create Account\n3. to Exit Application')
            choice = int(input('Enter the Choice: '))
            if choice == 1:
                print('-----------------------')
                print('         Login    ')
                print('-----------------------')
                usern = input('Username: ')
                passw = input('Password: ')
                login(usern=usern,passw=passw)
            if choice == 2:
                print('-----------------------')
                print('     Create Account    ')
                print('-----------------------')
                usern = input('Username: ')
                passw = input('Password: ')
                createAcc(usern=usern,passw=passw)
            if choice == 3:
                print('Thank You User! for using Inventory Management v1.1.\nDevloped By codewithpratham\nv1.1')
                exit()
        prgInittiate()
class InvManage():
        global mainmenu
        global disStock
        global StkDataAnl
        global graphPlot
        global dataExpMySql
        def mainmenu():
            print('----------------------------------------------------')
            print('                Inventory Management             ')
            print('----------------------------------------------------')
            print('1. Display the Stock')
            print('2. Stock Data Analysis')
            print('3. Stock Graph Plotting')
            print('4. Data Export to MySQL')
            print('5. Exit')
            choiceInput = int(input('Enter the Choice: '))
            while choiceInput >= 1 and choiceInput <= 5:
                if choiceInput == 1:
                    disStock()
                    print('\n')
                elif choiceInput == 2:
                    StkDataAnl()
                    print('\n')
                elif choiceInput == 3:
                    print('\n')
                    graphPlot()
                elif choiceInput == 4:
                    dataExpMySql()
                    print('\n')
                elif choiceInput == 5:
                    print('Thank You!!')
                    exit()
            else:
                print('Invalid Input!! Pls Enter Correct Input')
                mainmenu()
        def disStock():
            print('-----------------------')
            print('     Display Stock    ')
            print('-----------------------')
            print(stock)
            mainmenu()

        def StkDataAnl():
            def segChoice():
                print('-----------------------')
                print('     Segregation    ')
                print('-----------------------')
                print('1. By Company')
                print('2. By Qty')
                print('3. By Price')
                print('4. Go Back to Main Menu')
                segChoice = int(input('Enter the Choice: '))
                while segChoice >= 1 and segChoice <= 4:
                    if segChoice == 1:
                        print('Segregation By Company')
                        company = str(input('ENTER THE COMPANY NAME(enter n to exit): '))
                        if company == 'n':
                            StkDataAnl()
                        # elif stock['Company'] != company:
                        #     print("Invalid Company Name")
                        print(stock[['IndexNo','Name','Company','Qty']][(stock['Company'] == company)])
                    elif segChoice == 2:
                        print('Segregation By Qty')
                        print('1. Greater than given Qty')
                        print('2. Less than given Qty')
                        segQtyChoice = int(input('Enter the Choice: '))
                        while segQtyChoice >= 1 and segQtyChoice <= 3:
                            if segQtyChoice == 1:
                                print('Greater than given Qty')
                                qty = int(input('ENTER Qty(enter 0 to exit): '))
                                if qty == 0:
                                    StkDataAnl()
                                print(stock[['IndexNo','Name','Company','Qty']][(stock['Qty'] >= qty)])
                            elif segQtyChoice == 2:
                                print('Less than given Qty')
                                qty = int(input('ENTER Qty(enter 0 to exit): '))
                                if qty == 0:
                                    StkDataAnl()
                                print(stock[['IndexNo','Name','Company','Qty']][(stock['Qty'] <= qty)])
                        
            print('--------------------------------')
            print('       Stock Data Analysis    ')
            print('--------------------------------')
            print('1. Display the Maximum Total Amt')
            print('2. Display the Minimum Total Amt')
            print('3. Show Maximum Qty and Prd')
            print('4. Show Minimum Qty and Prd')
            print('5. Segregation')
            print('6. Go Back to Main Menu')
            daChoice = int(input('Enter the Choice: '))
            while daChoice >= 1 and daChoice <= 6:
                if daChoice == 1:
                    print('The Maximum Total Amount is: ')
                    print(stock[['IndexNo','TAmt','Name']][(stock['TAmt']) == stock.TAmt.max()])
                    break
                elif daChoice == 2:
                    print('The Minimum Total Amount is: ')
                    print(stock[['IndexNo','TAmt','Name']][(stock['TAmt']) == stock.TAmt.min()])
                    break
                elif daChoice == 3:
                    print('The Maximum Qty and Prd Name: ')
                    print(stock[['IndexNo','Qty','Name']][(stock['Qty']) == stock.Qty.max()])
                    break
                elif daChoice == 4:
                    print('The Minimum Qty and Prd Name: ')
                    print(stock[['IndexNo','Qty','Name']][(stock['Qty']) == stock.Qty.min()])
                    break
                elif daChoice ==5:
                    segChoice()               
                elif daChoice == 6:
                    mainmenu()
            else:
                print('Invalid Input!! Pls Enter Correct Input')
                StkDataAnl()

        def graphPlot():
            print('--------------------------------')
            print('       Stock Graph Ploting    ')
            print('--------------------------------')
            print('1. Display Line Graph for Qty vs Item')
            print('2. Display Vertical Bar Graph for Qty vs Item')
            print('3. Go Back to Main Menu')
            gphChoice = int(input('Enter the Choice: '))
            while gphChoice >= 1 and gphChoice <= 3:
                if gphChoice == 1:
                    print('Line Graph For Qty vs Item')
                    plt.plot(stock.loc[:,'Name'],stock.loc[:,'Qty'], color='orange',marker='*',linewidth='2',linestyle='dashdot')
                    plt.xlabel('ItemName')
                    plt.ylabel('Qty')
                    plt.xticks(rotation=90)
                    plt.title('Line Graph For Qty vs Item')
                    plt.show()
                    break
                elif gphChoice == 2:
                    print('Bar Graph For Qty vs Item')
                    plt.bar(stock.loc[:,'Name'],stock.loc[:,'Qty'], color='orange')
                    plt.xlabel('ItemName')
                    plt.ylabel('Qty')
                    plt.xticks(rotation=90)
                    plt.title('Bar Graph For Qty vs Item')
                    plt.show()
                    break
                elif gphChoice == 3:
                    mainmenu()
            else:
                print('Invalid Input!! Pls Enter Correct Input')

        def dataExpMySql():
            perm = input('Do You Want to Export the Data to MySQL(Enter Y or N): ')
            if perm == 'Y':
                user = str(input('Enter Your Username: '))
                passw = input('Enter Your Password: ')
                db = input('Enter Database Name: ')
                engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{str(passw)}@localhost:3306/{str(db)}')
                stock.to_sql('aps_bolarum_stores_data',engine,if_exists='append',index=False)
            elif perm == "N":
                mainmenu()