#Copyright (c) 2025 @sarlakmohammad
    #All rights reserved

import customtkinter
from customtkinter import CTkFont
import tkinter
from tkinter import ttk, StringVar
from tkinter.messagebox import showerror,showinfo,askokcancel
from database_FacCus import DBFacCus
from database_FacCont import DBFacCont
from BackUp import back_up
from PIL import Image

class Factor(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=0)
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=5)
        self.grid_rowconfigure(2,weight=0)

        ####################################### column 0
        self.frame_1 = customtkinter.CTkFrame(self,
                                            #   width=350,
                                            #   height=110,
                                              fg_color='#19A556'
                                              )
        self.frame_1.grid(column=0, row=0, sticky='nsew')

        self.frame_2 = customtkinter.CTkFrame(self,
                                            #   width=350,
                                            #   height=955,
                                              fg_color='#DBFFCB'
                                              )
        self.frame_2.grid(column=0, row=1, sticky='nsew', rowspan=2)
        ###################################### column 1
        self.frame_3 = customtkinter.CTkFrame(self,
                                            #   width=1000,
                                            #   height=110,
                                              fg_color='#F5DEB3'
                                              )
        self.frame_3.grid(column=1, row=0, sticky='nsew')
        self.frame_3.grid_columnconfigure(0,weight=2)
        self.frame_3.grid_columnconfigure(1,weight=1)
        self.frame_3.grid_columnconfigure(2,weight=1)
        self.frame_3.grid_columnconfigure(3,weight=2)
        self.frame_3.grid_rowconfigure(0,weight=1)

        self.frame_4 = customtkinter.CTkFrame(self,
                                            #   width=1000,
                                            #   height=500,
                                              fg_color='red'
                                              )
        self.frame_4.grid(column=1, row=1, sticky='nsew')
        self.frame_4.grid_columnconfigure(0,weight=1)
        self.frame_4.grid_rowconfigure(0,weight=1)

        self.tab_frame = customtkinter.CTkTabview(self,
                                                #   width=1000,
                                                #   height=455,
                                                  fg_color='#606060'
                                                  )
        self.tab_frame.grid(column=1, row=2, sticky='nsew')
        #
        self.tab_frame.add('factor')
        self.tab_frame.tab('factor').grid_rowconfigure(0,weight=1)
        self.tab_frame.tab('factor').grid_columnconfigure(0,weight=1)
        self.tab_frame.tab('factor').grid_columnconfigure(1,weight=1)
        self.tab_frame.tab('factor').grid_columnconfigure(2,weight=1)
        #
        self.tab_frame.add('...')
        ###################################### column 2
        self.frame_5 = customtkinter.CTkFrame(self,
                                            #   width=350,
                                            #   height=110,
                                              fg_color='#74899E'
                                              )
        self.frame_5.grid(column=2, row=0, sticky='nsew')

        self.frame_6 = customtkinter.CTkFrame(self,
                                            #   width=350,
                                            #   height=955,
                                              fg_color='#DBE8F7'
                                              )
        self.frame_6.grid(column=2, row=1, sticky='nsew', rowspan=2)
        ########################################################### vigets
        ################################################################### column 0
        self.cus_title = customtkinter.CTkLabel(self.frame_1,
                                               text='ثبت فاکتور',
                                               font=CTkFont(family='B Nazanin', size=30, weight='bold'),
                                               text_color="black"
                                               )
        self.cus_title.pack(pady=8,padx=5)
        ####
        self.cus_txt1 = customtkinter.CTkLabel(self.frame_2,
                                              text='شماره فاکتور',
                                              font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                              text_color='black'
                                              )
        self.cus_txt1.pack(pady=5,padx=5)

        self.cus_entry1 = customtkinter.CTkEntry(self.frame_2,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250
                                                 )
        self.cus_entry1.pack(pady=(0,10),padx=5)
        ####
        self.cus_txt2 = customtkinter.CTkLabel(self.frame_2,
                                              text='تاریخ فاکتور',
                                              font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                              text_color='black'
                                              )
        self.cus_txt2.pack(pady=5,padx=5)

        self.cus_entry2 = customtkinter.CTkEntry(self.frame_2,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250,
                                                 placeholder_text='1404/01/01'
                                                 )
        self.cus_entry2.pack(pady=(0,10),padx=5)
        ####
        self.cus_txt3 = customtkinter.CTkLabel(self.frame_2,
                                              text='آیدی مشتری',
                                              font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                              text_color='black'
                                              )
        self.cus_txt3.pack(pady=5,padx=5)

        self.cus_entry3 = customtkinter.CTkEntry(self.frame_2,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250
                                                 )
        self.cus_entry3.pack(pady=(0,10),padx=5)
        ####
        self.cus_txt4 = customtkinter.CTkLabel(self.frame_2,
                                              text='آیدی پروژه',
                                              font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                              text_color='black'
                                              )
        self.cus_txt4.pack(pady=5,padx=5)

        self.cus_entry4 = customtkinter.CTkEntry(self.frame_2,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250
                                                 )
        self.cus_entry4.pack(pady=(0,10),padx=5)
        ####
        self.cus_txt5 = customtkinter.CTkLabel(self.frame_2,
                                              text='مبلغ',
                                              font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                              text_color='black'
                                              )
        self.cus_txt5.pack(pady=5,padx=5)

        self.cus_entry5 = customtkinter.CTkEntry(self.frame_2,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250
                                                 )
        self.cus_entry5.pack(pady=(0,10),padx=5)
        ####
        self.cus_clear_btn = customtkinter.CTkButton(self.frame_2,
                                                     fg_color='#7C7C7C',
                                                     corner_radius=50,
                                                     text='خالی کردن',
                                                     font=CTkFont(family='B Nazanin', size=30),
                                                     text_color='white',
                                                     hover_color='#4E4E4E',
                                                     width=170,
                                                     command=self.clear_entry1
                                                     )
        self.cus_clear_btn.pack(pady=(10,0),padx=5)

        self.cus_submit_btn = customtkinter.CTkButton(self.frame_2,
                                                      fg_color='#008000',
                                                      corner_radius=50,
                                                      text='ثبت',
                                                      font=CTkFont(family='B Nazanin', size=30),
                                                      text_color='white',
                                                      hover_color='#005B00',
                                                      height=40,
                                                      width=170,
                                                      command=self.set_entry1
                                                      )
        self.cus_submit_btn.pack(pady=(10,0),padx=5)
        #################################################################### column 1
        self.Income_btn = customtkinter.CTkButton(self.frame_3,
                                                 fg_color='#2E8B57',
                                                 corner_radius=50,
                                                 text='Income',
                                                 font=CTkFont(family='Arial', size=30, weight='bold'),
                                                 text_color='white',
                                                 hover_color='#247045',
                                                 # command=
                                                 )
        self.Income_btn.grid(column=0, row=0)

        self.refresh_btn = customtkinter.CTkButton(self.frame_3,
                                                 fg_color='#4682B4',
                                                 corner_radius=50,
                                                 text='refresh',
                                                 font=CTkFont(family='Arial', size=30, weight='bold'),
                                                 text_color='white',
                                                 hover_color='#39698E',
                                                 command=self.refresh
                                                 )
        self.refresh_btn.grid(column=1, row=0, padx=(15,0))

        self.delete_selection_btn = customtkinter.CTkButton(self.frame_3,
                                                   fg_color='#CC0000',
                                                   corner_radius=50,
                                                   text='delete',
                                                   font=CTkFont(family='Arial', size=30, weight='bold'),
                                                   text_color='white',
                                                   hover_color='#990000',
                                                   command=self.delete_selection
                                                   )
        self.delete_selection_btn.grid(column=2, row=0, padx=(0,15))

        self.backup_btn = customtkinter.CTkButton(self.frame_3,
                                                   fg_color='#667686',
                                                   corner_radius=50,
                                                   text='BackUp',
                                                   font=CTkFont(family='Arial', size=30, weight='bold'),
                                                   text_color='white',
                                                   hover_color='#4E5862',
                                                   command=back_up
                                                   )
        self.backup_btn.grid(column=3, row=0)
        ####
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

        self.column = ['id', "شماره", "تاریخ", "طرف حساب", "آیدی پروژه", "هزینه", "وضعیت"]
        self.data_table = ttk.Treeview(self.frame_4,
                                       columns=self.column,
                                       selectmode='browse',
                                       height=12
                                       )
        self.data_table.grid(column=0, row=0, sticky='nsew')
        self.data_table.column('id', width=100, minwidth=0, anchor='center')
        self.data_table.heading('id', text='ID')
        self.data_table.column("شماره", width=250, minwidth=0, anchor='center')
        self.data_table.heading("شماره", text="شماره فاکتور")
        self.data_table.column("تاریخ", width=250, minwidth=0, anchor='center')
        self.data_table.heading("تاریخ", text="تاریخ")
        self.data_table.column("طرف حساب", width=250, minwidth=0, anchor='center')
        self.data_table.heading("طرف حساب", text="طرف حساب")
        self.data_table.column("آیدی پروژه", width=250, minwidth=0, anchor='center')
        self.data_table.heading("آیدی پروژه", text="پروژه")
        self.data_table.column("هزینه", width=250, minwidth=0, anchor='center')
        self.data_table.heading("هزینه", text="هزینه")
        self.data_table.column("وضعیت", width=100, minwidth=0, anchor='center')
        self.data_table.heading("وضعیت", text="وضعیت")

        self.data_table.tag_configure('0', font=CTkFont(family='B Nazanin', size=35), background='#1D5BB9')
        self.data_table.tag_configure('1', font=CTkFont(family='B Nazanin', size=35), background='#C00202')
        self.data_table.tag_configure('2', font=CTkFont(family='B Nazanin', size=35), background='#0DBC07')

        ########
        self.fac_frame1 = customtkinter.CTkFrame(self.tab_frame.tab('factor'),
                                                 fg_color='#FFFFCC'
                                                 )
        self.fac_frame1.grid(column=0, row=0, sticky='nsew')

        self.fac_txt1 = customtkinter.CTkLabel(self.fac_frame1,
                                               font=CTkFont(family='B Nazanin', size=30, weight='bold'),
                                               text='پیداکردن فاکتور',
                                               text_color='black'
                                               )
        self.fac_txt1.pack(pady=(5,0))

        self.fac_entry1 = customtkinter.CTkEntry(self.fac_frame1,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 height=50,
                                                 width=250,
                                                 text_color='black',
                                                 font=CTkFont(size=25, family='Arial'),
                                                 placeholder_text='factor ID',
                                                 )
        self.fac_entry1.pack(pady=15)

        self.fac_btn1 = customtkinter.CTkButton(self.fac_frame1,
                                                fg_color='#CEC109',
                                                corner_radius=50,
                                                text='search',
                                                font=CTkFont(family='Arial', size=30),
                                                text_color='white',
                                                hover_color='#AFA40B',
                                                command=self.search_factor
                                                )
        self.fac_btn1.pack()
        ####
        self.fac_frame2 = customtkinter.CTkFrame(self.tab_frame.tab('factor'),
                                                 fg_color='#98DADA'
                                                 )
        self.fac_frame2.grid(column=1,row=0,sticky='nsew')

        self.fac_var1 = StringVar(value='پیمانکار')
        self.fac_seg = customtkinter.CTkSegmentedButton(self.fac_frame2,
                                                        values=['مشتری','پیمانکار'],
                                                        font=CTkFont(family='B Nazanin', size=30, weight='bold'),
                                                        height=30,
                                                        variable=self.fac_var1,
                                                        fg_color='white',
                                                        unselected_color='#A0A0A0',
                                                        unselected_hover_color='#808080',
                                                        selected_color='#0054C3',
                                                        selected_hover_color='#0046A1',
                                                        text_color='white'
                                                        )
        self.fac_seg.pack()

        self.fac_image = customtkinter.CTkImage(Image.open('image/change2.png'),size=(100,100))
        self.fac_btn2 = customtkinter.CTkButton(self.fac_frame2,
                                                image=self.fac_image,
                                                width=100,
                                                height=100,
                                                text='تغییر وضعیت',
                                                font=CTkFont(family='B Nazanin', size=35, weight='bold'),
                                                compound='right',
                                                text_color='black',
                                                fg_color='#14A2A2',
                                                hover_color='#127D7D',
                                                command=self.change_state
                                                )
        self.fac_btn2.pack(pady=15)
        ####
        self.fac_frame3 = customtkinter.CTkFrame(self.tab_frame.tab('factor'),
                                                 fg_color='#FF9999'
                                                 )
        self.fac_frame3.grid(column=2, row=0, sticky='nsew')

        self.fac_txt2 = customtkinter.CTkLabel(self.fac_frame3,
                                               font=CTkFont(family='B Nazanin', size=30, weight='bold'),
                                               text='حذف کردن فاکتور',
                                               text_color='black'
                                               )
        self.fac_txt2.pack(pady=(5,0))

        self.fac_entry2 = customtkinter.CTkEntry(self.fac_frame3,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 height=50,
                                                 width=250,
                                                 text_color='black',
                                                 font=CTkFont(size=25, family='Arial'),
                                                 placeholder_text='factor ID',
                                                 )
        self.fac_entry2.pack(pady=11)

        self.fac_btn2 = customtkinter.CTkButton(self.fac_frame3,
                                                fg_color='#FF0000',
                                                corner_radius=50,
                                                text='حذف',
                                                font=CTkFont(family='B Nazanin', size=30),
                                                text_color='white',
                                                hover_color='#CC0000',
                                                command=self.delete_factor
                                                )
        self.fac_btn2.pack()
        ################################################################ column 2
        self.cont_title = customtkinter.CTkLabel(self.frame_5,
                                                text='ثبت صورت حساب',
                                                font=CTkFont(family='B Nazanin', size=30, weight='bold'),
                                                text_color="black"
                                                )
        self.cont_title.pack(pady=8,padx=5)
        ####
        self.cont_txt1 = customtkinter.CTkLabel(self.frame_6,
                                               text='شماره فاکتور',
                                               font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                               text_color='black'
                                               )
        self.cont_txt1.pack(pady=5,padx=5)

        self.cont_entry1 = customtkinter.CTkEntry(self.frame_6,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250
                                                 )
        self.cont_entry1.pack(pady=(0, 10),padx=5)
        ####
        self.cont_txt2 = customtkinter.CTkLabel(self.frame_6,
                                               text='تاریخ فاکتور',
                                               font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                               text_color='black'
                                               )
        self.cont_txt2.pack(pady=5,padx=5)

        self.cont_entry2 = customtkinter.CTkEntry(self.frame_6,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250,
                                                 placeholder_text='1404/01/01'
                                                 )
        self.cont_entry2.pack(pady=(0, 10),padx=5)
        ####
        self.cont_txt3 = customtkinter.CTkLabel(self.frame_6,
                                               text='آیدی پیمانکار',
                                               font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                               text_color='black'
                                               )
        self.cont_txt3.pack(pady=5,padx=5)

        self.cont_entry3 = customtkinter.CTkEntry(self.frame_6,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250
                                                 )
        self.cont_entry3.pack(pady=(0, 10),padx=5)
        ####
        self.cont_txt4 = customtkinter.CTkLabel(self.frame_6,
                                               text='آیدی پروژه',
                                               font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                               text_color='black'
                                               )
        self.cont_txt4.pack(pady=5,padx=5)

        self.cont_entry4 = customtkinter.CTkEntry(self.frame_6,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250
                                                 )
        self.cont_entry4.pack(pady=(0, 10),padx=5)
        ####
        self.cont_txt5 = customtkinter.CTkLabel(self.frame_6,
                                               text='مبلغ',
                                               font=CTkFont(family='B Nazanin', size=40, weight='bold'),
                                               text_color='black'
                                               )
        self.cont_txt5.pack(pady=5,padx=5)

        self.cont_entry5 = customtkinter.CTkEntry(self.frame_6,
                                                 corner_radius=10,
                                                 fg_color='white',
                                                 text_color='black',
                                                 font=CTkFont(size=25),
                                                 height=35,
                                                 width=250
                                                 )
        self.cont_entry5.pack(pady=(0, 10),padx=5)
        ####
        self.cont_clear_btn = customtkinter.CTkButton(self.frame_6,
                                                     fg_color='#7C7C7C',
                                                     corner_radius=50,
                                                     text='خالی کردن',
                                                     font=CTkFont(family='B Nazanin', size=30),
                                                     text_color='white',
                                                     hover_color='#4E4E4E',
                                                     width=170,
                                                     command=self.clear_entry2
                                                     )
        self.cont_clear_btn.pack(pady=(10, 0), padx=5)

        self.cont_submit_btn = customtkinter.CTkButton(self.frame_6,
                                                      fg_color='#008000',
                                                      corner_radius=50,
                                                      text='ثبت',
                                                      font=CTkFont(family='B Nazanin', size=30),
                                                      text_color='white',
                                                      hover_color='#005B00',
                                                      height=40,
                                                      width=170,
                                                      command=self.set_entry2
                                                      )
        self.cont_submit_btn.pack(pady=(10, 0),padx=5)

    db_FacCus = DBFacCus('Data/sarlak1404.db')
    db_FacCont = DBFacCont('Data/sarlak1404.db')

    def check_fac_type(self):
        _type = self.fac_seg.get()
        if _type == 'پیمانکار':
            return True
        else:
            return False

    def refresh(self):
        for item in self.data_table.get_children():
            self.data_table.delete(item)

        if self.check_fac_type():
            _data = self.db_FacCont.show_data()
            for contractor in _data:
                ######################### adding ***,***
                contractor = list(contractor)
                contractor[-2] = f'{contractor[-2]:,}'
                ######################### replace _ with /
                contractor[2] = contractor[2].replace('-','/')

                self.data_table.insert('', tkinter.END, values=contractor, tags='0')
        else:
            _data = self.db_FacCus.show_data()
            for customer in _data:
                ######################### adding ***,***
                customer = list(customer)
                customer[-2] = f'{customer[-2]:,}'
                ######################### replace _ with /
                customer[2] = customer[2].replace('-','/')

                self.data_table.insert('', tkinter.END, values=customer, tags='0')

    def set_entry2(self):
        factor = self.cont_entry1.get()
        date = self.cont_entry2.get()
        date = date.replace("/","-")
        contractor_id = self.cont_entry3.get()
        project_id = self.cont_entry4.get()
        cost = self.cont_entry5.get()
        cost = cost.replace(',','')
        cost = cost.replace('.','')
        if factor and contractor_id and project_id:
            self.db_FacCont.insert_into(factor, date, contractor_id, project_id, cost)
            self.refresh()
            showinfo('good', 'completed!')
        else:
            showerror('empty!', 'you should fill <فاکتور> and <آیدی پیمانکار/پروژه>')

    def set_entry1(self):
        factor = self.cus_entry1.get()
        date = self.cus_entry2.get()
        date = date.replace("/", "-")
        customer_id = self.cus_entry3.get()
        project_id = self.cus_entry4.get()
        cost = self.cus_entry5.get()
        cost = cost.replace(',', '')
        cost = cost.replace('.', '')
        if factor and customer_id and project_id:
            self.db_FacCus.insert_into(factor, date, customer_id, project_id, cost)
            self.refresh()
            showinfo('good', 'completed!')
        else:
            showerror('empty!', 'you should fill <فاکتور> and <آیدی مشتری/پروژه>')

    def clear_entry2(self):
        self.cont_entry1.delete(0,'end')
        self.cont_entry2.delete(0,'end')
        self.cont_entry3.delete(0,'end')
        self.cont_entry4.delete(0,'end')
        self.cont_entry5.delete(0,'end')

    def clear_entry1(self):
        self.cus_entry1.delete(0,'end')
        self.cus_entry2.delete(0,'end')
        self.cus_entry3.delete(0,'end')
        self.cus_entry4.delete(0,'end')
        self.cus_entry5.delete(0,'end')

    def delete_selection(self):
        try:
            _selected = self.data_table.selection()[0]
            self.data_table.delete(_selected)
        except IndexError:
            pass

    def delete_factor(self):
        _text = self.fac_entry2.get()
        try:
            if _text == "" or not _text.isnumeric():
                showerror('wrong entry!','*fill the entry* or *use numbers*')
                return -1
            if askokcancel('are you sure?','this action changes the main DataBase'):
                if self.check_fac_type():
                    self.db_FacCont.delete_data(_text)
                else:
                    self.db_FacCus.delete_data(_text)
                self.refresh()
        except TypeError:
            showerror('Not Founded!','factor not founded')

    def search_factor(self):
        for item in self.data_table.get_children():
            self.data_table.delete(item)

        _name = self.fac_entry1.get()
        _number = 0

        if self.check_fac_type():
            _data = self.db_FacCont.search_data(_name)
            for data in _data:
                ######################### adding ***,***
                data = list(data)
                data[-2] = f'{data[-2]:,}'
                ######################### replace _ with /
                data[2] = data[2].replace('-','/')

                _number += 1
                if data[-1] == 0:
                    self.data_table.insert('', tkinter.END, values=data, text='پرداخت نشده', tags='1')
                else:
                    self.data_table.insert('', tkinter.END, values=data, text='پرداخت شده', tags='2')
        else:
            _data = self.db_FacCus.search_data(_name)
            for data in _data:
                ######################### adding ***,***
                data = list(data)
                data[-2] = f'{data[-2]:,}'
                ######################### replace _ with /
                data[2] = data[2].replace('-','/')

                _number += 1
                if data[-1] == 0:
                    self.data_table.insert('', tkinter.END, values=data, text='پرداخت نشده', tags='1')
                else:
                    self.data_table.insert('', tkinter.END, values=data, text='پرداخت شده', tags='2')

    def change_state(self):
        try:
            _selection = self.data_table.selection()[0]
            _options = self.data_table.item(_selection, option='values')
            _factor_id = _options[0]
            if self.check_fac_type():
                self.db_FacCont.change_state(_factor_id)
            else:
                self.db_FacCus.change_state(_factor_id)
            self.refresh()
        except IndexError:
            pass