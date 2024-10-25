# imports
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# import csv
stock = pd.read_csv('D:/Coding/Python/school/IpProj/IpProj.csv')

# main code
def mainmenu():
    print('----------------------------------------------------')
    print('          APS Bolarum Electronic Stores             ')
    print('----------------------------------------------------')
    print('1. Display the Stock')
    print('2. Stock Data Analysis')
    print('3. Graph Plotting')
    print('4. Append Items')
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
            pass
        elif choiceInput == 4:
            print('\n')
            pass
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
    print('--------------------------------')
    print('       Stock Data Analysis    ')
    print('--------------------------------')
    print('1. Display the Maximum Total Amt')
    print('2. Display the Minimum Total Amt')
    print('3. Segregate by Company')
    print('4. Show Maximum Qty and Prd')
    print('5. Show Minimum Qty and Prd')
    print('6. Go Back to Main Menu')
    daChoice = int(input('Enter the Choice: '))
    while daChoice >= 1 and daChoice <= 6:
        if daChoice == 1:
            print('The Maximum Total Amount is: ')
            print(max(stock.loc[:,'TAmt']))
            break
        elif daChoice == 2:
            print('The Minimum Total Amount is: ')
            print(min(stock.loc[:,'TAmt']))
            break
        elif daChoice == 3:
            pass
            break
        elif daChoice == 4:
            print('The Maximum Qty and Prd Name: ')
            print(max(stock.loc[:,'Qty']))
            break
        elif daChoice == 5:
            print('The Minimum Qty and Prd Name: ')
            print(min(stock.loc[:,'Qty']))
            break
        elif daChoice == 6:
            mainmenu()
    else:
        print('Invalid Input!! Pls Enter Correct Input')
        StkDataAnl()
mainmenu()
    