from customtkinter import *
from contractor import Contractor
from customer import Customer
from project import Project
from Estimate_Top_Level import Estimate
from factor import Factor
from Income import open_income_page

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
toplevel_window = None

#functions
def open_toplevel():
    project_frame.entry3.focus()
    project_frame.entry3.delete(0,END)

    global toplevel_window
    if toplevel_window is None or not toplevel_window.winfo_exists():
        toplevel_window = Estimate(window)
        toplevel_window.title('برآورد')
    else:
        toplevel_window.focus()

def switch_mod(event):
    _name = mode_changer.get()
    _index = mode_changer.index(_name)
    if event.delta == 120:
        if _index == 0:
            mode_changer.set('customer')
        elif _index == 1:
            mode_changer.set('contractor')
        elif _index == 2:
            mode_changer.set('factors')
        else:
            mode_changer.set('projects')
    else:
        if _index == 0:
            mode_changer.set('factors')
        elif _index == 1:
            mode_changer.set('projects')
        elif _index == 2:
            mode_changer.set('customer')
        else:
            mode_changer.set('contractor')

def set_estimate(event):
    try:
        if not project_frame.entry3.get():
            project_frame.entry3.insert(0,toplevel_window.estimate)
    except AttributeError:
        pass

#vigets
mode_changer = CTkTabview(window,
                          anchor='n',
                          fg_color="white",
                          height=400
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
factor_frame = Factor(mode_changer.tab('factors'))

#operate
mode_changer.set('factors')
####
window.bind('<MouseWheel>',switch_mod)
project_frame.entry3.bind('<FocusIn>',set_estimate)
####
project_frame.estimate_btn.configure(command=open_toplevel)
####
def func():
    return open_income_page(project_frame.set_income())
factor_frame.Income_btn.configure(command=func)

#pack
mode_changer.grid(column=0,row=0,sticky='nsew',rowspan=2)
contractor_frame.grid(column=0,row=0,sticky='nsew')
customer_frame.grid(column=0,row=0,sticky='nsew')
project_frame.grid(column=0,row=0,sticky='nsew')
factor_frame.grid(column=0,row=0,sticky='nsew')

if __name__=='__main__':
    window.after(0, lambda: window.wm_state('zoomed'))
    window.mainloop()