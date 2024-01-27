import tkinter as tk
from tkinter import messagebox

def add_entry():
    name = name_entry.get()
    family = family_entry.get()
    age = age_entry.get()
    if name and family and age:
        textbox.insert(tk.END, f"{name} , {family} , {age}\n")
        clear_entry()
    else:
        messagebox.showerror("Error", "Please enter name, family and age")

def delete_entry():
    textbox.delete(tk.ANCHOR)

def clear_entry():
    name_entry.delete(0, tk.END)
    family_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

def fetch_entry():
    line = textbox.get(tk.ANCHOR)
    if line:
        name, family, age = line.split()
        name_entry.insert(0, name)
        family_entry.insert(0, family)
        age_entry.insert(0, age)

def exit_program():
    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if answer:
        root.destroy()

root = tk.Tk()
root.title("Python GUI Form")

top_frame = tk.Frame(root)
middle_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)

name_label = tk.Label(top_frame, text="Name:")
name_entry = tk.Entry(top_frame)
family_label = tk.Label(top_frame, text="Family:")
family_entry = tk.Entry(top_frame)
age_label = tk.Label(top_frame, text="City:")
age_entry = tk.Entry(top_frame)

textbox = tk.Listbox(middle_frame, width=40, height=10)

add_button = tk.Button(bottom_frame, text="Add", command=add_entry)
delete_button = tk.Button(bottom_frame, text="Delete", command=delete_entry)
clear_button = tk.Button(bottom_frame, text="Clear", command=clear_entry)
fetch_button = tk.Button(bottom_frame, text="Fetch", command=fetch_entry)
exit_button = tk.Button(bottom_frame, text="Exit", command=exit_program)

name_label.pack(side=tk.LEFT, padx=5, pady=5)
name_entry.pack(side=tk.LEFT, padx=5, pady=5)
family_label.pack(side=tk.LEFT, padx=5, pady=5)
family_entry.pack(side=tk.LEFT, padx=5, pady=5)
age_label.pack(side=tk.LEFT, padx=5, pady=5)
age_entry.pack(side=tk.LEFT, padx=5, pady=5)

textbox.pack(padx=5, pady=5)

add_button.pack(side=tk.LEFT, padx=5, pady=5)
delete_button.pack(side=tk.LEFT, padx=5, pady=5)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)
fetch_button.pack(side=tk.LEFT, padx=5, pady=5)
exit_button.pack(side=tk.LEFT, padx=5, pady=5)

top_frame.pack()
middle_frame.pack()
bottom_frame.pack()

root.mainloop()



