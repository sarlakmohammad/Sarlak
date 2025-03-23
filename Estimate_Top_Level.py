import customtkinter
from customtkinter import CTkFont

class Estimate(customtkinter.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry('700x700')

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)

        self.frame = {}
        self.entry = {}

        ###################### modify frames
        for i in range(1, 22):
            self.frame[f'frame_{i}'] = customtkinter.CTkFrame(self,
                                             width=180,
                                             height=180,
                                             fg_color='white'
                                             )
            self.frame[f'frame_{i}'].grid( column=(i-1)%5, row=(i-1)//5, sticky='nsew')

        self.frame['frame_22'] =customtkinter.CTkFrame(self,
                                             width=180,
                                             height=180,
                                             fg_color='white'
                                             )
        self.frame['frame_22'].grid(column=4,row=4,sticky='nsew')

        ###################### modify labels
        self.txt_1 = customtkinter.CTkLabel(self.frame['frame_1'],
                                                  text='کاغذ جلد',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_1.pack(pady=10)
        #####################################################
        self.txt_2 = customtkinter.CTkLabel(self.frame['frame_2'],
                                                  text='کاغذ داخل',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_2.pack(pady=10)
        #####################################################
        self.txt_3 = customtkinter.CTkLabel(self.frame['frame_3'],
                                                  text='فیلم',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_3.pack(pady=10)
        #####################################################
        self.txt_4 = customtkinter.CTkLabel(self.frame['frame_4'],
                                                  text='زینک',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_4.pack(pady=10)
        #####################################################
        self.txt_5 = customtkinter.CTkLabel(self.frame['frame_5'],
                                                  text='چاپ',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_5.pack(pady=10)
        #####################################################
        self.txt_6 = customtkinter.CTkLabel(self.frame['frame_6'],
                                                  text='اطلاعات متغیر',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_6.pack(pady=10)
        #####################################################
        self.txt_7 = customtkinter.CTkLabel(self.frame['frame_7'],
                                                  text='شابلون',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_7.pack(pady=10)
        #####################################################
        self.txt_8 = customtkinter.CTkLabel(self.frame['frame_8'],
                                                  text='سلفون',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_8.pack(pady=10)
        #####################################################
        self.txt_9 = customtkinter.CTkLabel(self.frame['frame_9'],
                                                  text='یووی',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_9.pack(pady=10)
        #####################################################
        self.txt_10 = customtkinter.CTkLabel(self.frame['frame_10'],
                                                  text='قالب',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_10.pack(pady=10)
        #####################################################
        self.txt_11 = customtkinter.CTkLabel(self.frame['frame_11'],
                                                  text='دایکات',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_11.pack(pady=10)
        #####################################################
        self.txt_12 = customtkinter.CTkLabel(self.frame['frame_12'],
                                                  text='برش',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_12.pack(pady=10)
        #####################################################
        self.txt_13 = customtkinter.CTkLabel(self.frame['frame_13'],
                                                  text='صحافی',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_13.pack(pady=10)
        #####################################################
        self.txt_14 = customtkinter.CTkLabel(self.frame['frame_14'],
                                                  text='بسته بندی',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_14.pack(pady=10)
        #####################################################
        self.txt_15 = customtkinter.CTkLabel(self.frame['frame_15'],
                                                  text='عملیات تکمیلی',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_15.pack(pady=10)
        #####################################################
        self.txt_16 = customtkinter.CTkLabel(self.frame['frame_16'],
                                                  text='کاغذ کاور',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_16.pack(pady=10)
        #####################################################
        self.txt_17 = customtkinter.CTkLabel(self.frame['frame_17'],
                                                  text='چسب',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_17.pack(pady=10)
        #####################################################
        self.txt_18 = customtkinter.CTkLabel(self.frame['frame_18'],
                                                  text='کلیشه',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_18.pack(pady=10)
        #####################################################
        self.txt_19 = customtkinter.CTkLabel(self.frame['frame_19'],
                                                  text='طلاکوب',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_19.pack(pady=10)
        #####################################################
        self.txt_20 = customtkinter.CTkLabel(self.frame['frame_20'],
                                                  text='برجسته',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_20.pack(pady=10)
        #####################################################
        self.txt_21 = customtkinter.CTkLabel(self.frame['frame_21'],
                                                  text='متفرقه',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_21.pack(pady=10)
        #####################################################
        self.txt_22 = customtkinter.CTkLabel(self.frame['frame_22'],
                                                  text='...',
                                                  text_color='black',
                                                  font=CTkFont(family='B Nazanin',size=25)
                                                  )
        self.txt_22.pack(pady=10)


        self.submit_btn = customtkinter.CTkButton(self,
                                                  fg_color='#008000',
                                                  hover_color='#006400',
                                                  text='تایید',
                                                  font=CTkFont(family='B Nazanin',size=60),
                                                  command=self.get_estimate
                                                  )
        self.submit_btn.grid(column=1,row=4,columnspan=3,sticky='nsew')

        ###################### modify entries
        for i in range(1, 23):
            self.entry[f'entry_{i}'] = self.entry_22 = customtkinter.CTkEntry(self.frame[f'frame_{i}'],
                                                                              fg_color='white',
                                                                              width=130,
                                                                              height=30,
                                                                              font=CTkFont('Arial', size=20),
                                                                              text_color='black'
                                                                              )
            self.entry[f'entry_{i}'].pack(pady=5)


    estimate = 0
    def get_estimate(self):
        self.estimate = 0
        for i in range(1,23):
            try:
                _money = self.entry[f'entry_{i}'].get()
                _money = _money.replace(',','')
                _money = _money.replace('.','')
                _money = int(_money)
                self.estimate += _money
            except ValueError:
                pass
        self.destroy()