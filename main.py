import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *  # Additional Import```
from calendar import calendar
from email.mime import image
from http.client import CONTINUE
from pydoc import locate
from tkinter import*
from tkinter import ttk
import tkinter as tk
import datetime
from tkcalendar import Calendar
from tkinter import messagebox
from connectDB import createconnection
from fetchTree import fetch_Tree
from tkinter import filedialog
from exportToDocx import (createDocxFile)
from createFrame import (mainwindow,createFrame_login,createFrame_home,createFrame_registerEmployee,createFrame_editEmployee,
                         createFrame_registerMember,createFrame_confirmSelling,createFrame_historyWorking,createFrame_customerManage,
                         createFrame_employeeManage,createFrame_stock,createFrame_manageListProduct,createFrame_RequisitionIngredients,
                         createFrame_orderIngredients,createFrame_printReport,createFrame_printReport2)

def widget_login():
    global frame_login,ety_username,ety_pwd
    frame_login = createFrame_login(window)
    Label(frame_login,image=photo_logo,bg='#FFCAD4').place(x=535,y=48)

    Label(frame_login,text="ชื่อผู้ใช้งาน :",font='tahoma 14 ',bg='#FFCAD4',fg='#9F8189').place(x=432,y=279)
    ety_username = Entry(frame_login,bg='#FFFFFF',font='tahoma 17 ',width=20,textvariable=userinfo)
    ety_username.place(x=432,y=321,width=415,height=60)

    Label(frame_login,text="รหัสผ่าน :",font='tahoma 14 ',bg='#FFCAD4',fg='#9F8189').place(x=432,y=399)
    ety_pwd = Entry(frame_login,bg='#FFFFFF',width=20,font='tahoma 17 ',show='*',textvariable=pwdinfo)
    ety_pwd.place(x=432,y=449,width=415,height=60)

    bt_login = Button(frame_login,text="เข้าสู่ระบบ",bg='#9F8189',fg='#FFE5D8',command=loginCallBack)
    bt_login.place(x=540,y=565,width=200,height=50)

def widget_home(): #ต้องทำ
    global pageNAME,userPERM
    global frame_home
    global ety_searchMenu
    global total
    global bt_edit_emplyee,bt_publish
    frame_home = createFrame_home(window)
    a = 0
    pageNAME = "HOME"
    Label(frame_home,image=photo_profile,text=" "+employee_name,bg='#FFCAD4',fg='#9F8189',compound=LEFT,font='tahoma 15 ').place(x=20,y=20)

    bt_edit_emplyee = Button(frame_home,text="จัดการบัญชีพนักงาน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_manageEmployee)
    bt_edit_emplyee.place(x=60,y=174,width=270,height=60)
    bt_edit_member = Button(frame_home,text="จัดการบัญชีสมาชิก",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_manageMember)
    bt_edit_member.place(x=60,y=265,width=270,height=60)
    bt_edit_stock = Button(frame_home,text="จัดการคลังวัตถุดิบ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_manageStock)
    bt_edit_stock.place(x=60,y=356,width=270,height=60)
    bt_edit_product = Button(frame_home,text="จัดการรายการสินค้า",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_manageListProduct)
    bt_edit_product.place(x=60,y=447,width=270,height=60)
    bt_publish = Button(frame_home,text="จัดพิมพ์รายงานการดำเนินงาน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_printReport)
    bt_publish.place(x=60,y=538,width=270,height=60)

    bt_search = Button(frame_home,image=photo_search,bg='#FBEEE6',fg='#9F8189',command=search_click)
    bt_search.place(x=691,y=44,width=52,height=50)
    ety_searchMenu = Entry(frame_home,bg='#FFFFFF',justify=CENTER)
    ety_searchMenu.place(x=498,y=44,width=200,height=50)
    bt_refresh = Button(frame_home,image=photo_refresh,bg='#FBEEE6',fg='#9F8189',command=(lambda: fetch_Tree(pageNAME,mytree_home1,cursor)))
    bt_refresh.place(x=754,y=44,width=52,height=50)

    Label(frame_home,text="ค้นหาจาก",font="tahoma 12 ",bg='#FFCAD4',fg='#9F8189').place(x=394,y=22)
    home_dropdown_clicked.set("ประเภท")
    option = OptionMenu(frame_home,home_dropdown_clicked,"ประเภท","ชื่อสินค้า")
    option.config(bg="#9F8189",fg='#ffffff',highlightthickness = 0)
    option.place(x=395,y=44,width=92,height=50)

    bt_reset = Button(frame_home,text="ยกเลิก",bg='#9F8189',fg='#FBEEE6',font='tahoma 14 bold',command=resetCallBack)
    bt_reset.place(x=837,y=596,width=100,height=60)
    bt_delete = Button(frame_home,text="ลบ",bg='#9F8189',fg='#FBEEE6',font='tahoma 14 bold',command=removeCallBack)
    bt_delete.place(x=985,y=596,width=100,height=60)
    bt_confirm = Button(frame_home,text="ยืนยัน",bg='#9F8189',fg='#FBEEE6',font='tahoma 14 bold',command=widget_confirmSelling)
    bt_confirm.place(x=1132,y=596,width=100,height=60)

    frame_total = Frame(frame_home,bg='#FFE5D8')
    frame_total.place(x=392,y=588,width=400,height=75)
    total = Label(frame_total,text="ยอดสุทธิ :         "+ str(a),font="tahoma 24 bold",bg='#FFE5D8',fg='#9F8189')
    total.place(x=16,y=10)
    Label(frame_total,text="บาท",font="tahoma 24 bold",bg='#FFE5D8',fg='#9F8189').place(x=324,y=10)

    bt_back = Button(frame_home,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
    bt_back.place(x=8,y=625,width=85,height=90)

    def widget_treeview_home1():
        global mytree_home1
        treeframe_home1 = Frame(frame_home,bg='#FFE5D8')
        treeframe_home1.place(x=392,y=148,height=400)
        style = ttk.Style(treeframe_home1)
        style.theme_use("default")
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
        style.configure("Treeview", rowheight=35)
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


        scrollbar = Scrollbar(treeframe_home1)
        scrollbar.pack(side=RIGHT,fill=Y)

        columns=("type","name","price")
        mytree_home1 = ttk.Treeview(treeframe_home1,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
        mytree_home1.pack()

        mytree_home1.heading("type",text="ประเภท",anchor='center')
        mytree_home1.heading("name",text="ชื่อสินค้า",anchor='center')
        mytree_home1.heading("price", text="ราคา (บาท)",anchor='center')

        mytree_home1.column("type",anchor='center',width=100)
        mytree_home1.column("name",anchor='center',width=200)
        mytree_home1.column("price",anchor='center',width=100)

        fetch_Tree(pageNAME,mytree_home1,cursor)
        mytree_home1.bind('<Double-1>',treeviewclick)
    widget_treeview_home1()

    def widget_treeview_home2():
        global mytree_home2
        treeframe_home2 = Frame(frame_home,bg='#FFE5D8')
        treeframe_home2.place(x=837,y=43,width=395,height=506)
        style = ttk.Style(treeframe_home2)
        style.theme_use("default")
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
        style.configure("Treeview", rowheight=45)
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        scrollbar = Scrollbar(treeframe_home2)
        scrollbar.pack(side=RIGHT,fill=Y)

        columns=("name","amount","price")
        mytree_home2 = ttk.Treeview(treeframe_home2,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
        mytree_home2.pack()

        mytree_home2.heading("name",text="ชื่อสินค้า",anchor='center')
        mytree_home2.heading("amount",text="จำนวน",anchor='center')
        mytree_home2.heading("price", text="ราคา (บาท)",anchor='center')

        mytree_home2.column("name",anchor='center',width=198)
        mytree_home2.column("amount",anchor='center',width=89)
        mytree_home2.column("price",anchor='center',width=89)

    widget_treeview_home2()

def widget_manageEmployee():
    global pageNAME,userPERM
    global frame_employeeManage
    global mytree
    global ety_search_employee1
    if userPERM == "พนักงาน" :
        # messagebox.showwarning("ระบบ:","ไม่มีสิทธิเข้าถึงในการใช้งาน")
        bt_edit_emplyee["state"] = DISABLED
    else :
        frame_employeeManage = createFrame_employeeManage(window)

        pageNAME = "MANAGE_EMPLOYEE"

        employee_name2info.set("")

        Label(frame_employeeManage,text="บัญชีพนักงาน",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=65,y=65)

        bt_registerEmployee = Button(frame_employeeManage,text="ลงทะเบียน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_registerEmployee)
        bt_registerEmployee.place(x=160,y=590,width=200,height=75)
        bt_editEmployee = Button(frame_employeeManage,text="แก้ไขจัดการ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_editEmployee)
        bt_editEmployee.place(x=410,y=590,width=200,height=75)
        bt_historyEmployee = Button(frame_employeeManage,text="ดูประวัติฯ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_historyWorking)
        bt_historyEmployee.place(x=660,y=590,width=200,height=75)
        bt_deleteEmployee = Button(frame_employeeManage,text="ลบบัญชีพนักงาน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=removeCallBack)
        bt_deleteEmployee.place(x=910,y=590,width=200,height=75)

        ety_search_employee1 = Entry(frame_employeeManage,width=30,justify=CENTER)
        ety_search_employee1.place(x=586,y=68,width=463,height=75)
        bt_search = Button(frame_employeeManage,image=photo_search,bg='#FBEEE6',fg='#9F8189',command=search_click)
        bt_search.place(x=1049,y=68,width=75,height=75)
        bt_refresh = Button(frame_employeeManage,image=photo_refresh,bg='#FBEEE6',fg='#9F8189',command=(lambda: fetch_Tree(pageNAME,mytree_employee1,cursor)))
        bt_refresh.place(x=1137,y=68,width=75,height=75)


        bt_back = Button(frame_employeeManage,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
        bt_back.place(x=8,y=625,width=85,height=90)

        Label(frame_employeeManage,text="ค้นหาจาก",font="tahoma 14 ",bg='#FFCAD4',fg='#9F8189').place(x=478,y=43)
        epy_dropdown_clicked.set("ชื่อ")
        option = OptionMenu(frame_employeeManage,epy_dropdown_clicked,"ชื่อ","นามสกุล","เพศ")
        option.config(bg="#9F8189",fg='#ffffff',highlightthickness = 0)
        option.place(x=478,y=68,width=100,height=75)

        def widget_treeview_employee():
            global mytree_employee1
            treeframe = Frame(frame_employeeManage,bg='#FFE5D8')
            treeframe.place(x=65,y=190,height=350)
            style = ttk.Style(treeframe)
            style.theme_use("default")
            style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
            style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
            style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
            style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

            scrollbar = Scrollbar(treeframe)
            scrollbar.pack(side=RIGHT,fill=Y)

            columns=("id","username","password","name","surName","gender","birth","phoneNumber","address")
            mytree_employee1 = ttk.Treeview(treeframe,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
            mytree_employee1.pack()

            mytree_employee1.heading("id",text="เลขบัตรประชาชน",anchor='center')
            mytree_employee1.heading("username",text="ชื่อผู้ใช้งาน",anchor='center')
            mytree_employee1.heading("password",text="รหัสผ่าน",anchor='center')
            mytree_employee1.heading("name",text="ชื่อ",anchor='center')
            mytree_employee1.heading("surName", text="นามสกุล",anchor='center')
            mytree_employee1.heading("gender",text="เพศ",anchor='center')
            mytree_employee1.heading("birth",text="วันเกิด",anchor='center')
            mytree_employee1.heading("phoneNumber", text="เบอร์โทรศัพท์",anchor='center')
            mytree_employee1.heading("gender", text="เพศ",anchor='center')
            mytree_employee1.heading("address", text="ที่อยู่",anchor='center')

            mytree_employee1.column("id",anchor='center',width=127)
            mytree_employee1.column("username",anchor='center',width=127)
            mytree_employee1.column("password",anchor='center',width=127)
            mytree_employee1.column("name",anchor='center',width=127)
            mytree_employee1.column("surName",anchor='center',width=127)
            mytree_employee1.column("gender",anchor='center',width=127)
            mytree_employee1.column("birth",anchor='center',width=127)
            mytree_employee1.column("phoneNumber",anchor='center',width=127)
            mytree_employee1.column("gender",anchor='center',width=127)
            mytree_employee1.column("address",anchor='center',width=127)

            fetch_Tree(pageNAME,mytree_employee1,cursor)
            mytree_employee1.bind('<Double-1>',treeviewclick)
        widget_treeview_employee()

def widget_historyWorking():
    global userpERM,pageNAME
    global frame_historyWorking
    global ety_search_history
    frame_historyWorking = createFrame_historyWorking(window)

    pageNAME = "HISTORY_EMPLOYEE"

    Label(frame_historyWorking,text="ประวัติการทำงาน",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=35,y=75)

    ety_search_history = Entry(frame_historyWorking,width=30,justify=CENTER,font='tahoma 20')
    ety_search_history.place(x=635,y=76,width=347,height=75)
    bt_search = Button(frame_historyWorking,image=photo_search,bg='#FBEEE6',fg='#9F8189',command=search_click)
    bt_search.place(x=982,y=76,width=85,height=75)
    bt_refresh = Button(frame_historyWorking,image=photo_refresh,bg='#FBEEE6',command=(lambda: fetch_Tree(pageNAME,mytree_employee2,cursor)))
    bt_refresh.place(x=1084,y=76,width=85,height=75)

    bt_back = Button(frame_historyWorking,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
    bt_back.place(x=8,y=625,width=85,height=90)

    Label(frame_historyWorking,text="ค้นหาจาก",font="tahoma 14 ",bg='#FFCAD4',fg='#9F8189').place(x=490,y=51)
    epy_dropdownhistory_clicked.set("เลขที่ออเดอร์")
    option = OptionMenu(frame_historyWorking,epy_dropdownhistory_clicked,"เลขที่ออเดอร์","ผู้ออกออเดอร์","วันที่ออเดอร์")
    option.config(bg="#9F8189",fg='#ffffff',highlightthickness = 0)
    option.place(x=490,y=76,width=130,height=75)


    def widget_treeview_history():
        global mytree_employee2
        treeframe = Frame(frame_historyWorking,bg='#FFE5D8')
        treeframe.place(x=154,y=203,height=418)
        style = ttk.Style(treeframe)
        style.theme_use("default")
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        scrollbar = Scrollbar(treeframe)
        scrollbar.pack(side=RIGHT,fill=Y)

        columns=("number_order","date_order","person_order","detail","totalPrice_order")
        mytree_employee2 = ttk.Treeview(treeframe,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
        mytree_employee2.pack()

        mytree_employee2.heading("number_order",text="เลขที่ออเดอร์",anchor='center')
        mytree_employee2.heading("date_order", text="วันที่ออเดอร์",anchor='center')
        mytree_employee2.heading("person_order", text="ผู้ออกออเดอร์",anchor='center')
        mytree_employee2.heading("detail", text="รายละเอียดออเดอร์",anchor='center')
        mytree_employee2.heading("totalPrice_order", text="ราคารวมออเดอร์",anchor='center')

        mytree_employee2.column("number_order",anchor='center',width=100)
        mytree_employee2.column("date_order",anchor='center',width=120)
        mytree_employee2.column("person_order",anchor='center',width=180)
        mytree_employee2.column("detail",anchor='center',width=460)
        mytree_employee2.column("totalPrice_order",anchor='center',width=145)
        
        fetch_Tree(pageNAME,mytree_employee2,cursor)

    widget_treeview_history()

def widget_registerEmployee():
    global userPERM,pageNAME
    global frame_registerEmployee
    global ety_calendar_employee_1 ,ety_address_employee_1,ety_Name_employee_1,ety_Id_employee_1,ety_phone_employee_1,ety_Username_employee_1,ety_surName_employee_1,ety_Pwd_employee_1,ety_NewPwd_employee_1
    frame_registerEmployee = createFrame_registerEmployee(window)

    pageNAME = "REGISTER_EMPLOYEE"

    Label(frame_registerEmployee,text="ลงทะเบียนพนักงาน",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=407,y=25)

    #left
    Label(frame_registerEmployee,text="ชื่อ (ภาษาไทย)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=119)
    ety_Name_employee_1 = Entry(frame_registerEmployee,width=30,textvariable=employee_name1info)
    ety_Name_employee_1.place(x=239,y=144,width=309,height=58)

    def validate1(P):
        if len(P) == 0:
            return True
        elif len(P) < 11 and P.isdigit():
            return True
        else:
            return False

    def validate2(P):
        if len(P) == 0:
            return True
        elif len(P) < 14 and P.isdigit():
            return True
        else:
            return False

    vcmd1 = (window.register(validate1), '%P')
    vcmd2 = (window.register(validate2), '%P')

    Label(frame_registerEmployee,text="เลขบัตรประชาชน (เลข 13 หลัก)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=226)
    ety_Id_employee_1 = Entry(frame_registerEmployee,width=30,textvariable=employee_id1info, validate="key", validatecommand=vcmd2)
    ety_Id_employee_1.place(x=239,y=252,width=309,height=58)
    Label(frame_registerEmployee,text="เบอร์โทรศัพท์ (เลข 10 หลัก) *",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=328)
    ety_phone_employee_1 = Entry(frame_registerEmployee,width=30,textvariable=employee_phone1info, validate="key", validatecommand=vcmd1)
    ety_phone_employee_1.place(x=239,y=353,width=309,height=58)
    Label(frame_registerEmployee,text="ชื่อผู้ใช้งาน",font="tahoma 16  ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=425)
    ety_Username_employee_1 = Entry(frame_registerEmployee,width=30,textvariable=employee_username1info)
    ety_Username_employee_1.place(x=239,y=454,width=309,height=58)
    Label(frame_registerEmployee,text="ที่อยู่",font="tahoma 16  ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=532)
    ety_address_employee_1 = Text(frame_registerEmployee,width=30)
    ety_address_employee_1.place(x=239,y=560,width=309,height=107)

    #right
    Label(frame_registerEmployee,text="นามสกุล (ภาษาไทย)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=119)
    ety_surName_employee_1 = Entry(frame_registerEmployee,width=30,textvariable=employee_surname1info)
    ety_surName_employee_1.place(x=732,y=144,width=309,height=58)
    Label(frame_registerEmployee,text="วัน/เดือน/ปี ที่เกิด",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=226)
    # frame_date_1 = Frame(frame_registerEmployee,width=30,bg='#FFFFFF')
    # frame_date_1.place(x=732,y=252,width=309,height=58)
    ety_calendar_employee_1 = Entry(frame_registerEmployee,width=30,state="readonly",textvariable=employee_date1info,readonlybackground='#FFFFFF')
    ety_calendar_employee_1.place(x=732,y=252,width=309,height=58)
    bt_date_1 = Button(frame_registerEmployee,image=photo_calendar,bg='#FFE5D8',command=popup_calendarRegisterEmployee)
    bt_date_1.place(x=976,y=253,width=65,height=57)
    Label(frame_registerEmployee,text="เพศ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=328)
    RadioButton_male_1 = Radiobutton(frame_registerEmployee, text = "ชาย", variable = employee_gender1info,value="ชาย",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
    RadioButton_male_1.place(x=745,y=363)
    RadioButton_female_1 = Radiobutton(frame_registerEmployee, text = "หญิง", variable = employee_gender1info,value="หญิง",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
    RadioButton_female_1.place(x=854,y=363)
    RadioButton_other_1 = Radiobutton(frame_registerEmployee, text = "อื่น ๆ", variable = employee_gender1info,value="อื่นๆ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
    RadioButton_other_1.place(x=964,y=363)
    Label(frame_registerEmployee,text="รหัสผ่าน",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=408)
    Label(frame_registerEmployee,text="ยืนยันรหัสผ่าน",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=488)
    ety_Pwd_employee_1 = Entry(frame_registerEmployee,width=30,textvariable=employee_pwd1info,show='*')
    ety_Pwd_employee_1.place(x=732,y=438,width=309,height=38)
    ety_NewPwd_employee_1 = Entry(frame_registerEmployee,width=30,show='*',textvariable=employee_conpwd1info)#เพิ่ม
    ety_NewPwd_employee_1.place(x=732,y=518,width=309,height=38)

    bt_clearData = Button(frame_registerEmployee,text="ยกเลิก",bg='#9F8189',fg='#FBEEE6',command=clearCallBack)
    bt_clearData.place(x=678,y=598,width=200,height=75)
    bt_confirm = Button(frame_registerEmployee,text="ยืนยัน",bg='#9F8189',fg='#FBEEE6',command=EmployeeManage_CallBack)
    bt_confirm.place(x=902,y=598,width=200,height=75)

    bt_back = Button(frame_registerEmployee,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
    bt_back.place(x=8,y=625,width=85,height=90)

def widget_editEmployee():
    global userPERM,pageNAME
    global frame_editEmployee
    global ety_calendar_employee_2 ,ety_address_employee_2,ety_Name_employee_2,ety_Id_employee_2,ety_phone_employee_2,ety_Username_employee_2,ety_surName_employee_2,ety_Pwd_employee_2,ety_NewPwd_employee_2
    if employee_name2info.get() == "" :
        messagebox.showwarning("ระบบ:","กรุณาเลือกพนักงานที่จะทำการแก้ไขข้อมูล")
    else :
        
        frame_editEmployee = createFrame_editEmployee(window)

        pageNAME = "EDIT_EMPLOYEE"

        Label(frame_editEmployee,text="แก้ไขข้อมูลพนักงาน",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=447,y=25)

        #left
        Label(frame_editEmployee,text="ชื่อ (ภาษาไทย)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=119)
        ety_Name_employee_2 = Entry(frame_editEmployee,width=30,textvariable=employee_name2info)
        ety_Name_employee_2.place(x=239,y=144,width=309,height=58)

        def validate1(P):
            if len(P) == 0:
                return True
            elif len(P) < 11 and P.isdigit():
                return True
            else:
                return False

        def validate2(P):
            if len(P) == 0:
                return True
            elif len(P) < 14 and P.isdigit():
                return True
            else:
                return False

        vcmd1 = (window.register(validate1), '%P')
        vcmd2 = (window.register(validate2), '%P')

        Label(frame_editEmployee,text="เลขบัตรประชาชน (เลข 13 หลัก)",font="tahoma 16  ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=226)
        ety_Id_employee_2 = Entry(frame_editEmployee,text="ชื่อ",width=30,textvariable=employee_id2info,state="readonly", validate="key",validatecommand=vcmd2,readonlybackground='#FFFFFF')
        ety_Id_employee_2.place(x=239,y=252,width=309,height=58)
        Label(frame_editEmployee,text="เบอร์โทรศัพท์ (เลข 10 หลัก) *",font="tahoma 16  ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=328)
        ety_phone_employee_2 = Entry(frame_editEmployee,text="ชื่อ",width=30,textvariable=employee_phone2info, validate="key",validatecommand=vcmd1)
        ety_phone_employee_2.place(x=239,y=353,width=309,height=58)
        Label(frame_editEmployee,text="ชื่อผู้ใช้งาน",font="tahoma 16  ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=428)
        ety_Username_employee_2 = Entry(frame_editEmployee,width=30,state="readonly",textvariable=employee_username2info,readonlybackground='#FFFFFF')
        ety_Username_employee_2.place(x=239,y=454,width=309,height=58)
        Label(frame_editEmployee,text="ที่อยู่",font="tahoma 16  ",bg='#FFCAD4',fg='#9F8189').place(x=239,y=532)
        ety_address_employee_2 = Text(frame_editEmployee,width=30)

        ety_address_employee_2.insert(1.0,epy_address)
        ety_address_employee_2.place(x=239,y=560,width=309,height=107)

        #right
        Label(frame_editEmployee,text="นามสกุล (ภาษาไทย)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=119)
        ety_surName_employee_2 = Entry(frame_editEmployee,width=30,textvariable=employee_surname2info)
        ety_surName_employee_2.place(x=732,y=144,width=309,height=58)
        Label(frame_editEmployee,text="วัน/เดือน/ปี ที่เกิด",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=226)
        # frame_date = Frame(frame_editEmployee,width=30,bg='#FFFFFF')
        # frame_date.place(x=732,y=252,width=309,height=58)
        ety_calendar_employee_2 = Entry(frame_editEmployee,width=30,state="readonly",textvariable=employee_date2info,readonlybackground='#FFFFFF')
        ety_calendar_employee_2.place(x=732,y=252,width=309,height=58)
        bt_date = Button(frame_editEmployee,image=photo_calendar,bg='#FFE5D8',command=popup_calendarEditEmployee)
        bt_date.place(x=976,y=253,width=65,height=57)
        Label(frame_editEmployee,text="เพศ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=328)
        RadioButton_male = Radiobutton(frame_editEmployee, text = "ชาย", variable = employee_gender2info,value="ชาย",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
        RadioButton_male.place(x=745,y=363)
        RadioButton_female = Radiobutton(frame_editEmployee, text = "หญิง", variable = employee_gender2info,value="หญิง",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
        RadioButton_female.place(x=854,y=363)
        RadioButton_other = Radiobutton(frame_editEmployee, text = "อื่น ๆ", variable = employee_gender2info,value="อื่นๆ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
        RadioButton_other.place(x=964,y=363)
        Label(frame_editEmployee,text="รหัสผ่าน",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=408)
        Label(frame_editEmployee,text="ยืนยันรหัสผ่าน",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=732,y=488)
        ety_Pwd_employee_2 = Entry(frame_editEmployee,width=30,textvariable=employee_pwd2info,show='*')
        ety_Pwd_employee_2.place(x=732,y=438,width=309,height=38)
        ety_NewPwd_employee_2 = Entry(frame_editEmployee,width=30,show='*',textvariable=employee_conpwd2info)#เพิ่ม
        ety_NewPwd_employee_2.place(x=732,y=518,width=309,height=38)

        bt_clearData = Button(frame_editEmployee,text="ยกเลิก",bg='#9F8189',fg='#FBEEE6',command=clearCallBack)
        bt_clearData.place(x=678,y=598,width=200,height=75)
        bt_confirm = Button(frame_editEmployee,text="ยืนยัน",bg='#9F8189',fg='#FBEEE6',command=EmployeeManage_CallBack)
        bt_confirm.place(x=902,y=598,width=200,height=75)

        bt_back = Button(frame_editEmployee,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
        bt_back.place(x=8,y=625,width=85,height=90)

def widget_manageMember():
    global pageNAME,userPERM
    global frame_customerManage
    global ety_search_customer
    frame_customerManage = createFrame_customerManage(window)

    pageNAME = "MANAGE_CUSTOMER"

    customer_name2info.set("")

    Label(frame_customerManage,text="บัญชีสมาชิก",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=65,y=65)

    bt_registerMember = Button(frame_customerManage,text="ลงทะเบียน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_registerMember)
    bt_registerMember.place(x=255,y=590,width=200,height=75)
    bt_editMember = Button(frame_customerManage,text="แก้ไขจัดการ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_editMember)
    bt_editMember.place(x=555,y=590,width=200,height=75)
    bt_deleteMember = Button(frame_customerManage,text="ลบบัญชีลูกค้า",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=removeCallBack)
    bt_deleteMember.place(x=855,y=590,width=200,height=75)

    ety_search_customer = Entry(frame_customerManage,width=30,justify=CENTER,font='tahoma 18')
    ety_search_customer.place(x=606,y=68,width=443,height=75)
    bt_search = Button(frame_customerManage,image=photo_search,bg='#FBEEE6',fg='#9F8189',command=search_click)
    bt_search.place(x=1049,y=68,width=75,height=75)
    bt_refresh = Button(frame_customerManage,image=photo_refresh,bg='#FBEEE6',command=(lambda: fetch_Tree(pageNAME,mytree_customer,cursor)))
    bt_refresh.place(x=1137,y=68,width=75,height=75)

    bt_back = Button(frame_customerManage,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
    bt_back.place(x=8,y=625,width=85,height=90)

    Label(frame_customerManage,text="ค้นหาจาก",font="tahoma 14 ",bg='#FFCAD4',fg='#9F8189').place(x=478,y=45)
    mb_dropdown_clicked.set("เบอร์โทรศัพท์")
    option = OptionMenu(frame_customerManage,mb_dropdown_clicked,"เบอร์โทรศัพท์","ชื่อ","นามสกุล",)
    option.config(bg="#9F8189",fg='#ffffff',highlightthickness = 0)
    option.place(x=478,y=68,width=120,height=75)

    def widget_treeview_customer():
        global mytree_customer
        treeframe = Frame(frame_customerManage,bg='#FFE5D8')
        treeframe.place(x=72,y=190,height=350)
        style = ttk.Style(treeframe)
        style.theme_use("default")
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        scrollbar = Scrollbar(treeframe)
        scrollbar.pack(side=RIGHT,fill=Y)

        columns=("phoneNumber","name","surName","gender","birth","email","address","point")
        mytree_customer = ttk.Treeview(treeframe,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
        mytree_customer.pack()

        mytree_customer.heading("phoneNumber",text="เบอร์โทรศัพท์",anchor='center')
        mytree_customer.heading("name",text="ชื่อ",anchor='center')
        mytree_customer.heading("surName", text="นามสกุล",anchor='center')
        mytree_customer.heading("gender", text="เพศ",anchor='center')
        mytree_customer.heading("birth", text="วันเกิด",anchor='center')
        mytree_customer.heading("email", text="อีเมล",anchor='center')
        mytree_customer.heading("address", text="ที่อยู่",anchor='center')
        mytree_customer.heading("point", text="แต้มสะสม",anchor='center')

        mytree_customer.column("phoneNumber",anchor='center',width=140)
        mytree_customer.column("name",anchor='center',width=140)
        mytree_customer.column("surName",anchor='center',width=140)
        mytree_customer.column("gender",anchor='center',width=140)
        mytree_customer.column("birth",anchor='center',width=140)
        mytree_customer.column("email",anchor='center',width=140)
        mytree_customer.column("address",anchor='center',width=140)
        mytree_customer.column("point",anchor='center',width=140)

        fetch_Tree(pageNAME,mytree_customer,cursor)
        mytree_customer.bind('<Double-1>',treeviewclick)
    widget_treeview_customer()

def widget_registerMember():
    global pageNAME,userPERM
    global frame_registerMember
    global ety_Name_member_1,ety_phone_member_1,ety_email_member_1,ety_surName_member_1,ety_calendar_member_1,ety_Address_Member_1
    frame_registerMember = createFrame_registerMember(window)

    pageNAME = "REGISTER_CUSTOMER"

    def validate1(P):
        if len(P) == 0:
            return True
        elif len(P) < 11 and P.isdigit():
            return True
        else:
            return False

    vcmd1 = (window.register(validate1), '%P')

    Label(frame_registerMember,text="สมัครสมาชิก",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=481,y=25)

    Label(frame_registerMember,text="ชื่อ (ภาษาไทย)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=257,y=116)
    ety_Name_member_1 = Entry(frame_registerMember,width=30,textvariable=customer_name1info)
    ety_Name_member_1.place(x=257,y=145,width=300,height=58)

    Label(frame_registerMember,text="เบอร์โทรศัพท์ (เลข 10 หลัก)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=257,y=247)
    ety_phone_member_1 = Entry(frame_registerMember,width=30, validate="key", validatecommand=vcmd1,textvariable=customer_phone1info)
    ety_phone_member_1.place(x=257,y=275,width=300,height=58)

    Label(frame_registerMember,text="อีเมล (example@gmail.com)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=257,y=375)
    ety_email_member_1 = Entry(frame_registerMember,width=30,textvariable=customer_email1info)
    ety_email_member_1.place(x=257,y=403,width=300,height=58)

    Label(frame_registerMember,text="นามสกุล (ภาษาไทย)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=714,y=116)
    ety_surName_member_1 = Entry(frame_registerMember,width=30,textvariable=customer_surname1info)
    ety_surName_member_1.place(x=714,y=145,width=300,height=58)

    Label(frame_registerMember,text="เพศ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=714,y=247)
    RadioButton_male_1 = Radiobutton(frame_registerMember, text = "ชาย", variable = customer_gender1info,value="ชาย",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
    RadioButton_male_1.place(x=729,y=296)
    RadioButton_female_1 = Radiobutton(frame_registerMember, text = "หญิง", variable = customer_gender1info,value="หญิง",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
    RadioButton_female_1.place(x=837,y=296)
    RadioButton_other_1 = Radiobutton(frame_registerMember, text = "อื่น ๆ", variable = customer_gender1info,value="อื่นๆ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
    RadioButton_other_1.place(x=947,y=296)

    Label(frame_registerMember,text="วัน/เดือน/ปี ที่เกิด",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=714,y=375)
    # frame_date = Frame(frame_registerMember,width=30,bg='#FFFFFF')
    # frame_date.place(x=714,y=404,width=300,height=58)
    ety_calendar_member_1 = Entry(frame_registerMember,width=30,state="readonly",textvariable=customer_date1info,readonlybackground='#FFFFFF')
    ety_calendar_member_1.place(x=714,y=404,width=300,height=58)
    bt_date_1 = Button(frame_registerMember,image=photo_calendar,bg='#FFE5D8',command=popup_calendarRegisterMember)
    bt_date_1.place(x=950,y=405,width=65,height=57)

    Label(frame_registerMember,text="ที่อยู่",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=257,y=510)
    ety_Address_Member_1 = Text(frame_registerMember,width=30)
    ety_Address_Member_1.place(x=257,y=539,width=309,height=107)


    bt_clearData = Button(frame_registerMember,text="ยกเลิก",bg='#9F8189',fg='#FBEEE6',command=clearCallBack)
    bt_clearData.place(x=696,y=575,width=200,height=75)
    bt_confirm = Button(frame_registerMember,text="ยืนยัน",bg='#9F8189',fg='#FBEEE6',command=EmployeeManage_CallBack)
    bt_confirm.place(x=928,y=575,width=200,height=75)

    bt_back = Button(frame_registerMember,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
    bt_back.place(x=8,y=625,width=85,height=90)

def widget_editMember():
    global pageNAME,userPERM
    global frame_editMember
    global ety_Name_member_2,ety_phone_member_2,ety_email_member_2,ety_surName_member_2,ety_calendar_member_2,ety_Address_Member_2
    if customer_name2info.get() == "" :
        messagebox.showwarning("ระบบ:","กรุณาเลือกลูกค้าที่จะทำการแก้ไขข้อมูล")
    else :
    
        frame_editMember = createFrame_registerMember(window)

        pageNAME = "EDIT_CUSTOMER"

        Label(frame_editMember,text="แก้ไขสมาชิก",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=481,y=25)

        Label(frame_editMember,text="ชื่อ (ภาษาไทย)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=257,y=116)
        ety_Name_member_2 = Entry(frame_editMember,width=30,textvariable=customer_name2info)
        ety_Name_member_2.place(x=257,y=145,width=300,height=58)

        Label(frame_editMember,text="เบอร์โทรศัพท์ (เลข 10 หลัก)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=257,y=247)
        ety_phone_member_2 = Entry(frame_editMember,width=30,textvariable=customer_phone2info,state="readonly",readonlybackground='#FFFFFF')
        ety_phone_member_2.place(x=257,y=275,width=300,height=58)

        Label(frame_editMember,text="อีเมล (example@gmail.com)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=257,y=375)
        ety_email_member_2 = Entry(frame_editMember,width=30,textvariable=customer_email2info)
        ety_email_member_2.place(x=257,y=403,width=300,height=58)

        Label(frame_editMember,text="นามสกุล (ภาษาไทย)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=714,y=116)
        ety_surName_member_2 = Entry(frame_editMember,width=30,textvariable=customer_surname2info)
        ety_surName_member_2.place(x=714,y=145,width=300,height=58)

        Label(frame_editMember,text="เพศ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=714,y=247)
        RadioButton_male_2 = Radiobutton(frame_editMember, text = "ชาย", variable = customer_gender2info,value="ชาย",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
        RadioButton_male_2.place(x=729,y=296)
        RadioButton_female_2 = Radiobutton(frame_editMember, text = "หญิง", variable = customer_gender2info,value="หญิง",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
        RadioButton_female_2.place(x=837,y=296)
        RadioButton_other_2 = Radiobutton(frame_editMember, text = "อื่น ๆ", variable = customer_gender2info,value="อื่นๆ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189')
        RadioButton_other_2.place(x=947,y=296)

        Label(frame_editMember,text="วัน/เดือน/ปี ที่เกิด",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=714,y=375)
        # frame_date = Frame(frame_editMember,width=30,bg='#FFFFFF')
        # frame_date.place(x=714,y=404,width=300,height=58)
        ety_calendar_member_2 = Entry(frame_editMember,width=30,state="readonly",textvariable=customer_date2info,readonlybackground='#FFFFFF')
        ety_calendar_member_2.place(x=714,y=404,width=300,height=58)
        bt_date_2 = Button(frame_editMember,image=photo_calendar,bg='#FFE5D8',command=popup_calendarEditMember)
        bt_date_2.place(x=950,y=405,width=65,height=57)

        Label(frame_editMember,text="ที่อยู่",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=257,y=510)
        ety_Address_Member_2 = Text(frame_editMember,width=30)
        ety_Address_Member_2.insert(1.0,mb_address)
        ety_Address_Member_2.place(x=257,y=539,width=309,height=107)


        bt_clearData = Button(frame_editMember,text="ยกเลิก",bg='#9F8189',fg='#FBEEE6',command=clearCallBack)
        bt_clearData.place(x=696,y=575,width=200,height=75)
        bt_confirm = Button(frame_editMember,text="ยืนยัน",bg='#9F8189',fg='#FBEEE6',command=EmployeeManage_CallBack)
        bt_confirm.place(x=928,y=575,width=200,height=75)

        bt_back = Button(frame_editMember,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
        bt_back.place(x=8,y=625,width=85,height=90)

def widget_confirmSelling():
    global frame_confirmSelling
    global pageNAME,userPERM
    global totalSellPriceAAA
    global ety_receive
    global discount
    if order_total == 0 :
        messagebox.showwarning('ระบบ','ไม่มีออเดอร์สินค้า')
    else :
        frame_confirmSelling = createFrame_confirmSelling(window)

        pageNAME = "COMFIRM_ORDER"

        def validate1(P):
            if len(P) == 0:
                return True
            elif len(P) < 11 and P.isdigit():
                return True
            else:
                return False

        vcmd1 = (window.register(validate1), '%P')

        discount.set("0")

        Label(frame_confirmSelling,text="ส่วนลด 10% (บาท)",font="tahoma 16 bold",bg='#FFCAD4',fg='#9F8189').place(x=65,y=388)
        ety_discount = Entry(frame_confirmSelling,textvariable=discount,state='readonly',readonlybackground='#FFFFFF',font="tahoma 30 bold",justify=CENTER)
        ety_discount.place(x=65,y=421,width=270,height=75)

        Label(frame_confirmSelling,text="พนักงานได้รับเงินมา (บาท)",font="tahoma 16 bold",bg='#FFCAD4',fg='#9F8189').place(x=355,y=388)
        ety_receive = Entry(frame_confirmSelling,bg='#FFFFFF',validate="key",validatecommand=vcmd1,font="tahoma 30 bold",justify=CENTER)
        ety_receive.place(x=355,y=421,width=270,height=75)

        Label(frame_confirmSelling,text="ยอดสุทธิ",font="tahoma 28 bold",bg='#FFCAD4',fg='#9F8189').place(x=65,y=549)
        frame_total = Frame(frame_confirmSelling,bg='#FFFFFF')
        frame_total.place(x=218,y=539,width=405,height=75)
        
        totalSellPriceAAA = Label(frame_total,text=order_total,font="tahoma 28 bold",bg='#FFFFFF',fg='#9F8189')
        totalSellPriceAAA.place(x=190,y=10)
        Label(frame_total,text="บาท",font="tahoma 28 bold",bg='#FFFFFF',fg='#9F8189').place(x=325,y=10)

        frame_blank = Label(frame_confirmSelling,image=photo_logo,bg='#FFFFFF')
        frame_blank.place(x=752,y=49,width=460,height=225)

        bt_member = Button(frame_confirmSelling,text='สมาชิก',bg='#9F8189',fg='#FFE5D8',font='tahoma 14 bold',command=popup_member)
        bt_member.place(x=752,y=312,width=460,height=95)

        Label(frame_confirmSelling,text="- - - - - - - - - - - - - - - - - - -",bg='#FFCAD4',fg='#9F8189',font='tahoma 27').place(x=788,y=473)

        bt_confirm = Button(frame_confirmSelling,text="ยืนยัน",bg='#9F8189',fg='#FBEEE6',font='tahoma 14 bold',command=confirmSellCallBack)
        bt_confirm.place(x=802,y=538,width=360,height=95)

        bt_back = Button(frame_confirmSelling,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
        bt_back.place(x=8,y=625,width=85,height=90)

        def widget_treeview():
            global mytreeSelling
            treeframe = Frame(frame_confirmSelling,bg='#FFE5D8')
            treeframe.place(x=65,y=50,width=558,height=300)
            style = ttk.Style(treeframe)
            style.theme_use("default")
            style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
            style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
            style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
            style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

            scrollbar = Scrollbar(treeframe)
            scrollbar.pack(side=RIGHT,fill=Y)

            columns=("name","amount","price")
            mytreeSelling = ttk.Treeview(treeframe,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
            mytreeSelling.pack()

            mytreeSelling.heading("name",text="ชื่อสินค้า",anchor='center')
            mytreeSelling.heading("amount", text="จำนวน",anchor='center')
            mytreeSelling.heading("price", text="ราคา (บาท)",anchor='center')

            mytreeSelling.column("name",anchor='center',width=258)
            mytreeSelling.column("amount",anchor='center',width=149)
            mytreeSelling.column("price",anchor='center',width=151)
        widget_treeview()
        confirmOrderCallBack()

def widget_manageStock():
    global pageNAME,userPERM
    global frame_stock
    global ety_nameIngredients,ety_amountIngredients
    global ety_searchBox_stock
    global bt_orderIngredients
    frame_stock = createFrame_stock(window)

    pageNAME = "MANAGE_STOCK"

    staple_amount_info.set("0")

    Label(frame_stock,image=photo_profile,text=" "+employee_name,bg='#FFCAD4',fg='#9F8189',compound=LEFT,font='tahoma 15 bold').place(x=20,y=20)

    Label(frame_stock,text="ค้นหาจากชื่อ",font="tahoma 14 ",bg='#FFCAD4',fg='#9F8189').place(x=395,y=7)
    ety_searchBox_stock = Entry(frame_stock,width=30,justify=CENTER,font='tahoma 20 ')
    ety_searchBox_stock.place(x=395,y=32,width=282,height=75)
    bt_search = Button(frame_stock,image=photo_search,bg='#FBEEE6',fg='#9F8189',command=search_click)
    bt_search.place(x=679,y=32,width=75,height=75)
    bt_refresh = Button(frame_stock,image=photo_refresh,bg='#FBEEE6',fg='#9F8189',command=(lambda: fetch_Tree(pageNAME,mytree_stock,cursor)))
    bt_refresh.place(x=772,y=32,width=75,height=75)

    Label(frame_stock,text="คลังวัตถุดิบ",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=944,y=32)

    Label(frame_stock,text="ชื่อวัตถุดิบ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=70,y=215)
    ety_nameIngredients = Entry(frame_stock,textvariable=staple_nameinfo,justify=CENTER)
    ety_nameIngredients.place(x=70,y=248,width=250,height=50)
    Label(frame_stock,text="จำนวน",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=70,y=314)
    ety_amountIngredients = Entry(frame_stock,textvariable=staple_amount_info,state="readonly",readonlybackground='#FFFFFF',justify=CENTER)
    ety_amountIngredients.place(x=70,y=347,width=250,height=50)
    Label(frame_stock,text="หน่วย",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=70,y=413)
    manageStock_dropdown_clicked.set("กรัม")
    option = OptionMenu(frame_stock,manageStock_dropdown_clicked,"กรัม","กิโลกรัม","ลิตร","ถุง","กระสอบ","ชุด","ขวด","ชิ้น","กระป๋อง","ห่อ","แพ็ค")
    option.config(bg="#9F8189",fg='#ffffff',highlightthickness = 0)
    option.place(x=70,y=446,width=250,height=50)

    bt_editIngredients = Button(frame_stock,text="แก้ไขวัตถุดิบ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=(lambda: stockCallBack("แก้ไข")))
    bt_editIngredients.place(x=967,y=207,width=200,height=75)
    bt_IncreaseIngredients = Button(frame_stock,text="เพิ่มวัตถุดิบ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=(lambda: stockCallBack("เพิ่ม")))
    bt_IncreaseIngredients.place(x=967,y=322,width=200,height=75)
    bt_deleteIngredients = Button(frame_stock,text="ลบวัตถุดิบ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=(lambda: stockCallBack("ลบ")))
    bt_deleteIngredients.place(x=967,y=437,width=200,height=75)
    bt_pickupIngredients = Button(frame_stock,text="เบิกวัตถุดิบ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_RequisitionIngredients)
    bt_pickupIngredients.place(x=303,y=607,width=200,height=75)
    bt_orderIngredients = Button(frame_stock,text="สั่งซื้อวัตถุดิบ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=widget_orderIngredients)
    bt_orderIngredients.place(x=738,y=607,width=200,height=75)

    bt_back = Button(frame_stock,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
    bt_back.place(x=8,y=625,width=85,height=90)

    def widget_treeview_stock():
        global mytree_stock ,treeframe_stock
        treeframe_stock = Frame(frame_stock,bg='#FFE5D8')
        treeframe_stock.place(x=395,y=172,height=400)
        style = ttk.Style(treeframe_stock)
        style.theme_use("default")
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        scrollbar = Scrollbar(treeframe_stock)
        scrollbar.pack(side=RIGHT,fill=Y)

        columns=("ingredients","amount","unit")
        mytree_stock = ttk.Treeview(treeframe_stock,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
        mytree_stock.pack()

        mytree_stock.heading("ingredients",text="ชื่อวัตถุดิบ",anchor='center')
        mytree_stock.heading("amount", text="ยอดคงเหลือ",anchor='center')
        mytree_stock.heading("unit", text="หน่วย",anchor='center')

        mytree_stock.column("ingredients",anchor='center',width=160)
        mytree_stock.column("amount",anchor='center',width=145)
        mytree_stock.column("unit",anchor='center',width=145)

        fetch_Tree(pageNAME,mytree_stock,cursor)
        mytree_stock.bind('<Double-1>',treeviewclick)
    widget_treeview_stock()

def widget_manageListProduct():
    global pageNAME,userPERM
    global frame_manageListProduct
    global ety_searchBox_product,ety_nameProduct,ety_priceProduct
    frame_manageListProduct = createFrame_manageListProduct(window)

    pageNAME = "MANAGE_PRODUCT"

    Label(frame_manageListProduct,image=photo_profile,text=" "+employee_name,bg='#FFCAD4',fg='#9F8189',compound=LEFT,font='tahoma 15 bold').place(x=20,y=20)

    ety_searchBox_product = Entry(frame_manageListProduct,width=30,justify=CENTER,font='tahoma 20 ')
    ety_searchBox_product.place(x=490,y=52,width=220,height=65)
    bt_search = Button(frame_manageListProduct,image=photo_search,bg='#FBEEE6',fg='#9F8189',command=search_click)
    bt_search.place(x=717,y=52,width=60,height=65)
    bt_refresh = Button(frame_manageListProduct,image=photo_refresh,bg='#FBEEE6',fg='#9F8189',command=(lambda: fetch_Tree(pageNAME,mytree_product,cursor)))
    bt_refresh.place(x=783,y=52,width=60,height=65)

    Label(frame_manageListProduct,text="ค้นหาจาก",font="tahoma 12 ",bg='#FFCAD4',fg='#9F8189').place(x=395,y=29)
    product_dropdown_select.set("ประเภท")
    option = OptionMenu(frame_manageListProduct,product_dropdown_select,"ประเภท","ชื่อ","ราคา")
    option.config(bg="#9F8189",fg='#ffffff',highlightthickness = 0)
    option.place(x=395,y=52,width=90,height=65)


    Label(frame_manageListProduct,text="รายการสินค้า",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=934,y=52)

    Label(frame_manageListProduct,text="ชื่อสินค้า",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=70,y=219)
    ety_nameProduct = Entry(frame_manageListProduct,textvariable=product_nameinfo,justify=CENTER)
    ety_nameProduct.place(x=70,y=250,width=250,height=50)

    def validate1(P):
        if len(P) == 0:
            return True
        elif len(P) < 11 and P.isdigit():
            return True
        else:
            return False

    vcmd1 = (window.register(validate1), '%P')

    Label(frame_manageListProduct,text="ราคาสินค้า (บาท)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=70,y=327)
    ety_priceProduct = Entry(frame_manageListProduct,textvariable=product_priceinfo, validate="key", validatecommand=vcmd1,justify=CENTER)
    ety_priceProduct.place(x=70,y=360,width=250,height=50)

    Label(frame_manageListProduct,text="ประเภทสินค้า",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=70,y=435)
    product_dropdown_type.set("กาแฟ")
    option = OptionMenu(frame_manageListProduct,product_dropdown_type,"กาแฟ","ชา","น้ำผลไม้","นม")
    option.config(bg="#9F8189",fg='#ffffff',highlightthickness = 0)
    option.place(x=70,y=470,width=250,height=55)


    bt_editProduct = Button(frame_manageListProduct,text="แก้ไขรายการ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=(lambda: productCallBack("แก้ไข")))
    bt_editProduct.place(x=967,y=237,width=200,height=75)
    bt_IncreaseProduct = Button(frame_manageListProduct,text="เพิ่มรายการ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=(lambda: productCallBack("เพิ่ม")))
    bt_IncreaseProduct.place(x=967,y=352,width=200,height=75)
    bt_deleteProduct = Button(frame_manageListProduct,text="ลบรายการ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=(lambda: productCallBack("ลบ")))
    bt_deleteProduct.place(x=967,y=467,width=200,height=75)

    bt_back = Button(frame_manageListProduct,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
    bt_back.place(x=8,y=625,width=85,height=90)

    def widget_treeview_product():
        global mytree_product
        treeframe = Frame(frame_manageListProduct,bg='#FFE5D8')
        treeframe.place(x=395,y=190,height=400)
        style = ttk.Style(treeframe)
        style.theme_use("default")
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        scrollbar = Scrollbar(treeframe)
        scrollbar.pack(side=RIGHT,fill=Y)

        columns=("type","name","price")
        mytree_product = ttk.Treeview(treeframe,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
        mytree_product.pack()

        mytree_product.heading("type",text="ประเภท",anchor='center')
        mytree_product.heading("name",text="ชื่อสินค้า",anchor='center')
        mytree_product.heading("price", text="ราคา",anchor='center')

        mytree_product.column("type",anchor='center',width=120)
        mytree_product.column("name",anchor='center',width=210)
        mytree_product.column("price",anchor='center',width=100)

        fetch_Tree(pageNAME,mytree_product,cursor)
        mytree_product.bind('<Double-1>',treeviewclick)
    widget_treeview_product()

def widget_RequisitionIngredients(): #ต้องทำ
    global frame_RequisitionIngredients, pageNAME
    global bt_confirmReq
    global ety_search_req
    frame_RequisitionIngredients = createFrame_RequisitionIngredients(window)
    pageNAME = "REQUISITION"

    Label(frame_RequisitionIngredients,text="เบิกวัตถุดิบ",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=987,y=49)

    Label(frame_RequisitionIngredients,text="ค้นหาจากชื่อ",font="tahoma 14 ",bg='#FFCAD4',fg='#9F8189').place(x=104,y=35)
    ety_search_req = Entry(frame_RequisitionIngredients,bg='#FFFFFF')
    ety_search_req.place(x=104,y=60,width=338,height=62)
    bt_search_req = Button(frame_RequisitionIngredients,image=photo_search,bg='#FBEEE6',fg='#9F8189',command=search_click)
    bt_search_req.place(x=445,y=60,width=62,height=62)
    bt_refresh = Button(frame_RequisitionIngredients,image=photo_refresh,bg='#FBEEE6',fg='#9F8189',command=(lambda: fetch_Tree(pageNAME,mytree_RequisitionIngredients,cursor)))
    bt_refresh.place(x=526,y=60,width=62,height=62)

    bt_resetReq = Button(frame_RequisitionIngredients,text="ยกเลิก",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=resetCallBack) 
    bt_resetReq.place(x=1020,y=202,width=200,height=75)
    bt_delReq = Button(frame_RequisitionIngredients,text="ลบ",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=removeCallBack)
    bt_delReq.place(x=1020,y=322,width=200,height=75)
    bt_confirmReq = Button(frame_RequisitionIngredients,text="ยืนยัน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=confirmReqCallback)
    bt_confirmReq.place(x=1020,y=442,width=200,height=75)

    bt_back = Button(frame_RequisitionIngredients,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
    bt_back.place(x=8,y=625,width=85,height=90)

    def widget_treeview1():
        global mytree_RequisitionIngredients
        treeframe = Frame(frame_RequisitionIngredients,bg='#FFE5D8')
        treeframe.place(x=104,y=146,width=400,height=445)
        style = ttk.Style(treeframe)
        style.theme_use("default")
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        scrollbar = Scrollbar(treeframe)
        scrollbar.pack(side=RIGHT,fill=Y)

        columns=("nameIngredients","amountInStock","unit")
        mytree_RequisitionIngredients = ttk.Treeview(treeframe,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
        mytree_RequisitionIngredients.pack()

        mytree_RequisitionIngredients.heading("nameIngredients",text="ชื่อวัตถุดิบ",anchor='center')
        mytree_RequisitionIngredients.heading("amountInStock", text="ยอดคงเหลือ",anchor='center')
        mytree_RequisitionIngredients.heading("unit", text="หน่วย",anchor='center')

        mytree_RequisitionIngredients.column("nameIngredients",anchor='center',width=160)
        mytree_RequisitionIngredients.column("amountInStock",anchor='center',width=120)
        mytree_RequisitionIngredients.column("unit",anchor='center',width=120)

        fetch_Tree(pageNAME,mytree_RequisitionIngredients,cursor)
        mytree_RequisitionIngredients.bind('<Double-1>',treeviewclick)
    widget_treeview1()

    def widget_treeview2():
        global mytree_RequisitionIngredients_2
        treeframe = Frame(frame_RequisitionIngredients,bg='#FFE5D8')
        treeframe.place(x=570,y=146,width=400,height=445)
        style = ttk.Style(treeframe)
        style.theme_use("default")
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        scrollbar = Scrollbar(treeframe)
        scrollbar.pack(side=RIGHT,fill=Y)

        columns=("nameIngredients","amountInRequest","unit")
        mytree_RequisitionIngredients_2 = ttk.Treeview(treeframe,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
        mytree_RequisitionIngredients_2.pack()

        mytree_RequisitionIngredients_2.heading("nameIngredients",text="ชื่อวัตถุดิบ",anchor='center')
        mytree_RequisitionIngredients_2.heading("amountInRequest", text="ยอดเบิก",anchor='center')
        mytree_RequisitionIngredients_2.heading("unit", text="หน่วย",anchor='center')

        mytree_RequisitionIngredients_2.column("nameIngredients",anchor='center',width=160)
        mytree_RequisitionIngredients_2.column("amountInRequest",anchor='center',width=120)
        mytree_RequisitionIngredients_2.column("unit",anchor='center',width=120)
    widget_treeview2()

def widget_orderIngredients():
    global pageNAME,userPERM
    global frame_orderIngredients
    global ety_searchMenu_orderstock
    global ety_dateOrderIngredients,ety_nameIngredients_order,ety_priceIngredients_order,ety_organization_order,ety_amountIngredients_order,ety_unitIngredients_order
    if userPERM == "พนักงาน" :
        # messagebox.showwarning("ระบบ:","ไม่มีสิทธิเข้าถึงในการใช้งาน")
        bt_orderIngredients["state"] = DISABLED
    else :
        frame_orderIngredients = createFrame_orderIngredients(window)

        pageNAME = "ORDER_STOCK"

        def validate1(P):
            if len(P) == 0:
                return True
            elif len(P) < 11 and P.isdigit():
                return True
            else:
                return False

        vcmd1 = (window.register(validate1), '%P')

        Label(frame_orderIngredients,text="สั่งซื้อวัตถุดิบ",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=776,y=55)

        Label(frame_orderIngredients,text="ค้นหาจากชื่อ",font="tahoma 14 ",bg='#FFCAD4',fg='#9F8189').place(x=70,y=42)
        ety_searchMenu_orderstock = Entry(frame_orderIngredients,bg='#FFFFFF')
        ety_searchMenu_orderstock.place(x=70,y=68,width=300,height=62)
        bt_search = Button(frame_orderIngredients,image=photo_search,bg='#FBEEE6',fg='#9F8189',command=search_click)
        bt_search.place(x=370,y=68,width=62,height=62)
        bt_refresh = Button(frame_orderIngredients,image=photo_refresh,bg='#FBEEE6',fg='#9F8189',command=(lambda: fetch_Tree(pageNAME,mytree_orderstock,cursor)))
        bt_refresh.place(x=443,y=68,width=62,height=62)

        bt_clear = Button(frame_orderIngredients,text="ยกเลิก",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=clearCallBack)
        bt_clear.place(x=640,y=605,width=200,height=75)
        bt_confirm = Button(frame_orderIngredients,text="ยืนยัน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=StockManage_CallBack)
        bt_confirm.place(x=970,y=605,width=200,height=75)

        Label(frame_orderIngredients,text="วันที่ซื้อวัตถุดิบ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=615,y=187)
        ety_dateOrderIngredients = Entry(frame_orderIngredients,width=30,state="readonly",textvariable=stapleorder_dateinfo,readonlybackground='#FFFFFF')
        ety_dateOrderIngredients.place(x=615,y=220,width=250,height=50)
        bt_date = Button(frame_orderIngredients,image=photo_calendar,bg='#FFE5D8',command=popup_calendarOrderIngredients)
        bt_date.place(x=802,y=220,width=67,height=50)
        Label(frame_orderIngredients,text="ชื่อวัตถุดิบ",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=615,y=306)
        ety_nameIngredients_order = Entry(frame_orderIngredients,width=30,textvariable=stapleorder_nameinfo,state="readonly",readonlybackground='#FFFFFF')
        ety_nameIngredients_order.place(x=615,y=334,width=250,height=50)
        Label(frame_orderIngredients,text="ราคาต่อหน่วย(บาท)",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=784,y=447)
        ety_priceIngredients_order = Entry(frame_orderIngredients,width=30, validate="key", validatecommand=vcmd1,textvariable=stapleorder_priceinfo)
        ety_priceIngredients_order.place(x=784,y=480,width=250,height=50)

        Label(frame_orderIngredients,text="บริษัท/องค์กร ที่ทำการค้า",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=940,y=187)
        ety_organization_order = Entry(frame_orderIngredients,width=30,textvariable=stapleorder_companyinfo)
        ety_organization_order.place(x=940,y=220,width=250,height=50)
        Label(frame_orderIngredients,text="จำนวน",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=940,y=301)
        ety_amountIngredients_order = Entry(frame_orderIngredients,width=30, validate="key", validatecommand=vcmd1,textvariable=stapleorder_amountinfo)
        ety_amountIngredients_order.place(x=940,y=334,width=160,height=50)

        Label(frame_orderIngredients,text="หน่วย",font="tahoma 16 ",bg='#FFCAD4',fg='#9F8189').place(x=1110,y=301)
        ety_unitIngredients_order = Entry(frame_orderIngredients,width=30,state="readonly",readonlybackground='#FFFFFF', validate="key", validatecommand=vcmd1,textvariable=stapleorder_unitinfo)
        ety_unitIngredients_order.place(x=1105,y=334,width=85,height=50)

        bt_back = Button(frame_orderIngredients,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
        bt_back.place(x=8,y=625,width=85,height=90)

        def widget_treeview_orderstock():
            global mytree_orderstock
            treeframe = Frame(frame_orderIngredients,bg='#FFE5D8')
            treeframe.place(x=60,y=172,width=450,height=400)
            style = ttk.Style(treeframe)
            style.theme_use("default")
            style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
            style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
            style.configure("Treeview.Heading", font=('Calibri', 13,'bold'),background='#FFE5D8') # Modify the font of the headings
            style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

            scrollbar = Scrollbar(treeframe)
            scrollbar.pack(side=RIGHT,fill=Y)

            columns=("nameIngredients","amountInStock","unit")
            mytree_orderstock = ttk.Treeview(treeframe,style="Treeview",columns=columns,show='headings',yscrollcommand = scrollbar.set)
            mytree_orderstock.pack()

            mytree_orderstock.heading("nameIngredients",text="ชื่อวัตถุดิบ",anchor='center')
            mytree_orderstock.heading("amountInStock", text="ยอดคงเหลือ",anchor='center')
            mytree_orderstock.heading("unit", text="หน่วย",anchor='center')

            mytree_orderstock.column("nameIngredients",anchor='center',width=160)
            mytree_orderstock.column("amountInStock",anchor='center',width=140)
            mytree_orderstock.column("unit",anchor='center',width=140)

            fetch_Tree(pageNAME,mytree_orderstock,cursor)
            mytree_orderstock.bind('<Double-1>',treeviewclick)
        widget_treeview_orderstock()

def widget_printReport():
    global pageNAME,userPERM
    global frame_printReport
    global ety_calendar_report

    if userPERM == "พนักงาน" :
        # messagebox.showwarning("ระบบ:","ไม่มีสิทธิเข้าถึงในการใช้งาน")
        bt_publish["state"] = DISABLED
    else :
        frame_printReport = createFrame_printReport(window)

        pageNAME = "PRINT_REPORT_1"

        Label(frame_printReport,text="พิมพ์รายงานการดำเนินงาน",bg='#FFCAD4',fg='#9F8189',font='tahoma 35 bold').place(x=368,y=80)

        Label(frame_printReport,text="ประเภทรายงาน",font="tahoma 14 ",bg='#FFCAD4',fg='#9F8189').place(x=196,y=252)

        report_dropdown_type.set("รายงานสรุปยอดขายสินค้า")
        option = OptionMenu(frame_printReport,report_dropdown_type,"รายงานสรุปยอดขายสินค้า","รายงานการเบิกวัตถุดิบ","รายงานการสั่งซื้อวัตถุดิบ")
        option.config(bg="#9F8189",fg='#FFE5D8',highlightthickness = 0,font='tahoma 14 bold')
        option.place(x=196,y=285,width=400,height=75)

        Label(frame_printReport,text="วันที่ของรายงาน",font="tahoma 14 ",bg='#FFCAD4',fg='#9F8189').place(x=708,y=252)
        # date_frame = Frame(frame_printReport,bg='snow')
        # date_frame.place(x=708,y=285,width=400,height=75)
        ety_calendar_report = Entry(frame_printReport,width=30,state="readonly",font='tahoma 28 bold',textvariable=report_dateinfo,readonlybackground='#FFFFFF')
        ety_calendar_report.place(x=708,y=285,width=400,height=75)
        bt_date = Button(frame_printReport,image=photo_calendar,bg='#FFE5D8',command=popup_calendarPrintReport)
        bt_date.place(x=1023,y=285,width=85,height=75)

        bt_print = Button(frame_printReport,text='พิมพ์รายงาน',bg='#9F8189',fg='#FFE5D8',font='tahoma 14 bold',command=printReport_clicked)
        bt_print.place(x=468,y=445,width=375,height=75)

        bt_back = Button(frame_printReport,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
        bt_back.place(x=8,y=625,width=85,height=90)

def printReport_clicked() :
    if report_dateinfo.get() == "" :
        messagebox.showwarning("ระบบ:","กรุณาระบุวันที่ที่จะพิมพ์รายงาน")
    else :
        if report_dropdown_type.get() == "รายงานสรุปยอดขายสินค้า" :
            sql = "SELECT * FROM orderlist WHERE order_date = ?"

        elif report_dropdown_type.get() == "รายงานการเบิกวัตถุดิบ" :
            sql = "SELECT * FROM requisitionlist WHERE requisition_date = ?"

        elif report_dropdown_type.get() == "รายงานการสั่งซื้อวัตถุดิบ" :
            sql = "SELECT * FROM stapleorder WHERE stapleorder_date = ?"
    
        cursor.execute(sql,[report_dateinfo.get()])
        result = cursor.fetchall()
        if result :
            widget_printReport2()
        else :
            messagebox.showwarning("ระบบ:","ไม่พบข้อมูลในระบบ")

def widget_printReport2() :
    global pageNAME,userPERM
    global frame_printReport2
    global text_showreport
    global result_list

    frame_printReport2 = createFrame_printReport2(window)
    pageNAME = "PRINT_REPORT_2"

    total_price = 0
    result_list = []
    report_type = report_dropdown_type.get()
    report_date = report_dateinfo.get()
    i = 0

    Label(frame_printReport2, text=report_dropdown_type.get(),font='tahoma 40 bold',bg='#FFCAD4',fg='#9F8189').place(x=40,y=25)

    text_showreport = Text(frame_printReport2,width=30)
    text_showreport.place(x=140,y=110,width=997,height=570)
    bt_back = Button(frame_printReport2,image=photo_exit,bg='#FFCAD4',relief=FLAT,command=backPAGE_Callback)
    bt_back.place(x=8,y=625,width=85,height=90)

    def save_report() :
        messagebox.showinfo("ระบบ:","พิมพ์รายงานสำเร็จ")
        filetext = (text_showreport.get(1.0,END))
        with open("report.txt","w",encoding="utf-8") as report :
            report.write(str(filetext))

    if report_dropdown_type.get() == "รายงานสรุปยอดขายสินค้า" :
        sql = "SELECT order_number,order_seller,order_list,order_price,order_getmoney,order_change FROM orderlist WHERE order_date = ?"
        cursor.execute(sql,[report_dateinfo.get()])

        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\tรายงานสรุปยอดขายสินค้า")
        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\tณ วันที่ : "+str(report_dateinfo.get()))
        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"     เลขที่ออเดอร์           ผู้ออกออเดอร์                           รายละเอียดออเดอร์                     ราคารวมออเดอร์           เงินที่รับมา         เงินทอน")
        text_showreport.insert(INSERT,"\n")
        while True :
            result = cursor.fetchone()
            if result == None :
                break
            text_showreport.insert(INSERT,"\n")
            text_showreport.insert(INSERT,"          ")
            text_showreport.insert(INSERT,result[0])
            text_showreport.insert(INSERT,"                     ")
            text_showreport.insert(INSERT,result[1])
            text_showreport.insert(INSERT,"\t\t\t\t")
            text_showreport.insert(INSERT,result[2])
            text_showreport.insert(INSERT,"\t\t\t\t\t")
            text_showreport.insert(INSERT,str(result[3])+" บาท")
            text_showreport.insert(INSERT,"\t\t")
            text_showreport.insert(INSERT,str(result[4])+" บาท")
            text_showreport.insert(INSERT,"\t         ")
            text_showreport.insert(INSERT,str(result[5])+" บาท")
            text_showreport.insert(INSERT,"\n")
            total_price = total_price + result[3]

            result_list.append(result)

        text_showreport.insert(INSERT,"\n\n\n\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\t\t\tราคารวม\t\t"+str(total_price)+"\t\tบาท")
        text_showreport.insert(INSERT,"\n\n\n\n\n")
        text_showreport.insert(INSERT,"          ยอดขายสินค้า\n          วันที่ : "+str(report_dateinfo.get()))

        text_showreport.configure(state='disabled')

    elif report_dropdown_type.get() == "รายงานการสั่งซื้อวัตถุดิบ" :
        sql = "select stapleorder_number,stapleorder_person,stapleorder_name,stapleorder_amount,stapleorder_unit,stapleorder_price,stapleorder_company from stapleorder where stapleorder_date=?"
        cursor.execute(sql,[report_dateinfo.get()])

        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\t รายงานการสั่งซื้อวัตถุดิบ")
        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\t  ณ วันที่ : "+str(report_dateinfo.get()))
        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"     เลขที่การสั่งซื้อวัตถุดิบ     ผู้ทำการสั่งซื้อวัตถุดิบ        ชื่อวัตถุดิบที่สั่งซื้อ      จำนวนที่ทำการสั่งซื้อ    ราคาของการสั่งซื้อ       บริษัทที่ทำการสั่งซื้อ")
        text_showreport.insert(INSERT,"\n")
        i = 0
        while True :
            result = cursor.fetchone()
            if result == None :
                break
            text_showreport.insert(INSERT,"\n")
            text_showreport.insert(INSERT,"                 ")
            text_showreport.insert(INSERT,result[0])
            text_showreport.insert(INSERT,"\t\t           ")
            text_showreport.insert(INSERT,result[1])
            text_showreport.insert(INSERT,"\t\t\t    ")
            text_showreport.insert(INSERT,result[2])
            text_showreport.insert(INSERT,"\t\t            ")
            text_showreport.insert(INSERT,str(result[3])+" "+str(result[4]))
            text_showreport.insert(INSERT,"\t\t             ")
            text_showreport.insert(INSERT,str(result[5])+" บาท")
            text_showreport.insert(INSERT,"\t\t            ")
            text_showreport.insert(INSERT,result[6])
            total_price = total_price + result[5]

            result_list.append(result)
            i = i + 1

        text_showreport.insert(INSERT,"\n\n\n\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\t\t\tจำนวนครั้งที่สั่งซื้อ\t\t\t"+str(i)+"\t\tครั้ง")
        text_showreport.insert(INSERT,"\n\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\t\t\tราคาที่สั่งซื้อทั้งหมด\t\t\t"+str(total_price)+"\t\tบาท")
        text_showreport.insert(INSERT,"\n\n\n\n\n")
        text_showreport.insert(INSERT,"          รายการสั่งซื้อวัตถุดิบ\n          วันที่ : "+str(report_dateinfo.get()))
        text_showreport.configure(state='disabled')

    elif report_dropdown_type.get() == "รายงานการเบิกวัตถุดิบ" :
        sql = "select requisition_number,requisition_person,requisition_list from requisitionlist where requisition_date=?"
        cursor.execute(sql,[report_dateinfo.get()])

        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\t  รายงานการเบิกวัตถุดิบ")
        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\t  ณ วันที่ : "+str(report_dateinfo.get()))
        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"\n")
        text_showreport.insert(INSERT,"               เลขที่การเบิกวัตถุดิบ                         ผู้ทำการเบิกวัตถุดิบ                                 รายละเอียดการเบิกวัตถุดิบ")
        text_showreport.insert(INSERT,"\n")

        i = 0
        while True :
            result = cursor.fetchone()
            if result == None :
                break
            text_showreport.insert(INSERT,"\n")
            text_showreport.insert(INSERT,"\t          ")
            text_showreport.insert(INSERT,result[0])
            text_showreport.insert(INSERT,"\t\t\t         ")
            text_showreport.insert(INSERT,result[1])
            text_showreport.insert(INSERT,"\t\t\t\t")
            text_showreport.insert(INSERT,result[2])
            text_showreport.insert(INSERT,"\n")

            result_list.append(result)
            i = i + 1
        
        text_showreport.insert(INSERT,"\n\n\n\n")
        text_showreport.insert(INSERT,"\t\t\t\t\t\t\t\tจำนวนการเบิกทั้งหมด\t\t\t"+str(i)+"\t\tครั้ง")
        text_showreport.insert(INSERT,"\n\n")
        text_showreport.insert(INSERT,"          รายการเบิกวัตถุดิบ\n          วันที่ : "+str(report_dateinfo.get()))
        text_showreport.configure(state='disabled')

    bt_print = Button(frame_printReport2,text='พิมพ์รายงาน',bg='#9F8189',fg='#FFE5D8',font='tahoma 14 bold',command=(lambda : createDocxFile(result_list,report_type,report_date,total_price,i)))
    bt_print.place(x=978,y=25,width=255,height=65)

def popup_calendarRegisterEmployee():
    global window_calendar1
    window_calendar1= Toplevel()
    window_calendar1.geometry("600x400")
    window_calendar1.title("Calendar")
    window_calendar1.config(bg='#FFCAD4')
    window_calendar1.resizable(False,False)

    cal = Calendar(window_calendar1, selectmode='day',locate='th_TH',date_pattern="dd/mm/yyyy",Background='#FBEEE6',foreground='#FFCAD4')
    cal.pack(pady = 20)
    def grad_date():
        # Label(frame_registerEmployee,text=cal.get_dateEmployee(),bg='#FFFFFF',font='tahoma 24 bold').place(x=752,y=258)
        employee_date1info.set(cal.get_date())
        # print(cal.get_date())
        window_calendar1.destroy()
    Button(window_calendar1, text = "Get Date",command=grad_date,bg='#9F8189').pack(pady=20)
    bt_cancel1 = Button(window_calendar1,image=photo_cancel,bg='#FFCAD4',relief=FLAT,command=window_calendar1.destroy)
    bt_cancel1.place(x=540,y=10,width=50,height=60)

def popup_calendarEditEmployee():
    global window_calendar1
    window_calendar1= Toplevel()
    window_calendar1.geometry("600x400")
    window_calendar1.title("Calendar")
    window_calendar1.config(bg='#FFCAD4')
    window_calendar1.resizable(False,False)

    cal = Calendar(window_calendar1, selectmode='day',locate='th_TH',date_pattern="dd/mm/yyyy",Background='#FBEEE6',foreground='#FFCAD4')
    cal.pack(pady = 20)
    def grad_date():
        # Label(frame_editEmployee,text=cal.get_date(),bg='#FFFFFF',font='tahoma 24 bold').place(x=752,y=258)
        employee_date2info.set(cal.get_date())
        # print(cal.get_date())
        window_calendar1.destroy()
    Button(window_calendar1, text = "Get Date",command=grad_date,bg='#9F8189').pack(pady=20)
    bt_cancel1 = Button(window_calendar1,image=photo_cancel,bg='#FFCAD4',relief=FLAT,command=window_calendar1.destroy)
    bt_cancel1.place(x=540,y=10,width=50,height=60)

def popup_calendarRegisterMember():
    global window_calendar1
    window_calendar1= Toplevel()
    window_calendar1.geometry("600x400")
    window_calendar1.title("Calendar")
    window_calendar1.config(bg='#FFCAD4')
    window_calendar1.resizable(False,False)

    cal = Calendar(window_calendar1, selectmode='day',locate='th_TH',date_pattern="dd/mm/yyyy",Background='#FBEEE6',foreground='#FFCAD4')
    cal.pack(pady = 20)
    def grad_date():
        # Label(frame_registerMember,text=cal.get_date(),bg='#FFFFFF',font='tahoma 24 bold').place(x=714,y=409)
        customer_date1info.set(cal.get_date())
        # print(cal.get_date())
        window_calendar1.destroy()
    Button(window_calendar1, text = "Get Date",command=grad_date,bg='#9F8189').pack(pady=20)
    bt_cancel1 = Button(window_calendar1,image=photo_cancel,bg='#FFCAD4',relief=FLAT,command=window_calendar1.destroy)
    bt_cancel1.place(x=540,y=10,width=50,height=60)

def popup_calendarEditMember():
    global window_calendar1
    window_calendar1= Toplevel()
    window_calendar1.geometry("600x400")
    window_calendar1.title("Calendar")
    window_calendar1.config(bg='#FFCAD4')
    window_calendar1.resizable(False,False)

    cal = Calendar(window_calendar1, selectmode='day',locate='th_TH',date_pattern="dd/mm/yyyy",Background='#FBEEE6',foreground='#FFCAD4')
    cal.pack(pady = 20)
    def grad_date():
        # Label(frame_editMember,text=cal.get_date(),bg='#FFFFFF',font='tahoma 24 bold').place(x=714,y=409)
        customer_date2info.set(cal.get_date())
        # print(cal.get_date())
        window_calendar1.destroy()
    Button(window_calendar1, text = "Get Date",command=grad_date,bg='#9F8189').pack(pady=20)
    bt_cancel1 = Button(window_calendar1,image=photo_cancel,bg='#FFCAD4',relief=FLAT,command=window_calendar1.destroy)
    bt_cancel1.place(x=540,y=10,width=50,height=60)

def popup_calendarOrderIngredients():
    global window_calendar1
    window_calendar1= Toplevel()
    window_calendar1.geometry("600x400")
    window_calendar1.title("Calendar")
    window_calendar1.config(bg='#FFCAD4')
    window_calendar1.resizable(False,False)

    cal = Calendar(window_calendar1, selectmode='day',locate='th_TH',date_pattern="dd/mm/yyyy",Background='#FBEEE6',foreground='#FFCAD4')
    cal.pack(pady = 20)
    def grad_date():
        # Label(frame_orderIngredients,text=cal.get_date(),bg='#FFFFFF',font='tahoma 20 bold').place(x=554,y=225)
        stapleorder_dateinfo.set(cal.get_date())
        # print(cal.get_date())
        window_calendar1.destroy()
    Button(window_calendar1, text = "Get Date",command=grad_date,bg='#9F8189').pack(pady=20)
    bt_cancel1 = Button(window_calendar1,image=photo_cancel,bg='#FFCAD4',relief=FLAT,command=window_calendar1.destroy)
    bt_cancel1.place(x=540,y=10,width=50,height=60)

def popup_calendarPrintReport():
    global window_calendar1
    window_calendar1= Toplevel()
    window_calendar1.geometry("600x400")
    window_calendar1.title("Calendar")
    window_calendar1.config(bg='#FFCAD4')
    window_calendar1.resizable(False,False)

    cal = Calendar(window_calendar1, selectmode='day',locate='th_TH',date_pattern="dd/mm/yyyy",Background='#FBEEE6',foreground='#FFCAD4')
    cal.pack(pady = 20)
    def grad_date():
        # Label(frame_printReport,text=cal.get_date(),bg='#FFFFFF',font='tahoma 36 bold').place(x=708,y=285)
        report_dateinfo.set(cal.get_date())
        # print(cal.get_date())
        window_calendar1.destroy()
    Button(window_calendar1, text = "Get Date",command=grad_date,bg='#9F8189').pack(pady=20)
    bt_cancel1 = Button(window_calendar1,image=photo_cancel,bg='#FFCAD4',relief=FLAT,command=window_calendar1.destroy)
    bt_cancel1.place(x=540,y=10,width=50,height=60)

def popup_member():
    global window_member
    global ety_telMember
    window_member = Toplevel()
    window_member.geometry("600x400")
    window_member.title("สมาชิก")
    window_member.config(bg='#FFCAD4')
    window_member.resizable(False,False)

    def validate1(P):
        if len(P) == 0:
            return True
        elif len(P) < 11 and P.isdigit():
            return True
        else:
            return False
    
    vcmd1 = (window.register(validate1), '%P')

    Label(window_member,text="กรอกเบอร์โทรศัพท์ที่ลงทะเบียนกับทางร้าน",bg='#FFCAD4',fg='#9F8189',font='tahoma 23 bold').place(x=92,y=90)
    ety_telMember = Entry(window_member, validate="key", validatecommand=vcmd1,font='tahoma 18 bold',justify=CENTER)
    ety_telMember.place(x=125,y=162,width=350,height=75)

    bt_IncreaseProduct = Button(window_member,text="ยืนยัน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=memberCheckCallback)
    bt_IncreaseProduct.place(x=225,y=304,width=150,height=50)

    bt_cancel2 = Button(window_member,image=photo_cancel,bg='#FFCAD4',relief=FLAT,command=window_member.destroy)
    bt_cancel2.place(x=540,y=10,width=50,height=60)

def popup_home(orderName,orderPrice):
    global window_home
    global ety_nameProduct
    window_home = Toplevel()
    window_home.geometry("600x400")
    window_home.title("สินค้า")
    window_home.config(bg='#FFCAD4')
    window_home.resizable(False,False)

    def validate1(P):
        if len(P) == 0:
            return True
        elif len(P) < 4 and P.isdigit():
            return True
        else:
            return False

    vcmd1 = (window.register(validate1), '%P')

    Label(window_home,text="ชื่อสินค้า : "+orderName,bg='#FFCAD4',fg='#9F8189',font='tahoma 24 bold').place(x=136,y=55)
    Label(window_home,text="ราคา : "+orderPrice+" บาท",bg='#FFCAD4',fg='#9F8189',font='tahoma 24 bold').place(x=136,y=107)
    ety_nameProduct = Spinbox(window_home,from_= 1, to = 25,justify=CENTER,validate="key",validatecommand=vcmd1,background='#FFFFFF')
    ety_nameProduct.place(x=150,y=178,width=300,height=50)

    bt_IncreaseProduct = Button(window_home,text="ยืนยัน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=popup_confirmCallBack)
    bt_IncreaseProduct.place(x=225,y=290,width=150,height=50)

    bt_cancel2 = Button(window_home,image=photo_cancel,bg='#FFCAD4',relief=FLAT,command=window_home.destroy)
    bt_cancel2.place(x=540,y=10,width=50,height=60)

def popup_Requisition(reqName,reqAmount,reqUnit):
    global window_Requisition
    global ety_reqAmt
    window_Requisition = Toplevel()
    window_Requisition.geometry("600x400")
    window_Requisition.title("วัตถุดิบ")
    window_Requisition.config(bg='#FFCAD4')
    window_Requisition.resizable(False,False)

    def validate1(P):
        if len(P) == 0:
            return True
        elif len(P) < 4 and P.isdigit():
            return True
        else:
            return False

    vcmd1 = (window.register(validate1), '%P')

    Label(window_Requisition,text="ชื่อวัตถุดิบ : "+reqName,bg='#FFCAD4',fg='#9F8189',font='tahoma 24 bold').place(x=136,y=55)
    Label(window_Requisition,text="จำนวนที่มีในคลัง : "+reqAmount,bg='#FFCAD4',fg='#9F8189',font='tahoma 24 bold').place(x=136,y=107)
    ety_reqAmt = Spinbox(window_Requisition,from_= 1, to = 25,justify=CENTER,background='#FFFFFF',validate="key",validatecommand=vcmd1)
    ety_reqAmt.place(x=150,y=178,width=300,height=50)

    bt_IncreaseProduct = Button(window_Requisition,text="ยืนยัน",font='tahoma 14 bold',bg='#9F8189',fg='#FBEEE6',command=popup_confirmCallBack)
    bt_IncreaseProduct.place(x=225,y=290,width=150,height=50)

    bt_cancel2 = Button(window_Requisition,image=photo_cancel,bg='#FFCAD4',relief=FLAT,command=window_Requisition.destroy)
    bt_cancel2.place(x=540,y=10,width=50,height=60)

def popup_bill():
    global window_bill
    global pageNAME
    global order_name_lst,order_amount_lst,order_price_lst
    global order_total,change,moneyReceive,total_order_price,tag

    moneyReceive = ety_receive.get()


    pageNAME = "HOME"
    frame_confirmSelling.destroy()
    mytree_home2.delete(*mytree_home2.get_children())
    
    if tag == "MEMBER": 
        change = int(moneyReceive) - int(member_total)
    else:
        change = int(moneyReceive) - int(order_total)

    order_count = 0
    yValue = 256
    window_bill = Toplevel()
    window_bill.geometry("400x800")
    window_bill.title("ใบเสร็จ")
    window_bill.config(bg='#FFFFFF')
    window_bill.resizable(False,False)

    Label(window_bill,image=photo_logo2,bg='#FFFFFF').pack()
    Label(window_bill,text="ผู้ขาย : "+employee_name,bg='#FFFFFF',font='tahoma 10 ').place(x=75,y=124)
    Label(window_bill,text="-"*35,font='tahoma 17',bg='#FFFFFF').place(x=75,y=142)
    Label(window_bill,text="ใบเสร็จรับเงิน",font='tahoma 17',bg='#FFFFFF').place(x=148,y=172)
    Label(window_bill,text="-"*35,font='tahoma 17',bg='#FFFFFF').place(x=75,y=202)
    Label(window_bill,text="ชื่อสินค้า",font='tahoma 13',bg='#FFFFFF').place(x=80,y=236)
    Label(window_bill,text="จำนวน",font='tahoma 13',bg='#FFFFFF').place(x=190,y=236)
    Label(window_bill,text="ราคา",font='tahoma 13',bg='#FFFFFF').place(x=280,y=236)
    while order_count+1 <= len(order_name_lst) :
        Label(window_bill,text=order_name_lst[order_count],font='tahoma 13',bg='#FFFFFF').place(x=80,y=yValue)
        Label(window_bill,text=order_amount_lst[order_count],font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue)
        Label(window_bill,text=order_price_lst[order_count],font='tahoma 13',bg='#FFFFFF').place(x=280,y=yValue)
        yValue+=20
        order_count+=1
    # Label(window_bill,text="ได้รับเงิน : " + str(moneyReceive),font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue+72)
    if tag == "MEMBER": 
        customerPoint = getCustomerPoint()
        Label(window_bill,text="ราคารวม : "+ str(int(order_total)),font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue+24)
        Label(window_bill,text="ส่วนลด : "+ str(int(Memberdiscount)),font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue+48)
        Label(window_bill,text="ยอดสุทธิ : "+ str(int(member_total)),font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue+96)
        Label(window_bill,text="ได้รับเงิน : " + str(moneyReceive),font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue+72)
        Label(window_bill,text="เงินทอน  : " + str(change),font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue+120)
        if customerPoint < 9 :
            customerPoint+=1
            Label(window_bill,text="***** จำนวนแต้มสะสม : "+str(customerPoint)+"/10 *****",font='tahoma 13',bg='#FFFFFF').place(x=94,y=685)
        elif customerPoint == 9 :
            customerPoint=0
            Label(window_bill,text="***** คุณได้รับสิทธิ๋แลกฟรี 1 แก้ว *****",font='tahoma 13',bg='#FFFFFF').place(x=74,y=685)
        addPoint(customerPoint)
        
    else:
        Label(window_bill,text="ยอดสุทธิ : "+ str(order_total),font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue+96)
        Label(window_bill,text="ได้รับเงิน : " + str(moneyReceive),font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue+72)
        Label(window_bill,text="เงินทอน  : " + str(change),font='tahoma 13',bg='#FFFFFF').place(x=190,y=yValue+120)
    
    Label(window_bill,text="วันที่ชำระ : "+ str(dateToday),font='tahoma 13',bg='#FFFFFF').place(x=124,y=705)
    if tag == "MEMBER": 
        sql = "select * from member where customer_phone = ?"
        cursor.execute(sql,[member_tel])
        result = cursor.fetchone()
        Label(window_bill,text="ชื่อสมาชิก : "+ str(result[1]+" "+result[2]),font='tahoma 13',bg='#FFFFFF').place(x=100,y=730)
    Label(window_bill,text="ขอขอบคุณที่ใช้บริการ",font='tahoma 13',bg='#FFFFFF').place(x=129,y=756)
    Label(window_bill,text="Thank you for drinking with us",font='tahoma 13',bg='#FFFFFF').place(x=94,y=775)
    
    addOrderToDB()

    tag = " "
    order_name_lst = []
    order_amount_lst = []
    order_price_lst = []
    order_total = 0
    total['text'] = "ยอดสุทธิ :         " + str(order_total)

def productCallBack(todo) :
    global productname_before_edit,productprice_before_edit,producttype_before_edit
    if todo == "เพิ่ม" :
        if product_nameinfo.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณาระบุชื่อสินค้า")
            ety_nameProduct.focus_force()
        else :
            if product_priceinfo.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณาระบุราคาสินค้า")
                ety_priceProduct.focus_force()
            else :
                sql = "select * from product where product_name = ?"
                cursor.execute(sql,[product_nameinfo.get()])
                result = cursor.fetchone()
                if result :
                    messagebox.showwarning("ระบบ:","สินค้ามีอยู่ในระบบอยู่แล้ว")
                else :
                    messagebox.showinfo("ระบบ:","เพิ่มรายการสินค้าสำเร็จ")
                    sql = "insert into product(product_name,product_type,product_price) values (?,?,?)"
                    cursor.execute(sql,[product_nameinfo.get(),product_dropdown_type.get(),int(product_priceinfo.get())])
                    conn.commit()
                    ety_nameProduct.delete(0,END)
                    ety_priceProduct.delete(0,END)
                    product_dropdown_type.set("กาแฟ")
                    fetch_Tree(pageNAME,mytree_product,cursor)
    
    elif todo == "แก้ไข" :
        if product_nameinfo.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณาเลือกสินค้าที่จะแก้ไข")
            ety_nameProduct.focus_force()
        else :
            if product_priceinfo.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณาระบุราคาสินค้า")
                ety_priceProduct.focus_force()
            else :
                messagebox.showinfo("ระบบ:","แก้ไขรายการสินค้าสำเร็จ")
                sql = "UPDATE product SET product_name=?,product_type=?,product_price=? WHERE product_name=? AND product_type=? AND product_price=?"
                cursor.execute(sql,[product_nameinfo.get(),product_dropdown_type.get(),int(product_priceinfo.get()),productname_before_edit,producttype_before_edit,productprice_before_edit])
                conn.commit()
                ety_nameProduct.delete(0,END)
                ety_priceProduct.delete(0,END)
                product_dropdown_type.set("กาแฟ")
                fetch_Tree(pageNAME,mytree_product,cursor)
                productname_before_edit = ""
                productprice_before_edit = ""
                producttype_before_edit = ""

    elif todo == "ลบ" :
        if product_nameinfo.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณาเลือกสินค้าที่จะลบ")
            ety_nameProduct.focus_force()
        else :
            if product_priceinfo.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณาระบุราคาสินค้า")
                ety_priceProduct.focus_force()
            else :
                msg = messagebox.askquestion ('ระบบ','ต้องการลบรายการสินค้าหรือไม่',icon = 'warning')
                if msg == "yes" :
                    sql = "select * from product where product_name=? AND product_type=? AND product_price=?"
                    cursor.execute(sql,[product_nameinfo.get(),product_dropdown_type.get(),product_priceinfo.get()])
                    result = cursor.fetchone()
                    if result :
                        messagebox.showinfo("ระบบ:","ลบรายการสินค้าสำเร็จ")
                        sql = "delete from product where product_name=? AND product_type=? AND product_price=?"
                        cursor.execute(sql,[product_nameinfo.get(),product_dropdown_type.get(),product_priceinfo.get()])
                        conn.commit()
                        ety_nameProduct.delete(0,END)
                        ety_priceProduct.delete(0,END)
                        product_dropdown_type.set("กาแฟ")
                        fetch_Tree(pageNAME,mytree_product,cursor)
                    else :
                        messagebox.showwarning("ระบบ:","ไม่พบรายการสินค้าที่จะลบ")

def stockCallBack(todo) :
    global staplename_before_edit
    amount = int(staple_amount_info.get())
    if todo == "เพิ่ม" :
        if amount > 0 :
            messagebox.showwarning("ระบบ:","ไม่สามารถเพิ่มวัตถุดิบพร้อมจำนวนได้")
        else :
            if staple_nameinfo.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณาระบุชื่อวัตถุดิบ")
                ety_nameIngredients.focus_force()
            else :
                sql = "select * from staple where staple_name = ?"
                cursor.execute(sql,[staple_nameinfo.get()])
                result = cursor.fetchone()
                if result :
                    messagebox.showwarning("ระบบ:","วัตถุดิบมีอยู่ในระบบแล้ว")
                else :
                    messagebox.showinfo("ระบบ:","เพิ่มวัตถุดิบสำเร็จ")
                    sql = "insert into staple(staple_name,staple_amount,staple_unit) values (?,?,?)"
                    cursor.execute(sql,[staple_nameinfo.get(),int(staple_amount_info.get()),manageStock_dropdown_clicked.get()])
                    conn.commit()
                    ety_nameIngredients.delete(0,END)
                    ety_amountIngredients.delete(0,END)
                    staple_amount_info.set("0")
                    manageStock_dropdown_clicked.set("กรัม")
                    fetch_Tree(pageNAME,mytree_stock,cursor)
    
    elif todo == "แก้ไข" :
        if staple_nameinfo.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณาเลือกวัตถุดิบที่จะแก้ไข")
            ety_nameIngredients.focus_force()
        else :
            messagebox.showinfo("ระบบ:","แก้ไขวัตถุดิบสำเร็จ")
            sql = "UPDATE staple SET staple_name=?,staple_amount=?,staple_unit=? WHERE staple_name=?"
            cursor.execute(sql,[staple_nameinfo.get(),int(staple_amount_info.get()),manageStock_dropdown_clicked.get(),staplename_before_edit])
            conn.commit()
            ety_nameIngredients.delete(0,END)
            ety_amountIngredients.delete(0,END)
            staple_amount_info.set("0")
            manageStock_dropdown_clicked.set("กรัม")
            fetch_Tree(pageNAME,mytree_stock,cursor)
            staplename_before_edit = ""

    elif todo == "ลบ" :
        if staple_nameinfo.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณาเลือกวัตถุดิบที่จะทำการลบ")
            ety_nameIngredients.focus_force()
        else :
            msg = messagebox.askquestion ('ระบบ','ต้องการลบวัตถุดิบหรือไม่',icon = 'warning')
            if msg == "yes" :
                sql = "select * from staple where staple_name=? AND staple_amount=? AND staple_unit=?"
                cursor.execute(sql,[staple_nameinfo.get(),int(staple_amount_info.get()),manageStock_dropdown_clicked.get()])
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("ระบบ:","ลบวัตถุดิบสำเร็จ")
                    sql = "delete from staple where staple_name=? AND staple_amount=? AND staple_unit=?"
                    cursor.execute(sql,[staple_nameinfo.get(),int(staple_amount_info.get()),manageStock_dropdown_clicked.get()])
                    conn.commit()
                    ety_nameIngredients.delete(0,END)
                    ety_amountIngredients.delete(0,END)
                    staple_amount_info.set("0")
                    manageStock_dropdown_clicked.set("กรัม")
                    fetch_Tree(pageNAME,mytree_stock,cursor)
                else :
                    messagebox.showwarning("ระบบ:","ไม่พบวัตถุดิบที่จะลบ")

def StockManage_CallBack() :
    global userPERM,pageNAME
    if pageNAME == "ORDER_STOCK" :
        if stapleorder_dateinfo.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณาระบุวันที่ทำการสั่งซื้อ")
            ety_dateOrderIngredients.focus_force()
        else :
            if stapleorder_companyinfo.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณากรอกชื่อบริษัทที่ซื้อวัตถุดิบ")
                ety_organization_order.focus_force()
            else :
                if stapleorder_nameinfo.get() == "" :
                    messagebox.showwarning("ระบบ:","กรุณาเลือกวัตถุดิบที่จะบันทึก")
                    ety_nameIngredients_order.focus_force()
                else :
                    if stapleorder_amountinfo.get() == "" :
                        messagebox.showwarning("ระบบ:","กรุณากรอกจำนวนวัตถุดิบที่ทำการสั่งซื้อ")
                        ety_amountIngredients_order.focus_force()
                    else :
                        if stapleorder_priceinfo.get() == ""  :
                            messagebox.showwarning("ระบบ:","กรุณากรอกราคาสุทธิของวัตถุดิบ")
                            ety_priceIngredients_order.focus_force()
                        else :
                            messagebox.showinfo("ระบบ:","บันทึกการสั่งซื้อสำเร็จ")
                            sql = "update staple set staple_amount=? where staple_name=?"
                            cursor.execute(sql,[int(staple_current_amount)+int(stapleorder_amountinfo.get()),stapleorder_nameinfo.get()])
                            conn.commit()

                            sql = "insert into stapleorder(stapleorder_date,stapleorder_person,stapleorder_name,stapleorder_amount,stapleorder_unit,stapleorder_price,stapleorder_company) values (?,?,?,?,?,?,?)"
                            cursor.execute(sql,[stapleorder_dateinfo.get(),employee_name,stapleorder_nameinfo.get(),int(stapleorder_amountinfo.get()),stapleorder_unitinfo.get(),int(stapleorder_amountinfo.get())*int(stapleorder_priceinfo.get()),stapleorder_companyinfo.get()])
                            conn.commit()

                            ety_dateOrderIngredients.delete(0,END)
                            ety_organization_order.delete(0,END)
                            ety_nameIngredients_order.delete(0,END)
                            ety_amountIngredients_order.delete(0,END)
                            ety_priceIngredients_order.delete(0,END)
                            ety_unitIngredients_order.delete(0,END)
                            stapleorder_unitinfo.set("")
                            stapleorder_dateinfo.set("")
                            stapleorder_nameinfo.set("")

                            fetch_Tree(pageNAME,mytree_orderstock,cursor)
                            fetch_Tree(pageNAME,mytree_stock,cursor)

def loginCallBack():
    global userPERM,pageNAME
    global epy_address
    global employee_name
    if userinfo.get() == "":
        messagebox.showwarning("ระบบ:","กรุณากรอกชื่อผู้ใช้งาน")
        ety_username.focus_force()
    else:
        if pwdinfo.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกรหัสผ่าน")
            ety_pwd.focus_force()
        else : 
            sql = "select * from employee where employee_username=? AND employee_password=?"
            cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("ระบบ:","เข้าสู่ระบบสำเร็จ")
                sql = "select * from employee where employee_username=? AND employee_password=?"
                cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
                result = cursor.fetchone()
                if result[9] == 'เจ้าของร้าน':
                    userPERM = 'เจ้าของร้าน'
                elif result[9] == 'พนักงาน':
                    userPERM = 'พนักงาน'
                employee_name = result[3] + " " +result[4]
                # print(employee_name)
                widget_home()
            else :
                messagebox.showwarning("ระบบ:","ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง")
                ety_username.select_range(0,END)
                ety_username.focus_force()

def EmployeeManage_CallBack() :
    global userPERM,pageNAME
    global epy_address,mb_address
    if pageNAME == "REGISTER_EMPLOYEE" :
        address = ety_address_employee_1.get(1.0, "end-1c")
        # print(address)
        if employee_name1info.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกชื่อพนักงาน")
            ety_Name_employee_1.focus_force()
        else :
            if employee_surname1info.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณากรอกนามสกุลพนักงาน")
                ety_surName_employee_1.focus_force()
            else :
                if employee_id1info.get() == "" :
                    messagebox.showwarning("ระบบ:","กรุณากรอกเลขบัตรประชาชนของพนักงาน")
                    ety_Id_employee_1.focus_force()
                else :
                    if employee_date1info.get() == "" :
                        messagebox.showwarning("ระบบ:","กรุณาระบุวันเกิดของพนักงาน")
                        ety_calendar_employee_1.focus_force()
                    else :
                        if employee_phone1info.get() == "" :
                            messagebox.showwarning("ระบบ:","กรุณากรอกเบอร์โทรศัพท์ของพนักงาน")
                            ety_phone_employee_1.focus_force()
                        else :
                            if employee_username1info.get() == "" :
                                messagebox.showwarning("ระบบ:","กรุณากรอกชื่อผู้ใช้งานของพนักงาน")
                                ety_Username_employee_1.focus_force()
                            else :
                                if employee_pwd1info.get() == "" :
                                    messagebox.showwarning("ระบบ:","กรุณากรอกรหัสผ่านของพนักงาน")
                                    ety_Pwd_employee_1.focus_force()
                                else :
                                    if employee_conpwd1info.get() == "" :
                                        messagebox.showwarning("ระบบ:","กรุณายืนยันรหัสผ่านของพนักงาน")
                                        ety_NewPwd_employee_1.focus_force()
                                    else :
                                        if address == "" :
                                            messagebox.showwarning("ระบบ:","กรุณากรอกที่อยู่ของพนักงาน")
                                        else :
                                            if len(employee_id1info.get()) != 13 :
                                                messagebox.showwarning("ระบบ:","กรุณากรอกเลขบัตรประชาชนของพนักงานให้ครบ")
                                                ety_Id_employee_1.focus_force()
                                            else :
                                                if len(employee_phone1info.get()) != 10 :
                                                    messagebox.showwarning("ระบบ:","กรุณากรอกเบอร์โทรศัพท์ของพนักงานให้ครบ")
                                                    ety_phone_employee_1.focus_force()
                                                else :
                                                    if employee_pwd1info.get() != employee_conpwd1info.get() :
                                                        messagebox.showwarning("ระบบ:","การยืนยันรหัสผ่านไม่ตรงกัน")
                                                    else :
                                                        sql = "select * from employee where employee_username=? OR employee_id=?"
                                                        cursor.execute(sql,[employee_username1info.get(),employee_id1info.get()])
                                                        result = cursor.fetchone()
                                                        if result :
                                                            messagebox.showwarning("ระบบ:","มีข้อมูลพนักงานอยู่ในระบบแล้ว")
                                                        else :
                                                            messagebox.showinfo("ระบบ:","ลงทะเบียนบัญชีพนักงานสำเร็จ")
                                                            sql = "insert into employee(employee_id,employee_username,employee_password,employee_name,employee_surname,employee_gender,employee_birth,employee_phone,employee_address,employee_permission) values (?,?,?,?,?,?,?,?,?,?)"
                                                            cursor.execute(sql,[employee_id1info.get(),employee_username1info.get(),employee_pwd1info.get(),employee_name1info.get(),employee_surname1info.get(),employee_gender1info.get(),ety_calendar_employee_1.get(),employee_phone1info.get(),address,"พนักงาน"])
                                                            conn.commit()
                                                            ety_Name_employee_1.delete(0,END)
                                                            ety_Id_employee_1.delete(0,END)
                                                            ety_phone_employee_1.delete(0,END)
                                                            ety_Username_employee_1.delete(0,END)
                                                            ety_address_employee_1.delete("1.0",END)
                                                            ety_surName_employee_1.delete(0,END)
                                                            ety_calendar_employee_1.delete(0,END)
                                                            employee_gender1info.set("ชาย")
                                                            ety_Pwd_employee_1.delete(0,END)
                                                            ety_NewPwd_employee_1.delete(0,END)
                                                            employee_date1info.set("")
                                                            address = ""
                                                            frame_registerEmployee.destroy()
                                                            pageNAME = "MANAGE_EMPLOYEE"
                                                            fetch_Tree(pageNAME,mytree_employee1,cursor)

                                                            employee_name2info.set("")

    elif pageNAME == "EDIT_EMPLOYEE" :
        address = ety_address_employee_2.get(1.0, "end-1c")
        # print(address)
        if employee_name2info.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกชื่อพนักงาน")
            ety_Name_employee_2.focus_force()
        else :
            if employee_surname2info.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณากรอกนามสกุลพนักงาน")
                ety_surName_employee_2.focus_force()
            else :
                if employee_id2info.get() == "" :
                    messagebox.showwarning("ระบบ:","กรุณากรอกเลขบัตรประชาชนของพนักงาน")
                    ety_Id_employee_2.focus_force()
                else :
                    if employee_date2info.get() == "" :
                        messagebox.showwarning("ระบบ:","กรุณาระบุวันเกิดของพนักงาน")
                        ety_calendar_employee_2.focus_force()
                    else :
                        if employee_phone2info.get() == "" :
                            messagebox.showwarning("ระบบ:","กรุณากรอกเบอร์โทรศัพท์ของพนักงาน")
                            ety_phone_employee_2.focus_force()
                        else :
                            if employee_username2info.get() == "" :
                                messagebox.showwarning("ระบบ:","กรุณากรอกชื่อผู้ใช้งานของพนักงาน")
                                ety_Username_employee_2.focus_force()
                            else :
                                if employee_pwd2info.get() == "" :
                                    messagebox.showwarning("ระบบ:","กรุณากรอกรหัสผ่านของพนักงาน")
                                    ety_Pwd_employee_2.focus_force()
                                else :
                                    if employee_conpwd2info.get() == "" :
                                        messagebox.showwarning("ระบบ:","กรุณายืนยันรหัสผ่านของพนักงาน")
                                        ety_NewPwd_employee_2.focus_force()
                                    else :
                                        if address == "" :
                                            messagebox.showwarning("ระบบ:","กรุณากรอกที่อยู่ของพนักงาน")
                                        else :
                                            if len(employee_id2info.get()) != 13 :
                                                messagebox.showwarning("ระบบ:","กรุณากรอกเลขบัตรประชาชนของพนักงานให้ครบ")
                                                ety_Id_employee_2.focus_force()
                                            else :
                                                if len(employee_phone2info.get()) != 10 :
                                                    messagebox.showwarning("ระบบ:","กรุณากรอกเบอร์โทรศัพท์ของพนักงานให้ครบ")
                                                    ety_phone_employee_2.focus_force()
                                                else :
                                                    if employee_pwd2info.get() != employee_conpwd2info.get() :
                                                        messagebox.showwarning("ระบบ:","การยืนยันรหัสผ่านไม่ตรงกัน")
                                                    else :
                                                        sql = "select * from employee where employee_username=? OR employee_id=?"
                                                        cursor.execute(sql,[employee_username2info.get(),employee_id2info.get()])
                                                        result = cursor.fetchone()
                                                        if result :
                                                            messagebox.showinfo("ระบบ:","แก้ไขข้อมูลพนักงานสำเร็จ")
                                                            sql = "UPDATE employee SET employee_id=?,employee_username=?,employee_password=?,employee_name=?,employee_surname=?,employee_gender=?,employee_birth=?,employee_phone=?,employee_address=?,employee_permission=? WHERE employee_id=? "
                                                            cursor.execute(sql,[employee_id2info.get(),employee_username2info.get(),employee_pwd2info.get(),employee_name2info.get(),employee_surname2info.get(),employee_gender2info.get(),ety_calendar_employee_2.get(),employee_phone2info.get(),address,"พนักงาน",employee_id2info.get()])
                                                            conn.commit()
                                                            ety_Name_employee_2.delete(0,END)
                                                            ety_Id_employee_2.delete(0,END)
                                                            ety_phone_employee_2.delete(0,END)
                                                            ety_Username_employee_2.delete(0,END)
                                                            ety_address_employee_2.delete("1.0",END)
                                                            ety_surName_employee_2.delete(0,END)
                                                            ety_calendar_employee_2.delete(0,END)
                                                            employee_gender2info.set("ชาย")
                                                            ety_Pwd_employee_2.delete(0,END)
                                                            ety_NewPwd_employee_2.delete(0,END)
                                                            employee_date2info.set("")
                                                            address = ""
                                                            epy_address = ""
                                                            frame_editEmployee.destroy()
                                                            pageNAME = "MANAGE_EMPLOYEE"
                                                            fetch_Tree(pageNAME,mytree_employee1,cursor)

    elif pageNAME == "REGISTER_CUSTOMER" :
        address = ety_Address_Member_1.get(1.0, "end-1c")

        domainlist = ["@gmail.com","@hotmail.com","@outlook.com"]
        i = 0
        # print(address)
        if customer_name1info.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกชื่อลูกค้า")
            ety_Name_member_1.focus_force()
        else :
            if customer_surname1info.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณากรอกนามสกุลลูกค้า")
                ety_surName_member_1.focus_force()
            else :
                if customer_phone1info.get() == "" :
                    messagebox.showwarning("ระบบ:","กรุณากรอกเบอร์โทรศัพท์ของลูกค้า")
                    ety_phone_member_1.focus_force()
                else :
                    if customer_email1info.get() == "" :
                        messagebox.showwarning("ระบบ:","กรุณากรอกอีเมลลูกค้า")
                        ety_email_member_1.focus_force()
                    else :
                        if customer_date1info.get() == "" :
                            messagebox.showwarning("ระบบ:","กรุณาระบุวันเกิดของลูกค้า")
                            ety_calendar_member_1.focus_force()
                        else :
                            if address == "" :
                                messagebox.showwarning("ระบบ:","กรุณากรอกที่อยู่ของลูกค้า")
                            else :
                                if len(customer_phone1info.get()) != 10 :
                                    messagebox.showwarning("ระบบ:","กรุณากรอกเบอร์โทรศัพท์ของลูกค้าให้ครบ")
                                    ety_phone_member_1.focus_force()
                                else :
                                    for x in domainlist :
                                        if x not in customer_email1info.get() :
                                            if i == len(domainlist)-1 :
                                                messagebox.showwarning("ระบบ:","รูปแบบ email ไม่ถูกต้อง")
                                                break
                                            i = i + 1
                                            continue
                                    else :
                                        sql = "select * from member where customer_phone=?"
                                        cursor.execute(sql,[customer_phone1info.get()])
                                        result = cursor.fetchone()
                                        if result :
                                            messagebox.showwarning("ระบบ:","ลูกค้าได้ทำการลงทะเบียนมาก่อนแล้ว")
                                        else :
                                            messagebox.showinfo("ระบบ:","ลงทะเบียนสมาชิกลูกค้าสำเร็จ")
                                            sql = "insert into member(customer_phone,customer_name,customer_surname,customer_gender,customer_birth,customer_email,customer_address,customer_point) values (?,?,?,?,?,?,?,?)"
                                            cursor.execute(sql,[customer_phone1info.get(),customer_name1info.get(),customer_surname1info.get(),customer_gender1info.get(),customer_date1info.get(),customer_email1info.get(),address,0])
                                            conn.commit()
                                            ety_Name_member_1.delete(0,END)
                                            ety_phone_member_1.delete(0,END)
                                            ety_Address_Member_1.delete("1.0",END)
                                            ety_surName_member_1.delete(0,END)
                                            ety_calendar_member_1.delete(0,END)
                                            customer_gender1info.set("ชาย")
                                            ety_email_member_1.delete(0,END)
                                            customer_date1info.set("")
                                            address = ""
                                            frame_registerMember.destroy()
                                            pageNAME = "MANAGE_CUSTOMER"
                                            fetch_Tree(pageNAME,mytree_customer,cursor)

                                            customer_name2info.set("")

    elif pageNAME == "EDIT_CUSTOMER" :
        address = ety_Address_Member_2.get(1.0, "end-1c")
        domainlist = ["@gmail.com","@hotmail.com","@outlook.com"]
        i = 0
        if customer_name2info.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกชื่อลูกค้า")
            ety_Name_member_2.focus_force()
        else :
            if customer_surname2info.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณากรอกนามสกุลลูกค้า")
                ety_surName_member_2.focus_force()
            else :
                if customer_phone2info.get() == "" :
                    messagebox.showwarning("ระบบ:","กรุณากรอกเบอร์โทรศัพท์ของลูกค้า")
                    ety_phone_member_2.focus_force()
                else :
                    if customer_email2info.get() == "" :
                        messagebox.showwarning("ระบบ:","กรุณากรอกอีเมลลูกค้า")
                        ety_email_member_2.focus_force()
                    else :
                        if customer_date2info.get() == "" :
                            messagebox.showwarning("ระบบ:","กรุณาระบุวันเกิดของลูกค้า")
                            ety_calendar_member_2.focus_force()
                        else :
                            if address == "" :
                                messagebox.showwarning("ระบบ:","กรุณากรอกที่อยู่ของลูกค้า")
                            else :
                                if len(customer_phone2info.get()) != 10 :
                                    messagebox.showwarning("ระบบ:","กรุณากรอกเบอร์โทรศัพท์ของลูกค้าให้ครบ")
                                    ety_phone_member_2.focus_force()
                                else :
                                    for x in domainlist :
                                        if x not in customer_email2info.get() :
                                            if i == len(domainlist)-1 :
                                                messagebox.showwarning("ระบบ:","รูปแบบ email ไม่ถูกต้อง")
                                                break
                                            i = i + 1
                                            continue
                                    else :
                                        sql = "select * from member where customer_phone=?"
                                        cursor.execute(sql,[customer_phone2info.get()])
                                        result = cursor.fetchone()
                                        if result :
                                            messagebox.showinfo("ระบบ:","แก้ไขข้อมูลสมาชิกลูกค้าสำเร็จ")
                                            sql = "UPDATE member SET customer_phone=?,customer_name=?,customer_surname=?,customer_gender=?,customer_birth=?,customer_email=?,customer_address=? WHERE customer_phone=?"
                                            cursor.execute(sql,[customer_phone2info.get(),customer_name2info.get(),customer_surname2info.get(),customer_gender2info.get(),customer_date2info.get(),customer_email2info.get(),address,customer_phone2info.get()])
                                            conn.commit()
                                            ety_Name_member_2.delete(0,END)
                                            ety_phone_member_2.delete(0,END)
                                            ety_Address_Member_2.delete("1.0",END)
                                            ety_surName_member_2.delete(0,END)
                                            ety_calendar_member_2.delete(0,END)
                                            customer_gender2info.set("ชาย")
                                            customer_date2info.set("")
                                            address = ""
                                            mb_address = ""
                                            frame_editMember.destroy()
                                            pageNAME = "MANAGE_CUSTOMER"
                                            fetch_Tree(pageNAME,mytree_customer,cursor)

def removeCallBack() :
    global epy_address,mb_address
    if pageNAME == "MANAGE_EMPLOYEE" :
        if employee_name2info.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณาเลือกพนักงานที่จะลบบัญชี")
        else :
            msg = messagebox.askquestion ('ระบบ','ต้องการลบบัญชีพนักงานหรือไม่',icon = 'warning')
            if msg == "yes" :
                sql = "delete from employee where employee_id = ?"
                cursor.execute(sql,[employee_id2info.get()])
                conn.commit()
                employee_name2info.set("")
                employee_surname2info.set("")
                employee_id2info.set("")
                employee_date2info.set("")
                employee_phone2info.set("")
                employee_gender2info.set("")
                employee_username2info.set("")
                employee_pwd2info.set("")
                epy_address = ""
                fetch_Tree(pageNAME,mytree_employee1,cursor)

    elif pageNAME == "MANAGE_CUSTOMER" :
        if customer_name2info.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณาเลือกบัญชีลูกค้าที่จะลบบัญชี")
        else :
            msg = messagebox.askquestion ('ระบบ','ต้องการลบบัญชีลูกค้าหรือไม่',icon = 'warning')
            if msg == "yes" :
                sql = "delete from member where customer_phone = ?"
                cursor.execute(sql,[customer_phone2info.get()])
                conn.commit()
                customer_name2info.set("")
                customer_surname2info.set("")
                customer_date2info.set("")
                customer_phone2info.set("")
                customer_gender2info.set("")
                mb_address = ""
                fetch_Tree(pageNAME,mytree_customer,cursor)
    
    elif pageNAME == "HOME" :
        global order_total
        global order_name_lst,order_amount_lst,order_price_lst
        
        try :
            selected_item = mytree_home2.selection()[0] ## get selected item
        except :
            messagebox.showwarning("ระบบ:","กรุณาเลือกรายการที่จะลบ")
        else :
            values = mytree_home2.item(mytree_home2.focus(),'values')
            nameOrder,removeQuan,removePrice = values[0],values[1],values[2]
            # print(nameOrder,removeQuan,removePrice)
            order_name_lst.remove(nameOrder)
            order_amount_lst.remove(removeQuan)
            order_price_lst.remove(int(removePrice))
            # removeOrder = int(removeQuan) * int(removePrice)
            order_total -= int(removePrice)
            total['text'] = "ยอดสุทธิ :         " + str(order_total)
            mytree_home2.delete(selected_item)

    elif pageNAME == "REQUISITION" :
        global req_name_lst,req_amount_lst,req_unit_lst
        
        try :
            selected_item = mytree_RequisitionIngredients_2.selection()[0] ## get selected item
        except :
            messagebox.showwarning("ระบบ:","กรุณาเลือกรายการที่จะลบ")
        else :
            values = mytree_RequisitionIngredients_2.item(mytree_RequisitionIngredients_2.focus(),'values')
            nameReq,amtReq,unitReq = values[0],values[1],values[2]
            req_name_lst.remove(nameReq)
            req_amount_lst.remove(amtReq)
            req_unit_lst.remove(unitReq)
            # print(req_name_lst,req_amount_lst)
            mytree_RequisitionIngredients_2.delete(selected_item)

def clearCallBack() :
    if pageNAME == "REGISTER_EMPLOYEE" :
        ety_Name_employee_1.delete(0, END)
        ety_surName_employee_1.delete(0, END)
        ety_Id_employee_1.delete(0, END)
        ety_calendar_employee_1.delete(0, END)
        ety_phone_employee_1.delete(0, END)
        ety_Username_employee_1.delete(0, END)
        ety_Pwd_employee_1.delete(0, END)
        ety_address_employee_1.delete("1.0",END)
        employee_gender1info.set("ชาย")
        employee_date1info.set("")
    elif pageNAME == "EDIT_EMPLOYEE" :
        ety_Name_employee_2.delete(0, END)
        ety_surName_employee_2.delete(0, END)
        # ety_Id_employee_2.delete(0, END)
        ety_calendar_employee_2.delete(0, END)
        ety_phone_employee_2.delete(0, END)
        ety_Username_employee_2.delete(0, END)
        ety_Pwd_employee_2.delete(0, END)
        ety_address_employee_2.delete("1.0",END)
        employee_gender2info.set("ชาย")
        employee_date2info.set("")
    elif pageNAME == "REGISTER_CUSTOMER" :
        ety_Name_member_1.delete(0, END)
        ety_phone_member_1.delete(0, END)
        ety_email_member_1.delete(0, END)
        ety_surName_member_1.delete(0, END)
        ety_calendar_member_1.delete(0, END)
        ety_Address_Member_1.delete("1.0",END)
        customer_gender1info.set("ชาย")
        customer_date1info.set("")
    elif pageNAME == "EDIT_CUSTOMER" :
        ety_Name_member_2.delete(0, END)
        # ety_phone_member_2.delete(0, END)
        ety_email_member_2.delete(0, END)
        ety_surName_member_2.delete(0, END)
        ety_calendar_member_2.delete(0, END)
        ety_Address_Member_2.delete("1.0",END)
        customer_gender2info.set("ชาย")
        customer_date2info.set("")

    elif pageNAME == "ORDER_STOCK"  :
        ety_dateOrderIngredients.delete(0, END)
        ety_nameIngredients_order.delete(0, END)
        ety_priceIngredients_order.delete(0, END)
        ety_organization_order.delete(0, END)
        ety_amountIngredients_order.delete(0, END)
        stapleorder_dateinfo.set("")
        stapleorder_nameinfo.set("")

def backPAGE_Callback() :
    global userPERM,pageNAME
    global address,epy_address,mb_address
    global order_total
    if pageNAME == "HOME" :
        msg = messagebox.askquestion ('ระบบ','ต้องการออกจากระบบหรือไม่',icon = 'warning')
        if msg == "yes" :
            ety_pwd.delete(0,END)
            order_total = 0
            frame_home.destroy()

    elif pageNAME == "EDIT_EMPLOYEE" :
        pageNAME = "MANAGE_EMPLOYEE"
        ety_Name_employee_2.delete(0,END)
        ety_Id_employee_2.delete(0,END)
        ety_phone_employee_2.delete(0,END)
        ety_Username_employee_2.delete(0,END)
        ety_address_employee_2.delete("1.0",END)
        ety_surName_employee_2.delete(0,END)
        ety_calendar_employee_2.delete(0,END)
        employee_gender2info.set("ชาย")
        ety_Pwd_employee_2.delete(0,END)
        ety_NewPwd_employee_2.delete(0,END)
        employee_date2info.set("")
        address = ""
        epy_address = ""
        frame_editEmployee.destroy()

    elif pageNAME == "REGISTER_EMPLOYEE" :
        pageNAME = "MANAGE_EMPLOYEE"
        ety_Name_employee_1.delete(0,END)
        ety_Id_employee_1.delete(0,END)
        ety_phone_employee_1.delete(0,END)
        ety_Username_employee_1.delete(0,END)
        ety_address_employee_1.delete("1.0",END)
        ety_surName_employee_1.delete(0,END)
        ety_calendar_employee_1.delete(0,END)
        employee_gender1info.set("ชาย")
        ety_Pwd_employee_1.delete(0,END)
        ety_NewPwd_employee_1.delete(0,END)
        employee_date1info.set("")
        address = ""
        frame_registerEmployee.destroy()

    elif pageNAME == "MANAGE_EMPLOYEE" :
        pageNAME = "HOME"
        frame_employeeManage.destroy()

    elif pageNAME == "HISTORY_EMPLOYEE" :
        pageNAME = "MANAGE_EMPLOYEE"
        frame_historyWorking.destroy()

    elif pageNAME == "EDIT_CUSTOMER" :
        pageNAME = "MANAGE_CUSTOMER"
        ety_Name_member_2.delete(0, END)
        ety_phone_member_2.delete(0, END)
        ety_email_member_2.delete(0, END)
        ety_surName_member_2.delete(0, END)
        ety_calendar_member_2.delete(0, END)
        ety_Address_Member_2.delete("1.0",END)
        customer_gender2info.set("ชาย")
        customer_date2info.set("")
        address = ""
        frame_editMember.destroy()

    elif pageNAME == "REGISTER_CUSTOMER" :
        pageNAME = "MANAGE_CUSTOMER"
        ety_Name_member_1.delete(0, END)
        ety_phone_member_1.delete(0, END)
        ety_email_member_1.delete(0, END)
        ety_surName_member_1.delete(0, END)
        ety_calendar_member_1.delete(0, END)
        ety_Address_Member_1.delete("1.0",END)
        customer_gender1info.set("ชาย")
        customer_date1info.set("")
        address = ""
        frame_registerMember.destroy()

    elif pageNAME == "MANAGE_CUSTOMER" :
        pageNAME = "HOME"
        frame_customerManage.destroy()

    elif pageNAME == "MANAGE_PRODUCT" :
        pageNAME = "HOME"
        ety_nameProduct.delete(0, END)
        ety_priceProduct.delete(0, END)
        product_dropdown_type.set("กาแฟ")
        frame_manageListProduct.destroy()

    elif pageNAME == "MANAGE_STOCK" :
        pageNAME = "HOME"
        ety_nameIngredients.delete(0, END)
        ety_amountIngredients.delete(0, END)
        staple_amount_info.set("0")
        frame_stock.destroy()

    elif pageNAME == "ORDER_STOCK" :
        pageNAME = "MANAGE_STOCK"
        ety_nameIngredients.delete(0, END)
        ety_amountIngredients.delete(0, END)
        staple_amount_info.set("0")
        stapleorder_unitinfo.set("")
        ety_unitIngredients_order.delete(0, END)

        ety_dateOrderIngredients.delete(0, END)
        stapleorder_dateinfo.set("")
        stapleorder_nameinfo.set("")
        ety_nameIngredients_order.delete(0, END)
        ety_priceIngredients_order.delete(0, END)
        ety_priceIngredients_order.delete(0, END)
        ety_organization_order.delete(0, END)
        ety_amountIngredients_order.delete(0, END)
        frame_orderIngredients.destroy()
        style = ttk.Style(treeframe_stock)
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")
    
    elif pageNAME == "COMFIRM_ORDER" :
        pageNAME = "HOME"
        frame_confirmSelling.destroy()
    
    elif pageNAME == "PRINT_REPORT_1" :
        pageNAME = "HOME"
        ety_calendar_report.delete(0, END)
        report_dropdown_type.set("รายงานสรุปยอดขายสินค้า")
        report_dateinfo.set("")
        frame_printReport.destroy()

    elif pageNAME == "PRINT_REPORT_2" :
        pageNAME = "PRINT_REPORT_1"
        ety_calendar_report.delete(0, END)
        report_dropdown_type.set("รายงานสรุปยอดขายสินค้า")
        report_dateinfo.set("")
        text_showreport.delete("1.0",END)
        result_list.clear()
        frame_printReport2.destroy()

    elif pageNAME == "REQUISITION" :
        pageNAME = "MANAGE_STOCK"
        ety_searchMenu.delete(0, END)
        frame_RequisitionIngredients.destroy()
        style = ttk.Style(treeframe_stock)
        style.configure("Treeview", background="#FFE5D8",fieldbackground="#FFE5D8", foreground="black")

def search_click() :
    if pageNAME == "HOME" :
        if ety_searchMenu.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกข้อมูลก่อนค้นหา")
        else :
            optiondata = home_dropdown_clicked.get()
            if optiondata == "ประเภท" :
                sql = "select * from product where product_type = ?"
            elif optiondata == "ชื่อสินค้า" :
                sql = "select * from product where product_name = ?"
            cursor.execute(sql,[ety_searchMenu.get()])
            result = cursor.fetchall()
            if result :
                ety_searchMenu.delete(0, END)
                ety_searchMenu.focus()
                mytree_home1.delete(*mytree_home1.get_children())
                for i,data in enumerate(result):
                    mytree_home1.insert('', 'end', values=(data[1],data[0], data[2]))
            else :
                messagebox.showwarning("ระบบ:","ไม่พบเมนูในรายการสินค้า")
                ety_searchMenu.delete(0, END)
                ety_searchMenu.focus()
                fetch_Tree(pageNAME,mytree_home1,cursor)

    elif pageNAME == "MANAGE_EMPLOYEE" :
        if ety_search_employee1.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกข้อมูลก่อนค้นหา")
        else :
            optiondata = epy_dropdown_clicked.get()
            if optiondata == "ชื่อ" :
                sql = "select * from employee where employee_name = ? and employee_permission = ?"
            elif optiondata == "นามสกุล" :
                sql = "select * from employee where employee_surname = ? and employee_permission = ?"
            elif optiondata == "เพศ" :
                sql = "select * from employee where employee_gender = ? and employee_permission = ?"
            cursor.execute(sql,[ety_search_employee1.get(),"พนักงาน"])
            result = cursor.fetchall()
            if result :
                ety_search_employee1.delete(0, END)
                ety_search_employee1.focus()
                mytree_employee1.delete(*mytree_employee1.get_children())
                for i,data in enumerate(result):
                    mytree_employee1.insert('', 'end', values=(data[0],data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
            else :
                messagebox.showwarning("ระบบ:","ไม่พบบัญชีผู้ใช้งาน")
                ety_search_employee1.delete(0, END)
                ety_search_employee1.focus()
                fetch_Tree(pageNAME,mytree_employee1,cursor)

    elif pageNAME == "HISTORY_EMPLOYEE" :
        if ety_search_history.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกข้อมูลก่อนค้นหา")
        else :
            optiondata = epy_dropdownhistory_clicked.get()
            if optiondata == "เลขที่ออเดอร์" :
                sql = "select * from orderlist where order_number = ?"
            elif optiondata == "ผู้ออกออเดอร์" :
                sql = "select * from orderlist where order_seller = ?"
            elif optiondata == "วันที่ออเดอร์" :
                sql = "select * from orderlist where order_date = ?"
            cursor.execute(sql,[ety_search_history.get()])
            result = cursor.fetchall()
            if result :
                ety_search_history.delete(0, END)
                ety_search_history.focus()
                mytree_employee2.delete(*mytree_employee2.get_children())
                for i,data in enumerate(result):
                    mytree_employee2.insert('', 'end', values=(data[0],data[1], data[2], data[3], data[4]))
            else :
                messagebox.showwarning("ระบบ:","ไม่พบประวัติการทำงาน")
                ety_search_history.delete(0, END)
                ety_search_history.focus()
                fetch_Tree(pageNAME,mytree_employee2,cursor)

    elif pageNAME == "MANAGE_CUSTOMER" :
        if ety_search_customer.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกข้อมูลก่อนค้นหา")
        else :
            optiondata = mb_dropdown_clicked.get()
            if optiondata == "เบอร์โทรศัพท์" :
                sql = "select * from member where customer_phone = ?"
            elif optiondata == "ชื่อ" :
                sql = "select * from member where customer_name = ?"
            elif optiondata == "นามสกุล" :
                sql = "select * from member where customer_surname = ?"
            cursor.execute(sql,[ety_search_customer.get()])
            result = cursor.fetchall()
            if result :
                ety_search_customer.delete(0, END)
                ety_search_customer.focus()
                mytree_customer.delete(*mytree_customer.get_children())
                for i,data in enumerate(result):
                    mytree_customer.insert('', 'end', values=(data[0],data[1], data[2], data[3], data[4], data[5], data[6] ,data[7]))
            else :
                messagebox.showwarning("ระบบ:","ไม่พบบัญชีสมาชิก")
                ety_search_customer.delete(0, END)
                ety_search_customer.focus()
                fetch_Tree(pageNAME,mytree_customer,cursor)

    elif pageNAME == "MANAGE_PRODUCT" :
        if ety_searchBox_product.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกข้อมูลก่อนค้นหา")
        else :
            optiondata = product_dropdown_select.get()
            if optiondata == "ประเภท" :
                sql = "select * from product where product_type = ?"
            elif optiondata == "ชื่อ" :
                sql = "select * from product where product_name = ?"
            elif optiondata == "ราคา" :
                sql = "select * from product where product_price = ?"
            cursor.execute(sql,[ety_searchBox_product.get()])
            result = cursor.fetchall()
            if result :
                ety_searchBox_product.delete(0, END)
                ety_searchBox_product.focus()
                mytree_product.delete(*mytree_product.get_children())
                for i,data in enumerate(result):
                    mytree_product.insert('', 'end', values=(data[1],data[0], data[2]))
            else :
                messagebox.showwarning("ระบบ:","ไม่พบสินค้า")
                ety_searchBox_product.delete(0, END)
                ety_searchBox_product.focus()
                fetch_Tree(pageNAME,mytree_product,cursor)

    elif pageNAME == "MANAGE_STOCK" :
        if ety_searchBox_stock.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกข้อมูลก่อนค้นหา")
        else :
            sql = "select * from staple where staple_name = ?"
            cursor.execute(sql,[ety_searchBox_stock.get()])
            result = cursor.fetchall()
            if result :
                ety_searchBox_stock.delete(0, END)
                ety_searchBox_stock.focus()
                mytree_stock.delete(*mytree_stock.get_children())
                for i,data in enumerate(result):
                    mytree_stock.insert('', 'end', values=(data[0],data[1]))
            else :
                messagebox.showwarning("ระบบ:","ไม่พบวัตถุดิบ")
                ety_searchBox_stock.delete(0, END)
                ety_searchBox_stock.focus()
                fetch_Tree(pageNAME,mytree_stock,cursor)

    elif pageNAME == "ORDER_STOCK" :
        if ety_searchMenu_orderstock.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกข้อมูลก่อนค้นหา")
        else :
            sql = "select * from staple where staple_name = ?"
            cursor.execute(sql,[ety_searchMenu_orderstock.get()])
            result = cursor.fetchall()
            if result :
                ety_searchMenu_orderstock.delete(0, END)
                ety_searchMenu_orderstock.focus()
                mytree_orderstock.delete(*mytree_orderstock.get_children())
                for i,data in enumerate(result):
                    mytree_orderstock.insert('', 'end', values=(data[0],data[1]))
            else :
                messagebox.showwarning("ระบบ:","ไม่พบวัตถุดิบ")
                ety_searchMenu_orderstock.delete(0, END)
                ety_searchMenu_orderstock.focus()
                fetch_Tree(pageNAME,mytree_orderstock,cursor)

    elif pageNAME == "REQUISITION" :
        if ety_search_req.get() == "" :
            messagebox.showwarning("ระบบ:","กรุณากรอกข้อมูลก่อนค้นหา")
        else :
            sql = "select * from staple where staple_name = ?"
            cursor.execute(sql,[ety_search_req.get()])
            result = cursor.fetchall()
            if result :
                ety_search_req.delete(0, END)
                ety_search_req.focus()
                mytree_RequisitionIngredients.delete(*mytree_RequisitionIngredients.get_children())
                for i,data in enumerate(result):
                    mytree_RequisitionIngredients.insert('', 'end', values=(data[0],data[1]))
            else :
                messagebox.showwarning("ระบบ:","ไม่พบวัตถุดิบ")
                ety_search_req.delete(0, END)
                ety_search_req.focus()
                fetch_Tree(pageNAME,mytree_RequisitionIngredients,cursor)

def treeviewclick(event) :
    global epy_address,mb_address
    global userPERM,pageNAME
    global productname_before_edit,productprice_before_edit,producttype_before_edit
    global staplename_before_edit
    global staple_current_amount
    global asdzxname,asdzxvalues

    if pageNAME == "MANAGE_EMPLOYEE" :
        values = mytree_employee1.item(mytree_employee1.focus(),'values')
        employee_name2info.set(values[3])
        employee_surname2info.set(values[4])
        employee_id2info.set(values[0])
        employee_date2info.set(values[6])
        employee_phone2info.set(values[7])
        employee_gender2info.set(values[5])
        employee_username2info.set(values[1])
        employee_pwd2info.set(values[2])
        epy_address = values[8]

    elif pageNAME == "MANAGE_CUSTOMER" :
        values = mytree_customer.item(mytree_customer.focus(),'values')
        customer_name2info.set(values[1])
        customer_surname2info.set(values[2])
        customer_date2info.set(values[4])
        customer_phone2info.set(values[0])
        customer_gender2info.set(values[3])
        customer_email2info.set(values[5])
        mb_address = values[6] 

    elif pageNAME == "MANAGE_PRODUCT" :
        values = mytree_product.item(mytree_product.focus(),'values')
        productname_before_edit = values[1]
        productprice_before_edit = values[2]
        producttype_before_edit = values[0]
        product_nameinfo.set(values[1])
        product_priceinfo.set(values[2])
        product_dropdown_type.set(values[0])

    elif pageNAME == "MANAGE_STOCK" :
        values = mytree_stock.item(mytree_stock.focus(),'values')
        staplename_before_edit = values[0]
        staple_nameinfo.set(values[0])
        staple_amount_info.set(values[1])
        manageStock_dropdown_clicked.set(values[2])

    elif pageNAME == "ORDER_STOCK" :
        values = mytree_orderstock.item(mytree_orderstock.focus(),'values')
        stapleorder_nameinfo.set(values[0])
        stapleorder_unitinfo.set(values[2])
        staple_current_amount = values[1]

    elif pageNAME == "HOME" :
        global orderName,orderPrice
        values = mytree_home1.item(mytree_home1.focus(),'values')
        orderName,orderPrice = values[1],values[2]
        popup_home(orderName,orderPrice)

    elif pageNAME == "REQUISITION" :
        global reqName,reqAmount,reqUnit
        values = mytree_RequisitionIngredients.item(mytree_RequisitionIngredients.focus(),'values')
        reqName,reqAmount,reqUnit = values[0],values[1],values[2]
        popup_Requisition(reqName,reqAmount,reqUnit)

def popup_confirmCallBack():
    global order_total

    if pageNAME == "HOME" :
        price = int(orderPrice) * int(ety_nameProduct.get())
        mytree_home2.insert("", tk.END, values=(orderName,ety_nameProduct.get(),price))
        order_name_lst.append(orderName)
        order_amount_lst.append(ety_nameProduct.get())
        order_price_lst.append(price)
        order_total += price
        total['text'] = "ยอดสุทธิ :         " + str(order_total)
        # print(order_name_lst,order_amount_lst,order_price_lst)
        window_home.destroy()
    
    elif pageNAME == "REQUISITION" :
        db_staple_amt = getTotalStaple(reqName)
        if int(ety_reqAmt.get()) <= int(db_staple_amt) :
            mytree_RequisitionIngredients_2.insert("", tk.END, values=(reqName,ety_reqAmt.get(),reqUnit))
            req_name_lst.append(reqName)
            req_amount_lst.append(ety_reqAmt.get())
            req_unit_lst.append(reqUnit)
            # print(req_name_lst,req_amount_lst)
            window_Requisition.destroy()
        else :
            messagebox.showwarning("ระบบ:","จำนวนคงเหลือในคลังไม่เพียงพอ")
            window_Requisition.destroy()

def confirmOrderCallBack():
    for child in mytree_home2.get_children():
        mytreeSelling.insert("",0,text=mytree_home2.item(child)["text"],values=mytree_home2.item(child)["values"])

def memberCheckCallback():
    global member_total
    global tag,member_tel,Memberdiscount
    global discount
    if ety_telMember.get() == "" :
                messagebox.showwarning("ระบบ:","กรุณาระบุเบอร์สมาชิก")
                ety_telMember.focus_force()
    else :
        sql = "select * from member where customer_phone = ?"
        cursor.execute(sql,[ety_telMember.get()])
        result = cursor.fetchone()
        if result :
            Memberdiscount = order_total*0.1
            discount.set(str(int(Memberdiscount)))
            tag = "MEMBER"
            member_total = order_total - Memberdiscount
            member_tel = ety_telMember.get()
            totalSellPriceAAA['text'] = str(int(member_total))
            ety_telMember.delete(0,END)
            window_member.destroy()

        else :
            messagebox.showinfo("ระบบ:","ไม่พบเบอร์สมาชิก")
            ety_telMember.delete(0,END)
            window_member.destroy()

def addOrderToDB():
    order_list = ""
    order_count = 0
    while order_count+1 <= len(order_name_lst) :
        order_list+=order_name_lst[order_count]+" "+order_amount_lst[order_count]+" แก้ว"
        if order_count+1 != len(order_name_lst):
            order_list+=", "
        order_count+=1

    sql = "insert into orderlist(order_date,order_seller,order_list,order_price,order_getmoney,order_change) values (?,?,?,?,?,?)"
    cursor.execute(sql,[dateToday,employee_name,order_list,total_order_price,moneyReceive,change])
    conn.commit()

def addPoint(customerPoint):
    sql = ''' 
                update member
                set customer_point=?
                where customer_phone=?
    '''
    cursor.execute(sql,[customerPoint,member_tel])
    conn.commit()

def confirmSellCallBack():
    global total_order_price

    if ety_receive.get() == "":
        messagebox.showwarning("ระบบ:","กรุณากรอกจำนวนเงิน")
        ety_receive.focus_force()
    else :
        if tag == "MEMBER":
            total_order_price = int(member_total)
            if int(ety_receive.get()) < int(member_total) :
                messagebox.showwarning("ระบบ:","กรุณากรอกจำนวนเงินให้เพียงพอ")
                ety_receive.focus_force()
            else : 
                popup_bill()

        else :
            total_order_price = int(order_total)
            if int(ety_receive.get()) < int(order_total) :
                messagebox.showwarning("ระบบ:","กรุณากรอกจำนวนเงินให้เพียงพอ")
                ety_receive.focus_force()
            else :
                popup_bill()

def confirmReqCallback():
    global req_name_lst,req_amount_lst,req_unit_lst
    
    if req_name_lst :
        req_list = ""
        req_count = 0
        while req_count+1 <= len(req_name_lst) :
            req_list+=req_name_lst[req_count]+" "+req_amount_lst[req_count]+" "+req_unit_lst[req_count]
            db_staple_amt = getTotalStaple(req_name_lst[req_count])
            total_staple_amt = int(db_staple_amt)-int(req_amount_lst[req_count])
            sql = ''' 
                        update staple
                        set staple_amount=?
                        where staple_name=?
            '''
            cursor.execute(sql,[total_staple_amt,req_name_lst[req_count]])
            conn.commit()
            if req_count+1 != len(req_name_lst):
                req_list+=", "
            req_count+=1

        messagebox.showinfo("ระบบ:","เบิกวัตถุดิบสำเร็จ")
        sql = "insert into requisitionlist(requisition_date,requisition_person,requisition_list) values (?,?,?)"
        cursor.execute(sql,[dateToday,employee_name,req_list])
        conn.commit()

        mytree_RequisitionIngredients_2.delete(*mytree_RequisitionIngredients_2.get_children())
        fetch_Tree(pageNAME,mytree_RequisitionIngredients,cursor)

        req_name_lst = []
        req_amount_lst = []
        req_unit_lst = []
        req_list = ""
    else :
        messagebox.showwarning("ระบบ:","กรุณาระบุวัตถุดิบที่ต้องการเบิก")

def resetCallBack():
    global order_name_lst,order_amount_lst,order_price_lst,order_total
    global req_name_lst,req_amount_lst,req_unit_lst
    if pageNAME == "HOME" :
        mytree_home2.delete(*mytree_home2.get_children())
        order_name_lst = []
        order_amount_lst = []
        order_price_lst = []
        order_total = 0
        total['text'] = "ยอดสุทธิ :         " + str(order_total)
    elif pageNAME == "REQUISITION" :
        mytree_RequisitionIngredients_2.delete(*mytree_RequisitionIngredients_2.get_children())
        req_name_lst = []
        req_amount_lst = []
        req_unit_lst = []
        # print(req_name_lst,req_amount_lst)
def getCustomerPoint():
    sql = 'select customer_point from member where customer_phone=?'
    cursor.execute(sql,[member_tel])
    result = cursor.fetchone()
    return result[0]

def getTotalStaple(staple_name):
    sql = 'select staple_amount from staple where staple_name=?'
    cursor.execute(sql,[staple_name])
    result = cursor.fetchone()
    return result[0]

w = 1280
h = 720

conn,cursor = createconnection()
window = mainwindow(w,h)

today_date = datetime.date.today()
dateToday = today_date.strftime("%d/%m/%Y")


userPERM = ' '
pageNAME = ' '
tag = ' '

#หน้าlogin
userinfo = StringVar()
pwdinfo = StringVar()

#ชื่อที่แสดงบนหน้าจอ
employee_name = ""

#หน้า home
home_dropdown_clicked = StringVar()
home_dropdown_clicked.set('ประเภท')
order_total = 0
member_total = 0
discount = StringVar()
discount.set("0")
total_order_price = 0

order_name_lst = []
order_amount_lst = []
order_price_lst = []

req_name_lst = []
req_amount_lst = []
req_unit_lst = []

#หน้าลงทะเบียนพนักงาน
employee_name1info = StringVar()
employee_surname1info = StringVar()
employee_id1info = StringVar()
employee_date1info = StringVar()
employee_phone1info = StringVar()
employee_gender1info = StringVar()
employee_gender1info.set("ชาย")
employee_username1info = StringVar()
employee_pwd1info = StringVar()
employee_conpwd1info = StringVar()

#หน้าแก้ไขพนักงาน
employee_name2info = StringVar()
employee_surname2info = StringVar()
employee_id2info = StringVar()
employee_date2info = StringVar()
employee_phone2info = StringVar()
employee_gender2info = StringVar()
employee_gender2info.set("ชาย")
employee_username2info = StringVar()
employee_pwd2info = StringVar()
employee_conpwd2info = StringVar()
epy_address = ""
epy_dropdown_clicked = StringVar()

#หน้าลงทะเบียนลูกค้า
customer_name1info = StringVar()
customer_surname1info = StringVar()
customer_date1info = StringVar()
customer_phone1info = StringVar()
customer_gender1info = StringVar()
customer_gender1info.set("ชาย")
customer_email1info = StringVar()

#หน้าดูประวัติพนักงาน
epy_dropdownhistory_clicked = StringVar()
epy_dropdownhistory_clicked.set("เลขที่ออเดอร์")

#หน้าแก้ไขลูกค้า
customer_name2info = StringVar()
customer_surname2info = StringVar()
customer_date2info = StringVar()
customer_phone2info = StringVar()
customer_gender2info = StringVar()
customer_gender2info.set("ชาย")
customer_email2info = StringVar()
mb_address = ""
mb_dropdown_clicked = StringVar()

#หน้าจัดการรายการสินค้า
product_nameinfo = StringVar()
product_priceinfo = StringVar()
product_dropdown_type = StringVar()
product_dropdown_type.set("กาแฟ")
product_dropdown_select = StringVar()
productname_before_edit = ""
productprice_before_edit = ""
producttype_before_edit = ""

#หน้าจัดการคลังวัตถุดิบ
manageStock_dropdown_clicked = StringVar()
manageStock_dropdown_clicked.set('กรัม')
staple_nameinfo = StringVar()
staple_amount_info = StringVar()
staple_amount_info.set("0")
staplename_before_edit = ""
# stapleamount_before_edit = ""

#หน้าสั่งซื้อวัตถุดิบ
stapleorder_dateinfo = StringVar()
stapleorder_nameinfo = StringVar()
stapleorder_priceinfo = StringVar()
stapleorder_companyinfo = StringVar()
stapleorder_amountinfo = StringVar()
stapleorder_unitinfo = StringVar()

#หน้าพิมพ์รายงาน
report_dateinfo = StringVar()
report_dropdown_type = StringVar()


# genderVar = StringVar(window,"1")
# genderEmployeeVar = StringVar(window,"1")

photo_logo = PhotoImage(file = "image/system/logo.png").subsample(5,5)
photo_logo2 = PhotoImage(file = "image/system/logo2.png").subsample(9,9)
photo_profile = PhotoImage(file = "image/system/profile.png").subsample(1,1)
photo_exit = PhotoImage(file = "image/system/exit.png")
photo_search = PhotoImage(file = "image/system/search.png")
photo_calendar = PhotoImage(file = "image/system/calendar.png")
photo_cancel = PhotoImage(file = "image/system/cancel.png")
photo_refresh = PhotoImage(file = "image/system/refresh.png")

widget_login()

window.mainloop()