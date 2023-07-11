from tkinter import *


def mainwindow(w,h):
    window = Tk()
    x = window.winfo_screenwidth()/2 - w/2
    y = window.winfo_screenheight()/2 - h/2
    window.geometry("%dx%d+%d+%d"%(w,h,x,y))
    window.title("กินกาแฟ by นู๋อ้อ")
    window.option_add("*font","Tahoma 12")
    window.config(bg='#FFCAD4')
    window.resizable(False,False)
    return window

def createFrame_login(window):
    frame_login = Frame(window,bg='#FFCAD4')
    frame_login.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_login

def createFrame_home(window):
    frame_home = Frame(window,bg='#FFCAD4')
    frame_home.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_home

def createFrame_registerEmployee(window):
    frame_registerEmployee  = Frame(window,bg='#FFCAD4')
    frame_registerEmployee.place(relx=0,rely=0,relheight=1,relwidth=1)
    frame_registerEmployee.rowconfigure((0,2,4,6,7,8),weight=1)
    # frame_registerEmployee.rowconfigure((1,3,5),weight=0)
    # frame_registerEmployee.columnconfigure((0,1),weight=2)
    return frame_registerEmployee

def createFrame_editEmployee(window):
    frame_editEmployee  = Frame(window,bg='#FFCAD4')
    frame_editEmployee.place(relx=0,rely=0,relheight=1,relwidth=1)
    frame_editEmployee.rowconfigure((0,2,4,6,7,8),weight=1)
    # frame_registerEmployee.rowconfigure((1,3,5),weight=0)
    # frame_registerEmployee.columnconfigure((0,1),weight=2)
    return frame_editEmployee

def createFrame_registerMember(window):
    frame_registerMember  = Frame(window,bg='#FFCAD4')
    frame_registerMember.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_registerMember

def createFrame_editMember(window):
    frame_editMember  = Frame(window,bg='#FFCAD4')
    frame_editMember.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_editMember


def createFrame_confirmSelling(window):
    frame_confirmSelling  = Frame(window,bg='#FFCAD4')
    frame_confirmSelling.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_confirmSelling

def createFrame_historyWorking(window):
    frame_historyWorking  = Frame(window,bg='#FFCAD4')
    frame_historyWorking.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_historyWorking

def createFrame_customerManage(window):
    frame_customerManage  = Frame(window,bg='#FFCAD4')
    frame_customerManage.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_customerManage

def createFrame_employeeManage(window):
    frame_employeeManage  = Frame(window,bg='#FFCAD4')
    frame_employeeManage.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_employeeManage

def createFrame_stock(window):
    frame_stock  = Frame(window,bg='#FFCAD4')
    frame_stock.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_stock

def createFrame_manageListProduct(window):
    frame_manageListProduct  = Frame(window,bg='#FFCAD4')
    frame_manageListProduct.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_manageListProduct

def createFrame_RequisitionIngredients(window):
    frame_RequisitionIngredients  = Frame(window,bg='#FFCAD4')
    frame_RequisitionIngredients.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_RequisitionIngredients

def createFrame_orderIngredients(window):
    frame_orderIngredients  = Frame(window,bg='#FFCAD4')
    frame_orderIngredients.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_orderIngredients

def createFrame_printReport(window):
    frame_printReport  = Frame(window,bg='#FFCAD4')
    frame_printReport.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_printReport

def createFrame_printReport2(window):
    frame_printReport2 = Frame(window,bg="#FFCAD4")
    frame_printReport2.place(relx=0,rely=0,relheight=1,relwidth=1)
    return frame_printReport2