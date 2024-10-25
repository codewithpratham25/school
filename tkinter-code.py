#import
import ttkbootstrap as ttk
import tkinter as tk
import mysql.connector
import pandas as pd
import sqlalchemy
from . import _class_

#Window Initiation
window = tk.Tk()
window.geometry('700x500')

#Main program
#Functions
def perm():
    if perm_input.get() == 'yes' or perm_input.get() == 'Yes':
        inside_label = ttk.Label(window,text='Please select one of the options below to continue: \n1. Data Entry 2. Data Retrieval and Export')
        inside_label.pack()
        def choice():
            if choice_input.get() == '1':
                def press():
                    print(username.get())
                userhost_label = ttk.Label(window,text='Userhost:')
                userhost = ttk.Entry(window)
                
                _class_.button.button(press)
                username_label = ttk.Label(window,text='Username:')
                username = ttk.Entry(window)
                passw_label = ttk.Label(window,text='Password:')
                passw = ttk.Entry(window)
                db_label = ttk.Label(window,text='Enter Database Name:')
                db =ttk.Entry(window)
                userhost_label.pack()
                userhost.pack()
                username_label.pack()
                username.pack()
                passw_label.pack()
                passw.pack()
                db_label.pack()
                db.pack()
        choice_input = ttk.Entry(window)
        choice_button = ttk.Button(window,text='Enter',command=choice)
        choice_input.pack()
        choice_button.pack()
    elif perm_input.get() == 'no' or perm_input.get() == 'No':
        exit()
    else:
        error_label = ttk.Label(window,text='Wrong Input!')
        error_label.pack()
#Variables
intro_label = ttk.Label(window,text='Hello, This is Python GUI Program which uses MySQL and Pandas Dataframe to Store and Display the Data.\n \nEnter Yes to continue or No to abort:- ')

perm_input = ttk.Entry(window)
perm_button = ttk.Button(window,text='Enter',command=perm)
#Packing
intro_label.pack()
perm_input.pack()
perm_button.pack()
window.mainloop()

