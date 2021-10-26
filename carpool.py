#!/usr/bin/env python
# coding: utf-8

# In[19]:


from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import shutil
import os


# In[2]:


try:
    con=sqlite3.connect(database="carpool.sqlite")
    cursor=con.cursor()
    table1="create table users(username text primary key,password text,mobile text,email text)"
    table2="create table cars(username text,src text,dest text,regno text primary key,model text,seats text,fuel text)"
    cursor.execute(table1)
    cursor.execute(table2)
    con.commit()
    con.close()
    print("tables created")
except Exception as e:
    print(e)


# In[24]:


win=Tk()
win.state("zoomed")
win.configure(bg="powder blue")
lbl_title=Label(win,text="Car Pooling",font=('',100,'bold','underline'),bg="powder blue")
lbl_title.pack()

img=Image.open("images/cp4.jpg").resize((400,150))
imgtk=ImageTk.PhotoImage(img,master=win)
lbl_img=Label(win,image=imgtk,borderwidth=2, relief="solid")
lbl_img.place(relx=.001,rely=0)

img2=Image.open("images/cp2.jpg").resize((400,150))
imgtk2=ImageTk.PhotoImage(img2,master=win)
lbl_img2=Label(win,image=imgtk2,borderwidth=2, relief="solid")
lbl_img2.place(relx=.747,rely=0)

img3=Image.open("images/login.png").resize((140,40))
imgtk3=ImageTk.PhotoImage(img3)

img4=Image.open("images/reset.png").resize((140,40))
imgtk4=ImageTk.PhotoImage(img4)

img5=Image.open("images/logout.png").resize((140,40))
imgtk5=ImageTk.PhotoImage(img5)

img6=Image.open("images/register.png").resize((140,40))
imgtk6=ImageTk.PhotoImage(img6)

img7=Image.open("images/newuser.png").resize((200,40))
imgtk7=ImageTk.PhotoImage(img7)

img8=Image.open("images/back.png").resize((140,40))
imgtk8=ImageTk.PhotoImage(img8)

img9=Image.open("images/Search1.png").resize((140,40))
imgtk9=ImageTk.PhotoImage(img9)

img10=Image.open("images/submit.png").resize((140,40))
imgtk10=ImageTk.PhotoImage(img10)

img11=Image.open("images/Update.png").resize((140,40))
imgtk11=ImageTk.PhotoImage(img11)

img12=Image.open("images/profilepic.jpg").resize((170,140))
imgtk12=ImageTk.PhotoImage(img12)

def home_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='brown')
    frm.place(x=400,y=300,relwidth=.5,relheight=.45)
    
    def newuser(event):
        frm.destroy()
        newuser_frame()
     
    def reset(event):
        e_user.delete(0,"end")
        e_pass.delete(0,"end")
        e_user.focus()
        
    def login(event):
        global loginuser_row
        u=e_user.get()
        p=e_pass.get()
        try:
            con=sqlite3.connect(database="carpool.sqlite")
            cursor=con.cursor()
            cursor.execute("select * from users where username=? and password=?",(u,p))
            loginuser_row=cursor.fetchone()
            con.close()
            if(loginuser_row==None):
                messagebox.showerror("Login","Invalid Username/Password")
            else:
                
                frm.destroy()
                login_frame()
            
        except Exception as e:
            messagebox.showerror("Login",str(e))
        
    lbl_user=Label(frm,text="Username",font=('',20,'bold'))
    lbl_pass=Label(frm,text="Password",font=('',20,'bold'))
    e_user=Entry(frm,font=('',20,'bold'),bd=5)
    e_user.focus()
    e_pass=Entry(frm,font=('',20,'bold'),bd=5,show="*")
    lbl_user.place(x=150,y=50)
    e_user.place(x=320,y=50)
    lbl_pass.place(x=150,y=130)
    e_pass.place(x=320,y=130)
    
    btn_login=Label(frm,image=imgtk3)
    btn_login.place(x=250,y=210)
    btn_login.bind("<Button>",login)
    
    btn_reset=Label(frm,image=imgtk4)
    btn_reset.place(x=400,y=210)
    btn_reset.bind("<Button>",reset)
    
    btn_new=Label(frm,image=imgtk7)
    btn_new.place(x=300,y=280)
    btn_new.bind("<Button>",newuser)
 

def newuser_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='brown')
    frm.place(x=400,y=200,relwidth=.5,relheight=.55)
    
    def reset(event):
        e_user.delete(0,"end")
        e_pass.delete(0,"end")
        e_mob.delete(0,"end")
        e_email.delete(0,"end")
        e_user.focus()
        
    def reg_todb(event):
        u=e_user.get()
        p=e_pass.get()
        m=e_mob.get()
        e=e_email.get()
        
        if(len(u)==0 or len(p)==0 or len(m)==0 or len(e)==0):
            messagebox.showwarning('Validation',"Please fill all fields!!")
        else:
            try:
                con=sqlite3.connect(database="carpool.sqlite")
                cursor=con.cursor()
                cursor.execute("insert into users values(?,?,?,?)",(u,p,m,e))
                con.commit()
                con.close()
                messagebox.showinfo("Registration","Registration Done!!")
                frm.destroy()
                home_frame()
            except Exception as e:
                messagebox.showerror("Registration","Username already exists!")

    lbl_user=Label(frm,text="Username",font=('',20,'bold'))
    lbl_pass=Label(frm,text="Password",font=('',20,'bold'))
    lbl_mob=Label(frm,text="Mobile",font=('',20,'bold'))
    lbl_email=Label(frm,text="Email",font=('',20,'bold'))
    
    e_user=Entry(frm,font=('',20,'bold'),bd=5)
    e_user.focus()
    e_pass=Entry(frm,font=('',20,'bold'),bd=5,show="*")
    e_mob=Entry(frm,font=('',20,'bold'),bd=5)
    e_email=Entry(frm,font=('',20,'bold'),bd=5)
        
    lbl_user.place(x=150,y=50)
    e_user.place(x=320,y=50)
    lbl_pass.place(x=150,y=130)
    e_pass.place(x=320,y=130)
    lbl_mob.place(x=150,y=210)
    e_mob.place(x=320,y=210)
    lbl_email.place(x=150,y=290)
    e_email.place(x=320,y=290)

    btn_reg=Label(frm,image=imgtk6)
    btn_reg.place(x=250,y=370)
    btn_reg.bind("<Button>",reg_todb)
    
    btn_reset=Label(frm,image=imgtk4)
    btn_reset.place(x=420,y=370)
    btn_reset.bind("<Button>",reset)

    
def login_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='brown')
    frm.place(x=300,y=200,relwidth=.65,relheight=.55)
    
    def logout(event):
        frm.destroy()
        home_frame()
        
    def search():
        frm.destroy()
        searchpool_frame()
        
    def create():
        frm.destroy()
        createpool_frame()    
     
    def update():
        frm.destroy()
        updateprofile_frame()
        
    def picture():
        img_path=filedialog.askopenfilename()
        shutil.copy(img_path,f"images/{loginuser_row[0]}.png")
        img=Image.open(f"images/{loginuser_row[0]}.png").resize((170,140))
        imgtk=ImageTk.PhotoImage(img)
        lbl_profilepic['image']=imgtk
        lbl_profilepic.image=imgtk
    
    lbl_wel=Label(frm,text=f"Welcome,{loginuser_row[0]}",font=('',15,'bold'),fg='green')
    lbl_wel.place(x=0,y=0)
    
    lbl_profilepic=Label(frm,image=imgtk12)
    lbl_profilepic.place(x=0,y=40)
    
    if(os.path.exists(f"images/{loginuser_row[0]}.png")):
        img=Image.open(f"images/{loginuser_row[0]}.png").resize((170,140))
        imgtk=ImageTk.PhotoImage(img)
        lbl_profilepic['image']=imgtk
        lbl_profilepic.image=imgtk
        
    
    btn_logout=Label(frm,image=imgtk5)
    btn_logout.place(relx=.86,rely=0)
    btn_logout.bind("<Button>",logout)
    
    btn_search=Button(frm,text="Search Pool",font=('',15,'bold'),bd=5,width=20,command=search)
    btn_search.place(relx=.35,rely=.1)
    
    btn_create=Button(frm,text="Create Pool",font=('',15,'bold'),bd=5,width=20,command=create)
    btn_create.place(relx=.35,rely=.3)

    btn_profile=Button(frm,text="Update profile",font=('',15,'bold'),bd=5,width=20,command=update)
    btn_profile.place(relx=.35,rely=.5)
    
    btn_profilepic=Button(frm,text="Profile picture",font=('',15,'bold'),bd=5,width=20,command=picture)
    btn_profilepic.place(relx=.35,rely=.7)
    
    
def searchpool_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='brown')
    frm.place(x=300,y=200,relwidth=.65,relheight=.55)
    
    def logout(event):
        frm.destroy()
        home_frame()
        
    def back(event):
        frm.destroy()
        login_frame()
    
    def searchpool_db(event):
        src=e_src.get().upper()
        dest=e_dest.get().upper()
        
        try:
            con=sqlite3.connect(database="carpool.sqlite")
            cursor=con.cursor()
            cursor.execute("select * from cars where src=? and dest=?",(src,dest))
            pools=cursor.fetchall()
            con.close()
            if(len(pools)==0):
                messagebox.showerror("Pool","Pool does not exist")
            else:
                con=sqlite3.connect(database="carpool.sqlite")
                cursor=con.cursor()
                st=ScrolledText(frm,width=115,height=18,font=('Arial',10,'bold','underline'))
                st.place(x=80,y=120)
                st.insert("end","Username\t\tCar Model\t\tRegno\t\tSeats\t\tFueltype\t\tMob\t\tEmail")
                
                for pool in pools:
                    cursor.execute("select mobile,email from users where username=?",(pool[0],))
                    m,e=cursor.fetchone()
                    st.insert("end",f"\n\n{pool[0]}\t\t{pool[4]}\t\t{pool[3]}\t\t{pool[5]}\t\t{pool[6]}\t\t{m}\t\t{e}","clr")
                    st.tag_config("clr",font=('',10),foreground='blue')
                st.configure(state="disabled")
                con.close()
        except Exception as e:
            messagebox.showerror("Pool",str(e))
        
    lbl_wel=Label(frm,text=f"Welcome,{loginuser_row[0]}",font=('',15,'bold'),fg='green')
    lbl_wel.place(x=0,y=0)
    
    btn_logout=Label(frm,image=imgtk5)
    btn_logout.place(relx=.86,rely=0)
    btn_logout.bind("<Button>",logout)
    
    btn_back=Label(frm,image=imgtk8)
    btn_back.place(relx=0,rely=.1)
    btn_back.bind("<Button>",back)
    
    lbl_src=Label(frm,text="Source",font=('',15,'bold'),fg='blue')
    lbl_src.place(relx=.2,rely=.1)
   
    e_src=Entry(frm,font=('',15),bd=3,width=10)
    e_src.focus()
    e_src.place(relx=.28,rely=.1)
    
    lbl_dest=Label(frm,text="Destination",font=('',15,'bold'),fg='blue')
    lbl_dest.place(relx=.44,rely=.1)
   
    e_dest=Entry(frm,font=('',15),bd=3,width=10)
    e_dest.place(relx=.56,rely=.1)
    
    btn_search=Label(frm,image=imgtk9)
    btn_search.place(relx=.34,rely=.17)
    btn_search.bind("<Button>",searchpool_db)
    

def createpool_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='brown')
    frm.place(x=300,y=200,relwidth=.65,relheight=.55)
    
    def logout(event):
        frm.destroy()
        home_frame()
        
    def back(event):
        frm.destroy()
        login_frame()
     
    def createpool_db(event):
        src=e_src.get()
        dest=e_dest.get()
        model=e_model.get()
        seat=cb_seat.get()
        regno=e_regno.get().replace(" ","")
        fueltype=cb_fueltype.get()
        
        try:
                con=sqlite3.connect(database="carpool.sqlite")
                cursor=con.cursor()
                cursor.execute("insert into cars values(?,?,?,?,?,?,?)",(loginuser_row[0],src.upper(),dest.upper(),regno.upper(),model.upper(),seat,fueltype.upper()))
                con.commit()
                con.close()
                messagebox.showinfo("Create Pool","Pool Created Successfully")
                frm.destroy()
                login_frame()
        except Exception as e:
                messagebox.showerror("Registration","This car already exists in Pool!")
        
    lbl_wel=Label(frm,text=f"Welcome,{loginuser_row[0]}",font=('',15,'bold'),fg='green')
    lbl_wel.place(x=0,y=0)
    
    btn_logout=Label(frm,image=imgtk5)
    btn_logout.place(relx=.86,rely=0)
    btn_logout.bind("<Button>",logout)
    
    btn_back=Label(frm,image=imgtk8)
    btn_back.place(relx=0,rely=.1)
    btn_back.bind("<Button>",back)
    
    lbl_src=Label(frm,text="Source",font=('',15,'bold'),fg='blue')
    lbl_src.place(relx=.2,rely=.15)
   
    e_src=Entry(frm,font=('',15),bd=3,width=12)
    e_src.focus()
    e_src.place(relx=.32,rely=.15)
    
    lbl_dest=Label(frm,text="Destination",font=('',15,'bold'),fg='blue')
    lbl_dest.place(relx=.5,rely=.15)
   
    e_dest=Entry(frm,font=('',15),bd=3,width=12)
    e_dest.place(relx=.62,rely=.15)
        
    lbl_model=Label(frm,text="Car Model",font=('',15,'bold'),fg='blue')
    lbl_model.place(relx=.2,rely=.3)
    
    e_model=Entry(frm,font=('',15),bd=3,width=12)
    e_model.place(relx=.32,rely=.3)
    
    lbl_seat=Label(frm,text="Seats",font=('',15,'bold'),fg='blue')
    lbl_seat.place(relx=.5,rely=.3)
    
    cb_seat=Combobox(frm,values=[2,3,4,5,6,7],font=('',12,'bold'))
    cb_seat.current(3)
    cb_seat.place(relx=.62,rely=.3)
    
    lbl_regno=Label(frm,text="Car Regno",font=('',15,'bold'),fg='blue')
    lbl_regno.place(relx=.2,rely=.45)
    
    e_regno=Entry(frm,font=('',15),bd=3,width=12)
    e_regno.place(relx=.32,rely=.45)
    
    lbl_fueltype=Label(frm,text="Fuel Type",font=('',15,'bold'),fg='blue')
    lbl_fueltype.place(relx=.5,rely=.45)
    
    cb_fueltype=Combobox(frm,values=['Petrol','Diesel','Petrol+CNG','Petrol+LPG','Electric'],font=('',12,'bold'))
    cb_fueltype.current(0)
    cb_fueltype.place(relx=.62,rely=.45)
    
    btn_submit=Label(frm,image=imgtk10)
    btn_submit.place(relx=.35,rely=.7)
    btn_submit.bind("<Button>",createpool_db)
    
    btn_reset=Label(frm,image=imgtk4)
    btn_reset.place(relx=.5,rely=.7)
    

def updateprofile_frame():
    frm=Frame(win,highlightthickness=3,highlightbackground='brown')
    frm.place(x=400,y=200,relwidth=.5,relheight=.55)
    def logout(event):
        frm.destroy()
        home_frame()
        
    def back(event):
        frm.destroy()
        login_frame()
        
    def update_todb(event):
        u=e_user.get()
        p=e_pass.get()
        m=e_mob.get()
        e=e_email.get()
        
        con=sqlite3.connect(database="carpool.sqlite")
        cursor=con.cursor()
        cursor.execute("update users set password=?,mobile=?,email=? where username=?",(p,m,e,u))
        con.commit()
        con.close()
        messagebox.showinfo("Update Profile","Record updated")
        frm.destroy()
        login_frame()
    
    lbl_user=Label(frm,text="Username",font=('',20,'bold'))
    lbl_pass=Label(frm,text="Password",font=('',20,'bold'))
    lbl_mob=Label(frm,text="Mobile",font=('',20,'bold'))
    lbl_email=Label(frm,text="Email",font=('',20,'bold'))
    
    e_user=Entry(frm,font=('',20,'bold'),bd=5)
    e_user.focus()
    e_pass=Entry(frm,font=('',20,'bold'),bd=5,show="*")
    e_mob=Entry(frm,font=('',20,'bold'),bd=5)
    e_email=Entry(frm,font=('',20,'bold'),bd=5)
        
    lbl_user.place(x=150,y=50)
    e_user.place(x=320,y=50)
    lbl_pass.place(x=150,y=130)
    e_pass.place(x=320,y=130)
    lbl_mob.place(x=150,y=210)
    e_mob.place(x=320,y=210)
    lbl_email.place(x=150,y=290)
    e_email.place(x=320,y=290)

    btn_update=Label(frm,image=imgtk11)
    btn_update.place(x=250,y=370)
    btn_update.bind("<Button>",update_todb)
    
    btn_reset=Label(frm,image=imgtk4)
    btn_reset.place(x=420,y=370)

    lbl_wel=Label(frm,text=f"Welcome,{loginuser_row[0]}",font=('',15,'bold'),fg='green')
    lbl_wel.place(x=0,y=0)
    
    btn_logout=Label(frm,image=imgtk5)
    btn_logout.place(relx=.815,rely=0)
    btn_logout.bind("<Button>",logout)
    
    btn_back=Label(frm,image=imgtk8)
    btn_back.place(relx=0,rely=.1)
    btn_back.bind("<Button>",back)
    
    con=sqlite3.connect(database="carpool.sqlite")
    cursor=con.cursor()
    cursor.execute("select mobile,email,password from users where username=?",(loginuser_row[0],))
    row=cursor.fetchone()
    e_user.configure(state="normal")
    e_user.delete(0,"end")
    e_user.insert(0,loginuser_row[0])
    e_user.configure(state="disabled")
    
    e_pass.delete(0,"end")
    e_pass.insert(0,row[2])
    
    e_mob.delete(0,"end")
    e_mob.insert(0,row[0])
    
    e_email.delete(0,"end")
    e_email.insert(0,row[1])
    con.close()
    
home_frame()
win.mainloop()


# In[ ]:




