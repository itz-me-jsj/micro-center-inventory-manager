from customtkinter import *
from tkinter import ttk
from PIL import Image
from CTkMessagebox import CTkMessagebox
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
set_appearance_mode("dark")

set_default_color_theme("green")
app=CTk()
y=1200
x=800
sw=app.winfo_screenwidth()
sh=app.winfo_screenheight()
q=(sw-y)//2
z=(sh-x)//2
app.geometry(f"{y}x{x}+{q+33}+{z-11}")
app.title("Micro Center")
app.resizable(False,False)
role=""
pg=IntVar()
no=25
app.tk.call('source','forest-dark.tcl')
style=ttk.Style()
style.theme_use('forest-dark')

#----------------------------------------Functions-----------------------------------------
def Change_page(page,new):                  # Used to change pages
        page.pack_forget()
        new.pack(fill="both",expand="True")

def start():                                # Used to start the progress bar    
    pg_bar.set(0)
    progress=1/no
    step=0
    for i in range(no):
        for j in range(1900000):
            pass
        step=step+progress
        pg_bar.set(step)
        pg_bar.update_idletasks()
    Change_page(page1,lg)

def login_Page(r):                          # Used to change from page 1 to login page
    but1.configure(anchor="w",compound="left")
    but2.configure(anchor="w",compound="left")
    but1.configure(state="disabled")
    but2.configure(state="disabled")
    global role
    role=r
    lab1.configure(text=role+" Login")
    label2.configure(text="The "+role+" Dashboard")
    start()

def check():                                # Used to check for password and username
        username =entry1.get()
        password =entry2.get()
        if role=="Admin":
            if username in au and password in apas:
                Change_page(lg,page2)
            elif len(username)==0 and len(password)==0:
                CTkMessagebox(title="Error", message="Username And Password Can't Be empty", 
                              icon="cancel", font=("monospace", 15, "bold"), text_color="white",
                              width=350,button_color="#03773d",button_hover_color="#2a8c56",
                              wraplength=300,sound=True,master=lg)
            elif len(username)==0:
                CTkMessagebox(title="Error", message="Username Can't Be Empty", 
                              icon="cancel", font=("monospace", 15, "bold"), text_color="white",
                              width=350,button_color="#03773d",button_hover_color="#2a8c56",
                              wraplength=300,sound=True,master=lg)
            elif len(password)==0:    
                CTkMessagebox(title="Error", message="Password Can't Be Empty",
                              icon="cancel", font=("monospace", 15, "bold"), text_color="white",
                              width=350,button_color="#03773d",button_hover_color="#2a8c56",
                              wraplength=300,sound=True,master=lg)
            else:
                CTkMessagebox(title="Error", message="Username Or Password Is Incorrect",
                              icon="cancel", font=("monospace", 15, "bold"), text_color="white",
                              wraplength=300,button_color="#03773d",button_hover_color="#2a8c56",
                              sound=True,master=lg)
            
        else:
            if username in eu and password in epas:
                Change_page(lg,page2)
            elif len(username)==0 and len(password)==0:
                CTkMessagebox(title="Error", message="Username Or Password Can't Be Empty",
                              icon="cancel", font=("monospace", 15, "bold"), text_color="white",
                              wraplength=300,button_color="#03773d",button_hover_color="#2a8c56",
                              sound=True,master=lg)
            elif len(username)==0:
                CTkMessagebox(title="Error", message="Username Can't Be Empty", 
                          icon="cancel", font=("monospace", 15, "bold"), text_color="white",
                          width=300,button_color="#03773d",button_hover_color="#2a8c56",
                          wraplength=300,sound=True,master=lg)
            elif len(password)==0:    
                CTkMessagebox(title="Error", message="Password Can't Be Empty",
                              icon="cancel", font=("monospace", 15, "bold"), text_color="white",
                              width=300,button_color="#03773d",button_hover_color="#2a8c56",
                              wraplength=300,sound=True,master=lg)
            else:
                CTkMessagebox(title="Error", message="Username Or Password Is Incorrect",
                              icon="cancel", font=("monospace", 15, "bold"), text_color="white",
                              wraplength=300,button_color="#03773d",button_hover_color="#2a8c56",
                              sound=True,master=lg)

def show_password():                        # Used to show password
        entry2.configure(show="")
        show_password_btn.configure(command=hide_password)

def hide_password():                        # Used to hide password
        entry2.configure(show="*")
        show_password_btn.configure(command=show_password)

def change_color(b1,b2,b3,b4,b5):           # Used to change the button colors in the side frame
    b1.configure(fg_color="#202020",hover_color="#202020")
    b2.configure(fg_color="transparent")
    b3.configure(fg_color="transparent")
    b4.configure(fg_color="transparent")
    b5.configure(fg_color="transparent")

def Change_table(t1,t2,t3,b1,b2,b3,b4,b5):  # Used to Change the table
    t1.pack_forget()
    t2.pack(expand=True, fill="both")
    if t3=="st_table":
        scroll.configure(command=st_table.yview)
        scrollx.configure(command=st_table.xview)
    else:
        scroll.configure(command=ord_table.yview)
        scrollx.configure(command=ord_table.xview)
    change_color(b1,b2,b3,b4,b5)

    if b1==but3:
        sr_img.configure(command=lambda:search_values("st_table"))
        option1.configure(values=parts[0])
        entry3.delete(0,len(entry3.get()))
        reset_but()
        option1.set("")
        
    if b1==but4:
        sr_img.configure(command=lambda:search_values("ord_table"))
        option1.configure(values=repairs[0])
        entry3.delete(0,len(entry3.get()))
        reset_but()
        option1.set("")

def add_menu():                             # Used to load the add menu
    global a
    if up_window is not None or del_window is not None:
        if up_window is not None:
            CTkMessagebox(title="Error",message="Close Update Menu Before Opening Add Menu",text_color="#ffffff",
                          font=("monospace", 15, "bold"),width=350,icon="cancel",
                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                          sound=True,wraplength=300,master=main_frame)
            return
        
        else:
            CTkMessagebox(title="Error",message="Close Delete Menu Before Opening Add Menu",text_color="#ffffff",
                          font=("monospace", 15, "bold"),width=350,icon="cancel",
                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                          sound=True,wraplength=300,master=main_frame)
            return
        
    else:
        main_frame.place_forget()
        a=1
        add_frame.place(relx=0.22,rely=0.0,relwidth=0.78, relheight=1.0)
        but3.configure(fg_color="transparent",hover_color="#2a8c56",command=None)
        but4.configure(fg_color="transparent",hover_color="#2a8c56",command=None)
        but5.configure(fg_color="transparent",hover_color="#2a8c56")
        but6.configure(fg_color="transparent",hover_color="#2a8c56")
        but7.configure(fg_color="transparent",hover_color="#2a8c56")

def exit_add():                             # Used to exit the add menu
    reset_but()
    update_label("Stock")
    global a
    a=None                    # Used to change to the main frame
    add_frame.place_forget()
    page2.pack(fill="both",expand=True)
    main_frame.place(relx=0.22,rely=0.0,relwidth=0.78, relheight=1.0)
    but3.configure(fg_color="#202020",hover_color="#202020",
                   command=lambda:Change_table(ord_table,st_table,"st_table",but3,but4,but5,but6,but7))
    but4.configure(command=lambda:Change_table(st_table,ord_table,"ord_table",but4,but3,but5,but6,but7))
    ord_table.pack_forget()
    st_table.pack(fill="both",expand=True)
    scroll.configure(command=st_table.yview)
    scrollx.configure(command=st_table.xview)

def update_label(c):                        # Used to change the label of the Id Entry 
    global p
    if c=="Stock":
        add_lab3.configure(text="Part ID")
        add_lab4.configure(text="Part Name")
        add_lab5.configure(text="Manufacturer")
        add_lab6.configure(text="Compatibility")
        add_op2.configure(values=p)
        add_lab7.place(relx=0.053,rely=0.6,anchor="w")
        add_lab8.place(relx=0.5,rely=0.6,anchor="w")
        add_lab11.configure(text="Price")
        add_rb1.place(relx=0.053,rely=0.7)
        add_rb2.place(relx=0.053,rely=0.8)
        add_rb3.place(relx=0.5,rely=0.7)
        add_rb4.place(relx=0.5,rely=0.8)
        add_rb5.place_forget()
        add_rb6.place_forget()
        add_rb7.place_forget()
        add_rb8.place_forget()
        add_rb9.place_forget()
        add_rb10.place_forget()
        reset_but()
        add_op1.set("Stock")
    
    else:
        add_lab3.configure(text="Customer ID")
        add_lab4.configure(text="Customer Name")
        add_lab5.configure(text="Part ID")
        add_lab6.configure(text="Part Used")
        add_op2.configure(values=k)
        add_lab11.configure(text="Fee")
        add_lab13.place(relx=0.053,rely=0.6,anchor="w")
        add_lab14.place(relx=0.5,rely=0.6,anchor="w")
        add_rb5.place(relx=0.053,rely=0.68)
        add_rb6.place(relx=0.053,rely=0.76)
        add_rb7.place(relx=0.053,rely=0.84)
        add_rb8.place(relx=0.5,rely=0.68)
        add_rb9.place(relx=0.5,rely=0.76)
        add_rb10.place(relx=0.5,rely=0.84)
        add_rb1.place_forget()
        add_rb2.place_forget()
        add_rb3.place_forget()
        add_rb4.place_forget()
        reset_but()
        add_op1.set("Orders")

def Change_Label_no(q):                     # Used to change the label of both price and quantity
    global n
    global m
    if q=="increase1":
        n+=1
    elif q=="decrease1"and n>0:
        n-=1  
    elif q=="increase2":
        m+=500  
    elif q=="decrease2"and m>0:
        m-=500
    add_lab10.configure(text=str(n))
    add_lab12.configure(text=str(m))

def change_label(a):                        # Used to change the labels in the update menu
        if a=="Stock":
            up_lab3.configure(text="Part ID")
            up_lab5.configure(text="Part Name")
            up_op2.configure(values=s)
            reset_but()
            up_op1.set("Stock")
        elif a=="Orders":
            up_lab3.configure(text="Customer ID")
            up_lab5.configure(text="Customer Name")
            up_op2.configure(values=o)
            reset_but()
            up_op1.set("Orders")
        elif a in s:
            up_lab5.configure(text=a)
        elif  a in o:
            up_lab5.configure(text=a)

def change_label2(a):                       # Used to change the labels in the delete menu
        if a=="Stock":
            del_lab3.configure(text="Part ID")
            del_op2.configure(values=s)
            reset_but()
            del_op1.set("Stock")
        elif a=="Orders":
            del_lab3.configure(text="Customer ID")
            del_op2.configure(values=o)
            reset_but()
            del_op1.set("Orders")

def Click_Unclick(c):                       # Used to change the select/deselect the ratiobutton in the add menu
    global con,use,rep,pog,derb
    if c=="rb1":                        # deselect the unselected buttons
        add_rb2.deselect()
        con="New"
    elif c=="rb2":
        add_rb1.deselect()
        con="Used"
    elif c=="rb3":
        add_rb4.deselect()
        use="Yes"
    elif c=="rb4":
        add_rb3.deselect()
        use="No"
    elif c=="rb5":
        add_rb6.deselect()
        add_rb7.deselect()
        rep="PC"
    elif c=="rb6":
        add_rb5.deselect()
        add_rb7.deselect()
        rep="Laptop"
    elif c=="rb7":
        add_rb6.deselect()
        add_rb5.deselect()
        rep="Server"
    elif c=="rb8":
        add_rb9.deselect()
        add_rb10.deselect()
        pog="Pending"
    elif c=="rb9":
        add_rb8.deselect()
        add_rb10.deselect()
        pog="In Progress"
    elif c=="rb10":
        add_rb8.deselect()
        add_rb9.deselect()
        pog="Completed"
    elif c=="d1":
        del_rb2.deselect()
        del_lab4.place(relx=0.51,rely=0.45,anchor="w")
        del_op2.place(relx=0.501,rely=0.55,anchor="w")
        derb="Single Cell"
    elif c=="d2":
        del_rb1.deselect()
        del_lab4.place_forget()
        del_op2.place_forget()
        derb="Entire Row"

def update_window():                        # Used to load the update window
    global up_window
    if a==1:
        CTkMessagebox(title="Error",message="Close Add Menu Before Opening Update Menu",text_color="#ffffff",
                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                      sound=True,wraplength=300,master=main_frame)
        return
    
    elif del_window is not None:
       CTkMessagebox(title="Error",message="Close Delete Menu Before Opening Update Menu",text_color="#ffffff",
                     font=("monospace", 15, "bold"),width=350,icon="cancel",
                     button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                     sound=True,wraplength=300,master=main_frame)
       return
    
    elif up_window is None:
        up_window=CTkToplevel(app, fg_color="#1a1a1a")
        w=500
        h=400
        app_x=app.winfo_x()
        app_y=app.winfo_y()
        app_w=app.winfo_width()
        app_h=app.winfo_height()
        x=app_x+(app_w // 2)-(w // 2)
        y=app_y+(app_h // 2)-(h // 2)
        up_window.geometry("{}x{}+{}+{}".format(w,h,x,y))
        up_window.title("Update Window")
        up_window.attributes("-topmost", True)
        change_color(but5,but3,but4,but6,but7)
        up_window.protocol("WM_DELETE_WINDOW",close_up_window)
        up_window.resizable(False,False)
        up_menu()

def delete_window():                        # Used to load the delete window
    global del_window
    if a==1:
        CTkMessagebox(title="Error",message="Close Add Menu Before Opening Delete Menu",text_color="#ffffff",
                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                      sound=True,wraplength=300,master=main_frame)
        return
    
    elif up_window is not None:
        CTkMessagebox(title="Error",message="Close Update Menu Before Opening Delete Menu",text_color="#ffffff",
                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                      sound=True,wraplength=300,master=main_frame)
        return
    
    elif del_window is None:
        del_window=CTkToplevel(app, fg_color="#1a1a1a")
        w=450
        h=500
        app_x=app.winfo_x()
        app_y=app.winfo_y()
        app_w=app.winfo_width()
        app_h=app.winfo_height()
        x=app_x+(app_w // 2)-(w // 2)
        y=app_y+(app_h // 2)-(h // 2)
        del_window.geometry("{}x{}+{}+{}".format(w,h,x,y))
        del_window.title("Delete Window")
        del_window.attributes("-topmost", True)
        change_color(but6,but3,but4,but5,but7)
        del_window.protocol("WM_DELETE_WINDOW",close_up_window)
        del_window.resizable(False,False)
        del_menu()

def close_up_window():                      # Used to close the windows
    global up_window,del_window
    if up_window is not None:
        up_window.destroy()
    elif del_window is not None:
        del_window.destroy()
    up_window=None
    del_window=None

def log_out():                              # Used to close the app
    if page1.winfo_ismapped(): 
        app.destroy()
        return
    
    elif lg.winfo_ismapped():
        msg=CTkMessagebox(title="Warning",message="Are You Sure You Want To Leave",text_color="#ffffff",
                          font=("monospace", 15, "bold"),width=350,icon="warning",master=lg,
                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                          sound=True,wraplength=300,option_1="Yes",option_2="No")
        if msg.get()=="Yes":
            app.destroy()
        return
    
    elif a==1:
        CTkMessagebox(title="Warning",message="Please Close The Creation Menu Before Loging Out",text_color="#ffffff",
                      font=("monospace", 15, "bold"),width=350,icon="warning",
                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                      sound=True,wraplength=300,master=main_frame)
        
    elif up_window is not None:
        CTkMessagebox(title="Warning",message="Please Close The Update Menu Before Loging Out",text_color="#ffffff",
                      font=("monospace", 15, "bold"),width=350,icon="warning",
                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                      sound=True,wraplength=300,master=main_frame)
        
    elif del_window is not None:
        CTkMessagebox(title="Warning",message="Please Close The Delete Menu Before Loging Out",text_color="#ffffff",
                      font=("monospace", 15, "bold"),width=350,icon="warning",
                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                      sound=True,wraplength=300,master=main_frame)
    
    else:
        log=CTkMessagebox(title="Log Out",message="Do You Want To Logout",text_color="#ffffff",
                          font=("monospace", 15, "bold"),option_1="Yes",option_2="No",width=350,
                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                          sound=True,wraplength=300,master=main_frame)
        if log.get()=="Yes":
            app.destroy()

app.protocol("WM_DELETE_WINDOW",log_out)
#----------------------------------------PAGE 1 OF APP-----------------------------------------
page1=CTkFrame(app,fg_color="transparent")
page1.pack(fill="both",expand=True)
bg_img=CTkImage(Image.open("bg.png"),size=(800,800))
ad_img=CTkImage(Image.open("admin.png"),size=(40,40))
emp_img=CTkImage(Image.open("employee.png"),size=(40,40))
i=CTkImage(Image.open("logo.png"),size=(75,75))

leb=CTkButton(page1,image=i,fg_color="#242424",hover_color="#242424",text_color="#03773d",
              text="Micro Center",font=("Arial",35,"bold"),width=100,height=100,)
t='''Welcome To 
Micro Center!'''
paragraph="""This application is designed to help users
manage their computer repair shops more efficiently. Please select your role below to continue."""
lab=CTkLabel(page1,text=t,font=("Arial",61,"bold"),justify="left",text_color="#03773d")
label=CTkLabel(page1,text=paragraph,font=("Arial",20),justify="left",height=70,wraplength=450)
bg_lab=CTkLabel(page1,text="",image=bg_img,height=600,width=800)
leb.place(relx=0.016,rely=0.02)
lab.place(relx=0.3485,rely=0.43,anchor="e")
label.place(relx=0.3445,rely=0.58,anchor="e")   
bg_lab.place(relx=0.36,rely=0.5,anchor="w")

but1=CTkButton(page1,text="  Admin",corner_radius=10,width=207,
               font=("Arial",29,"bold"),height=60,image=ad_img,anchor="w",
               fg_color="#03773d", hover_color="#2a8c56",command=lambda:login_Page("Admin"))
but2=CTkButton(page1,text="Employee",font=("Arial",29,"bold"),
               corner_radius=10,width=200,height=60,image=emp_img,
               fg_color="#03773d",hover_color="#2a8c56",command=lambda:login_Page("Employee"))
but1.place(relx=0.199,rely=0.7,anchor="e")
but2.place(relx=0.39,rely=0.7,anchor="e")

pg_bar=CTkProgressBar(page1,width=1200,height=15,orientation="horizontal",corner_radius=0,
                      variable=pg,progress_color="#03773d")

pg_bar.place(relx=0.0,rely=0.983)

#----------------------------------------Login Page--------------------------------------------
img=CTkImage(Image.open("login.jpg"),size=(1200,800))
ur=CTkImage(Image.open("user.png"),size=(35,35))
lok=CTkImage(Image.open("lock.png"),size=(27,27))

lg=CTkFrame(app,fg_color="transparent")
bg=CTkLabel(lg,text="",image=img,bg_color="transparent")
lg_frame=CTkFrame(bg,width=400,height=500,corner_radius=10,fg_color="#313131")
lab1=CTkLabel(lg_frame,text="Login",font=("Arial",36,"bold"))
bg.pack(fill="both",expand=True)
lg_frame.place(relx=0.5,rely=0.5,anchor="center")
lab1.place(relx=0.5,rely=0.15,anchor="center")

#Username Entry
entry1_frame=CTkFrame(lg_frame,fg_color="#202020",width=350,height=40,corner_radius=7)
ur_lab=CTkLabel(entry1_frame,text="",image=ur)
entry1=CTkEntry(entry1_frame,width=300,height=40,placeholder_text="UserName",font=("Arial", 18),
                fg_color="#202020",border_color="#202020")
entry1_frame.place(relx=0.065,rely=0.32)
ur_lab.place(relx=0.01,rely=0.5,anchor="w")
entry1.place(relx=0.12,rely=0.0,)

#Password Entry
entry2_frame=CTkFrame(lg_frame,fg_color="#202020",width=350,height=40,corner_radius=7)
lok_lab=CTkLabel(entry2_frame,text="",image=lok)
entry2=CTkEntry(entry2_frame,width=300,height=40,placeholder_text="Password",font=("Arial", 18),
                show="*",fg_color="#202020",border_color="#202020")
entry2_frame.place(relx=0.065,rely=0.45)
lok_lab.place(relx=0.015,rely=0.5,anchor="w")
entry2.place(relx=0.12,rely=0.0,)

show_password_btn=CTkCheckBox(lg_frame, text=" Show Password",
                                font=("Arial", 14),command=show_password)
butl=CTkButton(lg_frame,text="Login",font=("Arial",40,"bold"),
               corner_radius=10,width=250,height=60,
               fg_color="#03773d",hover_color="#2a8c56",command=check)
show_password_btn.place(relx=0.065,rely=0.55)
butl.place(relx=0.2,rely=0.7)

#Username/Passwords
au=["A001","A002"]
eu=["E001","E002"]
apas=["admlogin123"]
epas=["emplogin123"]
#----------------------------------------PAGE 2 OF APP-----------------------------------------
page2 = CTkFrame(app, fg_color="#1a1a1a") 
# SideBar
sidebar=CTkFrame(page2,fg_color="#03773d")
sidebar.place(relx=0.0, anchor="nw", relwidth=0.22, relheight=1.0) 
img1=CTkImage(Image.open("logo.png"),size=(150,150))
img2=CTkImage(Image.open("stock button.png"),size=(37,37))
img3=CTkImage(Image.open("order button.png"),size=(37,37))
img4=CTkImage(Image.open("update button.png"),size=(37,37))
img5=CTkImage(Image.open("delete button.png"),size=(37,37))
img6=CTkImage(Image.open("log-out button.png"),size=(37,37))
logo=CTkLabel(sidebar,text="",image=img1,fg_color="transparent")
logo.place(relx=0.21,rely=0.033,anchor="nw")
logo_label=CTkLabel(sidebar,text="Micro Center",fg_color="transparent",font=("Arial",38,"bold"))
logo_label.place(relx=0.4975,rely=0.25,anchor="center")
button_frame=CTkFrame(sidebar,fg_color="transparent")
button_frame.place(relx=0.5,rely=0.57,anchor="center")

parts = [["Part ID", "Part Name", "Manufacturer", "Compatibility", "Quantity", "Price", "Condition", "In Use"]]
repairs = [["Customer ID","Customer Name","Repair Item","Part Used","Part Id","Quantity","Fee","Order Progress"]]
up_window=None 
del_window=None

but3=CTkButton(button_frame,text="Stock",corner_radius=10,width=200,
               font=("Arial",32,"bold"),height=53,fg_color="#202020",image=img2,anchor="w",
               hover_color="#2a8c56",
               command=lambda:Change_table(ord_table,st_table,"st_table",but3,but4,but5,but6,but7))
but4=CTkButton(button_frame,text="Orders",font=("Arial",32,"bold"),image=img3,
               corner_radius=10,width=200,height=53,fg_color="transparent",anchor="w",
               hover_color="#2a8c56",
               command=lambda:Change_table(st_table,ord_table,"ord_table",but4,but3,but5,but6,but7))
but5=CTkButton(button_frame,text="Update",corner_radius=10,width=200,image=img4,
               font=("Arial",32,"bold"),height=53,fg_color="transparent",
               hover_color="#2a8c56",anchor="w",command=lambda:update_window())
but6=CTkButton(button_frame,text="Delete ",font=("Arial",32,"bold"),image=img5,
               corner_radius=10,width=200,height=53,fg_color="transparent",
               hover_color="#2a8c56",anchor="w",command=lambda:delete_window())
but7=CTkButton(button_frame,text="Logout",font=("Arial",32,"bold"),image=img6,
               corner_radius=10,width=200,height=53,fg_color="transparent",
               hover_color="#2a8c56",anchor="w",command=lambda:log_out())
but3.pack(pady=10)
but4.pack(pady=10)
but5.pack(pady=10)
but6.pack(pady=10)
but7.pack(pady=10)

#Main Frame
main_frame=CTkFrame(page2,fg_color="transparent")
main_frame.place(relx=0.22,rely=0.0,relwidth=0.78, relheight=1.0) 

label2 = CTkLabel(main_frame, text='The Admin Dashboard',font=("Arial", 40, "bold"),text_color="#03773d")
buta=CTkButton(main_frame,text="+New",font=("Arial",20,"bold"),
               corner_radius=10,width=90,height=40,fg_color="#03773d",
               hover_color="#2a8c56",command=lambda:add_menu())
label2.place(relx=0.053,rely=0.03,anchor="nw")
buta.place(relx=0.9497,rely=0.0875,anchor="se")

#Dynamic Wiget frame
Dynamic_frame=CTkFrame(main_frame,fg_color="transparent",height=120,width=840)
Dynamic_frame.place(relx=0.051,rely=0.11)
img7=CTkImage(Image.open("stock.png"),size=(65,65))
img8=CTkImage(Image.open("orders.png"),size=(65,65))
img9=CTkImage(Image.open("finished.png"),size=(65,65))

w1=CTkFrame(Dynamic_frame,fg_color="#03773d",height=80,width=250)
w1.place(relx=0.0,rely=0.5,anchor="w")
w1_img=CTkLabel(w1,text="",image=img7,fg_color="transparent")
w1_lab=CTkLabel(w1,text="Stock",font=("Arial",24,"bold"),fg_color="transparent")
w1_lab2=CTkLabel(w1,text="15",font=("Arial",24,"bold"))
w1_img.place(relx=0.18,rely=0.5,anchor="center")
w1_lab.place(relx=0.35,rely=0.1,anchor="nw")
w1_lab2.place(relx=0.35,rely=0.5,anchor="nw")

w2=CTkFrame(Dynamic_frame,fg_color="#03773d",height=80,width=250)
w2.place(relx=0.5,rely=0.5,anchor="center")
w2_img=CTkLabel(w2,text="",image=img8,fg_color="transparent")
w2_lab=CTkLabel(w2,text="Orders",font=("Arial",24,"bold"),fg_color="transparent")
w2_lab2=CTkLabel(w2,text="10",font=("Arial",24,"bold"))
w2_img.place(relx=0.19,rely=0.5,anchor="center")
w2_lab.place(relx=0.37,rely=0.1,anchor="nw")
w2_lab2.place(relx=0.37,rely=0.5,anchor="nw")

w3=CTkFrame(Dynamic_frame,fg_color="#03773d",height=80,width=250)
w3.place(relx=0.851,rely=0.5,anchor="center")
w3_img=CTkLabel(w3,text="",image=img9,fg_color="transparent")
w3_lab=CTkLabel(w3,text="Completed",font=("Arial",24,"bold"),fg_color="transparent")
w3_lab2=CTkLabel(w3,text="20",font=("Arial",24,"bold"))
w3_img.place(relx=0.19,rely=0.5,anchor="center")
w3_lab.place(relx=0.37,rely=0.1,anchor="nw")
w3_lab2.place(relx=0.37,rely=0.5,anchor="nw")

#Search Frame
img10=CTkImage(Image.open("search.png"),size=(25,25))
search_frame=CTkFrame(main_frame,fg_color="#313131",height=60,width=840)
search_frame.place(relx=0.051,rely=0.28)

sr_img=CTkButton(search_frame,image=img10,height=40,width=40,fg_color="#03773d",text="",
                 command=lambda:search_values("st_table"))
entry3=CTkEntry(search_frame,placeholder_text="Search",height=40,width=465,font=("Arial", 18),
                border_color="#03773d",border_width=2.3)
option1=CTkComboBox(search_frame,border_color="#03773d",height=40,width=170,
                    font=("Arial",16),button_color="#03773d",dropdown_fg_color="#313131",state="readonly",
                    values=parts[0])
sr_reset=CTkButton(search_frame,height=40,width=95,text="Reset",font=("Arial",24,"bold"),fg_color="#03773d",
                   command=lambda:reset_but())
sr_img.place(relx=0.048,rely=0.5,anchor="center")
entry3.place(relx=0.36,rely=0.5,anchor="center")
option1.place(relx=0.75,rely=0.5,anchor="center")
sr_reset.place(relx=0.92,rely=0.5,anchor="center")

#Table Frame
table_frame=CTkFrame(main_frame,fg_color="transparent",height=1000,width=840,corner_radius=10)
table_frame.place(relx=0.051,rely=0.399,relheight=0.57,relwidth=0.902)
scroll=CTkScrollbar(table_frame,button_color="#03773d",button_hover_color="#03773d")
scrollx=CTkScrollbar(table_frame,orientation="horizontal",button_color="#03773d",
                     button_hover_color="#03773d")
scroll.pack(side="right",fill="y")
scrollx.pack(side="bottom",fill='x')

#Stock Table
st_table=ttk.Treeview(table_frame,columns=(["Part ID","Part Name","Manufacturer","Compatibility","Quantity",
                                             "Price","Condition","In Use"]),show="headings",height=16,
                                             yscrollcommand=scroll.set,xscrollcommand=scrollx.set)
style.configure("Treeview",rowheight=39,font=("Arial",14),background="#202020",anchor="center")
style.configure("Treeview.Heading",font=("Arial",18,"bold"),background="#202020",)
scroll.configure(command=st_table.yview)
scrollx.configure(command=st_table.xview)

st_table.pack(fill="both",expand=True)
st_table.heading("Part ID",text="Part ID")
st_table.heading("Part Name",text="Part Name")
st_table.heading("Manufacturer",text="Manufacturer")
st_table.heading("Compatibility",text="Compatibility")
st_table.heading("Quantity",text="Quantity")
st_table.heading("Price",text="Price")
st_table.heading("Condition",text="Condition")
st_table.heading("In Use",text="In use")

st_table.column("Part ID",width=120,anchor="center",stretch=False)
st_table.column("Part Name",width=230,anchor="center",stretch=False)
st_table.column("Manufacturer",width=170,anchor="center",stretch=False)
st_table.column("Compatibility",width=180,anchor="center",stretch=False)
st_table.column("Quantity",width=120,anchor="center",stretch=False)
st_table.column("Price",width=120,anchor="center",stretch=False)
st_table.column("Condition",width=140,anchor="center",stretch=False)
st_table.column("In Use",width=120,anchor="center",stretch=False)

#Orders Table
ord_table=ttk.Treeview(table_frame,columns=(["Customer ID","Customer Name","Repair Item","Part Used",
                                             "Part ID","Quantity","Fee","Order Progress",]),
                       show="headings",height=16,yscrollcommand=scroll.set,xscrollcommand=scrollx.set)

ord_table.heading("Customer ID",text="Customer ID")
ord_table.heading("Customer Name",text="Customer Name")
ord_table.heading("Repair Item",text="Repair Item")
ord_table.heading("Part Used",text="Part Used")
ord_table.heading("Part ID",text="Part ID")
ord_table.heading("Quantity",text="Quantity")
ord_table.heading("Fee",text="Fee")
ord_table.heading("Order Progress",text="Order Progress")

ord_table.column("Customer ID",width=190,anchor="center",stretch=False)
ord_table.column("Customer Name",width=190,anchor="center",stretch=False)
ord_table.column("Repair Item",width=178,anchor="center",stretch=False)
ord_table.column("Part Used",width=230,anchor="center",stretch=False)
ord_table.column("Part ID",width=128,anchor="center",stretch=False)
ord_table.column("Quantity",width=100,anchor="center",stretch=False)
ord_table.column("Fee",width=100,anchor="center",stretch=False)
ord_table.column("Order Progress",width=200,anchor="center",stretch=False)

for row in repairs[1:]:
    ord_table.insert("","end",values=row)

#----------------------------------------Add Page--------------------------------------
add_frame=CTkFrame(page2,fg_color="transparent")
a=None
add_lab1=CTkLabel(add_frame, text='The Creation Panel',font=("Arial", 45, "bold"),text_color="#03773d")
add_lab1.place(relx=0.053,rely=0.03,anchor="nw")

#Table Widget
l=["Stock","Orders"]
add_lab2=CTkLabel(add_frame,text="Table",font=("Arial",34,"bold"),text_color="#03773d")
add_op1=CTkComboBox(add_frame,values=l,height=35,width=150,font=("Arial",18),
                   dropdown_fg_color="#343638",command=update_label,state="readonly")
add_lab2.place(relx=0.053,rely=0.2,anchor="w")
add_op1.place(relx=0.053,rely=0.26,anchor="w")

#Part ID/Customer ID Widget
add_lab3=CTkLabel(add_frame,text="Part ID",font=("Arial",34,"bold"),text_color="#03773d")
add_entry1=CTkEntry(add_frame,height=35,width=300,font=("Arial",18,"bold"))
add_lab3.place(relx=0.3,rely=0.2,anchor="w")
add_entry1.place(relx=0.3,rely=0.26,anchor="w")

col_frame=CTkFrame(add_frame,fg_color="transparent")
col_frame.place(relx=0,rely=0.32,relwidth=1,relheight=0.6)

#Part Name/Customer Name Widget
add_lab4=CTkLabel(col_frame,text="Part Name",font=("Arial",34,"bold"),text_color="#03773d")
add_entry2=CTkEntry(col_frame,height=35,width=300,font=("Arial",18,"bold"))
add_lab4.place(relx=0.053,rely=0.05,anchor="w")
add_entry2.place(relx=0.053,rely=0.15,anchor="w")

#Manufacture/Part ID Widget
add_lab5=CTkLabel(col_frame,text="Manufacturer",font=("Arial",34,"bold"),text_color="#03773d")
add_entry3=CTkEntry(col_frame,height=35,width=300,font=("Arial",18,"bold"))
add_entry3.bind("<KeyRelease>",lambda event:order_part_id())
add_lab5.place(relx=0.5,rely=0.05,anchor="w")
add_entry3.place(relx=0.5,rely=0.15,anchor="w")

#Compatibility/Part Used Widget
p=["Intel","Amd","Universal"]
k=[]
add_lab6=CTkLabel(col_frame,text="Compatibility",font=("Arial",34,"bold"),text_color="#03773d")
add_op2=CTkComboBox(col_frame,values=p,height=35,width=250,font=("Arial",18),
                   dropdown_fg_color="#343638",state="readonly",command=lambda v:order_part_used(v))
add_lab6.place(relx=0.053,rely=0.3,anchor="w")
add_op2.place(relx=0.053,rely=0.37)

#Condition Widget
con=""
add_lab7=CTkLabel(col_frame,text="Condition",font=("Arial",34,"bold"),text_color="#03773d")
add_rb1=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="New",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb1"))
add_rb2=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="Used",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb2"))
add_lab7.place(relx=0.053,rely=0.6,anchor="w")
add_rb1.place(relx=0.053,rely=0.7)
add_rb2.place(relx=0.053,rely=0.8)

#In use Widget
use=""
add_lab8=CTkLabel(col_frame,text="In use",font=("Arial",34,"bold"),text_color="#03773d")
add_rb3=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="Yes",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb3"))
add_rb4=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="No",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb4"))
add_lab8.place(relx=0.5,rely=0.6,anchor="w")
add_rb3.place(relx=0.5,rely=0.7)
add_rb4.place(relx=0.5,rely=0.8)

#Quantity Widget
n=1 
add_lab9=CTkLabel(col_frame,text="Quantity",font=("Arial",34,"bold"),text_color="#03773d")
q_frame=CTkFrame(col_frame,fg_color="transparent",width=125,height=40)
add_lab9.place(relx=0.5,rely=0.3,anchor="w")
q_frame.place(relx=0.5,rely=0.45,anchor="w")
q_but1=CTkButton(q_frame,text="+",font=("Arial",24,"bold"),text_color="#ffffff",width=30,height=30,
                 fg_color="#03773d",hover_color="#2a8c56",command=lambda:Change_Label_no("increase1"))
q_but2=CTkButton(q_frame,text="-",font=("Arial",24,"bold"),text_color="#ffffff",width=30,height=30,
                 fg_color="#03773d",hover_color="#2a8c56",command=lambda:Change_Label_no("decrease1"))
add_lab10=CTkLabel(q_frame,text="1",font=("Arial",28,"bold"),text_color="#ffffff")

q_but1.place(relx=0.0,rely=0.1)
add_lab10.place(relx=0.5,rely=0.5,anchor="center")
q_but2.place(relx=0.757,rely=0.1)

#Price/Fee Widget
m=500   
add_lab11=CTkLabel(col_frame,text="Price",font=("Arial",34,"bold"),text_color="#03773d")
p_frame=CTkFrame(col_frame,fg_color="transparent",width=155,height=40)
add_lab11.place(relx=0.782,rely=0.3,anchor="w")
p_frame.place(relx=0.782,rely=0.45,anchor="w")
p_but1=CTkButton(p_frame,text="+",font=("Arial",24,"bold"),text_color="#ffffff",width=30,height=30,
                 fg_color="#03773d",hover_color="#2a8c56",command=lambda:Change_Label_no("increase2"))
p_but2=CTkButton(p_frame,text="-",font=("Arial",24,"bold"),text_color="#ffffff",width=30,height=30,
                 fg_color="#03773d",hover_color="#2a8c56",command=lambda:Change_Label_no("decrease2"))
add_lab12=CTkLabel(p_frame,text="500",font=("Arial",28,"bold"),text_color="#ffffff")

p_but1.place(relx=0.0,rely=0.1)
add_lab12.place(relx=0.5,rely=0.5,anchor="center")
p_but2.place(relx=0.8,rely=0.1)

#Repair Item
rep=""
add_lab13=CTkLabel(col_frame,text="Repair Item",font=("Arial",34,"bold"),text_color="#03773d")
add_rb5=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="PC",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb5"))
add_rb6=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="Laptop",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb6"))
add_rb7=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="Server",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb7"))

#Order Progress Widget
pog=""
add_lab14=CTkLabel(col_frame,text="Order Progress",font=("Arial",34,"bold"),text_color="#03773d")
add_rb8=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="Pending",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb8"))
add_rb9=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="In Progress",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb9"))
add_rb10=CTkRadioButton(col_frame,radiobutton_height=30,radiobutton_width=30,
                       text="Complete",font=("Arial",24),text_color="#ffffff",
                       fg_color="#03773d",border_width_checked=5,
                       command=lambda:Click_Unclick("rb10"))

#Add/Reset/Exit Button
abut=CTkButton(add_frame,text="Add",height=30,width=200,font=("Arial",45,"bold"),fg_color="#03773d",
               hover_color="#2a8c56",command=lambda:add_but())
rbut=CTkButton(add_frame,text="Reset",height=30,width=200,font=("Arial",45,"bold"),fg_color="transparent",
               border_color="#03773d",border_width=3,command=lambda:reset_but())
ebut=CTkButton(add_frame,text="Exit",height=30,width=200,font=("Arial",45,"bold"),fg_color="#03773d",
               hover_color="#2a8c56",command=lambda:exit_add())
rbut.place(relx=0.5,rely=0.934,anchor="center")
abut.place(relx=0.053,rely=0.9,anchor="nw")
ebut.place(relx=0.947,rely=0.936,anchor="e")

#----------------------------------------Update Window-----------------------------------------
up_lab3=None
up_lab5=None
up_op1=None
up_op2=None
up_entry1=None
up_entry2=None
s=parts[0][1:]
o=repairs[0][1:]

def up_menu():                          # The update window
    global up_lab3,up_op1,up_lab5,up_op2,up_entry1,up_entry2
    up_frame=CTkFrame(up_window,fg_color="#1a1a1a")
    up_frame.pack(fill="both",expand=True)
    up_lab1=CTkLabel(up_frame,text="The Update Menu",font=("Arial",34,"bold"),text_color="#03773d")
    up_lab1.place(relx=0.051,rely=0.1,anchor="w")

    #Table Widget
    l=["Stock","Orders"]
    up_lab2=CTkLabel(up_frame,text="Table",font=("Arial",26,"bold"),text_color="#03773d")
    up_op1=CTkComboBox(up_frame,values=l,height=35,width=175,font=("Arial",18),
                   dropdown_fg_color="#343638",command=change_label,state="readonly")
    up_lab2.place(relx=0.051,rely=0.3,anchor="w")
    up_op1.place(relx=0.051,rely=0.4,anchor="w")

    #Part ID Widget
    up_lab3=CTkLabel(up_frame,text="Part ID",font=("Arial",26,"bold"),text_color="#03773d")
    up_entry1=CTkEntry(up_frame,height=35,width=250,font=("Arial",18,"bold"))
    up_lab3.place(relx=0.45,rely=0.3,anchor="w")
    up_entry1.place(relx=0.45,rely=0.4,anchor="w")

    #Column Name Widget
    up_lab4=CTkLabel(up_frame,text="Column",font=("Arial",26,"bold"),text_color="#03773d")
    up_op2=CTkComboBox(up_frame,values=s,height=35,width=175,font=("Arial",18),
                   dropdown_fg_color="#343638",command=change_label,state="readonly")
    up_lab4.place(relx=0.051,rely=0.55,anchor="w")
    up_op2.place(relx=0.051,rely=0.65,anchor="w")

    #Column Entry Widget
    up_lab5=CTkLabel(up_frame,text="Part Name",font=("Arial",26,"bold"),text_color="#03773d")
    up_entry2=CTkEntry(up_frame,height=35,width=250,font=("Arial",18,"bold"))
    up_lab5.place(relx=0.45,rely=0.55,anchor="w")
    up_entry2.place(relx=0.45,rely=0.65,anchor="w")

    #Update/Reset/Exit Button
    abut2=CTkButton(up_frame,text="Update",height=20,width=131,font=("Arial",34,"bold"),fg_color="#03773d",
               hover_color="#2a8c56",command=lambda:update_but())
    rbut2=CTkButton(up_frame,text="Reset",height=20,width=130,font=("Arial",34,"bold"),fg_color="transparent",
               border_color="#03773d",border_width=3,command=lambda:reset_but())
    ebut2=CTkButton(up_frame,text="Exit",height=20,width=130,font=("Arial",34,"bold"),fg_color="#03773d",
               hover_color="#2a8c56",command=lambda:close_up_window())
    abut2.place(relx=0.051,rely=0.9,anchor="w")
    rbut2.place(relx=0.5,rely=0.9,anchor="center")
    ebut2.place(relx=0.95,rely=0.9,anchor="e")

#----------------------------------------Delete Window------------------------------------------
del_lab3=None
del_op1=None
del_lab4=None
del_entry1=None
del_op2=None
del_rb1=None
del_rb2=None
derb=""

def del_menu():                         # The delete window
    global del_lab3,del_lab4,del_op1,del_op2,del_rb1,del_rb2,del_entry1
    del_frame=CTkFrame(del_window,fg_color="#1a1a1a")
    del_frame.pack(fill="both",expand=True)
    del_lab1=CTkLabel(del_frame,text="The Delete Menu",font=("Arial",34,"bold"),text_color="#03773d")
    del_lab1.place(relx=0.051,rely=0.1,anchor="w")

    #Table Widget
    l=["Stock","Orders"]
    del_lab2=CTkLabel(del_frame,text="Table",font=("Arial",26,"bold"),text_color="#03773d")
    del_op1=CTkComboBox(del_frame,values=l,height=35,width=175,font=("Arial",18),
                   dropdown_fg_color="#343638",command=change_label2,state="readonly")
    del_lab2.place(relx=0.051,rely=0.25,anchor="w")
    del_op1.place(relx=0.053,rely=0.35,anchor="w")

    #Part ID/Customer ID Widget
    del_lab3=CTkLabel(del_frame,text="Part ID",font=("Arial",26,"bold"),text_color="#03773d")
    del_entry1=CTkEntry(del_frame,height=35,width=200,font=("Arial",18,"bold"))
    del_lab3.place(relx=0.51,rely=0.25,anchor="w")
    del_entry1.place(relx=0.501,rely=0.35,anchor="w")

    #Column Widget
    del_lab4=CTkLabel(del_frame,text="Column",font=("Arial",26,"bold"),text_color="#03773d")
    del_op2=CTkComboBox(del_frame,values=s,height=35,width=175,font=("Arial",18),
                   dropdown_fg_color="#343638",command=change_label2,state="readonly")
    
    #Delete Method Widget
    del_lab6=CTkLabel(del_frame,text="Delete Method",font=("Arila",26,"bold"),text_color="#03773d")
    del_rb1=CTkRadioButton(del_frame,radiobutton_height=30,radiobutton_width=30,text="Single Cell",
                           font=("Arial",22,"bold"),text_color="#ffffff",fg_color="#03773d",
                           border_width_checked=5,command=lambda:Click_Unclick("d1"))
    del_rb2=CTkRadioButton(del_frame,radiobutton_height=30,radiobutton_width=30,text="Entire Row",
                           font=("Arial",22,"bold"),text_color="#ffffff",fg_color="#03773d",
                           border_width_checked=5,command=lambda:Click_Unclick("d2"))
    del_lab6.place(relx=0.053,rely=0.45,anchor="w")
    del_rb1.place(relx=0.053,rely=0.55,anchor="w")
    del_rb2.place(relx=0.053,rely=0.6)

    abut3=CTkButton(del_frame,text="Delete",height=20,width=111,font=("Arial",30,"bold"),fg_color="#03773d",
               hover_color="#2a8c56",command=lambda:delete_but())
    rbut3=CTkButton(del_frame,text="Reset",height=20,width=110,font=("Arial",30,"bold"),fg_color="transparent",
               border_color="#03773d",border_width=3,command=lambda:reset_but())
    ebut3=CTkButton(del_frame,text="Exit",height=20,width=110,font=("Arial",30,"bold"),fg_color="#03773d",
               hover_color="#2a8c56",command=lambda:close_up_window())
    abut3.place(relx=0.053,rely=0.9,anchor="w")
    rbut3.place(relx=0.5,rely=0.9,anchor="center")
    ebut3.place(relx=0.947,rely=0.9,anchor="e")

#----------------------------------------SQL Program--------------------------------------------
mycon = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
cur=mycon.cursor()

def create_database():                  # Used to create the database
    q='''create database if not exists Micro_Center'''
    cur.execute(q)
    q='''use Micro_Center'''
    cur.execute(q)
    mycon.commit()

def create_table():                     # Used to create the table
    s='''create table if not exists stock
        (Part_ID varchar(32) primary key,
        Part_Name varchar(32) not null,
        Manufacturer varchar(32) not null,
        Compatibility varchar(32) not null,
        Quantity int(3),
        Price int(7),
        Status varchar(32),
        In_Use varchar(32))'''
   
    o='''create table if not exists orders
        (Customer_ID varchar(32) primary key,
        Customer_Name varchar(32) not null,
        Repair_Item varchar(32) not null,
        Part_Used varchar(32) not null,
        Part_ID varchar(32),
        Quantity int(3),
        Fee int(7),
        Order_Progress varchar(32))'''
    cur.execute(s)
    cur.execute(o)

def insert_values():                    # Used to insert default values in the table
    q='''select Part_ID from stock'''
    cur.execute(q)
    d1=cur.fetchall()
    if d1==[] and st_table.get_children()==():
        s='''insert into stock values
            ('P101', 'Ryzen 5 5600X', 'AMD', 'AMD', 7, 15000, 'New', 'Yes'),
            ('P102', 'Core i5 12400F', 'Intel', 'Intel', 12, 15500, 'New', 'No'),
            ('P103', 'B550M Pro Mobo', 'MSI', 'AMD', 20, 10000, 'New', 'Yes'),
            ('P104', 'Z690 Aorus Mobo', 'Gigabyte', 'Intel', 15, 12500, 'New', 'No'),
            ('P105', 'RTX 3060 Ti', 'NVIDIA', 'Universal', 25, 35000, 'Used', 'Yes'),
            ('P106', 'RX 6700 XT', 'AMD', 'Universal', 18, 30000, 'New', 'No'),
            ('P107', '16GB DDR4', 'Corsair', 'Universal', 30, 4000, 'New', 'Yes'),
            ('P108', '16GB DDR4', 'Kingston', 'Universal', 25, 4500, 'New', 'No'),
            ('P109', 'Ryzen 7 5800X', 'AMD', 'AMD', 30, 20000, 'New', 'Yes'),
            ('P110', 'Core i7 12700K', 'Intel', 'Intel', 22, 25000, 'Used', 'No'),
            ('P111', 'Air Cooler Hyper 212', 'Cooler Master', 'Universal', 15, 3500, 'New', 'Yes'),
            ('P112', 'Liquid Cooler H100i', 'Corsair', 'Universal', 25, 9500, 'New', 'No'),
            ('P113', 'Ryzen 9 5900X', 'AMD', 'AMD', 14, 30000, 'New', 'Yes'),
            ('P114', 'Core i9 12900K', 'Intel', 'Intel', 12, 35000, 'Used', 'No'),
            ('P115', 'B450M Steel Mobo', 'ASRock', 'AMD', 20, 9000, 'Used', 'Yes'),
            ('P116', 'Z790 Hero Mobo', 'ASUS', 'Intel', 8, 20000, 'New', 'No'),
            ('P117', 'RX 6600', 'AMD', 'Universal', 26, 15000, 'New', 'Yes'),
            ('P118', 'RTX 3080', 'NVIDIA', 'Universal', 6, 60000, 'Used', 'No'),
            ('P119', '16GB DDR4', 'G.Skill', 'Universal', 30, 5000, 'New', 'Yes'),
            ('P120', '16GB DDR4', 'ADATA', 'Universal', 25, 5500, 'New', 'No'),
            ('P121', '1TB HDD', 'Seagate', 'Universal', 25, 3500, 'New', 'No'),
            ('P122', '2TB HDD', 'Western Digital', 'Universal', 20, 6000, 'New', 'Yes'),
            ('P123', '500GB NVMe SSD', 'Samsung', 'Universal', 15, 5500, 'New', 'No'),
            ('P124', '1TB NVMe SSD', 'Crucial', 'Universal', 12, 9500, 'New', 'Yes'),
            ('P125', '2TB SATA SSD', 'Kingston', 'Universal', 10, 15000, 'Used', 'No'),
            ('P126', 'Air Cooler MasterFan 120', 'Cooler Master', 'Universal', 20, 3000, 'New', 'Yes'),
            ('P127', 'Liquid Cooler Kraken X63', 'NZXT', 'Universal', 10, 12000, 'New', 'No'),
            ('P128', 'B550 Gaming Mobo', 'ASUS', 'AMD', 18, 11000, 'New', 'Yes'),
            ('P129', 'Z690 Extreme Mobo', 'Gigabyte', 'Intel', 12, 22000, 'New', 'No'),
            ('P130', 'RTX 3090', 'NVIDIA', 'Universal', 5, 120000, 'Used', 'Yes')'''
        cur.execute(s)
        mycon.commit() 
              
    w='''select Customer_ID from orders'''
    cur.execute(w)
    d2=cur.fetchall()
    if d2==[] and ord_table.get_children()==():
        o='''insert into orders values
            ('C101', 'Alice Smith', 'PC', 'Ryzen 5 5600X', 'P101', 1, 8000, 'In Progress'),
            ('C102', 'Bob Johnson', 'PC', 'Core i5 12400F', 'P102', 1, 7000, 'Pending'),
            ('C103', 'Charlie Brown', 'PC', 'B550M Pro Mobo', 'P103', 1, 6000, 'Completed'),
            ('C104', 'David Lee', 'Server', 'Z690 Aorus Mobo', 'P104', 1, 7500, 'In Progress'),
            ('C105', 'Eva Green', 'PC', 'RTX 3060 Ti', 'P105', 1, 9500, 'Pending'),
            ('C106', 'Frank Wright', 'Server', 'RX 6700 XT', 'P106', 1, 8500, 'Completed'),
            ('C107', 'Grace Hall', 'Laptop', '16GB DDR4', 'P107', 2, 4000, 'In Progress'),
            ('C108', 'Henry Adams', 'Laptop', '16GB DDR4', 'P108', 2, 4500, 'Pending'),
            ('C109', 'Ivy Clark', 'PC', 'Ryzen 7 5800X', 'P109', 1, 9000, 'Completed'),
            ('C110', 'Jack Miller', 'Server', 'Core i7 12700K', 'P110', 1, 10000, 'In Progress'),
            ('C111', 'Kathy Wilson', 'PC', 'Air Cooler Hyper 212', 'P111', 1, 3000, 'Pending'),
            ('C112', 'Leo Martinez', 'Server', 'Liquid Cooler H100i', 'P112', 1, 7000, 'Completed'),
            ('C113', 'Mia Lopez', 'PC', 'Ryzen 9 5900X', 'P113', 1, 10000, 'In Progress'),
            ('C114', 'Nathan Scott', 'Server', 'Core i9 12900K', 'P114', 1, 9500, 'Pending'),
            ('C115', 'Olivia Turner', 'PC', 'B450M Steel Mobo', 'P115', 1, 6000, 'Completed'),
            ('C116', 'Peter Parker', 'Server', 'Z790 Hero Mobo', 'P116', 1, 8000, 'In Progress'),
            ('C117', 'Quinn Reed', 'PC', 'RX 6600', 'P117', 1, 7000, 'Pending'),
            ('C118', 'Rachel Evans', 'Server', 'RTX 3080', 'P118', 1, 10000, 'Completed'),
            ('C119', 'Steve Young', 'Laptop', '16GB DDR4', 'P119', 2, 5000, 'In Progress'),
            ('C120', 'Tina Collins', 'Laptop', '16GB DDR4', 'P120', 2, 5500, 'Pending'),
            ('C121', 'Uma Sanders', 'PC', '1TB HDD', 'P121', 1, 3500, 'Completed'),
            ('C122', 'Victor Hughes', 'Server', '2TB HDD', 'P122', 1, 6000, 'In Progress'),
            ('C123', 'Wendy Price', 'PC', '500GB NVMe SSD', 'P123', 1, 5500, 'Pending'),
            ('C124', 'Xander Bell', 'Server', '1TB NVMe SSD', 'P124', 1, 9500, 'Completed'),
            ('C125', 'Yara Foster', 'PC', '2TB SATA SSD', 'P125', 1, 10000, 'In Progress'),
            ('C126', 'Zack Murphy', 'PC', 'Air Cooler MasterFan 120', 'P126', 1, 3000, 'Pending'),
            ('C127', 'Amy Brooks', 'Server', 'Liquid Cooler Kraken X63', 'P127', 1, 8000, 'Completed'),
            ('C128', 'Brian Cox', 'Server', 'B550 Gaming Mobo', 'P128', 1, 10000, 'In Progress'),
            ('C129', 'Clara Diaz', 'Server', 'Z690 Extreme Mobo', 'P129', 1, 10000, 'Pending'),
            ('C130', 'Dylan Fox', 'Server', 'RTX 3090', 'P130', 1, 10000, 'Completed')'''
        cur.execute(o)
        mycon.commit() 

def dynamic_display():                  # Used to change the no in the dynamic display
    q='''select count(*) from stock'''
    cur.execute(q)
    e=cur.fetchall()
    s1=e[0][0]
    w1_lab2.configure(text=f"{s1}")
    j='''select count(*) from orders'''
    cur.execute(j)
    w=cur.fetchall()
    o1=w[0][0]
    w2_lab2.configure(text=f"{o1}")
    n='''select count(*) from orders where Order_Progress='Completed' '''
    cur.execute(n)
    d=cur.fetchall()
    c1=d[0][0]
    w3_lab2.configure(text=f"{c1}")

def display_table():                    # Used the display the sql tables
    q='''select * from stock'''
    cur.execute(q)
    data=cur.fetchall()
    for i in data:
        st_table.insert("","end",values=i)
    w='''select * from orders'''
    cur.execute(w)
    data=cur.fetchall()
    for i in data:
        ord_table.insert("","end",values=i)
    j='''select * from stock'''
    cur.execute(j)
    h=cur.fetchall()
    for i in h:
        if i[1]!="":
            k.append(i[1]) 

def search_values(t):                   # Used to seacrh values
    if t=="st_table":
        if entry3.get()!="" and option1.get()!="":
            s=entry3.get()
            col=option1.get().strip()
            col=col.replace(" ","_")
            if col=="Condition":
                q='''select * from stock where Status=%s'''
                cur.execute(q,(s,))
                data=cur.fetchall()
                if data!=[]:
                    for item in st_table.get_children():
                        st_table.delete(item)
                    for row in data:
                        st_table.insert("","end",values=row)
                else:
                    CTkMessagebox(title="Error",message="The Entry Is Not Availabe",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="cancel",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
            else:
                q = f'''select * from stock where {col}= %s'''
                cur.execute(q,(s,))
                data=cur.fetchall()
                if data!=[]:
                    for item in st_table.get_children():
                        st_table.delete(item)
                    for row in data:
                        st_table.insert("","end",values=row)
                else:
                    CTkMessagebox(title="Error",message="The Entry Is Not Availabe",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="cancel",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
                    
        else:
            CTkMessagebox(title="Error",message="The Entries Is Missing ",text_color="#ffffff",
                          font=("monospace", 15, "bold"),width=350,icon="cancel",
                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                          sound=True,wraplength=300,master=main_frame)
            
    if t=="ord_table":
        if entry3.get()!="" and option1.get()!= "":
            s=entry3.get()
            col=option1.get().strip()
            col=col.replace(" ","_")
            q=f'''select * from orders where {col}=%s'''
            cur.execute(q,(s,))
            data=cur.fetchall()
            if data!=[]:
                for item in ord_table.get_children():
                    ord_table.delete(item)
                for row in data:
                    ord_table.insert("","end",values=row)
            else:
                CTkMessagebox(title="Error",message="The Entry Is Not Availabe",text_color="#ffffff",
                              font=("monospace", 15, "bold"),width=350,icon="cancel",
                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                              sound=True,wraplength=300,master=main_frame)
            
        else:
            CTkMessagebox(title="Error",message="The Entry Is Missing ",text_color="#ffffff",
                          font=("monospace", 15, "bold"),width=350,icon="cancel",
                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                          sound=True,wraplength=300,master=main_frame)
    
def add_but():                          # Used to add values in the table
    if a==1:
        if add_op1.get()=="" or add_op2.get()=="":
            CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                          font=("monospace", 15, "bold"),width=350,icon="cancel",
                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                          sound=True,wraplength=300,master=main_frame)
            
        elif add_op1.get()=="Stock":
            if add_entry1.get()=="" or add_entry2.get()=="" or add_entry3.get()=="" or con=="" or use=="":
                CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                              font=("monospace", 15, "bold"),width=350,icon="cancel",
                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                              sound=True,wraplength=300,master=main_frame)
            else:
                msg=CTkMessagebox(title="Conformation",message="Confirm Adding This Record?",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
                if msg.get()=="Yes":
                    s='''select * from stock where Part_ID= %s'''
                    cur.execute(s,(add_entry1.get(),))
                    data=cur.fetchone()
                    if data==None:
                        q='''insert into stock values(%s,%s,%s,%s,%s,%s,%s,%s)'''
                        cur.execute(q,(add_entry1.get(),add_entry2.get(),add_entry3.get(),
                                        add_op2.get(),n,m,con,use))
                        mycon.commit()
                        CTkMessagebox(title="Success",message="The Record Has Been Successfully Added",text_color="#ffffff",
                                      font=("monospace", 15, "bold"),width=350,icon="check",
                                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                      sound=True,wraplength=300,master=main_frame)
                        for i in st_table.get_children():
                            st_table.delete(i)
                        for i in ord_table.get_children():
                            ord_table.delete(i)
                        reset_but()
                        scroll.configure(command=st_table.yview)
                        scrollx.configure(command=st_table.xview)
                        display_table()
                        dynamic_display()
                    else:
                        CTkMessagebox(title="Error",message="The Part ID Already Exists",text_color="#ffffff",
                                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                      sound=True,wraplength=300,master=main_frame)
                    
        elif add_op1.get()=="Orders":
            if add_entry1.get()=="" or add_entry2.get()=="" or add_entry3.get()=="" or rep=="" or pog=="":
                CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                              font=("monospace", 15, "bold"),width=350,icon="cancel",
                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                              sound=True,wraplength=300,master=main_frame)
            else:
                msg=CTkMessagebox(title="Conformation",message="Confirm Adding This Record?",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
                if msg.get()=="Yes":
                    s='''select * from orders where Customer_ID= %s'''
                    cur.execute(s,(add_entry1.get(),))
                    data=cur.fetchone()
                    if data==None:
                        q='''select * from stock where Part_ID=%s'''
                        cur.execute(q,(add_entry3.get(),))
                        d=cur.fetchone()
                        if (d[4]-n) >0 or (d[4]-n)==0:
                            v=d[4]-n
                            q='''insert into orders values(%s,%s,%s,%s,%s,%s,%s,%s)'''
                            cur.execute(q,(add_entry1.get(),add_entry2.get(),rep,
                                            add_op2.get(),add_entry3.get(),n,m,pog))
                            mycon.commit()
                            q='''update stock set Quantity=%s where Part_ID=%s'''
                            cur.execute(q,(v,add_entry3.get()))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Added",text_color="#ffffff",
                                          font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i)
                            reset_but()
                            scroll.configure(command=ord_table.yview)
                            scrollx.configure(command=ord_table.xview)
                            display_table()
                            dynamic_display()
                        else:
                            CTkMessagebox(title="Error",message="The Quantity Entered Is More That The Available ",text_color="#ffffff",
                                          font=("monospace", 15, "bold"),width=350,icon="cancel",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)

                    else:
                        CTkMessagebox(title="Error",message="The Customer ID Already Exists",text_color="#ffffff",
                                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                      sound=True,wraplength=300,master=main_frame)
        
        k.clear()
        j='''select * from stock'''
        cur.execute(j)
        h=cur.fetchall()
        for i in h:
            if i[1]!="":
                k.append(i[1])

def update_but():                       # Used to update values in the table
    if up_window is not None:
        if up_op1.get()=="" or up_op2.get()=="":
            CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                          font=("monospace", 15, "bold"),width=350,icon="cancel",
                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                          sound=True,wraplength=300,master=main_frame)
        
        elif up_op1 is not None and up_op1.get()=="Stock":
            if up_entry1.get()=="" or up_entry2.get()=="":
                CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                              font=("monospace", 15, "bold"),width=350,icon="cancel",
                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                              sound=True,wraplength=300,master=main_frame)
            else:
                msg=CTkMessagebox(title="Conformation",message="Confirm Updating This Record?",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
                if msg.get()=="Yes":
                    s='''select * from stock where Part_ID= %s'''
                    cur.execute(s,(up_entry1.get(),))
                    data=cur.fetchone()
                    if data is not None:
                        if up_op2.get()=="Condition":
                            a=up_op2.get()
                            q='''update stock set Status=%s where Part_ID=%s'''
                            cur.execute(q,(up_entry2.get(),up_entry1.get()))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Updated",text_color="#ffffff",
                                          font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i)
                            reset_but()

                        elif up_op2.get()=="Quantity" or up_op2.get()=="Price":
                            if up_entry2.get().isdigit():
                                a=up_op2.get()
                                q=f'''update stock set {a}=%s where Part_ID=%s'''
                                cur.execute(q,(up_entry2.get(),up_entry1.get()))
                                mycon.commit()
                                CTkMessagebox(title="Success",message="The Record Has Been Successfully Updated",text_color="#ffffff",
                                              font=("monospace", 15, "bold"),width=350,icon="check",
                                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                              sound=True,wraplength=300,master=main_frame)
                                for i in st_table.get_children():
                                    st_table.delete(i)
                                for i in ord_table.get_children():
                                    ord_table.delete(i)
                                reset_but()
                            else:
                                CTkMessagebox(title="Warning",message="The Column Accepts Only Numbers",text_color="#ffffff",
                                              font=("monospace", 15, "bold"),width=350,icon="warning",
                                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                              sound=True,wraplength=300,master=main_frame)

                        elif up_op2.get()=="Part Name":
                            q='''select * from orders where Part_ID=%s'''
                            cur.execute(q,(up_entry1.get(),))
                            data=cur.fetchall()
                            if data is not None:
                                msg=CTkMessagebox(title="Warning",button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                                  message="The Record being Upated Is Being Used By A Customer Do You Still Want To Update It?",
                                                  font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                                  sound=True,wraplength=300,master=main_frame,text_color="#ffffff")
                                if msg.get()=="Yes":
                                    q='''update stock set Part_Name=%s where Part_ID=%s'''
                                    cur.execute(q,(up_entry2.get(),up_entry1.get()))
                                    mycon.commit()
                                    q='''update orders set Part_Used=%s where Part_ID=%s'''
                                    cur.execute(q,(up_entry2.get(),up_entry1.get(),))
                                    mycon.commit()
                                    CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",text_color="#ffffff",
                                                  font=("monospace", 15, "bold"),width=350,icon="check",
                                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                                  sound=True,wraplength=300,master=main_frame)
                                    for i in st_table.get_children():
                                        st_table.delete(i)
                                    for i in ord_table.get_children():
                                        ord_table.delete(i)
                                    reset_but()
                        
                        else:
                            a=up_op2.get().strip()
                            column=a.replace(" ","_")
                            q=f'''update stock set {column}=%s where Part_ID=%s'''
                            cur.execute(q,(up_entry2.get(),up_entry1.get()))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Updated",text_color="#ffffff",
                                          font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i)
                            reset_but()
                    else:
                        CTkMessagebox(title="Error",message="The Part ID Does Not Exists",text_color="#ffffff",
                                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                      sound=True,wraplength=300,master=main_frame)
                 
                    scroll.configure(command=st_table.yview)
                    scrollx.configure(command=st_table.xview)
                    display_table()
                    dynamic_display()
                    k.clear()
                    j='''select * from stock'''
                    cur.execute(j)
                    h=cur.fetchall()
                    for i in h:
                        if i[1]!="":
                            k.append(i[1])  

        elif up_op1.get()=="Orders":
            if up_entry1.get()=="" or up_entry2.get()=="":
                CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                              font=("monospace", 15, "bold"),width=350,icon="cancel",
                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                              sound=True,wraplength=300,master=main_frame)
            else:
                msg=CTkMessagebox(title="Conformation",message="Confirm Updating This Record?",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
                if msg.get()=="Yes":
                    s='''select * from orders where Customer_ID= %s'''
                    cur.execute(s,(up_entry1.get(),))
                    data=cur.fetchone()
                    if data is not None:
                        if up_op2.get()=="Quantity" or up_op2.get()=="Fee":
                            if up_entry2.get().isdigit():
                                a=up_op2.get()
                                q=f'''update orders set {a}=%s where Customer_ID=%s'''
                                cur.execute(q,(up_entry2.get(),up_entry1.get()))
                                mycon.commit()
                                CTkMessagebox(title="Success",message="The Record Has Been Successfully Updated",
                                              text_color="#ffffff",font=("monospace", 15, "bold"),width=350,icon="check",
                                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                              sound=True,wraplength=300,master=main_frame)
                                for i in st_table.get_children():
                                    st_table.delete(i)
                                for i in ord_table.get_children():
                                    ord_table.delete(i)
                                reset_but()
                            else:
                                CTkMessagebox(title="Warning",message="The Column Accepts Only Numbers",text_color="#ffffff",
                                              font=("monospace", 15, "bold"),width=350,icon="warning",
                                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                              sound=True,wraplength=300,master=main_frame)
                        else:
                            a=up_op2.get().strip()
                            column=a.replace(" ","_")
                            q=f'''update orders set `{column}`=%s where Customer_ID=%s'''
                            cur.execute(q,(up_entry2.get(),up_entry1.get()))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Updated",text_color="#ffffff",
                                          font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i)
                           
                    else:
                        CTkMessagebox(title="Error",message="The Customer ID Does Not Exists",text_color="#ffffff",
                                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                      sound=True,wraplength=300,master=main_frame)
                    display_table()
                    dynamic_display()
                    scroll.configure(command=ord_table.yview)
                    scrollx.configure(command=ord_table.xview)
        
def delete_but():                       # Used to  delete values in the table
    if del_window is not None:
        if del_op1.get()=="" or derb=="" or del_entry1.get()=="":
            CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                          font=("monospace", 15, "bold"),width=350,icon="cancel",
                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                          sound=True,wraplength=300,master=main_frame)
            
        elif del_op1 is not None and del_op1.get().lower()=="stock":
            if del_entry1.get()=="" or derb=="":
                CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                              font=("monospace", 15, "bold"),width=350,icon="cancel",
                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                              sound=True,wraplength=300,master=main_frame)
              
            elif (del_entry1.get()=="" or del_op2.get()=="") and derb=="Single Cell":
                CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                              font=("monospace", 15, "bold"),width=350,icon="cancel",
                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                              sound=True,wraplength=300,master=main_frame)  
                  
            elif del_entry1.get()!="" and derb=="Entire Row":
                msg=CTkMessagebox(title="Conformation",message="Confirm Deleting This Record?",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
                if msg.get()=="Yes":
                    s='''select * from stock where Part_ID=%s'''
                    cur.execute(s,(del_entry1.get(),))
                    data=cur.fetchone()
                    if data is not None:
                        s1='''select * from orders where Part_Used=%s'''
                        cur.execute(s1,(data[1],))
                        d=cur.fetchone()
                        cur.fetchall()
                        if d is not None:
                            msg=CTkMessagebox(title="Warning",button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                              message="The Record being Deleted Is Being Used By A Customer Do You Still Want To Delete It?",
                                              font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                              sound=True,wraplength=300,master=main_frame,text_color="#ffffff")
                            if msg.get()=="Yes":
                                q='''delete from stock where Part_ID=%s'''
                                cur.execute(q,(del_entry1.get(),))
                                mycon.commit()
                                q='''update orders set Part_Used="",Quantity=0,Fee=0,Part_ID="" where Part_ID=%s'''
                                cur.execute(q,(del_entry1.get(),))
                                mycon.commit()
                                CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",text_color="#ffffff",
                                              font=("monospace", 15, "bold"),width=350,icon="check",
                                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                              sound=True,wraplength=300,master=main_frame)
                                for i in st_table.get_children():
                                    st_table.delete(i)
                                for i in ord_table.get_children():
                                    ord_table.delete(i)
                                reset_but()
                                scroll.configure(command=st_table.yview)
                                scrollx.configure(command=st_table.xview)
                                display_table()
                                dynamic_display()
                        else:        
                            q='''delete from stock where Part_ID=%s'''
                            cur.execute(q,(del_entry1.get(),))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",text_color="#ffffff",
                                          font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i)
                                reset_but()
                            scroll.configure(command=st_table.yview)
                            scrollx.configure(command=st_table.xview)
                            display_table()
                            dynamic_display()
                            k.clear()
                            j='''select * from stock'''
                            cur.execute(j)
                            h=cur.fetchall()
                            for i in h:
                                if i[1]!="":
                                    k.append(i[1])
                    else:
                        CTkMessagebox(title="Error",message="The Part ID Does Not Exists",text_color="#ffffff",
                                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                      sound=True,wraplength=300,master=main_frame)                
                                    
            elif del_entry1.get()!="" and derb=="Single Cell" and del_op2.get()!="":
                msg=CTkMessagebox(title="Conformation",message="Confirm Deleting This Record?",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
                if msg.get()=="Yes":
                    s='''select * from stock where Part_ID= %s'''
                    cur.execute(s,(del_entry1.get(),))
                    data=cur.fetchone()
                    cur.fetchall()
                    if data is not None:
                        a=del_op2.get().strip()
                        column=a.replace(" ","_")
                        if column=="Part_Name":
                            s1='''select * from orders where Part_Used=%s'''
                            cur.execute(s1,(data[1],))
                            d=cur.fetchone()
                            cur.fetchall()
                            if d is not None:
                                msg=CTkMessagebox(title="Warning",button_color="#03773d",
                                                  button_hover_color="#2a8c56",button_width=40,
                                                  message="The Record being Deleted Is Being Used By A Customer Do \
                                                           You Still Want To Delete It?",
                                                  font=("monospace", 15, "bold"),width=350,icon="info",
                                                  option_1="Yes",option_2="No",sound=True,wraplength=300,
                                                  master=main_frame,text_color="#ffffff")
                                if msg.get()=="Yes":
                                    q='''update stock set Part_Name='' where Part_Name=%s'''
                                    cur.execute(q,(data[1],))
                                    mycon.commit()
                                    q='''update orders set Part_Used="",Quantity=0,Fee=0 where Part_ID=%s'''
                                    cur.execute(q,(del_entry1.get(),))
                                    mycon.commit()
                                    CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",
                                                  text_color="#ffffff",font=("monospace", 15, "bold"),width=350,
                                                  icon="check",button_color="#03773d",button_hover_color="#2a8c56",
                                                  button_width=40,sound=True,wraplength=300,master=main_frame)
                                    for i in st_table.get_children():
                                        st_table.delete(i)
                                    for i in ord_table.get_children():
                                        ord_table.delete(i)
                                    reset_but()
                                    scroll.configure(command=st_table.yview)
                                    scrollx.configure(command=st_table.xview)
                                    display_table()
                                    dynamic_display()
                                    k.clear()
                                    j='''select * from stock'''
                                    cur.execute(j)
                                    h=cur.fetchall()
                                    for i in h:
                                        if i[1]!="":
                                            k.append(i[1])

                        elif column=="Quantity" or column=="Price":
                            q=f'''update stock set {column}=0 where Part_ID=%s'''
                            cur.execute(q,(del_entry1.get(),))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",
                                          text_color="#ffffff",font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i) 

                        elif column=="Condition":
                            q=f'''update stock set Status='' where Part_ID=%s'''
                            cur.execute(q,(del_entry1.get(),))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",
                                          text_color="#ffffff",font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i)
                            
                        else:
                            q=f'''update stock set {column}='' where Part_ID=%s'''
                            cur.execute(q,(del_entry1.get(),))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",
                                          text_color="#ffffff",font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i)
                        
                    else:
                         CTkMessagebox(title="Error",message="The Part ID Does Not Exists",text_color="#ffffff",
                                       font=("monospace", 15, "bold"),width=350,icon="cancel",
                                       button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                       sound=True,wraplength=300,master=main_frame)
                    reset_but()
                    scroll.configure(command=st_table.yview)
                    scrollx.configure(command=st_table.xview)
                    display_table()
                    dynamic_display()
                    k.clear()
                    j='''select * from stock'''
                    cur.execute(j)
                    h=cur.fetchall()
                    for i in h:
                        if i[1]!="":
                            k.append(i[1]) 

        elif del_op1 is not None and del_op1.get()=="Orders":
            if del_entry1.get()=="" or derb=="":
                CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                              font=("monospace", 15, "bold"),width=350,icon="cancel",
                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                              sound=True,wraplength=300,master=main_frame) 
                    
            elif (del_entry1.get()=="" or del_op2.get()=="") and derb=="Single Cell":
                CTkMessagebox(title="Error",message="The Entries Are Missing",text_color="#ffffff",
                              font=("monospace", 15, "bold"),width=350,icon="cancel",
                              button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                              sound=True,wraplength=300,master=main_frame)
                
            elif del_entry1.get()!="" and derb=="Entire Row":
                msg=CTkMessagebox(title="Conformation",message="Confirm Adding This Record?",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
                if msg.get()=="Yes":
                    s='''select * from orders where Customer_ID= %s'''
                    cur.execute(s,(del_entry1.get(),))
                    data=cur.fetchone()
                    if data is not None:
                        q=f'''delete from orders where Customer_ID=%s'''
                        cur.execute(q,(del_entry1.get(),))
                        mycon.commit()
                        CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",
                                      text_color="#ffffff",font=("monospace", 15, "bold"),width=350,icon="check",
                                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                      sound=True,wraplength=300,master=main_frame)
                        for i in st_table.get_children():
                            st_table.delete(i)
                        for i in ord_table.get_children():
                                ord_table.delete(i)
                        scroll.configure(command=ord_table.yview)
                        scrollx.configure(command=ord_table.xview)
                        reset_but()
                        display_table()
                        dynamic_display()

                    else:
                        CTkMessagebox(title="Error",message="The Customer ID Does Not Exists",text_color="#ffffff",
                                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                      sound=True,wraplength=300,master=main_frame)
                         
            elif (del_entry1.get()!="" and del_op2.get()!="") and derb=="Single Cell":
                msg=CTkMessagebox(title="Conformation",message="Confirm Deleting This Record?",text_color="#ffffff",
                                  font=("monospace", 15, "bold"),width=350,icon="info",option_1="Yes",option_2="No",
                                  button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                  sound=True,wraplength=300,master=main_frame)
                if msg.get()=="Yes":
                    s='''select * from orders where Customer_ID= %s'''
                    cur.execute(s,(del_entry1.get(),))
                    data=cur.fetchone()
                    if data is not None:
                        a=del_op2.get().strip()
                        column=a.replace(" ","_")
                        if column=="Quantity" or column=="Fee":
                            q=f'''update orders set {column}=0 where Customer_ID=%s'''
                            cur.execute(q,(del_entry1.get(),))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",
                                          text_color="#ffffff",font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i)

                        else:
                            q=f'''update orders set {column}='' where Customer_ID=%s'''
                            cur.execute(q,(del_entry1.get(),))
                            mycon.commit()
                            CTkMessagebox(title="Success",message="The Record Has Been Successfully Deleted",
                                          text_color="#ffffff",font=("monospace", 15, "bold"),width=350,icon="check",
                                          button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                          sound=True,wraplength=300,master=main_frame)
                            for i in st_table.get_children():
                                st_table.delete(i)
                            for i in ord_table.get_children():
                                ord_table.delete(i)    
                    else:
                        CTkMessagebox(title="Error",message="The Customer ID Does Not Exists",text_color="#ffffff",
                                      font=("monospace", 15, "bold"),width=350,icon="cancel",
                                      button_color="#03773d",button_hover_color="#2a8c56",button_width=40,
                                      sound=True,wraplength=300,master=main_frame)
                        
                    reset_but()
                    display_table()
                    scroll.configure(command=st_table.yview)
                    scrollx.configure(command=st_table.xview)
                    dynamic_display() 

def reset_but():                        # Used to reset the entries in the add/update/delete windows
    global n,m
    if a==1:
        if add_op1.get().lower()=="stock":
            add_entry1.delete(0,"end")
            add_entry2.delete(0,"end")
            add_entry3.delete(0,"end")
            add_op1.set("")
            add_op2.set("")
            add_rb1.deselect()
            add_rb2.deselect()
            add_rb3.deselect()
            add_rb4.deselect()
            n=1
            m=500
            add_lab10.configure(text=n)
            add_lab12.configure(text=m)
        else:
            add_entry1.delete(0,"end")
            add_entry2.delete(0,"end")
            add_entry3.delete(0,"end")
            add_op1.set("")
            add_op2.set("")
            add_rb5.deselect()
            add_rb6.deselect()
            add_rb7.deselect()
            add_rb8.deselect()
            add_rb9.deselect()
            add_rb10.deselect()
            n=1
            m=500
            add_lab10.configure(text=n)
            add_lab12.configure(text=m)

    if up_window is not None:
        up_op1.set("")
        up_op2.set("")
        up_entry1.delete(0,"end")
        up_entry2.delete(0,"end")
    
    if del_window is not None:
        if derb=="Entire Row":
            del_op1.set("")
            del_rb2.deselect()
            del_entry1.delete(0,"end")
        else:
            del_op1.set("")
            del_op2.set("")
            del_rb1.deselect("")
            del_entry1.delete(0,"end")
            del_lab4.place_forget()
            del_op2.place_forget()
    
    else:
        entry3.delete(0,"end")
        option1.set("")
        for i in st_table.get_children():
            st_table.delete(i)
        for i in ord_table.get_children():
            ord_table.delete(i)
        display_table()

def order_part_used(a):                 # Used to display the part id of the part used selected by the user
    if add_op1.get()=="Orders":
        if add_op2.get() is not None:
            L='''select Part_ID from stock where Part_Name=%s'''
            cur.execute(L,(a,))
            data=cur.fetchall()
            if data!=[]:
                p=data[0]
                add_entry3.delete(0,"end")
                add_entry3.insert(0,p)

def order_part_id():                    # Used to display the part used of the part id selected by the user
    if add_op1.get()=="Orders":
        if add_entry3.get()!="":
            z=add_entry3.get()
            l='''select Part_Name from stock where Part_ID=%s''' 
            cur.execute(l,(z,)) 
            data=cur.fetchall()
            if data!=[]:
                p=data[0][0] 
                add_op2.set(p)


create_database()
create_table()
insert_values()
dynamic_display()
display_table()

app.mainloop()