from tkinter import *

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "admin":
        main_frame.destroy()
        show_books_frame = Frame(root)
        show_books_frame.pack()
        
        borrowed_books_label = Label(show_books_frame, text="کتاب های قرض گرفته شده:")
        borrowed_books_label.pack()
        
        borrowed_books_listbox = Listbox(show_books_frame)
        
        show_button = Button(show_books_frame, text="نمایش", command=show_book_details)
        show_button.pack()
        
        add_book_frame = Frame(show_books_frame)
        add_book_frame.pack()
        
        book_title_entry = Entry(add_book_frame)
        book_title_entry.pack()
        
        author_entry = Entry(add_book_frame)
        author_entry.pack()
        
        shelf_entry = Entry(add_book_frame)
        shelf_entry.pack()
        
        publication_year_entry = Entry(add_book_frame)
        publication_year_entry.pack()
        
        add_button = Button(add_book_frame, text="اضافه کردن", command=add_book)
        add_button.pack()
        
        delete_button = Button(add_book_frame, text="حذف", command=delete_book)
        delete_button.pack()
        
        search_button = Button(add_book_frame, text="جست و جو", command=search_book)
        search_button.pack()
        
        edit_button = Button(add_book_frame, text="ویرایش", command=edit_book)
        edit_button.pack()
        
        return_button = Button(add_book_frame, text="بازگشت", command=return_to_main_page)
        return_button.pack()
        
    else:
        show_error_message()

def show_book_details():
    selected_book = borrowed_books_listbox.get(borrowed_books_listbox.curselection())
    
def add_book():
    book_title = book_title_entry.get()
    author = author_entry.get()
    shelf = shelf_entry.get()
    publication_year = publication_year_entry.get()
    
    
def delete_book():
    selected_book = borrowed_books_listbox.get(borrowed_books_listbox.curselection())
    
def search_book():
    search_query = book_title_entry.get()
    
def edit_book():
    selected_book = borrowed_books_listbox.get(borrowed_books_listbox.curselection())
    
def return_to_main_page():
    show_books_frame.destroy()
    create_main_page()

def show_error_message():
    error_message = Toplevel(root)
    error_message.title("خطا")
    
    error_label = Label(error_message, text="نام کاربری یا رمز عبور اشتباه است")
    error_label.pack()

def create_main_page():
    global main_frame
    main_frame = Frame(root)
    main_frame.pack()
    
    title_label = Label(main_frame, text="برنامه ورود و دریافت کتاب")
    title_label.pack()
    
    admin_button = Button(main_frame, text="ورود مسئول", command=enter_admin_page)
    admin_button.pack()
    
    members_button = Button(main_frame, text="ورود اعضا", command=enter_members_page)
    members_button.pack()
    
    search_button = Button(main_frame, text="جست و جو", command=search_page)
    search_button.pack()

def enter_admin_page():
    main_frame.destroy()
    admin_frame = Frame(root)
    admin_frame.pack()
    
    admin_title_label = Label(admin_frame, text="ورود مسئول")
    admin_title_label.pack()
    
    username_label = Label(admin_frame, text="نام کاربری:")
    username_label.pack()
    
    username_entry = Entry(admin_frame)
    username_entry.pack()
    
    password_label = Label(admin_frame, text="رمز عبور:")
    password_label.pack()
    
    password_entry = Entry(admin_frame, show="*")
    password_entry.pack()
    
    login_button = Button(admin_frame, text="ورود", command=check_credentials)
    login_button.pack()

def enter_members_page():
    main_frame.destroy()
    members_frame = Frame(root)
    members_frame.pack()

    members_title_label = Label(members_frame, text="ورود اعضا")
    members_title_label.pack()

    login_button = Button(members_frame, text="ورود", command=login_member)
    login_button.pack()

    register_button = Button(members_frame, text="ثبت نام", command=register_member)
    register_button.pack()

def login_member():
    pass

def register_member():
    members_frame.destroy()
    register_frame = Frame(root)
    register_frame.pack()

    register_title_label = Label(register_frame, text="ثبت نام")
    register_title_label.pack()

    name_label = Label(register_frame, text="نام:")
    name_label.pack()

    name_entry = Entry(register_frame)
    name_entry.pack()

    family_label = Label(register_frame, text="نام خانوادگی:")
    family_label.pack()

    family_entry = Entry(register_frame)
    family_entry.pack()

    class_label = Label(register_frame, text="کلاس:")
    class_label.pack()

    class_entry = Entry(register_frame)
    class_entry.pack()

    phone_label = Label(register_frame, text="شماره تماس:")
    phone_label.pack()

    phone_entry = Entry(register_frame)
    phone_entry.pack()

    birth_date_label = Label(register_frame, text="تاریخ تولد:")
    birth_date_label.pack()

    birth_date_entry= Entry(register_frame)
    birth_date_entry.pack()

    username_label = Label(register_frame, text="نام کاربری:")
    username_label.pack()

    username_entry = Entry(register_frame)
    username_entry.pack()

    password_label = Label(register_frame, text="رمز عبور:")
    password_label.pack()

    password_entry = Entry(register_frame, show="*")
    password_entry.pack()

    accept_checkbox = Checkbutton(register_frame, text="شرایط و قوانین را میپذیرم")
    accept_checkbox.pack()

    register_button = Button(register_frame, text="ثبت نام", command=save_member_info)
    register_button.pack()

def save_member_info():
    name = name_entry.get()
    family = family_entry.get()
    class_ = class_entry.get()
    phone = phone_entry.get()
    birth_date = birth_date_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    
def search_page():
    search_frame = Toplevel(root)
    search_frame.title("جستجو")
    
    search_title_label = Label(search_frame, text="جستجو")
    search_title_label.pack()
    
    search_entry = Entry(search_frame)
    search_entry.pack()
    
    search_button = Button(search_frame, text="جست و جو", command=search_books)
    search_button.pack()
    
    books_listbox = Listbox(search_frame)

root = Tk()
root.title("برنامه ورود و دریافت کتاب")
create_main_page()
root.mainloop()