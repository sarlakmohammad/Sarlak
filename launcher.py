from customtkinter import *
from contractor import Contractor
from customer import Customer
from project import Project

#window_panel
window = CTk()
window.title("taher sarlak")
window.iconbitmap('icon/2.ico')

width =  window.winfo_screenwidth()
height = window.winfo_screenheight()
window.minsize(width,height)
window.geometry(f"{width}x{height}+0+0")

window.grid_columnconfigure(0,weight=1)
window.grid_rowconfigure(0,weight=1)
window.grid_rowconfigure(1,weight=21)

#variabels

#functions

#vigets
mode_changer = CTkTabview(window,
                          anchor='n',
                          fg_color="white",

                          )
mode_changer.add('customer')
mode_changer.tab('customer').grid_columnconfigure(0,weight=1)
mode_changer.tab('customer').grid_rowconfigure(0,weight=1)


mode_changer.add('contractor')
mode_changer.tab('contractor').grid_columnconfigure(0,weight=1)
mode_changer.tab('contractor').grid_rowconfigure(0,weight=1)

mode_changer.insert(0,'projects')
mode_changer.tab('projects').grid_columnconfigure(0,weight=1)
mode_changer.tab('projects').grid_rowconfigure(0,weight=1)

mode_changer.insert(3,'factors')
mode_changer.tab('factors').grid_columnconfigure(0,weight=1)
mode_changer.tab('factors').grid_rowconfigure(0,weight=1)

contractor_frame = Contractor(mode_changer.tab('contractor'))
customer_frame = Customer(mode_changer.tab('customer'))
project_frame = Project(mode_changer.tab('projects'))

#operate
mode_changer.set('factors')

#pack
mode_changer.grid(column=0,row=0,sticky='nsew',rowspan=2)
contractor_frame.grid(column=0,row=0,sticky='nsew')
customer_frame.grid(column=0,row=0,sticky='nsew')
project_frame.grid(column=0,row=0,sticky='nsew')

if __name__=='__main__':
    window.after(0, lambda: window.wm_state('zoomed'))
    window.mainloop()