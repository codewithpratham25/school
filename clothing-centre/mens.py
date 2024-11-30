import pandas as pd
import mysql.connector
import sqlalchemy
import matplotlib.pyplot as plt

#stock
mensStock = pd.read_csv('A:/codewithpratham/school/clothing-centre/mens.csv')

#main code
class Mens():
    global mens
    def mens():
        def prtStock():
            print(mensStock)
        print('\n')
        space = '\t\t\t\t'
        print(f'{space}+---------------+')
        print(f'{space}   MENS WEAR')
        print(f'{space}+---------------+')
        print(f'{space}1. Display Items\n{space}2. Purchase\n{space}3. Exit')
        choice = int(input(f'{space}Choice: '))
        while choice >=1 and choice <= 3:
            if choice ==1:
                prtStock()
                mens()
            if choice == 2:
                prdcode = input('Enter PrdCode of the Prd you want to purchase: ')
                print(mensStock[['PrdName','PrdCode','PrdType','PrdSize','Disc','SalePrice']][mensStock['PrdCode'] == prdcode],'\tAdded to Cart')
                mens()
            if choice == 3:
                exit()
Mens.mens()
