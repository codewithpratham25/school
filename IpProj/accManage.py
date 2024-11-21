import pandas as pd
import sqlalchemy   
#main code
class InvAccManage():
    global prgIni
    def prgIni():
        global createAcc
        global login
        def createAcc(usern,passw):
            usern = usern
            passw = passw
            engine = sqlalchemy.create_engine(f'mysql+pymysql://root:mysql@localhost:3306/invmanagement')
            userDf = pd.read_sql_query('SELECT * FROM userandpass',engine)
            cond = (usern == (userDf[['Username']][(userDf['Password'] == passw)]))
            if cond.values == True:
               print('User Already Exists!! Pls Login!')
               print(f'Logging In {usern}...')
               login(usern=usern,passw=passw)
            else:
                serDict = {'Username':pd.Series(usern),'Password':pd.Series(passw)}
                userDF = pd.DataFrame(serDict)
                engine = sqlalchemy.create_engine(f'mysql+pymysql://root:mysql@localhost:3306/invmanagement')
                userDF.to_sql('userandpass',engine,if_exists='append',index=False)
        def login(usern,passw):
            usern = usern
            passw = passw
            engine = sqlalchemy.create_engine(f'mysql+pymysql://root:mysql@localhost:3306/invmanagement')
            userDf = pd.read_sql_query('SELECT * FROM userandpass',engine)
            cond = (usern == (userDf[['Username']][(userDf['Password'] == passw)]))
            if cond.values == True:
               print('User Login Successful!')
               from mainmenu import MainMenu as Main
               Main.mainmenu()
            else:
                print('Invalid Credentials!!')
                createAcc(usern=usern,passw=passw)
        print('---------------------------------------------------------------')
        print('Hello User! Welcome to Inventory Management v1.1.')
        print('This is a Command Line based application to Manage Inventory.')
        print('---------------------------------------------------------------')
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
            print('-----------------------')
            print('         Login    ')
            print('-----------------------')
            logusern = input('Username: ')
            logpassw = input('Password: ')
            login(usern=logusern,passw=logpassw)
        if choice == 3:
            print('---------------------------------------------------------------')
            print('Thank You User! for using Inventory Management v1.1.\nDevloped By codewithpratham\nv1.1')
            print('---------------------------------------------------------------')
            exit()
    prgIni()
