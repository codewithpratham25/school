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
    print('3. Stock Graph Plotting')
    print('4. Exit')
    choiceInput = int(input('Enter the Choice: '))
    while choiceInput >= 1 and choiceInput <= 4:
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
    print('3. Show Maximum Qty and Prd')
    print('4. Show Minimum Qty and Prd')
    print('5. Go Back to Main Menu')
    daChoice = int(input('Enter the Choice: '))
    while daChoice >= 1 and daChoice <= 5:
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
        elif daChoice == 5:
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
            plt.plot(stock.loc[:,'Name'],stock.loc[:,'Qty'], color='orange')
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

mainmenu()
    