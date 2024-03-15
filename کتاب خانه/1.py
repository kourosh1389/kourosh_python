import tkinter as tk

def login_admin():
    admin_username = admin_username_entry.get()
    admin_password = admin_password_entry.get()
    if admin_username == "admin" and admin_password == "admin123":
        admin_page()

def admin_page():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Page")
    
    # Create and configure the book listbox
    book_listbox = tk.Listbox(admin_window)
    book_listbox.pack()
    
    # Create the entry fields for book details
    book_name_entry = tk.Entry(admin_window)
    book_name_entry.pack()
    author_entry = tk.Entry(admin_window)
    author_entry.pack()
    shelf_entry = tk.Entry(admin_window)
    shelf_entry.pack()
    year_entry = tk.Entry(admin_window)
    year_entry.pack()
    
    def add_book():
        book_name = book_name_entry.get()
        author = author_entry.get()
        shelf = shelf_entry.get()
        year = year_entry.get()
        book_listbox.insert(tk.END, f"{book_name} - {author} - {shelf} - {year}")
    
    def delete_book():
        selected_index = book_listbox.curselection()
        if selected_index:
            book_listbox.delete(selected_index)
    
    def search_book():
        search_query = book_name_entry.get()
        matching_books = [book for book in book_listbox.get(0, tk.END) if search_query.lower() in book.lower()]
        book_listbox.delete(0, tk.END)
        for book in matching_books:
            book_listbox.insert(tk.END, book)
    
    def edit_book():
        selected_index = book_listbox.curselection()
        if selected_index:
            book_name = book_name_entry.get()
            author = author_entry.get()
            shelf = shelf_entry.get()
            year = year_entry.get()
            book_listbox.delete(selected_index)
            book_listbox.insert(selected_index, f"{book_name} - {author} - {shelf} - {year}")
    
    def show_book():
        selected_index = book_listbox.curselection()
        if selected_index:
            book_details = book_listbox.get(selected_index)
            book_name, author, shelf, year = book_details.split(" - ")
            book_name_entry.delete(0, tk.END)
            book_name_entry.insert(tk.END, book_name)
            author_entry.delete(0, tk.END)
            author_entry.insert(tk.END, author)
            shelf_entry.delete(0, tk.END)
            shelf_entry.insert(tk.END, shelf)
            year_entry.delete(0, tk.END)
            year_entry.insert(tk.END, year)
    
    # Create the buttons
    add_button = tk.Button(admin_window, text="Add", command=add_book)
    add_button.pack()
    delete_button = tk.Button(admin_window, text="Delete", command=delete_book)
    delete_button.pack()
    search_button = tk.Button(admin_window, text="Search", command=search_book)
    search_button.pack()
    edit_button = tk.Button(admin_window, text="Edit", command=edit_book)
    edit_button.pack()
    show_button = tk.Button(admin_window, text="Show", command=show_book)
    show_button.pack()

def login_member():
    member_window = tk.Toplevel(root)
    member_window.title("Member Page")
    
    # Create and configure the borrowed books listbox
    borrowed_books_listbox = tk.Listbox(member_window)
    borrowed_books_listbox.pack()

def search_page():
    search_window = tk.Toplevel(root)
    search_window.title("Search Page")
    
    # Create and configure the search listbox
    search_listbox = tk.Listbox(search_window)
    search_listbox.pack()
    
    def search_books():
        search_query = book_name_entry.get()
        matching_books = [book for book in book_listbox.get(0, tk.END) if search_query.lower() in book.lower()]
        search_listbox.delete(0, tk.END)
        for book in matching_books:
            search_listbox.insert(tk.END, book)
    
    def show_book():
        selected_index = search_listbox.curselection()
        if selected_index:
            book_details = search_listbox.get(selected_index)
            book_name, author, shelf, year = book_details.split(" - ")
            book_name_entry.delete(0, tk.END)
            book_name_entry.insert(tk.END, book_name)
            author_entry.delete(0, tk.END)
            author_entry.insert(tk.END, author)
            shelf_entry.delete(0, tk.END)
            shelf_entry.insert(tk.END, shelf)
            year_entry.delete(0, tk.END)
            year_entry.insert(tk.END, year)
    
    # Create the entry fields for book details
    book_name_entry = tk.Entry(search_window)
    book_name_entry.pack()
    author_entry = tk.Entry(search_window)
    author_entry.pack()
    shelf_entry = tk.Entry(search_window)
    shelf_entry.pack()
    year_entry = tk.Entry(search_window)
    year_entry.pack()
    
    # Create the buttons
    search_button = tk.Button(search_window, text="Search", command=search_books)
    search_button.pack()
    show_button = tk.Button(search_window, text="Show", command=show_book)
    show_button.pack()

root = tk.Tk()
root.title("Library Management System")

# Create the main page buttons
admin_button = tk.Button(root, text="Admin Login", command=login_admin)
admin_button.pack()
member_button = tk.Button(root, text="Member Login", command=login_member)
member_button.pack()
search_button = tk.Button(root, text="Search", command=search_page)
search_button.pack()

root.mainloop()