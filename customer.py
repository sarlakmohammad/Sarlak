import tkinter
from tkinter import StringVar
from tkinter.messagebox import showinfo, showerror, showwarning, askokcancel
from tkinter import ttk
import customtkinter
from customtkinter import CTkFont
from database_customer import DBCustomer

class Customer(customtkinter.CTkFrame):

    def is_numeric(self,event):
        x = self.entry3.get()
        if not x.isnumeric() and x != "":
            showwarning('', 'phone number should be numeric!')
            self.entry3.delete(0, 'end')
            self.entry3.focus()

    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        ############################################ column 0
        self.frame_1 = customtkinter.CTkFrame(self,
                                         fg_color='#48D1CC',
                                         height=51
                                         )
        self.frame_1.grid(column=0, row=0, sticky='nsew')

        self.frame_2 = customtkinter.CTkFrame(self,
                                         fg_color='#F5FFFA',#CECECE
                                         height=765
                                         )
        self.frame_2.grid(column=0, row=1, sticky='nsew')
        self.frame_2.grid_columnconfigure(0, weight=1)
        self.frame_2.grid_rowconfigure(0, weight=1)
        self.frame_2.grid_rowconfigure(1, weight=1)
        self.frame_2.grid_rowconfigure(2, weight=1)
        self.frame_2.grid_rowconfigure(3, weight=1)
        self.frame_2.grid_rowconfigure(4, weight=1)

        self.frame_3 = customtkinter.CTkFrame(self,
                                         fg_color='#E88282',#FF9E9E
                                         height=255
                                         )
        self.frame_3.grid(column=0, row=2, sticky='nsew')
        ############################################ column 1
        self.frame_4 = customtkinter.CTkFrame(self,
                                              fg_color='#0EB95E',
                                              height=51
                                              )
        self.frame_4.grid(column=1, row=0,columnspan=3 ,sticky='nsew')
        self.frame_4.grid_rowconfigure(0,weight=1)
        self.frame_4.grid_columnconfigure(0,weight=1)
        self.frame_4.grid_columnconfigure(1,weight=1)

        self.frame_5 = customtkinter.CTkScrollableFrame(self,
                                              fg_color='#DBFFCB',
                                              height=765,
                                              # scrollbar_button_color='#0000C0',
                                              # scrollbar_button_hover_color='#00009B'
                                              )
        self.frame_5.grid(column=1, row=1, columnspan=3, sticky='nsew')
        self.frame_5.grid_rowconfigure(0,weight=1)
        self.frame_5.grid_columnconfigure(0,weight=1)

        self.frame_6 = customtkinter.CTkFrame(self,
                                              fg_color='#2BDF79',#FF9292
                                              height=255
                                              )
        self.frame_6.grid(column=1, row=2, sticky='nsew')
        ############################################ column 2
        self.frame_7 = customtkinter.CTkFrame(self,
                                              fg_color='#19A556',#A4FFB0
                                              height=255
                                              )
        self.frame_7.grid(column=2, row=2, sticky='nsew')
        ############################################ column 3
        self.frame_8 = customtkinter.CTkFrame(self,
                                              fg_color='#167D43',#C5FFA4
                                              height=255
                                              )
        self.frame_8.grid(column=3, row=2, sticky='nsew')

        ########################################################### vigets
        ############################################ row 0
        self.tab_name = customtkinter.CTkLabel(self.frame_1,
                                            text='مشتری جدید',
                                            font=CTkFont(family='B Nazanin',size=30,weight='bold'),
                                            text_color="black"
                                            )
        self.tab_name.pack()
        ##################
        self.refresh_btn = customtkinter.CTkButton(self.frame_4,
                                                   fg_color='#4682B4',
                                                   corner_radius=50,
                                                   text='refresh',
                                                   font=CTkFont(family='Arial', size=30,weight='bold'),
                                                   text_color='white',
                                                   hover_color='#39698E',
                                                   command=self.refresh
                                                   )
        self.refresh_btn.grid(column=1,row=0)

        self.delete_selection_btn = customtkinter.CTkButton(self.frame_4,
                                                   fg_color='#FF0000',
                                                   corner_radius=50,
                                                   text='delete',
                                                   font=CTkFont(family='Arial', size=30, weight='bold'),
                                                   text_color='white',
                                                   hover_color='#DE0000',
                                                   command=self.delete_selection
                                                   )
        self.delete_selection_btn.grid(column=0, row=0)
        ############################################ row 1 (1)
        self.entry_frame1 = customtkinter.CTkFrame(self.frame_2,fg_color='#F5FFFA')
        self.entry_frame1.grid(column=0,row=0,sticky='nsew')
        self.text_entry1 = customtkinter.CTkLabel(self.entry_frame1,
                                            text=':شرکت',
                                            font=CTkFont(family='B Nazanin', size=30),
                                            text_color="black"
                                            )
        self.text_entry1.pack(pady=5)
        self.entry1 = customtkinter.CTkEntry(self.entry_frame1,
                                             corner_radius=10,
                                             fg_color='white',
                                             height=35,
                                             width=200,
                                             text_color='black',
                                             font=CTkFont(family='B Nazanin',size=20),
                                             justify='right'
                                             )
        self.entry1.pack()
        ##################
        self.entry_frame2 = customtkinter.CTkFrame(self.frame_2, fg_color='#F5FFFA')
        self.entry_frame2.grid(column=0, row=1, sticky='nsew')
        self.text_entry2 = customtkinter.CTkLabel(self.entry_frame2,
                                                  text=':نام مشتری',
                                                  font=CTkFont(family='B Nazanin', size=30),
                                                  text_color="black"
                                                  )
        self.text_entry2.pack(pady=5)
        self.entry2 = customtkinter.CTkEntry(self.entry_frame2,
                                             corner_radius=10,
                                             fg_color='white',
                                             height=35,
                                             width=200,
                                             text_color='black',
                                             font=CTkFont(family='B Nazanin',size=20),
                                             justify='right'
                                             )
        self.entry2.pack()
        ##################
        self.entry_frame3 = customtkinter.CTkFrame(self.frame_2, fg_color='#F5FFFA')
        self.entry_frame3.grid(column=0, row=2, sticky='nsew')
        self.text_entry3 = customtkinter.CTkLabel(self.entry_frame3,
                                                  text=':شماره تلفن',
                                                  font=CTkFont(family='B Nazanin', size=30),
                                                  text_color="black"
                                                  )
        self.text_entry3.pack(pady=5)
        self.entry3 = customtkinter.CTkEntry(self.entry_frame3,
                                             corner_radius=10,
                                             fg_color='white',
                                             height=35,
                                             width=200,
                                             text_color='black',
                                             font=CTkFont(size=20)
                                             )
        self.entry3.pack()
        self.entry3.bind('<FocusOut>', command=self.is_numeric)
        ##################
        self.entry_frame4 = customtkinter.CTkFrame(self.frame_2, fg_color='#F5FFFA')
        self.entry_frame4.grid(column=0, row=3, sticky='nsew')
        self.text_entry4 = customtkinter.CTkLabel(self.entry_frame4,
                                                  text=':شماره موبایل',
                                                  font=CTkFont(family='B Nazanin', size=30),
                                                  text_color="black"
                                                  )
        self.text_entry4.pack(pady=5)
        self.entry4 = customtkinter.CTkEntry(self.entry_frame4,
                                             corner_radius=10,
                                             fg_color='white',
                                             height=35,
                                             width=200,
                                             text_color='black',
                                             font=CTkFont(size=20)
                                             )
        self.entry4.pack()
        ##################
        self.entry_frame5 = customtkinter.CTkFrame(self.frame_2, fg_color='#F5FFFA')
        self.entry_frame5.grid(column=0, row=4, sticky='nsew')
        self.clear_btn = customtkinter.CTkButton(self.entry_frame5,
                                                 fg_color='#7C7C7C',
                                                 corner_radius=50,
                                                 text='خالی کردن',
                                                 font=CTkFont(family='B Nazanin', size=30),
                                                 text_color='white',
                                                 hover_color='#4E4E4E',
                                                 command=self.clear_entry
                                                 )
        self.clear_btn.pack()
        self.submit_btn = customtkinter.CTkButton(self.entry_frame5,
                                                  fg_color='#008000',
                                                  corner_radius=50,
                                                  text='ثبت',
                                                  font=CTkFont(family='B Nazanin', size=30),
                                                  text_color='white',
                                                  hover_color='#005B00',
                                                  command=self.set_entry
                                                  )
        self.submit_btn.pack(pady=(10,0))
        ############################################ row 1
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=70,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=50,
                        )
        style.map('Treeview', background=[('selected', '#1B417A')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=('B Nazanin', 20)
                        )
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])

        self.column = ['id','شرکت','نام مشتری','شماره تلفن','شماره موبایل','بدهکار','پرداخت شده','مانده']
        self.data_table = ttk.Treeview(self.frame_5,
                                       columns=self.column,
                                       selectmode='browse',
                                       height=12
                                       )
        self.data_table.grid(column=0,row=0,sticky='nsew')
        self.data_table.column('id',width=50,minwidth=0,anchor='center',stretch=False)
        self.data_table.heading('id',text='ID')
        self.data_table.column('شرکت', width=250, minwidth=0, anchor='center', stretch=False)
        self.data_table.heading('شرکت', text='شرکت')
        self.data_table.column('نام مشتری', width=250, minwidth=0, anchor='center', stretch=False)
        self.data_table.heading('نام مشتری', text='نام مشتری')
        self.data_table.column('شماره تلفن', width=150, minwidth=0, anchor='center', stretch=False)
        self.data_table.heading('شماره تلفن', text=' تلفن')
        self.data_table.column('شماره موبایل', width=220, minwidth=0, anchor='center', stretch=False)
        self.data_table.heading('شماره موبایل', text='موبایل')
        self.data_table.column('بدهکار', width=200, minwidth=0, anchor='center', stretch=False)
        self.data_table.heading('بدهکار', text='بدهکار')
        self.data_table.column('پرداخت شده', width=200, minwidth=0, anchor='center', stretch=False)
        self.data_table.heading('پرداخت شده', text='پرداخت شده')
        self.data_table.column('مانده', width=200, minwidth=0, anchor='center')
        self.data_table.heading('مانده', text='مانده')

        self.data_table.tag_configure('0', font=CTkFont(family='B Nazanin', size=35),background='#1D5BB9')
        self.data_table.tag_configure('1', font=CTkFont(family='B Nazanin', size=35),background='#C00202')
        self.data_table.tag_configure('2', font=CTkFont(family='B Nazanin', size=35),background='#0DBC07')
        self.data_table.tag_configure('3', font=CTkFont(family='B Nazanin', size=35),background='#919191')

        ############################################ row 2 (1)
        self.delete_text = customtkinter.CTkLabel(self.frame_3,
                                                  font=CTkFont(family='B Nazanin', size=30,weight='bold'),
                                                  text='حذف شرکت (@مشتری)',
                                                  text_color='black'
                                                  )
        self.delete_text.pack(pady=8)

        self.delete_entry = customtkinter.CTkEntry(self.frame_3,
                                                   corner_radius=10,
                                                   fg_color='white',
                                                   height=70,
                                                   width=320,
                                                   text_color='black',
                                                   font=CTkFont(size=30,family='B Nazanin'),
                                                   placeholder_text='شرکت مورد نظر را حذف کنید',
                                                   justify='right'
                                                   )
        self.delete_entry.pack(pady=(10,0))

        self.delete_btn = customtkinter.CTkButton(self.frame_3,
                                                  fg_color='#FF0000',
                                                  corner_radius=50,
                                                  text='حذف',
                                                  font=CTkFont(family='B Nazanin', size=30),
                                                  text_color='white',
                                                  hover_color='#DE0000',
                                                  command=self.delete_customer
                                                  )
        self.delete_btn.pack(pady=20)
        ############################################ row 2 (2)
        self.debt_or_paid_var1 = StringVar(value='بدهی')
        self.debt_or_paid = customtkinter.CTkSegmentedButton(self.frame_6,
                                                             values=['پرداخت شده','بدهی'],
                                                             font=CTkFont(family='B Nazanin', size=30,weight='bold'),
                                                             height=30,
                                                             variable=self.debt_or_paid_var1,
                                                             fg_color='white',
                                                             unselected_color='#A0A0A0',
                                                             unselected_hover_color='#808080',
                                                             selected_color='#0054C3',
                                                             selected_hover_color='#0046A1',
                                                             text_color='white'
                                                             )
        self.debt_or_paid.pack(pady=8)

        self.debt_or_paid_entry = customtkinter.CTkEntry(self.frame_6,
                                                         corner_radius=10,
                                                         fg_color='white',
                                                         height=70,
                                                         width=320,
                                                         text_color='black',
                                                         font=CTkFont(size=27, family='B Nazanin'),
                                                         placeholder_text='بدهی یا مبلغ پرداختی را اضافه کنید',
                                                         )
        self.debt_or_paid_entry.pack(pady=(10,0))

        self.debt_or_paid_btn = customtkinter.CTkButton(self.frame_6,
                                                   fg_color='#1E90FF',
                                                   corner_radius=50,
                                                   height=60,
                                                   text='ثبت',
                                                   font=CTkFont(family='B Nazanin', size=30),
                                                   text_color='white',
                                                   hover_color='#2079D2',
                                                   command=self.add_debt_or_paid
                                                   )
        self.debt_or_paid_btn.pack(pady=20)
        ############################################ row 2 (3)
        self.search_text1 = customtkinter.CTkLabel(self.frame_7,
                                                  font=CTkFont(family='B Nazanin', size=30, weight='bold'),
                                                  text='نام مشتری',
                                                  text_color='black'
                                                  )
        self.search_text1.pack(pady=8)

        self.search_entry1 = customtkinter.CTkEntry(self.frame_7,
                                                   corner_radius=10,
                                                   fg_color='white',
                                                   height=70,
                                                   width=300,
                                                   text_color='black',
                                                   font=CTkFont(size=30, family='B Nazanin'),
                                                   placeholder_text='مشتری مورد نظر را پیدا کنید',
                                                   justify='right'
                                                   )
        self.search_entry1.pack(pady=(10, 0))

        self.search_btn1 = customtkinter.CTkButton(self.frame_7,
                                                  fg_color='#1E90FF',
                                                  corner_radius=50,
                                                  text='search',
                                                  font=CTkFont(family='Arial', size=30),
                                                  text_color='white',
                                                  hover_color='#2079D2',
                                                  command=self.search_customer
                                                  )
        self.search_btn1.pack(pady=20)
        ############################################ row 2 (4)
        self.search_text2 = customtkinter.CTkLabel(self.frame_8,
                                                   font=CTkFont(family='B Nazanin', size=30, weight='bold'),
                                                   text='نام شرکت',
                                                   text_color='black'
                                                   )
        self.search_text2.pack(pady=8)

        self.search_entry2 = customtkinter.CTkEntry(self.frame_8,
                                                    corner_radius=10,
                                                    fg_color='white',
                                                    height=70,
                                                    width=300,
                                                    text_color='black',
                                                    font=CTkFont(size=30, family='B Nazanin'),
                                                    placeholder_text='شرکت مورد نظر را پیدا کنید',
                                                    justify='right'
                                                    )
        self.search_entry2.pack(pady=(10, 0))

        self.search_btn2 = customtkinter.CTkButton(self.frame_8,
                                                   fg_color='#1E90FF',
                                                   corner_radius=50,
                                                   text='search',
                                                   font=CTkFont(family='Arial', size=30),
                                                   text_color='white',
                                                   hover_color='#2079D2',
                                                   command=self.search_company
                                                   )
        self.search_btn2.pack(pady=20)

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=2)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=15)
        self.grid_rowconfigure(2, weight=3)

    db_customer = DBCustomer('Data/sarlak1404.db')

    def refresh(self):
        for item in self.data_table.get_children():
            self.data_table.delete(item)

        _data = self.db_customer.show_data()
        for customer in _data:
            ######################### adding ***,***
            customer = list(customer)
            _copy = customer.copy()
            _copy = _copy[-3:]
            for i in range(3):
                customer.pop()
            for i in _copy:
                x = f"{i:,}"
                customer.append(x)
            #########################
            self.data_table.insert('', tkinter.END, values=customer, tags='0')

    def set_entry(self):
        company = self.entry1.get()
        customer = self.entry2.get()
        landline = self.entry3.get()
        phone_number = self.entry4.get()
        if company:
            self.db_customer.insert_into(company, customer, landline, phone_number)
            self.refresh()
            showinfo('good','completed!')
        else:
            showerror('empty!','you should fill <شرکت>')

    def clear_entry(self):
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry3.delete(0,'end')
        self.entry4.delete(0,'end')

    def delete_customer(self):
        _text = self.delete_entry.get()
        if _text == "":
            showerror('empty entry','you should enter something first!')
        elif _text.isnumeric():
            _data = self.db_customer.get_data1(_text)
            if _data:
                self.db_customer.delete_data1(_text)
                showinfo('deleted', f'ID={_text} is successfully deleted')
                self.delete_entry.delete(0, 'end')
                self.refresh()
            else:
                showwarning(':/', f'ID={_text} not founded!')
        elif _text[0] == '@':
            _data = self.db_customer.get_data2(_text[1:])
            if _data:
                self.db_customer.delete_data2(_text[1:])
                showinfo('deleted', f'{_text[1:]} is successfully deleted')
                self.delete_entry.delete(0, 'end')
                self.refresh()
            else:
                showwarning(':/', f'{_text[1:]} not founded!')
        else:
            _data = self.db_customer.get_data3(_text)
            if _data:
                self.db_customer.delete_data3(_text)
                showinfo('deleted',f'{_text} is successfully deleted')
                self.delete_entry.delete(0,'end')
                self.refresh()
            else:
                showwarning(':/',f'{_text} not founded!')

    def delete_selection(self):
        try:
            _selected = self.data_table.selection()[0]
            self.data_table.delete(_selected)
        except IndexError:
            pass

    def search_customer(self):
        for item in self.data_table.get_children():
            self.data_table.delete(item)
        _name = self.search_entry1.get()
        _data = self.db_customer.search_data1(_name)
        _number = 0
        try:
            for data in _data:
                ######################### adding ***,***
                data = list(data)
                _copy = data.copy()
                _copy = _copy[-3:]
                for i in range(3):
                    data.pop()
                for i in _copy:
                    x = f"{i:,}"
                    data.append(x)
                #########################
                _number += 1
                if data[7][0] == '-':
                    self.data_table.insert('', tkinter.END, values=data, text='طلبکار', tags='2')
                elif data[7] == '0':
                    self.data_table.insert('', tkinter.END, values=data, text='بی حساب', tags='3')
                else:
                    self.data_table.insert('', tkinter.END, values=data, text='بدهکار', tags='1')
            if _number == 0:
                raise TypeError
            showinfo('successful', f'{_number} item is founded')

        except TypeError:
            showwarning('oops', 'nothing founded!')

    def search_company(self):
        for item in self.data_table.get_children():
            self.data_table.delete(item)
        _name = self.search_entry2.get()
        _data = self.db_customer.search_data2(_name)
        _number = 0
        try:
            for data in _data:
                ######################### adding ***,***
                data = list(data)
                _copy = data.copy()
                _copy = _copy[-3:]
                for i in range(3):
                    data.pop()
                for i in _copy:
                    x = f"{i:,}"
                    data.append(x)
                #########################
                _number += 1
                if data[7][0] == '-':
                    self.data_table.insert('', tkinter.END, values=data, text='طلبکار', tags='2')
                elif data[7] == '0':
                    self.data_table.insert('', tkinter.END, values=data, text='بی حساب', tags='3')
                else:
                    self.data_table.insert('', tkinter.END, values=data, text='بدهکار', tags='1')
            if _number == 0:
                raise TypeError
            showinfo('successful', f'{_number} item is founded')
        except TypeError:
            showwarning('oops', 'nothing founded!')

    def add_debt_or_paid(self):
        _text = self.debt_or_paid.get()
        _money = self.debt_or_paid_entry.get()
        _money = _money.replace('.', '')
        _money = _money.replace(',', '')
        try:
            _selection = self.data_table.selection()[0]
            _options = self.data_table.item(_selection, option='values')
            if _text == 'بدهی' and _money:
                if askokcancel('are you sure?','this action changes the main DataBase'):
                    self.db_customer.change_data1(_money,_options[0])
                    self.db_customer.update_data(_options[0])
                    self.refresh()
            elif _text == 'پرداخت شده' and _money:
                if askokcancel('are you sure?','this action changes the main DataBase'):
                    self.db_customer.change_data2(_money, _options[0])
                    self.db_customer.update_data(_options[0])
                    self.refresh()
            else:
                showwarning('not allowed!',"debt/paid can't be empty")
        except IndexError:
            showerror('oops','please select something from table first!')