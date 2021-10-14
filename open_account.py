import sys
import os
from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("library")
root.resizable(False,False)
root.geometry("1200x600")
db = sqlite3.connect("bank.db")#===================================DATABASE CREATION====================
c=db.cursor() #==================================MAKING PATH=======================
q ="create table  if not exists employee(Name text primary_key NOT NULL,Password text NOT NULL,Contact text,Email text,Age interger)"
c.execute(q)  
#login page text variablename
nm=StringVar()
pwd=StringVar()
cn=StringVar()
eml=StringVar()
ag=StringVar()
nme=StringVar()
passwrd=StringVar()
name_c=StringVar()
pwd_c=StringVar()
def main_page():
    #---------FRAMES---------------------
    topframe=Frame(root, bg="pink",borderwidth=5,height=100,width=1200,relief='ridge')
    frame1 =Frame(root, bg="peachpuff",borderwidth=2,height=500,width=1200,relief='ridge')
    frame2 =Frame(root, bg="lavenderblush",borderwidth=5,height=450,width=1163,relief="ridge")
    bottomframe1=Frame(root, bg="oldlace",borderwidth=5,height=250,width=440,relief='ridge')
    
    topframe.place(x=0,y=0)
    frame1.place(x=0,y=100)
    frame2.place(x=20,y=130)
    bottomframe1.place(x=380,y=300)
    
    home_l=Label(frame2,text="HOME PAGE",bg="lavenderblush",font=("Helvetica", 60,"bold"),fg="pink")
    home_l.place(x=330,y=50)
    
    login=Button(bottomframe1,text="LOG IN",command=login_page,height=5,width=35,bg="peachpuff",relief="ridge",font=("Helvetica", 10,"bold"))
    login.place(x=80,y=15)
    signup=Button(bottomframe1,text="SIGN UP",command=signup_page,height=5,width=35,bg="peachpuff",relief="ridge",font=("Helvetica", 10,"bold"))
    signup.place(x=80,y=130)
def change_password():
    global nme,passwrd,name_c,pwd_c
    change_frame=Frame(root, bg="lavenderblush",borderwidth=5,height=450,width=1163,relief="ridge")
    change_frame.place(x=20,y=130)
    reg=Label(change_frame,text="CHANGE PASSWORD",bg="lavenderblush",font=("Helvetica",18,"bold","underline")).place(x=500,y=50) 
    
    name1=Label(change_frame,text="USER NAME",bg="lavenderblush",font=("Helvetica",18,"bold")).place(x=430,y=150) 
    name2=Entry(change_frame,bd=3,textvariable=name_c).place(x=650,y=155)
    #Password===================================================
    
    pswd1=Label(change_frame,text="PASSWORD",bg="lavenderblush",font=("Helvetica",18,"bold")).place(x=430,y=220)
    pswd2=Entry(change_frame,bd=3,textvariable=pwd_c,show="*").place(x=650,y=225)
    
    login_1=Button(change_frame,text="SAVE",command=update,height=2,width=42,bg="peachpuff",relief="ridge",font=("Helvetica", 10,"bold"))
    login_1.place(x=430,y=320)
    back=Button(change_frame,text="<------BACK",command=admin_page,height=2,width=15,bg="lavenderblush",relief="ridge",font=("Helvetica", 10,"bold"))
    back.place(x=0,y=0)
    admin_b=Button(change_frame,text="SIGNUP------>",command=login_page,height=2,width=15,bg="lavenderblush",relief="ridge",font=("Helvetica", 10,"bold"))
    admin_b.place(x=1025,y=0)
def update():
    global nme,passwrd,name_c,pwd_c
    n=nme.get()
    p=pwd_c.get()
    print("n=====",n)
    print("pswdn=====",p)
    
    db = sqlite3.connect("bank.db")
    c=db.cursor()
    try:
        c.execute("""update employee set
                  Password=:ppp
                  where Name=:nameee""",
                  {
                  'ppp':p,
                  'nameee':n
                  })
        messagebox.showinfo("password",message=["Password change sucessfully"])
    except:
        messagebox.showwarning("Warning",message=["Incorrect Username"])
     
    db.commit()  #use to reflect changes into database permanently
    db.close()

def delete_user():
    global nme,passwrd
    n=nme.get()
    p=passwrd.get()
    db = sqlite3.connect("bank.db")
    c=db.cursor()
    c.execute("delete from employee where Name=:nn",{'nn':n})
    messagebox.showinfo("Delete",message=["Your Account Deleted"])
    main_page()
     
    db.commit()  #use to reflect changes into database permanently
    db.close()
    
def admin_page():
    global nm,pwd,cn,eml,ag
    adminframe =Frame(root, bg="lavenderblush",borderwidth=5,height=450,width=1163,relief="ridge")
    adminframe.place(x=20,y=130)
    reg=Label(adminframe,text="ADMIN PAGE",bg="lavenderblush",font=("Helvetica",18,"bold","underline")).place(x=500,y=20) 
    bottomframe1=Frame(adminframe, bg="oldlace",borderwidth=5,height=250,width=440,relief='ridge')
    bottomframe1.place(x=380,y=130)
    login=Button(bottomframe1,text="CHANGE PASSWORD",command=change_password,height=5,width=35,bg="peachpuff",relief="ridge",font=("Helvetica", 10,"bold"))
    login.place(x=80,y=15)
    signup=Button(bottomframe1,text="DELETE USER",command=delete_user,height=5,width=35,bg="peachpuff",relief="ridge",font=("Helvetica", 10,"bold"))
    signup.place(x=80,y=130)
    back=Button(adminframe,text="<------BACK",command=login_page,height=2,width=15,bg="lavenderblush",relief="ridge",font=("Helvetica", 10,"bold"))
    back.place(x=0,y=0)
    admin_b=Button(adminframe,text="HOME------>",command=main_page,height=2,width=15,bg="lavenderblush",relief="ridge",font=("Helvetica", 10,"bold"))
    admin_b.place(x=1025,y=0)
def login_execution():
    global nme,passwrd
    db = sqlite3.connect("bank.db")
    c=db.cursor()
    try:
        c.execute("select * from employee where Name=:name and Password=:pswd",{'name':nme.get(),'pswd':passwrd.get()})
        record=c.fetchall() 
        print("---------",record[0][0],record[0][1])
        db.commit()
        db.close()
        admin_page()
        
    except:
        messagebox.showwarning("Warning",message=["Incorrect Name or Password"])
    
def login_page():
    
    loginframe =Frame(root, bg="lavenderblush",borderwidth=5,height=450,width=1163,relief="ridge")
    loginframe.place(x=20,y=130)
    reg=Label(loginframe,text="LOG IN FORM",bg="lavenderblush",font=("Helvetica",18,"bold","underline")).place(x=500,y=50) 
    
    name1=Label(loginframe,text="USER NAME",bg="lavenderblush",font=("Helvetica",18,"bold")).place(x=430,y=150) 
    name2=Entry(loginframe,bd=3,textvariable=nme).place(x=650,y=155)
    #Password===================================================
    
    pswd1=Label(loginframe,text="PASSWORD",bg="lavenderblush",font=("Helvetica",18,"bold")).place(x=430,y=220)
    pswd2=Entry(loginframe,bd=3,textvariable=passwrd,show="*").place(x=650,y=225)
    
    login_1=Button(loginframe,text="LOG IN",command=login_execution,height=2,width=42,bg="peachpuff",relief="ridge",font=("Helvetica", 10,"bold"))
    login_1.place(x=430,y=320)
    back=Button(loginframe,text="<------BACK",command=main_page,height=2,width=15,bg="lavenderblush",relief="ridge",font=("Helvetica", 10,"bold"))
    back.place(x=0,y=0)
    admin_b=Button(loginframe,text="SIGNUP------>",command=signup_page,height=2,width=15,bg="lavenderblush",relief="ridge",font=("Helvetica", 10,"bold"))
    admin_b.place(x=1025,y=0)
def signup_execution():
    global nm,pwd,cn,eml,ag
    db = sqlite3.connect("bank.db")
    c=db.cursor()
    c.execute("insert into employee values(:name2,:pswd2,:cont2,:email2,:age2)",
             {
              'name2':nm.get(),
              'pswd2':pwd.get(),
              'cont2':cn.get(),
              'email2':eml.get(),
              'age2':ag.get()
             })
    
    db.commit()  #use to reflect changes into databse permanently
    db.close()
    login_page()
def signup_page():
    global nm,pwd,cn,eml,ag
    signupframe =Frame(root, bg="lavenderblush",borderwidth=5,height=450,width=1163,relief="ridge")
    signupframe.place(x=20,y=130)
    reg=Label(signupframe,text="SIGN UP FORM",bg="lavenderblush",font=("Helvetica",18,"bold","underline")).place(x=500,y=20) 
    name1=Label(signupframe,text="NAME",bg="lavenderblush",font=("Helvetica",18,"bold")).place(x=430,y=100) 
    name2=Entry(signupframe,bd=3,textvariable=nm).place(x=650,y=95)
    #Password===================================================
    
    pswd1=Label(signupframe,text="PASSWORD",bg="lavenderblush",font=("Helvetica",18,"bold")).place(x=430,y=150)
    pswd2=Entry(signupframe,bd=3,textvariable=pwd,show="*").place(x=650,y=145)
    #Contact====================================================
    
    cont1=Label(signupframe,text="CONTACT NO.",bg="lavenderblush",font=("Helvetica",18,"bold")).place(x=430,y=200)
    cont2=Entry(signupframe,bd=3,textvariable=cn).place(x=650,y=195)
    #Email======================================================
    
    email1=Label(signupframe,text="EMAIL ID",bg="lavenderblush",font=("Helvetica",18,"bold")).place(x=430,y=250)
    email2=Entry(signupframe,bd=3,textvariable=eml).place(x=650,y=245)
    #Age========================================================
    
    age1=Label(signupframe,text="AGE",bg="lavenderblush",font=("Helvetica",18,"bold")).place(x=430,y=300)
    age2=Entry(signupframe,bd=3,textvariable=ag).place(x=650,y=295)
    
    login_1=Button(signupframe,text="SIGN UP",command=signup_execution,height=2,width=42,bg="peachpuff",relief="ridge",font=("Helvetica", 10,"bold"))
    login_1.place(x=430,y=350)
    back=Button(signupframe,text="<------BACK",command=main_page,height=2,width=15,bg="lavenderblush",relief="ridge",font=("Helvetica", 10,"bold"))
    back.place(x=0,y=0)
    admin_b=Button(signupframe,text="ADMIN------>",command=login_page,height=2,width=15,bg="lavenderblush",relief="ridge",font=("Helvetica", 10,"bold"))
    admin_b.place(x=1025,y=0)

main_page()
root.mainloop()