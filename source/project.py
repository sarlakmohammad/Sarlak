#Copyright (c) 2025 @sarlakmohammad
    #All rights reserved

import tkinter
from tkinter import StringVar,ttk
from tkinter.messagebox import showinfo, showerror, showwarning, askokcancel
import customtkinter
from customtkinter import CTkFont
from database_project import DBProject

class Project(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        ##############width and height
        # self.height = self.winfo_height()
        # row_0 = self.height//21
        # row_1 = 15*self.height//21

        ############################################ column 0
        self.frame_1 = customtkinter.CTkFrame(self,
                                         fg_color='#48D1CC',
                                        #  height=row_0
                                         )
        self.frame_1.grid(column=0, row=0, sticky='nsew')

        self.frame_2 = customtkinter.CTkFrame(self,
                                         fg_color='#F5FFFA',#CECECE
                                        #  height=row_1
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
                                         )
        self.frame_3.grid(column=0, row=2, sticky='nsew')
        ############################################ column 1
        self.frame_4 = customtkinter.CTkFrame(self,
                                              fg_color='#FF8C00',
                                            #   height=row_0
                                              )
        self.frame_4.grid(column=1, row=0,columnspan=3 ,sticky='nsew')
        self.frame_4.grid_rowconfigure(0,weight=1)
        self.frame_4.grid_columnconfigure(0,weight=1)
        self.frame_4.grid_columnconfigure(1,weight=1)

        self.frame_5 = customtkinter.CTkScrollableFrame(self,
                                              fg_color='#FFB757',
                                            #   height=row_1,
                                              # scrollbar_button_color='#0000C0',
                                              # scrollbar_button_hover_color='#00009B'
                                              )
        self.frame_5.grid(column=1, row=1, columnspan=3, sticky='nsew')
        self.frame_5.grid_rowconfigure(0,weight=1)
        self.frame_5.grid_columnconfigure(0,weight=1)

        self.frame_6 = customtkinter.CTkFrame(self,
                                              fg_color='#FFA07A',#FF9292
                                              )
        self.frame_6.grid(column=1, row=2, sticky='nsew')
        ############################################ column 2
        self.frame_7 = customtkinter.CTkFrame(self,
                                              fg_color='#FD7442',#A4FFB0
                                              )
        self.frame_7.grid(column=2, row=2, sticky='nsew')
        ############################################ column 3
        self.frame_8 = customtkinter.CTkFrame(self,
                                              fg_color='#FF4500',#C5FFA4
                                              )
        self.frame_8.grid(column=3, row=2, sticky='nsew')

        ########################################################### vigets
        ############################################ row 0
        self.tab_name = customtkinter.CTkLabel(self.frame_1,
                                            text='پروژه جدید',
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
                                            text=':اسم پروژه',
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
                                                  text=':آیدی مشتری',
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
                                             font=CTkFont(family='Arial',size=20)
                                             )
        self.entry2.pack()
        ##################
        self.entry_frame3 = customtkinter.CTkFrame(self.frame_2, fg_color='#F5FFFA')
        self.entry_frame3.grid(column=0, row=2, sticky='nsew')
        self.text_entry3 = customtkinter.CTkLabel(self.entry_frame3,
                                                  text=':برآورد هزینه',
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
        self.estimate_btn = customtkinter.CTkButton(self.entry_frame3,
                                                width=200,
                                                font=CTkFont(family='B Nazanin', size=30),
                                                fg_color='#008B8B',
                                                text='برآورد',
                                                text_color='white',
                                                hover_color='#007373',
                                                # command=self.open_toplevel
                                                )
        self.estimate_btn.pack()
        ##################
        self.entry_frame4 = customtkinter.CTkFrame(self.frame_2, fg_color='#F5FFFA')
        self.entry_frame4.grid(column=0, row=3, sticky='nsew')
        self.text_entry4 = customtkinter.CTkLabel(self.entry_frame4,
                                                  text=':تاریخ شروع',
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
                                             font=CTkFont(size=20),
                                             placeholder_text='1404/01/01'
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
        self.clear_btn.pack(pady=(5,0))
        self.submit_btn = customtkinter.CTkButton(self.entry_frame5,
                                                  fg_color='#008000',
                                                  corner_radius=50,
                                                  text='ثبت',
                                                  font=CTkFont(family='B Nazanin', size=30),
                                                  text_color='white',
                                                  hover_color='#005B00',
                                                  command=self.set_entry
                                                  )
        self.submit_btn.pack(pady=5)
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

        self.column = ['id','پروژه','مشتری','برآورد','هزینه','مغایرت','پرداختی','وضعیت تسویه']
        self.data_table = ttk.Treeview(self.frame_5,
                                       columns=self.column,
                                       selectmode='browse',
                                       height=12
                                       )
        self.data_table.grid(column=0,row=0,sticky='nsew')
        self.data_table.column('id',width=100,minwidth=0,anchor='center')
        self.data_table.heading('id',text='ID')
        self.data_table.column('پروژه', width=215, minwidth=0, anchor='center')
        self.data_table.heading('پروژه', text='پروژه')
        self.data_table.column('مشتری', width=215, minwidth=0, anchor='center')
        self.data_table.heading('مشتری', text='مشتری')
        self.data_table.column('برآورد', width=215, minwidth=0, anchor='center')
        self.data_table.heading('برآورد', text='برآورد')
        self.data_table.column('هزینه', width=215, minwidth=0, anchor='center')
        self.data_table.heading('هزینه', text='هزینه')
        self.data_table.column('مغایرت', width=100, minwidth=0, anchor='center')
        self.data_table.heading('مغایرت', text='مغایرت')
        self.data_table.column('پرداختی', width=215, minwidth=0, anchor='center')
        self.data_table.heading('پرداختی', text='پرداختی')
        self.data_table.column('وضعیت تسویه', width=125, minwidth=0, anchor='center')
        self.data_table.heading('وضعیت تسویه', text='وضعیت تسویه')

        self.data_table.tag_configure('0', font=CTkFont(family='B Nazanin', size=35),background='#1D5BB9')
        self.data_table.tag_configure('1', font=CTkFont(family='B Nazanin', size=35),background='#C00202')
        self.data_table.tag_configure('2', font=CTkFont(family='B Nazanin', size=35),background='#0DBC07')
        self.data_table.tag_configure('3', font=CTkFont(family='B Nazanin', size=35),background='#919191')

        ############################################ row 2 (1)
        self.delete_text = customtkinter.CTkLabel(self.frame_3,
                                                  font=CTkFont(family='B Nazanin', size=30,weight='bold'),
                                                  text='حذف پروژه',
                                                  text_color='black'
                                                  )
        self.delete_text.pack(pady=(16,8))

        self.delete_entry = customtkinter.CTkEntry(self.frame_3,
                                                   corner_radius=10,
                                                   fg_color='white',
                                                   height=70,
                                                   width=320,
                                                   text_color='black',
                                                   font=CTkFont(size=30,family='B Nazanin'),
                                                   placeholder_text='پروژه مورد نظر را حذف کنید',
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
                                                  command=self.delete_project
                                                  )
        self.delete_btn.pack(pady=20)
        ############################################ row 2 (2)
        self.debt_or_paid_var1 = StringVar(value='هزینه')
        self.debt_or_paid = customtkinter.CTkSegmentedButton(self.frame_6,
                                                             values=['پرداختی','هزینه'],
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
                                                         width=300,
                                                         text_color='black',
                                                         font=CTkFont(size=28, family='B Nazanin'),
                                                         placeholder_text='هزینه یا پرداختی را ثبت کنید',
                                                         )
        self.debt_or_paid_entry.pack(pady=(10,0))

        self.debt_or_paid_btn = customtkinter.CTkButton(self.frame_6,
                                                   fg_color='#1E90FF',
                                                   corner_radius=50,
                                                   text='ثبت',
                                                   font=CTkFont(family='B Nazanin', size=30),
                                                   text_color='white',
                                                   hover_color='#2079D2',
                                                   command=self.add_cost_or_paid
                                                   )
        self.debt_or_paid_btn.pack(pady=20)
        ############################################ row 2 (3)
        self.search_text1 = customtkinter.CTkLabel(self.frame_7,
                                                  font=CTkFont(family='B Nazanin', size=30, weight='bold'),
                                                  text='پیدا کردن پروژه',
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
                                                   placeholder_text='آیدی یا اسم پروژه را وارد کنید',
                                                   justify='right'
                                                   )
        self.search_entry1.pack(pady=(15, 0))

        self.search_btn1 = customtkinter.CTkButton(self.frame_7,
                                                  fg_color='#1E90FF',
                                                  corner_radius=13,
                                                  text='search',
                                                  font=CTkFont(family='Arial', size=30),
                                                  text_color='white',
                                                  hover_color='#2079D2',
                                                  height=50,
                                                  command=self.search_project
                                                  )
        self.search_btn1.pack(pady=(20,0))
        ############################################ row 2 (4)
        self.show_con_txt = customtkinter.CTkLabel(self.frame_8,
                                                   font=CTkFont(family='B Nazanin', size=30, weight='bold'),
                                                   text='پیمانکار های پروژه',
                                                   text_color='black'
                                                   )
        self.show_con_txt.pack(pady=8)

        self.show_con_entry = customtkinter.CTkEntry(self.frame_8,
                                                    corner_radius=10,
                                                    fg_color='white',
                                                    height=70,
                                                    width=300,
                                                    text_color='black',
                                                    font=CTkFont(size=30, family='B Nazanin'),
                                                    placeholder_text='آیدی پیمانکار را وارد کنید',
                                                    justify='right'
                                                    )
        self.show_con_entry.pack(pady=(15, 0))

        self.show_con_btn = customtkinter.CTkButton(self.frame_8,
                                                   fg_color='#1E90FF',
                                                   corner_radius=13,
                                                   text='search',
                                                   font=CTkFont(family='Arial', size=30),
                                                   text_color='white',
                                                   hover_color='#2079D2',
                                                   height=50,
                                                   command=self.search_cont
                                                   )
        self.show_con_btn.pack(pady=(20,0))

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=3)
        self.grid_columnconfigure(3, weight=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=15)
        self.grid_rowconfigure(2, weight=0)

    db_project = DBProject('Data/sarlak1404.db')

    # done_image = tkinter.PhotoImage(file='image/1.png')
    # not_done_image = tkinter.PhotoImage(file='image/0.png')
    def refresh(self):
        for item in self.data_table.get_children():
            self.data_table.delete(item)

        _data = self.db_project.show_data()
        for project in _data:

            project = list(project)
            ######################### edit contradiction
            try:
                _contradiction = int(project[5])
                _contradiction = _contradiction / int(project[4]) * 100
                project[5] = f'{int(_contradiction)}%'
            except ZeroDivisionError:
                project[5] = f'? %'

            ######################### adding ***,***
            for i in [3,4,6]:
                _copy = project[i]
                project.pop(i)
                _copy = f"{_copy:,}"
                project.insert(i,_copy)

            project[7] = bool(project[7])
            self.data_table.insert('', tkinter.END, values=project, tags='0')

    def set_entry(self):
        project = self.entry1.get()
        customer_id = self.entry2.get()
        estimate = self.entry3.get()
        estimate = estimate.replace('.', '')
        estimate = estimate.replace(',', '')
        date = self.entry4.get()
        date = date.replace("/","-")
        if project and estimate and customer_id:
            self.db_project.insert_into(project, customer_id, estimate, date)
            self.refresh()
            showinfo('good','completed!')
        else:
            showerror('empty entry!','you should fill <اسم پروژه> and <برآورد> and <آیدی مشتری>')

    def clear_entry(self):
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry3.delete(0,'end')
        self.entry4.delete(0,'end')

    def delete_project(self):
        _project = self.delete_entry.get()
        if _project == "":
            showerror('empty entry','you should enter something first!')
        elif _project.isnumeric():
            _data = self.db_project.get_data1(_project)
            if _data:
                if askokcancel('are you sure?','this action changes the main DataBase'):
                    self.db_project.delete_data1(_project)
                    showinfo('deleted', f'ID={self.delete_entry.get()} is successfully deleted')
                    self.delete_entry.delete(0, 'end')
                    self.refresh()
            else:
                showwarning(':/', f'ID={_project} not founded!')
        else:
            _data = self.db_project.get_data2(_project)
            if _data:
                if askokcancel('are you sure?','this action changes the main DataBase'):
                    self.db_project.delete_data2(_project)
                    showinfo('deleted',f'{self.delete_entry.get()} is successfully deleted')
                    self.delete_entry.delete(0,'end')
                    self.refresh()
            else:
                showwarning(':/',f'{_project} not founded!')

    def delete_selection(self):
        try:
            _selected = self.data_table.selection()[0]
            self.data_table.delete(_selected)
        except IndexError:
            pass

    def search_project(self):
        for item in self.data_table.get_children():
            self.data_table.delete(item)
        _name = self.search_entry1.get()
        if _name.isnumeric():
            _data = self.db_project.search_data1(_name)
        else:
            _data = self.db_project.search_data2(_name)
        _number = 0
        try:
            for data in _data:

                data = list(data)
                #########################  edit contradiction
                try:
                    _contradiction = int(data[5])
                    _contradiction = _contradiction / int(data[4]) * 100
                    data[5] = f'{int(_contradiction)}%'
                except ZeroDivisionError:
                    data[5] = f'? %'

                ######################### adding ***,***
                for i in [3, 4, 6]:
                    _copy = data[i]
                    data.pop(i)
                    _copy = f"{_copy:,}"
                    data.insert(i, _copy)

                data[7] = bool(data[7])
                _number += 1
                if data[5][0] == '-':
                    self.data_table.insert('', tkinter.END, values=data, text='ضرر', tags='1')
                elif data[5] == '0%' or data[5] == '? %':
                    self.data_table.insert('', tkinter.END, values=data, text='بی سود و زیان', tags='3')
                else:
                    self.data_table.insert('', tkinter.END, values=data, text='سود', tags='2')
            if _number == 0:
                raise TypeError
            showinfo('successful', f'{_number} item is founded')

        except TypeError:
            showwarning('oops', 'nothing founded!')

    def search_cont(self):
        _id = self.show_con_entry.get()
        if _id:
            _data = self.db_project.search_data3(_id)
            if not _data:
                showwarning('oops', 'nothing founded!')
                return 0
            _text = f"project_id={_id}\n{len(_data)} item founded:\n"
            for i in _data:
                _text = _text + (f"$ id={i[0]}\tname={i[1]}\n")
            showinfo("sucsuccessfuly founded!",_text)
        else:
            showerror('empty entry','you should enter something first!')

    def add_cost_or_paid(self):
        _text = self.debt_or_paid.get()
        _money = self.debt_or_paid_entry.get()
        _money = _money.replace('.','')
        _money = _money.replace(',','')
        try:
            _selection = self.data_table.selection()[0]
            _options = self.data_table.item(_selection, option='values')
            if _text == 'هزینه' and _money:
                if askokcancel('are you sure?','this action changes the main DataBase'):
                    _paid = int(_options[6].replace(',',''))
                    _cost = int(_money)
                    _contradiction = _paid - _cost
                    self.db_project.change_data1(_money,_options[0])
                    self.db_project.update_data1(_options[0],_contradiction)
                    self.db_project.update_data2(_options[0])
                    self.refresh()
            elif _text == 'پرداختی' and _money:
                if askokcancel('are you sure?','this action changes the main DataBase'):
                    _paid = int(_money)
                    _cost = int(_options[4].replace(',', ''))
                    _contradiction = _paid - _cost
                    self.db_project.change_data2(_money, _options[0])
                    self.db_project.update_data1(_options[0], _contradiction)
                    self.db_project.update_data2(_options[0])
                    self.refresh()
            else:
                showwarning('not allowed!',"debt/paid can't be empty")
        except IndexError:
            showerror('oops','please select something from table first!')

    def set_income(self):
        _dict = {}
        _data = self.db_project.show_income()
        for data in _data:
            _income = data[0]
            _income = int(_income)
            _income /= 10000000
            _income = round(_income,2)

            _date = data[1]
            _date = _date.split('-')
            _date = int(_date[1])

            try:
                _dict[_date] = _income + _dict.get(_date)
            except TypeError:
                _dict[_date] = _income

        return _dict.items()