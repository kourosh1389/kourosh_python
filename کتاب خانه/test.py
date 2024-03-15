from tkinter import messagebox
from tkinter import *
import tkinter as tk
root = tk.Tk()
root['bg'] = '#4bd6a0'
root.title("wellcom!")
root.geometry('400x300')
root.resizable()
#=================================
btn_exit = Button(root , text = 'exit' , bg = 'red' , fg = 'black' , font= 'arial 15 bold' , width= 9 )
btn_exit.place(x= 280 , y= 100)
#=================================
lst_1 = Listbox(root, bg= 'white' , fg= 'red' ,width= 10 , height= 11)
lst_1.place(x= 10 , y= 10)
#=================================
name_entry = tk.Entry(root, fg= 'red' , bg= '#ACBBEA' , font= 'arial 15 bold')
name_entry.place(x= 100 , y= 260)
#==================================
name_label = tk.Label( text="NAME:")
name_label.place(x= 50 , y= 223)
#======================================
accept_checkbox = Checkbutton(root, text="شرایط و قوانین را میپذیرم")
accept_checkbox.pack()
root.mainloop()