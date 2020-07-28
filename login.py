import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import pymysql
import datetime
import cv2
from time import sleep
import os
import numpy as np



class Login_System():

    def __init__(self,root):
        self.root = root

       # self.splash_screen()



        self.root.title("Facial Recognition Attendence System")
        self.root.geometry("1530x830+0+0")
        ##=============All Images=======================##
        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        self.logo_icon = PhotoImage(file = "images/login.png")
        self.user_icon = PhotoImage(file = "images/username.png")
        self.pass_icon = PhotoImage(file= "images/password.png")

        self.uname = StringVar()
        self.upass = StringVar()
        
        
        bg_lbl = Label(self.root, image = self.bg_icon).pack()

        title = Label(self.root, text = "Attendence System Login", font=("times new roman",40, "bold"), bg="yellow", fg = "red", bd =10, relief = GROOVE )
        title.place(x=0, y=0, relwidth = 1)

        Login_Frame = Frame(self.root, bg  = "white")
        Login_Frame.place(x=530,y= 200)

        logolbl = Label(Login_Frame, image = self.logo_icon, bd = 0 )
        logolbl.grid(row=0,columnspan = 2, pady = 20)

        lblUser = Label(Login_Frame, text = "UserName", image = self.user_icon, compound = LEFT, font = ("times new roman",20,"bold"),bg ="white").grid(row=1,column=0, padx =20, pady =10)
        txtUser = Entry(Login_Frame, bd = 5, textvariable = self.uname, relief = GROOVE, font = ("",15)).grid(row=1, column = 1)
        lblpass = Label(Login_Frame, text = "Password", image = self.pass_icon, compound = LEFT, font = ("times new roman",20,"bold"),bg ="white").grid(row=2,column=0, padx =20, pady =10)
        txtPass = Entry(Login_Frame, bd = 5, textvariable = self.upass,show="*", relief = GROOVE, font = ("",15)).grid(row=2, column = 1)
        
        lbl_text = Label(Login_Frame)
        lbl_text.grid(row=3, columnspan=2)

        btn_log  =Button(Login_Frame, text = "Login", command = self.login, width  =15, font=("times new roman", 14, "bold"), bg = "yellow", fg = "red").grid(row = 4, column= 1, pady =10)
    

    
    
    
    def login(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()

        if self.uname.get() == "" or self.upass.get() == "":
            messagebox.showerror("Error", "Fill SOmething")
        else:
            #cur.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (self.uname.get(), self.upass.get()))
            cur.execute("select * from admins where username = %s and password = %s",(self.uname.get(),
                                                                                       self.upass.get()
                                                                                    ))
            credentials = cur.fetchone()
            self.username_active = self.uname.get()
            if credentials is not None:

                if credentials[1]=="aadipy" and credentials[2] == "aadipy":
                    self.uname.set("")
                    self.upass.set("")
                    self.admin_panel()

                else:
                
                    self.uname.set("")
                    self.upass.set("")
                    self.homepage()
            else:
                messagebox.showerror("Invalid","Invalid Username or password.")
                self.uname.set("")
                self.upass.set("")   
        cur.close()
        con.close()



    def admin_panel(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Facial Recognition Attendence System")
        self.root.geometry("1530x830+0+0")

        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        bg_lbl = Label(self.root, image = self.bg_icon).pack()
        title = Label(self.root, text = "Attendence System Login(ADMIN PANEL)", font=("times new roman",40, "bold"), bg="yellow", fg = "red", bd =10, relief = GROOVE )
        title.place(x=0, y=0, relwidth = 1)

        #=====$===============$ MAin Frame $ +===========================

        self.main_frame_admin = Frame(self.root, bd = 4, relief= RIDGE, bg = "midnight blue")
        self.main_frame_admin.place(x=20, y=100, width=185, height = 720)

        self.side_frame_admin = Frame(self.root, bd = 4, relief= RIDGE, bg = "midnight blue")
        self.side_frame_admin.place(x=210, y=100, width=1310, height = 720)

        self.middle_frame_admin = Frame(self.side_frame_admin, bd = 4, relief= RIDGE, bg = "midnight blue")
        self.middle_frame_admin.place(x=0, y=0, width=1300, height = 710)

        add_department = Button(self.main_frame_admin,text = "Add Department",command = self.dept_add, width  =15, font=("times new roman", 14, "bold"), bg = "yellow", fg = "red")
        add_department.grid(row = 0, column = 0)

        add_year = Button(self.main_frame_admin,text = "Add year",command = self.year_add, width  =15, font=("times new roman", 14, "bold"), bg = "yellow", fg = "red")
        add_year.grid(row = 1, column = 0)

        add_section = Button(self.main_frame_admin,text = "Add section",command = self.section_addd, width  =15, font=("times new roman", 14, "bold"), bg = "yellow", fg = "red")
        add_section.grid(row = 2, column = 0)

        add_faculity_btn = Button(self.main_frame_admin,text = "Add faculity",command = self.faculty_add, width  =15, font=("times new roman", 14, "bold"), bg = "yellow", fg = "red")
        add_faculity_btn.grid(row = 3, column = 0)
        add_faculity_btn = Button(self.main_frame_admin,text = "Logout",command = self.logout, width  =15, font=("times new roman", 14, "bold"), bg = "yellow", fg = "red")
        add_faculity_btn.grid(row = 4, column = 0)

    

    def faculty_add(self):
        self.middle_frame_admin.destroy()
        self.middle_frame_admin = Frame(self.side_frame_admin, bd = 4, relief= RIDGE, bg = "midnight blue")
        self.middle_frame_admin.place(x=0, y=0, width=1300, height = 710)


    #============All Variables=============================
        
    
        self.name_var = StringVar()
        self.mobile_var  =StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.username_var = StringVar()
        self.password_var = StringVar()
        self.dept_name_var = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()

    #============Manage Frame ============================

        self.manage_frame = Frame(self.middle_frame_admin, bd = 4, relief= RIDGE, bg = "crimson")
        self.manage_frame.place(x=5, y=5, width=400, height = 580)

        manage_title= Label(self.manage_frame,bg= "crimson",fg = "white" ,text = "Add Faculty", font=("times new roman", 30, "bold"))
        manage_title.grid(row=0, columnspan =2, pady = 20)


        lbl_name = Label(self.manage_frame, text = "Name", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_name.grid(row=1, column  = 0 , pady = 10, padx = 20, sticky = "w")

        txt_name = Entry(self.manage_frame,textvariable = self.name_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_name.grid(row=1, column  = 1, pady = 10, padx = 20)

        lbl_mobile = Label(self.manage_frame, text = "Contact", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_mobile.grid(row=2, column  = 0 , pady = 10, padx = 20, sticky = "w")

        txt_mobile = Entry(self.manage_frame,textvariable = self.mobile_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_mobile.grid(row=2, column  = 1, pady = 10, padx = 20)


        lbl_gender = Label(self.manage_frame, text = "Gender", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_gender.grid(row=3, column  = 0 , pady = 10, padx = 20, sticky = "w")

        combo_gender = ttk.Combobox(self.manage_frame, textvariable = self.gender_var,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_gender['values']  =('Male', "Female", 'Other')
        combo_gender.grid(row =3, column  =1, pady = 10, padx= 20)

        lbl_address = Label(self.manage_frame, text = "Address", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_address.grid(row=4, column  = 0 , pady = 10, padx = 20, sticky = "w")

        self.txt_address = Text(self.manage_frame, width=30, height = 4, font=("", 10))
        self.txt_address.grid(row = 4, column = 1, padx= 20, pady =10, sticky = "w")

        

        lbl_username = Label(self.manage_frame, text = "Username", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_username.grid(row=5, column  = 0 , pady = 10, padx = 20, sticky = "w")

        txt_username = Entry(self.manage_frame,textvariable = self.username_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_username.grid(row = 5, column = 1, padx = 20, pady =10)

        lbl_password= Label(self.manage_frame, text = "Password", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_password.grid(row = 6, column = 0, padx = 20, pady = 10, sticky = "w")

        txt_password = Entry(self.manage_frame,textvariable = self.password_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_password.grid(row = 6, column = 1, padx = 20, pady =10)

        lbl_department = Label(self.manage_frame, text = "Department", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_department.grid(row=7, column  = 0 , pady = 10, padx = 20, sticky = "w")

        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select * from department")
        rows = cur.fetchall()
        department = []
        self.dept_dict = {}
        for i in rows:
            department.append(i[1])
            self.dept_dict[i[1]] = i[0]
        combo_department = ttk.Combobox(self.manage_frame, textvariable = self.dept_name_var,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_department['values']  =(department)
        combo_department.grid(row =7, column  =1, pady = 10, padx= 20)


        Addbtn  =Button(self.manage_frame, text="Add",command = self.add_faculty, width = 10).grid(row=8, column = 0 , padx= 10, pady = 10)
        clearbtn  =Button(self.manage_frame, command = self.clear_faculty,text="Clear", width = 10).grid(row=8, column = 1 , padx= 10, pady = 10)
    
         #============detail Frame ============================
        
        detail_frame = Frame(self.middle_frame_admin, bd = 4, relief= RIDGE, bg = "crimson")
        detail_frame.place(x=430, y=5, width=840, height = 580)

        lbl_search= Label(detail_frame, text = "Search By", bg ="crimson", font=("times new roman", 10,"bold"), fg = "white")
        lbl_search.grid(row=0, column = 0, pady = 20, sticky = "w")

        combo_search = ttk.Combobox(detail_frame,textvariable = self.search_by,width = 8, state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_search['values']  =("name",'branch')
        combo_search.grid(row =0, column  =1, pady = 10, padx= 20)


        txt_search = Entry(detail_frame, textvariable = self.search_text, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_search.grid(row=0, column  = 2, pady = 10, padx = 20, sticky = "w")

        search_btn  =Button(detail_frame,command = self.search_faculty, text="Search", width = 10).grid(row=0, column = 3, padx= 10, pady = 10)
        showall_btn  =Button(detail_frame,command = self.fetch_faculty, text="Showall", width = 10).grid(row=0, column = 4 , padx= 10, pady = 10)


        back_btn  =Button(detail_frame,command = self.homepage, text="Back", width = 10)
        back_btn.place(x =590, y= 600, width = 200, height = 100 )
    #======================Table Frame ==================================

        Table_frame = Frame(detail_frame, bd = 4, relief= RIDGE, bg = "crimson")
        Table_frame.place(x=10, y=70, width=825, height = 500)

        scroll_x = Scrollbar(Table_frame, orient= HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient= VERTICAL)
        self.faculty_table = ttk.Treeview(Table_frame, columns=("facultyid", "name", "mobile", "gender",'address','username','password', "deptno"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT, fill = Y)
        scroll_x.config(command = self.faculty_table.xview)
        scroll_y.config(command = self.faculty_table.yview)
        self.faculty_table.heading("facultyid", text = "Faculty ID")
        self.faculty_table.heading("name", text = "Name")
        self.faculty_table.heading("mobile", text = "Mobile")
        self.faculty_table.heading("gender", text = "Gender")
        self.faculty_table.heading("address", text = "Address")
        self.faculty_table.heading("username", text = "Username")
        self.faculty_table.heading("password", text = "Password")
        self.faculty_table.heading("deptno", text = "Dept No")
        
        self.faculty_table['show']='headings'
        self.faculty_table.column('facultyid', width = 100)
        self.faculty_table.column('name', width = 100)
        self.faculty_table.column('mobile', width = 100)
        self.faculty_table.column('gender', width = 100)
        self.faculty_table.column('address', width = 100)
        self.faculty_table.column('username', width = 100)
        self.faculty_table.column('password', width = 100)
        self.faculty_table.column('deptno', width = 100)

        self.faculty_table.pack(fill = BOTH, expand = 1)
        self.faculty_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_faculty()

    def fetch_faculty(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select * from facultyinfo")
        rows = cur.fetchall()
        if len(rows)!= 0 :
            self.faculty_table.delete(*self.faculty_table.get_children())
            for row in rows:
                self.faculty_table.insert('', END, values =row)
            con.commit()
        con.close()
    
    
    def search_faculty(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select * from facultyinfo where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!= 0 :
            self.faculty_table.delete(*self.faculty_table.get_children())
            for row in rows:
                self.faculty_table.insert('', END, values =row)
            con.commit()
        else:
            self.faculty_table.delete(*self.faculty_table.get_children())

        con.close()
    
    def add_faculty(self):
        if (self.name_var.get()=="" or self.dept_name_var.get()==""): 
        ##or (self.Email_var.get()=="" or self.Gender_var.get()="") or (self.year_var.get()="" or self.branch_var.get()="") or (self.section_var.get()=="" or self.contact_var.get()==""))
            messagebox.showerror("Error","All fields are required!!!")
        else:
            dept_no = self.dept_dict[self.dept_name_var.get()]
            con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
            cur = con.cursor()
            cur.execute('Insert into facultyinfo values(%s,%s,%s,%s,%s,%s,%s,%s)', (0,
                                                                        self.name_var.get().title(),
                                                                        self.mobile_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.txt_address.get('1.0', END),
                                                                        self.username_var.get(),
                                                                        self.password_var.get(),
                                                                        dept_no                                                                       
                                                                        ))
            cur.execute('Insert into admins values(%s,%s,%s)', (
                                                                self.name_var.get().title(),
                                                                self.username_var.get(),
                                                                self.password_var.get()
                                                                                                                                           
                                                                ))
                                                                        
                                                                        
            con.commit()
            self.fetch_faculty()
            self.clear()
            con.close()
            messagebox.showinfo("Sucess", "Record has been inserted")

    def clear_faculty(self):
        self.name_var.set("")
        self.mobile_var.set("")
        self.gender_var.set("")
        self.txt_address.delete("1.0",END)
        self.username_var.set("")
        self.password_var.set("")
        self.dept_name_var.set("")
    


    def dept_add(self):
        #self.root.destroy()
        #self.root = tk.Tk()
        #self.root.title("Facial Recognition Attendence System")
        #self.root.geometry("600x500+500+220")
        self.middle_frame_admin = Frame(self.side_frame_admin, bd = 4, relief= RIDGE, bg = "midnight blue")
        self.middle_frame_admin.place(x=0, y=0, width=1300, height = 710)

        #------------------------------$ FRAMES $-------------------------------------

        depart_add = Frame(self.middle_frame_admin, bd = 4, relief = RIDGE, bg = "crimson")
        depart_add.place(x= 5, y = 5, width = 290, height = 490)

        self.show_dept_table = Frame(self.middle_frame_admin, bd = 4, relief = RIDGE, bg = "crimson")
        self.show_dept_table.place(x = 300, y = 5, width = 290, height = 490 )

        #-----------------------------$ VAriables $---------------------------------------

        self.dept_name = StringVar()

        #-----------------------------$ add DEPARTMENT $----------------------------------

        department_lbl = Label(depart_add, text = "Department", bg = "crimson", fg = "white", font=("times new roman", 20, "bold") )
        department_lbl.place(x = 70, y = 30)

        txt_department = Entry(depart_add, textvariable = self.dept_name, width = 15 ,font = ("times new roman", 20,  "bold"), bd = 5, relief = GROOVE)
        txt_department.place(x = 25, y = 100)

        department_btn = Button(depart_add, command = self.depart_DB, text = "ADD DEPARTMENT", width = 15)
        department_btn.place(x = 25,y = 170)

        back_btn = Button(depart_add, command = self.admin_panel, text = "BACK", width = 15)
        back_btn.place(x = 25,y = 220)

        #---------------------------$ department table $----------------------------------

        

        scroll_x = Scrollbar(self.show_dept_table, orient = HORIZONTAL)
        scroll_y = Scrollbar(self.show_dept_table, orient = VERTICAL)

        self.department_table = ttk.Treeview(self.show_dept_table, columns=('dept_no', "dept_name"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side= RIGHT, fill = Y)

        scroll_x.config(command = self.department_table.xview)
        scroll_y.config(command = self.department_table.yview)

        self.department_table.heading('dept_no', text = "DEPT ID")
        self.department_table.heading('dept_name', text = "DEPARTMENT TABLE")

        self.department_table['show'] = 'headings'

        self.department_table.column('dept_no', width = 100)
        self.department_table.column('dept_name', width = 100)

        self.department_table.pack(fill= BOTH, expand = 1)
        self.department_table.bind("<ButtonRelease-1>", self.set_cursor)
        self.fetch_dept()
    

    def set_cursor(self):
        cursor_row = self.department_table.focus()
        content = self.department_table.item(cursor_row)
        row = content["values"]

        self.dept_name.set(row[1])

    def fetch_dept(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select * from department")
        rows = cur.fetchall()
        if len(rows)!= 0 :
            self.department_table.delete(*self.department_table.get_children())
            for row in rows:
                self.department_table.insert('', END, values =row)
            con.commit()
        con.close()



    def depart_DB(self):
        
        if self.dept_name.get()== "":
            messagebox.showerror("Error", "BOX CAN'T BE EMPTY")
        
        else:
            con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
            cur = con.cursor()
            cur.execute("Insert into department values(%s,%s)",(0,
                                                            self.dept_name.get()))
            con.commit()
            self.dept_name.set("")
            messagebox.showinfo("Sucess","Sucessfully added department")
            self.fetch_dept()
            con.close()

    def year_add(self):
        self.middle_frame_admin.destroy()
        self.middle_frame_admin = Frame(self.side_frame_admin, bd = 4, relief= RIDGE, bg = "midnight blue")
        self.middle_frame_admin.place(x=0, y=0, width=1300, height = 710)

        #------------------------------$ FRAMES $-------------------------------------

        year_add = Frame(self.middle_frame_admin, bd = 4, relief = RIDGE, bg = "crimson")
        year_add.place(x= 5, y = 5, width = 290, height = 490)

        self.show_year_table = Frame(self.middle_frame_admin, bd = 4, relief = RIDGE, bg = "crimson")
        self.show_year_table.place(x = 300, y = 5, width = 290, height = 490 )

        #-----------------------------$ VAriables $---------------------------------------

        self.y_name = StringVar()
        self.depart_name = StringVar()

        #-----------------------------$ add DEPARTMENT $----------------------------------

        lbl_department= Label(year_add, text = "Department", bg ="crimson", font=("times new roman", 20,"bold"), fg = "white")
        lbl_department.place(x =  70, y = 30)
        
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select * from department")
        rows = cur.fetchall()
        department = []
        self.dept_dict = {}
        for i in rows:
            department.append(i[1])
            self.dept_dict[i[1]]  = i[0] 

        combo_department = ttk.Combobox(year_add, textvariable = self.depart_name,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_department['values']  =(department)
        combo_department.place(x = 25, y = 100)
        
        combo_department.bind("<<ComboboxSelected>>", self.search_year_fetch)
        year_lbl = Label(year_add, text = "Batch Year", bg = "crimson", fg = "white", font=("times new roman", 20, "bold") )
        year_lbl.place(x = 70, y = 170)

        txt_year = Entry(year_add, textvariable = self.y_name, width = 10,font = ("times new roman", 20,  "bold"), bd = 5, relief = GROOVE)
        txt_year.place(x = 25, y = 240)

        

        

        year_btn = Button(year_add, command = self.year_DB, text = "ADD YEAR", width = 15)
        year_btn.place(x = 70,y = 310)

        back_btn = Button(year_add, command = self.admin_panel, text = "BACK", width = 15)
        back_btn.place(x = 70,y = 340)

        #---------------------------$ department table $----------------------------------

        

        scroll_x = Scrollbar(self.show_year_table, orient = HORIZONTAL)
        scroll_y = Scrollbar(self.show_year_table, orient = VERTICAL)

        self.year_table = ttk.Treeview(self.show_year_table, columns=('year_no', "dept_name", "dept_year"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side= RIGHT, fill = Y)

        scroll_x.config(command = self.year_table.xview)
        scroll_y.config(command = self.year_table.yview)

        self.year_table.heading('year_no', text = "YEAR ID")
        self.year_table.heading('dept_name', text = "DEPARTMENT NAME")
        self.year_table.heading('dept_year', text = "DEPT YEAR")

        self.year_table['show'] = 'headings'

        self.year_table.column('year_no', width = 50)
        self.year_table.column('dept_name', width = 100)
        self.year_table.column('dept_year', width = 50)

        self.year_table.pack(fill= BOTH, expand = 1)
        self.year_table.bind("<ButtonRelease-1>", self.set_cursor_year)
        self.fetch_Year()


    def year_DB(self):
        if self.y_name.get()== "":
            messagebox.showerror("Error", "BOX CAN'T BE EMPTY")
        
        else:
            con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
            cur = con.cursor()
            dept_sel  = self.depart_name.get()
            
            dept_number = self.dept_dict[dept_sel]
            cur.execute("Insert into deptyear values(%s,%s,%s)",(0,
                                                            self.y_name.get(),
                                                            dept_number
                                                            ))
            con.commit()
            self.y_name.set("")
            messagebox.showinfo("Sucess","Sucessfully added department")
            self.fetch_Year()
            con.close()


    def search_year_fetch(self,ev):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        dept_sel  = self.depart_name.get()
        cur.execute("select dy.year_no,d.dept_name,dy.dept_year from deptyear dy,department d where d.dept_no=dy.dept_no and d.dept_name=%s", dept_sel)
        rows = cur.fetchall()
        if len(rows)!= 0 :
            self.year_table.delete(*self.year_table.get_children())
            for row in rows:
                self.year_table.insert('', END, values =row)
            con.commit()
        con.close()

    


    def set_cursor_year(self,ev):
        pass

    def fetch_Year(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select dy.year_no,d.dept_name,dy.dept_year from deptyear dy,department d where d.dept_no=dy.dept_no")
        rows = cur.fetchall()
        if len(rows)!= 0 :
            self.year_table.delete(*self.year_table.get_children())
            for row in rows:
                self.year_table.insert('', END, values =row)
            con.commit()
        con.close()

    def section_addd(self):
        self.middle_frame_admin.destroy()
        self.middle_frame_admin = Frame(self.side_frame_admin, bd = 4, relief= RIDGE, bg = "midnight blue")
        self.middle_frame_admin.place(x=0, y=0, width=1300, height = 710)

        #------------------------------$ FRAMES $-------------------------------------

        self.section_add = Frame(self.middle_frame_admin, bd = 4, relief = RIDGE, bg = "crimson")
        self.section_add.place(x= 5, y = 5, width = 300, height = 595)

        self.show_section_table = Frame(self.middle_frame_admin, bd = 4, relief = RIDGE, bg = "crimson")
        self.show_section_table.place(x = 310, y = 5, width = 390, height = 595 )

        #-----------------------------$ VAriables $---------------------------------------

        self.year_name = StringVar()
        self.department_name = StringVar()
        self.section_name = StringVar()

        #-----------------------------$ add DEPARTMENT $----------------------------------

        lbl_department= Label(self.section_add, text = "Department", bg ="crimson", font=("times new roman", 20,"bold"), fg = "white")
        lbl_department.place(x =  70, y = 30)
        
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select * from department")
        rows = cur.fetchall()
        department = []
        self.dept_dict = {}
        for i in rows:
            department.append(i[1])
            self.dept_dict[i[1]] = i[0] 

        combo_department = ttk.Combobox(self.section_add, textvariable = self.department_name,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_department['values']  =(department)
        combo_department.place(x = 25, y = 100)
        combo_department.bind("<<ComboboxSelected>>", self.search_section_year_fetch)


        year_lbl = Label(self.section_add, text = "Batch Year", bg = "crimson", fg = "white", font=("times new roman", 20, "bold") )
        year_lbl.place(x = 70, y = 170)

        combo_year = ttk.Combobox(self.section_add, textvariable = self.year_name,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_year['values']  =()
        combo_year.place(x = 25, y = 240)

        section_lbl = Label(self.section_add, text = "SECTION", bg = "crimson", fg = "white", font=("times new roman", 20, "bold") )
        section_lbl.place(x = 70, y = 310)

        txt_section = Entry(self.section_add, textvariable = self.section_name,width = 10,font = ("times new roman", 20,  "bold"), bd = 5, relief = GROOVE)
        txt_section.place(x = 25, y = 400)
        
        section_btn = Button(self.section_add, command = self.section_DB, text = "ADD SECTION", width = 15)
        section_btn.place(x = 70,y = 490)

        back_btn = Button(self.section_add, command = self.admin_panel, text = "BACK", width = 15)
        back_btn.place(x = 70,y = 520)

        #---------------------------$ department table $----------------------------------

        

        scroll_x = Scrollbar(self.show_section_table, orient = HORIZONTAL)
        scroll_y = Scrollbar(self.show_section_table, orient = VERTICAL)

        #self.section_table = ttk.Treeview(self.show_section_table, columns=('section_no', "section_name", "dept_year","dept_name"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        self.section_table = ttk.Treeview(self.show_section_table, columns=('section_no', "section_name"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side= RIGHT, fill = Y)

        scroll_x.config(command = self.section_table.xview)
        scroll_y.config(command = self.section_table.yview)

        self.section_table.heading('section_no', text = "SECTION ID")
        self.section_table.heading('section_name', text = "SECTION NAME")
        #self.section_table.heading('year_no', text = "YEAR")
        #self.section_table.heading('dept_name', text = "DEPT NAME")

        self.section_table['show'] = 'headings'

        self.section_table.column('section_no', width = 50)
        self.section_table.column('section_name', width = 100)
        #self.section_table.column('year_no', width = 50)
        #self.section_table.column('dept_name', width = 50)

        self.section_table.pack(fill= BOTH, expand = 1)
        self.section_table.bind("<ButtonRelease-1>", self.set_cursor_year)
        self.fetch_section()

    def fetch_section(self):
        pass
    def section_DB(self):
        if self.section_name.get()== "":
            messagebox.showerror("Error", "BOX CAN'T BE EMPTY")
        
        else:
            dept_sel  = self.department_name.get()
            year_sel = self.year_name.get()
            con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
            cur = con.cursor()

            
            dept_number = self.dept_dict[dept_sel]
            year_number = self.year_all_details[year_sel]
            cur.execute("Insert into section values(%s,%s,%s)",(0,
                                                            self.section_name.get(),
                                                            year_number
                                                            ))
            con.commit()
            self.year_name.set("")
            messagebox.showinfo("Sucess","Sucessfully added sectioN")
            self.fetch_section()
            con.close()

    def search_section_year_fetch(self, ev):
        self.section_table.delete(*self.section_table.get_children())
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        dept_sel  = self.department_name.get()
        cur.execute("select d.* from deptyear d where d.dept_no in (select dy.dept_no from department dy where dy.dept_name = %s)", dept_sel)
        rows = cur.fetchall()
        self.year = []
        self.year_all_details = {}
        for i in rows:
            self.year.append(i[1])
            self.year_all_details[i[1]]=i[0]


        combo_year = ttk.Combobox(self.section_add, textvariable = self.year_name,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_year['values']  =(self.year)
        combo_year.place(x = 25, y = 240)
        combo_year.bind("<<ComboboxSelected>>", self.search_section_fetch)


    def search_section_fetch(self,ev):

        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        year_sel = self.year_name.get()
        
        year_id = self.year_all_details[year_sel]
        cur.execute("select section_id, section_name from section where year_no = %s", year_id)
        rows = cur.fetchall()

        if len(rows)!= 0 :
            self.section_table.delete(*self.section_table.get_children())
            for row in rows:
                self.section_table.insert('', END, values =row)
            con.commit()

        con.close()


        

        

    def homepage(self):

        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Facial Recognition Attendence System")
        self.root.geometry("1530x830+0+0")

        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        bg_lbl = Label(self.root, image = self.bg_icon).pack()
        title = Label(self.root, text = "Attendence System Login", font=("times new roman",40, "bold"), bg="yellow", fg = "red", bd =10, relief = GROOVE )
        title.place(x=0, y=0, relwidth = 1)

        #=========================== Image icon =================================

        self.main_frame = Frame(self.root, bd = 4, relief= RIDGE, bg = "midnight blue")
        self.main_frame.place(x=20, y=100, width=1480, height = 720)

        self.add_student_image =ImageTk.PhotoImage(file= "images/add_student.jpg")
        self.train_student_image =PhotoImage(file= "images/train.png")
        self.recognize =PhotoImage(file= "images/recognize.png")
        self.show_attendence =PhotoImage(file= "images/show_attendence.png")

        add_btn = Button(self.main_frame, image=self.add_student_image, command=self.add_student,border=0, height = 300, width=300)
        
        add_btn.grid(row = 0,column = 0, padx = 10, pady = 10)
        add_label = Label(self.main_frame, text = "Add Student", font=("times new roman",20, "bold"), bg="yellow", fg = "red", bd =10, relief = GROOVE )
        add_label.grid(row=1, column=0)

        #add_student_label = Label(self.main_frame, text = "Add Student", font=("Freestyle Script",20, "bold"), fg = "red", bd =10 )
       # add_student_label.place(x=100, y=310)

        train_btn = Button(self.main_frame, image=self.train_student_image, command=self.train_image,border=0, height = 300, width=300)
        
        train_btn.grid(row = 0,column = 1, padx = 10, pady = 10)
        train_label = Label(self.main_frame, text = "Train System", font=("times new roman",20, "bold"), bg="yellow", fg = "red", bd =10, relief = GROOVE )
        train_label.grid(row=1, column=1)

        recognize_btn = Button(self.main_frame, image=self.recognize, command=self.recognizers,border=0, height = 300, width=300)
        
        recognize_btn.grid(row = 0,column = 2, padx = 10, pady = 10)

        take_label = Label(self.main_frame, text = "Take Attendence", font=("times new roman",20, "bold"), bg="yellow", fg = "red", bd =10, relief = GROOVE )
        take_label.grid(row=1, column=2)

        view_attendence_btn = Button(self.main_frame, image=self.show_attendence, command=self.view_attendence,border=0, height = 300, width=300)
        
        view_attendence_btn.grid(row = 0,column = 3, padx = 10, pady = 10)

        show_label = Label(self.main_frame, text = "Show Attendence", font=("times new roman",20, "bold"), bg="yellow", fg = "red", bd =10, relief = GROOVE )
        show_label.grid(row=1, column=3)


        logout_btn = Button(self.main_frame, command=self.logout,border=0,text = 'Logout', height = 5, width=20)
        
        logout_btn.grid(row = 2,column = 0,padx = 10, pady = 50)

    def logout(self):
        self.root.destroy()
        root = tk.Tk()
        obj = Login_System(root)
        root.mainloop()
        
        
    def add_student(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Facial Recognition Attendence System")
        self.root.geometry("1530x830+0+0")

        title_label = Label(self.root,bd = 10, relief = GROOVE, text="Attendence System", font=("times new roman", 40, "bold"), bg = "yellow", fg = "red")
        title_label.pack(side=TOP, fill = X )

    #============All Variables=============================
        
        
        self.Roll_number = StringVar()
        self.Name_var = StringVar()
        self.fname_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.catgory_var = StringVar()
        self.year_var  =StringVar()
        self.section_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()
        

    #============Manage Frame ============================

        self.manage_frame = Frame(self.root, bd = 4, relief= RIDGE, bg = "crimson")
        self.manage_frame.place(x=20, y=100, width=450, height = 720)

        manage_title= Label(self.manage_frame,bg= "crimson",fg = "white" ,text = "Add Student", font=("times new roman", 30, "bold"))
        manage_title.grid(row=0, columnspan =2, pady = 20)


        roll_number = Label(self.manage_frame, text = "Roll Number", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        roll_number.grid(row=1, column  = 0 , pady = 10, padx = 20, sticky = "w")

        txt_roll = Entry(self.manage_frame,textvariable = self.Roll_number, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_roll.grid(row=1, column  = 1, pady = 10, padx = 20)

        lbl_name = Label(self.manage_frame, text = "Name", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_name.grid(row=2, column  = 0 , pady = 10, padx = 20, sticky = "w")

        txt_name = Entry(self.manage_frame,textvariable = self.Name_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_name.grid(row=2, column  = 1, pady = 10, padx = 20)

        lbl_fname = Label(self.manage_frame, text = "Father's name", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_fname.grid(row=3, column  = 0 , pady = 10, padx = 20, sticky = "w")

        txt_fname = Entry(self.manage_frame,textvariable = self.fname_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_fname.grid(row=3, column  = 1, pady = 10, padx = 20)

        lbl_email = Label(self.manage_frame, text = "E-mail", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_email.grid(row=4, column  = 0 , pady = 10, padx = 20, sticky = "w")
        txt_email = Entry(self.manage_frame,textvariable = self.Email_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_email.grid(row =4, column  =1, pady = 10, padx= 20)
        
        lbl_gender = Label(self.manage_frame, text = "Gender", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_gender.grid(row=5, column  = 0 , pady = 10, padx = 20, sticky = "w")

        combo_gender = ttk.Combobox(self.manage_frame, textvariable = self.Gender_var,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_gender['values']  =('Male', "Female", 'Other')
        combo_gender.grid(row =5, column  =1, pady = 10, padx= 20)

        lbl_category = Label(self.manage_frame, text = "Category", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_category.grid(row=6, column  = 0 , pady = 10, padx = 20, sticky = "w")

        combo_category = ttk.Combobox(self.manage_frame, textvariable = self.catgory_var,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_category['values']  =('General', "SC", "ST", "OBC", "Other")
        combo_category.grid(row =6, column  =1, pady = 10, padx= 20)

        lbl_year = Label(self.manage_frame, text = "Year", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_year.grid(row=7, column  = 0 , pady = 10, padx = 20, sticky = "w")

        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("Select deptno from facultyinfo where username = %s",self.username_active)
        self.dept_no_active=cur.fetchone()[0]

        cur.execute("select dept_year, year_no from deptyear where dept_no = %s", self.dept_no_active)
        rows = cur.fetchall()
        year = list(map(lambda x: x[0], rows))
        self.year_dict = {}
        self.yearmap = {}
        for i in rows:
            self.year_dict[i[0]] = i[1]
            self.yearmap[i[1]] = i[0]
        print(self.year_dict)


        combo_year = ttk.Combobox(self.manage_frame, textvariable = self.year_var,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_year['values']  = year
        combo_year.grid(row =7, column  =1, pady = 10, padx= 20)
        combo_year.bind("<<ComboboxSelected>>", self.search_section_fetch)

        lbl_section = Label(self.manage_frame, text = "Section", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_section.grid(row=8, column  = 0 , pady = 10, padx = 20, sticky = "w")
        combo_section = ttk.Combobox(self.manage_frame, textvariable = self.section_var,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_section['values']  =()
        combo_section.grid(row =8, column  =1, pady = 10, padx= 20)

        lbl_contact = Label(self.manage_frame, text = "Contact", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_contact.grid(row = 9, column = 0, padx = 20, pady = 10, sticky = "w")

        txt_contact = Entry(self.manage_frame,textvariable = self.contact_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_contact.grid(row = 9, column = 1, padx = 20, pady =10)

        lbl_DOB = Label(self.manage_frame, text = "D.O.B", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_DOB.grid(row=10, column  = 0 , pady = 10, padx = 20, sticky = "w")

        txt_DOB = Entry(self.manage_frame,textvariable = self.dob_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_DOB.grid(row=10, column  = 1, pady = 10, padx = 20)

        lbl_address = Label(self.manage_frame, text = "Address", bg= "crimson", fg= "white", font= ("tims new roman", 10, "bold"))
        lbl_address.grid(row= 11, column  = 0 , pady = 10, padx = 20, sticky = "w")

        self.txt_address = Text(self.manage_frame, width=30, height = 4, font=("", 10))
        self.txt_address.grid(row = 11, column = 1, padx= 20, pady =10, sticky = "w")
         
    #=============Button Frame ================================

        btn_frame = Frame(self.manage_frame, bd = 4, relief  =RIDGE, bg = "crimson")
        btn_frame.place(x=18, y=650, width =420)

        Addbtn  =Button(btn_frame, text="Add",command = self.add_students, width = 10).grid(row=0, column = 0 , padx= 10, pady = 10)
        updatebtn  =Button(btn_frame,command = self.update_data, text="Update", width = 10).grid(row=0, column = 1 , padx= 10, pady = 10)
        deletebtn  =Button(btn_frame, command = self.delete_data, text="Delete", width = 10).grid(row=0, column = 2 , padx= 10, pady = 10)
        clearbtn  =Button(btn_frame, command = self.clear,text="Clear", width = 10).grid(row=0, column = 3 , padx= 10, pady = 10)
    
    
    
    #============detail Frame ============================
        
        detail_frame = Frame(self.root, bd = 4, relief= RIDGE, bg = "crimson")
        detail_frame.place(x=500, y=100, width=1000, height = 720)

        lbl_search= Label(detail_frame, text = "Search By", bg ="crimson", font=("times new roman", 20,"bold"), fg = "white")
        lbl_search.grid(row=0, column = 0, pady = 20, sticky = "w")

        combo_search = ttk.Combobox(detail_frame,textvariable = self.search_by,width = 10, state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_search['values']  =('roll_no', "name", 'contact')
        combo_search.grid(row =0, column  =1, pady = 10, padx= 20)


        txt_search = Entry(detail_frame, textvariable = self.search_text, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_search.grid(row=0, column  = 2, pady = 10, padx = 20, sticky = "w")

        search_btn  =Button(detail_frame,command = self.search_data, text="Search", width = 10).grid(row=0, column = 3, padx= 10, pady = 10)
        showall_btn  =Button(detail_frame,command = self.fetch_data, text="Showall", width = 10).grid(row=0, column = 4 , padx= 10, pady = 10)
        Image_btn  =Button(detail_frame,command = self.take_image, text="Take Image", width = 10)
        Image_btn.place(x =10, y= 600, width = 200, height = 100 )

        delete_Image_btn  =Button(detail_frame,command = self.delete_image, text="Delete Image", width = 10)
        delete_Image_btn.place(x =300, y= 600, width = 200, height = 100 )

        back_btn  =Button(detail_frame,command = self.homepage, text="Back", width = 10)
        back_btn.place(x =590, y= 600, width = 200, height = 100 )
    #======================Table Frame ==================================

        Table_frame = Frame(detail_frame, bd = 4, relief= RIDGE, bg = "crimson")
        Table_frame.place(x=10, y=70, width=950, height = 500)

        scroll_x = Scrollbar(Table_frame, orient= HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient= VERTICAL)
        self.Student_table = ttk.Treeview(Table_frame, columns=("roll", "name","Father's name", "email", "gender",'category','section', "contact", "dob", "address"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT, fill = Y)
        scroll_x.config(command = self.Student_table.xview)
        scroll_y.config(command = self.Student_table.yview)
        self.Student_table.heading("roll", text = "Roll no.")
        self.Student_table.heading("name", text = "Name")
        self.Student_table.heading("Father's name", text = "Father")
        self.Student_table.heading("email", text = "Email")
        self.Student_table.heading("gender", text = "Gender")
        self.Student_table.heading("category", text = "Category")
        
        self.Student_table.heading("section", text = "Section")
        self.Student_table.heading("contact", text = "Contact")
        self.Student_table.heading("dob", text = "D.O.B")
        self.Student_table.heading("address", text = "Address")
        self.Student_table['show']='headings'
        self.Student_table.column('roll', width = 100)
        self.Student_table.column('name', width = 100)
        self.Student_table.column("Father's name", width = 100)
        self.Student_table.column('email', width = 100)
        self.Student_table.column('gender', width = 100)
        self.Student_table.column('category', width = 100)
        
        self.Student_table.column('section', width = 100)
        self.Student_table.column('contact', width = 100)
        self.Student_table.column('dob', width =100 )
        self.Student_table.column('address', width = 150)

        self.Student_table.pack(fill = BOTH, expand = 1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    def add_students(self):
        if (self.Roll_number.get()=="" or self.Name_var.get()==""): 
        ##or (self.Email_var.get()=="" or self.Gender_var.get()="") or (self.year_var.get()="" or self.branch_var.get()="") or (self.section_var.get()=="" or self.contact_var.get()==""))
            messagebox.showerror("Error","All fields are required!!!")
        else:
            con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
            cur = con.cursor()
            cur.execute('Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (self.Roll_number.get(),
                                                                        self.Name_var.get().title(),
                                                                        self.fname_var.get(),
                                                                        self.Email_var.get(),
                                                                        self.Gender_var.get(),
                                                                        self.catgory_var.get(),
                                                                        self.section_details[self.section_var.get()],
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0', END)
                                                                        ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Sucess", "Record has been inserted")
    
    def search_section_fetch(self,ev):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        self.year_select_active = self.year_var.get()
        self.year_no_active = self.year_dict[self.year_select_active]
        cur.execute('select section_name, section_id from section where year_no = %s', self.year_no_active)
        rows = cur.fetchall()
        section = list(map(lambda x: x[0], rows))
        self.section_details = {}
    
        for i in rows:
            self.section_details[i[0]] = i[1]
        combo_section = ttk.Combobox(self.manage_frame, textvariable = self.section_var,state = 'readonly', font = ("times new roman", 13, "bold") )
        combo_section['values']  =(section)
        combo_section.grid(row =8, column  =1, pady = 10, padx= 20)

    def fetch_data(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows)!= 0 :
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values =row)
            con.commit()
        con.close()

    def clear(self):
        
        self.Roll_number.set("")
        self.Name_var.set("")
        self.fname_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.catgory_var.set("")
        self.section_var.set("")
        self.year_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete('1.0', END)

    def get_cursor(self,ev):
        
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        row = content["values"]
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select year_no from section where section_id = %s",row[6])
        year_no = cur.fetchone()[0]
        

        cur.execute('select dept_year from deptyear where year_no = %s', year_no)
        year_name = cur.fetchone()[0]

        cur.execute('select section_name from section where section_id = %s', row[6])
        sectionname = cur.fetchone()[0]

        

        self.Roll_number.set(row[0])
        self.Name_var.set(row[1])
        self.fname_var.set(row[2])
        self.Email_var.set(row[3])
        self.Gender_var.set(row[4])
        self.catgory_var.set(row[5])
        self.year_var.set(year_name)
        self.section_var.set(sectionname)
        self.contact_var.set(row[7])
        self.dob_var.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END, row[9])

    def update_data(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute('select year_no from deptyear where dept_no = %s', self.dept_no_active )
        rows = cur.fetchall()
        year_no_list = set(map(lambda x: x[0], rows))
        cur.execute('select * from section where year_no in %s', year_no_list)
        rows = cur.fetchall()
        section_details = {}
    
        for i in rows:
            section_details[i[1]] = i[0]
        
        

        cur.execute('update student set name=%s,fname=%s,email=%s,gender=%s,category=%s,section_id=%s,contact=%s,dob=%s,address=%s where roll_no=%s', (
                                                                        self.Name_var.get(),
                                                                        self.fname_var.get(),
                                                                        self.Email_var.get(),
                                                                        self.Gender_var.get(),
                                                                        self.catgory_var.get(),
                                                                        section_details[self.section_var.get()],
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0', END),
                                                                        self.Roll_number.get(),
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("delete from student where roll_no = %s", self.Roll_number.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!= 0 :
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values =row)
            con.commit()
        con.close()


    def take_image(self):
            Id=(self.Roll_number.get())
            name=(self.Name_var.get())
            flag = True
            if(flag):
                cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
                harcascadePath = "haarcascade_frontalface_default.xml"
                detector=cv2.CascadeClassifier(harcascadePath)
                sampleNum=0
                while(True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                        #incrementing sample number 
                        sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                        cv2.imshow('frame',img)
            #wait for 100 miliseconds 
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
            # break if the sample number is morethan 100
                    elif sampleNum>60:
                        break
                cam.release()
                cv2.destroyAllWindows() 
                res = "Images Saved for ID : " + Id +" Name : "+ name
                messagebox.showinfo("Sucess", "Sucessful Stored the images of" + res )

    def delete_image(self):

        for file in os.listdir('TrainingImage/'):
            a = file.split(".")
            if a[1] == self.Roll_number.get():
                os.remove("TrainingImage/"+file)
        messagebox.showinfo("Sucess", "Image sucessfully deleted")

    def train_image(self): 
        recognizer=cv2.face.LBPHFaceRecognizer_create()
        path='TrainingImage'

        def getImagesWithID(path):
            imgPaths=[os.path.join(path,f) for f in os.listdir(path)]
            faces=[]
            Ids=[]
            for imgPath in imgPaths:
                faceImg=Image.open(imgPath).convert("L")
                faceNp=np.array(faceImg,'uint8')
                ID=int(os.path.split(imgPath)[-1].split('.')[1])
                faces.append(faceNp)
                Ids.append(ID)
                cv2.imshow("traning", faceNp)
                cv2.waitKey(10)
            return np.array(Ids), faces

        Ids, faces=getImagesWithID(path)
        recognizer.train(faces,Ids)
        recognizer.save("recognizer/trainingData.yml")
        messagebox.showinfo("sucess", "Sucessfully trainied")
        cv2.destroyAllWindows()
    
    def recognizers(self):
        faceDetect=cv2.CascadeClassifier(os.path.abspath('haarcascade_frontalface_default.xml'))
        cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        rec=cv2.face.LBPHFaceRecognizer_create()
        rec.read("recognizer/trainingData.yml")

        def getProfile(u_id):
            con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
            cursor = con.cursor()
            cmd="SELECT * FROM student WHERE roll_no="+str(u_id)
            cursor.execute(cmd)
            profile=None
            for row in cursor:
                profile=row
            con.close()
            return profile
        done=False
        u_id=0
        #font = cv2.cv2.InitFont(cv2.cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
        fontface = cv2.FONT_HERSHEY_SIMPLEX
        fontcolor = (0, 0, 204)
        while(True):
            ret, img=cam.read()
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceDetect.detectMultiScale(gray, 1.3,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                u_id, conf=rec.predict(gray[y:y+h, x:x+w])
                self.profile=getProfile(u_id)
                
                if conf>60:
                    profile=None
                if (self.profile!=None):
                    #cv2.cv.putText(cv2.cv.fromarray(img),str(u_id),(x,y+h),font,255)
                    cv2.putText(img, "Roll No:"+str(self.profile[0]), (x,y+h+30), fontface, 0.6, fontcolor, 2)
                    cv2.putText(img, "Name :"+str(self.profile[1]), (x,y+h+60), fontface, 0.6, fontcolor, 2)
                    #cv2.putText(img, "Gender:"+str(profile[2]), (x,y+h+90), fontface, 0.6, fontcolor, 2)
                    #cv2.putText(img, "Occupation:"+str(profile[3]), (x,y+h+120), fontface, 0.6, fontcolor, 2)
                    done=True

            cv2.imshow("Attendence Recognizer", img)
            if(cv2.waitKey(1)==ord('q')) or done:
                break;
        cam.release()
        sleep(3)
        cv2.destroyAllWindows()
        if self.profile!=None:
            messagebox.showinfo("Status", "Attendence Marked!!!! {}".format(self.profile[0]))
            self.mark_attendence()

    def mark_attendence(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        cur.execute("select d.dept_year from deptyear d, section s where s.section_id = %s and s.year_no = d.year_no", self.profile[6])
        student_year = cur.fetchone()[0]
        cur.execute("select dd.dept_name from deptyear d, section s, department dd where s.section_id = %s and s.year_no = d.year_no and d.dept_no = dd.dept_no", self.profile[6])
        branch = cur.fetchone()[0]
        cur.execute("Select section_name from section where section_id = %s", self.profile[6])
        section = cur.fetchone()[0]
        year, month, date = str(datetime.date.today()).split("-")
        time,_= str(datetime.datetime.now().time()).split(".")
        cur.execute('Insert into markattendence values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (self.profile[0],
                                                                        self.profile[1].title(),
                                                                        student_year,
                                                                        branch,
                                                                        section,
                                                                        date,
                                                                        month,
                                                                        year,
                                                                        time
                                                                        ))
        

        con.commit()
        con.close()
        messagebox.showinfo("Sucessful","sucessful")

    def view_attendence(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Facial Recognition Attendence System")
        self.root.geometry("1530x830+0+0")

        title_label = Label(self.root,bd = 10, relief = GROOVE, text="Attendence System", font=("times new roman", 40, "bold"), bg = "yellow", fg = "red")
        title_label.pack(side=TOP, fill = X )

    #-------------------------------------------------------------------------------------------------------------------

        self.roll_number_search = StringVar()
        self.roll_name_option = StringVar()
        self.name_search = StringVar()
        self.cyear_search  =StringVar()
        self.branch_search = StringVar()
        self.section_search = StringVar()
        self.date_search = StringVar()
        self.month_search = StringVar()
        self.year_search = StringVar()
        self.val_dic = {"Roll No": self.roll_number_search, "Name":self.name_search }
        self.years=[]
        year, month, date= str(datetime.date.today()).split("-")
        

    #--------------------------------------------------------------------------------------------------------------------


        

        
    #--------------------------------------------------------------------------------------------------------------------------------------------

        show_attendence_frame = Frame(self.root, bd = 4, relief= RIDGE, bg = "crimson")
        show_attendence_frame.place(x=10, y=100, width=1500, height = 720)

        Table_frame = Frame(show_attendence_frame, bd = 4, relief= RIDGE, bg = "crimson")
        Table_frame.place(x=20, y=70, width=1460, height = 500)

        scroll_x = Scrollbar(Table_frame, orient= HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient= VERTICAL)
        self.attendence_table = ttk.Treeview(Table_frame, columns=("roll", "name", "stu_year","branch",'section','date','month', "year", "time"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT, fill = Y)
        scroll_x.config(command = self.attendence_table.xview)
        scroll_y.config(command = self.attendence_table.yview)
        self.attendence_table.heading("roll", text = "Roll no.")
        self.attendence_table.heading("name", text = "Name")
        self.attendence_table.heading("stu_year", text = "Student_Year")
        self.attendence_table.heading("branch", text = "Branch")
        self.attendence_table.heading("section", text = "Section")
        self.attendence_table.heading("date", text = "Date")
        self.attendence_table.heading("month", text = "Month")
        self.attendence_table.heading("year", text = "Year")
        self.attendence_table.heading("time", text = "Time")
        self.attendence_table['show']='headings'

        self.attendence_table.column('roll',width = 100)
        self.attendence_table.column('name',width = 100)
        self.attendence_table.column('stu_year',width = 100)
        self.attendence_table.column('branch',width = 100)
        self.attendence_table.column('section',width = 100)
        
        self.attendence_table.column('date',width = 100)
        self.attendence_table.column('month',width = 100)
        self.attendence_table.column('year',width = 100)
        self.attendence_table.column('time',width = 100)

        self.attendence_table.pack(fill = BOTH, expand = 1)
        self.fetch_attendence_data()


        back_btn  =Button(show_attendence_frame,command = self.homepage, text="Back", width = 10)
        back_btn.place(x =590, y= 600, width = 200, height = 100 )
        

    def fetch_attendence_data(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        year, month, date = str(datetime.date.today()).split("-")
        cur.execute("select * from markattendence where month = %s", month)
        rows = cur.fetchall()
        if len(rows)!= 0 :
            self.attendence_table.delete(*self.attendence_table.get_children())
            for row in rows:
                self.attendence_table.insert('', END, values =row)
            con.commit()
        con.close()

    def attendence_filter(self):
        con  = pymysql.connect(host="localhost", user = "root", password = "", database = "attendence")
        cur = con.cursor()
        
        cur.execute("select * from markattendence where roll ="+str(self.roll_number_search.get()) + " and date ="+str(self.date_search.get()) + " and month = "+str(self.month_search.get())+ " and year ="+str(self.year_search.get())+ " and stu_year ="+str(self.cyear_search.get())+ " and branch = "+str(self.branch_search.get()) )
        rows = cur.fetchall()
        if len(rows)!= 0 :
            self.attendence_table.delete(*self.attendence_table.get_children())
            for row in rows:
                self.attendence_table.insert('', END, values =row)
            con.commit()
        con.close()

    
root = tk.Tk()
obj = Login_System(root)
root.mainloop()
