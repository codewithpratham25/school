import tkinter as tk
import ttkbootstrap as ttk
window = tk.Tk()
class button():
    def button(func):
        button = ttk.Button(window,text='Enter',command=func)
        button.pack()