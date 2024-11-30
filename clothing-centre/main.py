import pandas as pd
import mysql.connector
import sqlalchemy
import matplotlib.pyplot as plt
from mens import *
#main code
class Main():
    def Init():
        space = '\t\t\t\t'
        print(f'{space}+---------------------------------------------------------------------------------+')
        print(f'{space}Welcome to Command Line Purchase Portal for Pratham Clothing Centre Pvt Ltd .. v1.1')
        print(f'{space}+---------------------------------------------------------------------------------+')
        enter = input(f'{space}Press n to proceed ')
        if enter == 'n':
            print(f'{space}+-----------------------------+')
            print(f'{space}   PRATHAM CLOTHING CENTRE')
            print(f'{space}+-----------------------------+')
            print(f'{space}** Disc Sale Will Start From 1 Jan 2025 **')
            print(f'{space}1. Mens Wear\n{space}2. Womens Wear\n{space}3. Kids Wear')
            choice = int(input(f'{space}Choice: '))
            while choice >=1 and choice <= 4:
                if choice == 1:
                    Mens.mens()
Main.Init()
