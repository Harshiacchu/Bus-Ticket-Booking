from tkinter import *
from tkinter import ttk
import tkcalendar as tkc
import time
import mysql.connector as sql
from tkinter import messagebox
from PIL import ImageTk
import seating
import profile
import random

def view_seats1():
    global str_viewseats, ft_win1, f1, t1, d1, Usern, Passn
    ft_win.withdraw()
    ft_win1.withdraw()
    str_viewseats = '170'
    girl1 = 1
    seating.third_win(str_viewseats, girl1, f1, t1, d1, Usern, Passn)
def view_seats2():
    global str_viewseats, ft_win1, f1, f1, t1, d1, Usern, Passn
    ft_win.withdraw()
    ft_win1.withdraw()
    str_viewseats = '190'
    girl2 = 2
    seating.third_win(str_viewseats, girl2, f1, t1, d1, Usern, Passn)
def view_seats3():
    global str_viewseats, ft_win1, f1, t1, d1, Usern, Passn
    ft_win.withdraw()
    ft_win1.withdraw()
    str_viewseats = '150'
    girl3 = 3
    seating.third_win(str_viewseats, girl3, f1, t1, d1, Usern, Passn)
def view_seats4():
    global str_viewseats, ft_win1, f1, t1, d1, Usern, Passn
    ft_win.withdraw()
    ft_win1.withdraw()
    str_viewseats = '160'
    girl4 = 4
    seating.third_win(str_viewseats, girl4, f1, t1, d1, Usern, Passn)
def view_seats5():
    global str_viewseats, ft_win1, f1, t1, d1, Usern, Passn
    ft_win.withdraw()
    ft_win1.withdraw()
    str_viewseats = '140'
    girl5 = 5
    seating.third_win(str_viewseats, girl5, f1, t1, d1, Usern, Passn)
def view_seats6():
    global str_viewseats, ft_win1, f1, t1, d1, Usern, Passn
    ft_win.withdraw()
    ft_win1.withdraw()
    str_viewseats = '150'
    girl6 = 6
    seating.third_win(str_viewseats, girl6, f1, t1, d1, Usern, Passn)
def view_seats7():
    global str_viewseats, ft_win1, f1, t1, d1, Usern, Passn
    ft_win.withdraw()
    ft_win1.withdraw()
    str_viewseats = '120'
    girl7 = 7
    seating.third_win(str_viewseats, girl7, f1, t1, d1, Usern, Passn)
def view_seats8():
    global str_viewseats, ft_win1, f1, t1, d1, Usern, Passn
    ft_win.withdraw()
    ft_win1.withdraw()
    str_viewseats = '180'
    girl8 = 8
    seating.third_win(str_viewseats, girl8, f1, t1, d1, Usern, Passn)
def view_seats9():
    global str_viewseats, ft_win1, f1, t1, d1, Usern, Passn
    ft_win1.withdraw()
    str_viewseats = '200'
    girl9 = 9
    seating.third_win(str_viewseats, girl9, f1, t1, d1, Usern, Passn)

def date_win():
    global ft_win1, ft_win, et_logo
    ft_win1 = Toplevel()
    ft_win1.title("ESCAPE TRAVELS")
    ft_win1.geometry("820x600+0+0")
    ft_win1.resizable('False','False')

    mycanvas = Canvas(ft_win1, width=800)
    mycanvas.pack(side=LEFT, fill=Y)

    s = ttk.Scrollbar(ft_win1, orient='vertical', command=mycanvas.yview)
    s.pack(side=RIGHT, fill=Y)

    mycanvas.config(yscrollcommand=s.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.config(scrollregion=mycanvas.bbox('all')))

    second = Frame(mycanvas, bg='aquamarine',width=1350,height=690)
    mycanvas.create_window((0,0), window=second, anchor='nw')

    Frame(second, bg='white', width=780, height=80).pack(padx=10, pady=10)
    et_logo = ImageTk.PhotoImage(file='ET logo.jpg')
    Label(second, image=et_logo, relief='flat').place(x=25, y=25)
    Label(second, text='ESCAPE TRAVELS', bg='white', font=('Verdana bold',15)).place(x=140, y=30)
    Label(second, text='Book your choices of buses on\nEscape travels', bg='white', font=('Calibri',10)).place(x=400, y=30)
    Label(second, text='9 buses available', bg='white', font=('Calibri',15)).place(x=600, y=30)

    Frame(second, bg='white', width=780, height=200).pack(padx=10, pady=10)
    Label(second, bg='white', font=('Verdana',15), text='AC Sleeper Bus').place(x=30, y=120)
    Label(second, bg='white', font=('Times',10), text='Cost per ticket').place(x=30, y=200)
    Label(second, bg='white', font=('Times bold',10), text='Rs. 170').place(x=120, y=200)
    #Label(second, bg='white', font=('Calibri bold',13), text='08:06').place(x=350, y=120)
    Label(second, bg='white', font=('Calibri',12), text=f1).place(x=350, y=150)
    #Label(second, bg='white', font=('Calibri',13), fg='grey60', text='07h 45m').place(x=450, y=120)
    #Label(second, bg='white', font=('Calibri',13), text='15:45').place(x=550, y=120)
    Label(second, bg='white', font=('Calibri',12), text=t1).place(x=550, y=150)
    Button(second, relief='flat', bg='pale green', font=('Times bold',15), text='View Seats', command=view_seats1).place(x=672, y=269)

    Frame(second, bg='white', width=780, height=200).pack(padx=10, pady=10)
    Label(second, bg='white', font=('Verdana',15), text='AC Sleeper Seater Bus').place(x=30, y=340)
    Label(second, bg='white', font=('Times',10), text='Cost per ticket').place(x=30, y=420)
    Label(second, bg='white', font=('Times bold',10), text='Rs. 190').place(x=120, y=420)
    Label(second, bg='white', font=('Calibri',12), text=f1).place(x=350, y=370)
    Label(second, bg='white', font=('Calibri',12), text=t1).place(x=550, y=370)
    Button(second, relief='flat', bg='pale green', font=('Times bold',15), text='View Seats', command=view_seats2).place(x=672, y=489)

    Frame(second, bg='white', width=780, height=200).pack(padx=10, pady=10)
    Label(second, bg='white', font=('Verdana',15), text='Classic Bus').place(x=30, y=560)
    Label(second, bg='white', font=('Times',10), text='Cost per ticket').place(x=30, y=640)
    Label(second, bg='white', font=('Times bold',10), text='Rs. 150').place(x=120, y=640)
    Label(second, bg='white', font=('Calibri',12), text=f1).place(x=350, y=590)
    Label(second, bg='white', font=('Calibri',12), text=t1).place(x=550, y=590)
    Button(second, relief='flat', bg='pale green', font=('Times bold',15), text='View Seats', command=view_seats3).place(x=672, y=709)

    Frame(second, bg='white', width=780, height=200).pack(padx=10, pady=10)
    Label(second, bg='white', font=('Verdana',15), text='Deluxe Bus').place(x=30, y=780)
    Label(second, bg='white', font=('Times',10), text='Cost per ticket').place(x=30, y=860)
    Label(second, bg='white', font=('Times bold',10), text='Rs. 160').place(x=120, y=860)
    Label(second, bg='white', font=('Calibri',12), text=f1).place(x=350, y=810)
    Label(second, bg='white', font=('Calibri',12), text=t1).place(x=550, y=810)
    Button(second, relief='flat', bg='pale green', font=('Times bold',15), text='View Seats', command=view_seats4).place(x=672, y=929)

    Frame(second, bg='white', width=780, height=200).pack(padx=10, pady=10)
    Label(second, bg='white', font=('Verdana',15), text='Non AC Sleeper Bus').place(x=30, y=1000)
    Label(second, bg='white', font=('Times',10), text='Cost per ticket').place(x=30, y=1080)
    Label(second, bg='white', font=('Times bold',10), text='Rs. 140').place(x=120, y=1080)
    Label(second, bg='white', font=('Calibri',12), text=f1).place(x=350, y=1030)
    Label(second, bg='white', font=('Calibri',12), text=t1).place(x=550, y=1030)
    Button(second, relief='flat', bg='pale green', font=('Times bold',15), text='View Seats', command=view_seats5).place(x=672, y=1149)

    Frame(second, bg='white', width=780, height=200).pack(padx=10, pady=10)
    Label(second, bg='white', font=('Verdana',15), text='Non AC Sleeper Seater Bus').place(x=30, y=1220)
    Label(second, bg='white', font=('Times',10), text='Cost per ticket').place(x=30, y=1300)
    Label(second, bg='white', font=('Times bold',10), text='Rs. 150').place(x=120, y=1300)
    Label(second, bg='white', font=('Calibri',12), text=f1).place(x=350, y=1250)
    Label(second, bg='white', font=('Calibri',12), text=t1).place(x=550, y=1250)
    Button(second, relief='flat', bg='pale green', font=('Times bold',15), text='View Seats', command=view_seats6).place(x=672, y=1369)

    Frame(second, bg='white', width=780, height=200).pack(padx=10, pady=10)
    Label(second, bg='white', font=('Verdana',15), text='Ordinary Bus').place(x=30, y=1440)
    Label(second, bg='white', font=('Times',10), text='Cost per ticket').place(x=30, y=1520)
    Label(second, bg='white', font=('Times bold',10), text='Rs. 120').place(x=120, y=1520)
    Label(second, bg='white', font=('Calibri',12), text=f1).place(x=350, y=1470)
    Label(second, bg='white', font=('Calibri',12), text=t1).place(x=550, y=1470)
    Button(second, relief='flat', bg='pale green', font=('Times bold',15), text='View Seats', command=view_seats7).place(x=672, y=1589)

    Frame(second, bg='white', width=780, height=200).pack(padx=10, pady=10)
    Label(second, bg='white', font=('Verdana',15), text='Semi Deluxe Bus').place(x=30, y=1660)
    Label(second, bg='white', font=('Times',10), text='Cost per ticket').place(x=30, y=1740)
    Label(second, bg='white', font=('Times bold',10), text='Rs. 180').place(x=120, y=1740)
    Label(second, bg='white', font=('Calibri',12), text=f1).place(x=350, y=1690)
    Label(second, bg='white', font=('Calibri',12), text=t1).place(x=550, y=1690)
    Button(second, relief='flat', bg='pale green', font=('Times bold',15), text='View Seats', command=view_seats8).place(x=672, y=1809)

    Frame(second, bg='white', width=780, height=200).pack(padx=10, pady=10)
    Label(second, bg='white', font=('Verdana',15), text='Super Deluxe Bus').place(x=30, y=1880)
    Label(second, bg='white', font=('Times',10), text='Cost per ticket').place(x=30, y=1960)
    Label(second, bg='white', font=('Times bold',10), text='Rs. 200').place(x=120, y=1960)
    Label(second, bg='white', font=('Calibri',12), text=f1).place(x=350, y=1910)
    Label(second, bg='white', font=('Calibri',12), text=t1).place(x=550, y=1910)
    Button(second, relief='flat', bg='pale green', font=('Times bold',15), text='View Seats', command=view_seats9).place(x=672, y=2029)

def book(mainvar_fun):
    global ft_win, b,cb
    Mainvar_fun = mainvar_fun
    if mainvar_fun == 3:
        abcdef = 0
    else:
        b.withdraw()
    ft_win = Toplevel()
    ft_win.title("Escape Travels")
    #ft_win.attributes('-alpha', 0.)  #to make the screen transparent
    #ft_win.configure(bg='mint cream')
    style = ttk.Style(ft_win)
    #style.theme_use('clam')
    ft_win.geometry('1350x690+0+0')
    ft_win.resizable(width=False, height=False)
    cb=ImageTk.PhotoImage(file='cb1.jpg')
    Label(ft_win,image=cb).place(x=0,y=0)
    
    def go_to_main_page():
        global ft_win,b
        b.deiconify()
        ft_win.destroy()                
    
    frame1 = Frame(ft_win, bg='mint cream', width=920, height=300)
    frame1.place(x=250, y=200)

    def button_hover(e):
        my_b['bg']='mint cream'
        Label(frame1, text='Go to main page', bg='light yellow').place(x=2, y=40)
    def button_hover_leave(e):
        my_b['bg']='mint cream'
        Label(frame1,text='                                 ', bg='mint cream').place(x=2, y=40)
    my_b=Button(frame1, text='<', cursor='hand2', font=('Calibri',15), relief='flat', height=1, width=2, bg='mint cream', command=go_to_main_page)
    my_b.place(x=5, y=5)
    my_b.bind('<Enter>',button_hover)
    my_b.bind('<Leave>',button_hover_leave)
    
    Label(frame1, text='CHOOSE YOUR BUSES', font=('Times bold', 30), bg="mint cream").place(x=230, y=20)
    num=["Chennai", "Pondicherry", "Madurai", "Coimbatore", "Trichy", "Salem", "Vellore", "Thanjavur", "Erode", "Tirunelveli", "Tiruppur", "Dindigul", "Thoothukudi", "Ooty", "Viluppuram", "Kanchipuram", "Kumbakonam", "Nagapatinam", "Kodaikanal", "Pudukkottai", "Tiruvannamalai", "Dharmapuri", "Karur", "Chidambaram", "Nagercoil", "Palani", "Rameswaram", "Chengalpattu", "Cuddalore", "Ramanathapuram", "Perambalur", "Namakkal", "Karaikudi", "Kanchipuram", "Kanyakumari", "Pollachi", "Mayiladuthurai", "Thiruvarur", "Krishnagiri", "Hosur", "Tenkasi", "Virudhunagar", "Kallakkurichi", "Srivilliputhur", "Arakonam", "Sivakasi", "Mettur", "Valparai", "Ariyalur", "Tiruchengode"]
    variable = StringVar(ft_win)
    variable.set("choose")

    a2=StringVar()
    b2=StringVar()
    c2=StringVar()

    from_label = Label(frame1, text='FROM', font=('Times bold',14), bg='mint cream').place(x=50, y=110)
    from_title = ttk.Combobox(frame1, text="From", font=('Times bold',14), state='readonly', justify=CENTER, background='white', values=num, textvariable=a2)
    from_title.place(x=50,  y=160)
    #from_title.current(0)

    to_label = Label(frame1, text='TO', font=('Times bold',14), bg='mint cream').place(x=350, y=110)
    to_title = ttk.Combobox(frame1, text="To", font=('Times bold', 14), state='readonly', justify=CENTER, background='white', values=num, textvariable=b2)
    to_title.place(x=350, y=160)
    #to_title.current(0)

    from_label = Label(frame1, text='DEPARTURE DATE', font=('Times bold',14), bg='mint cream').place(x=650, y=110)
    date_entry = tkc.DateEntry(frame1, width=20, height=22, font=(28), bg='white smoke', fg='mint cream', textvariable=c2)
    date_entry.place(x=650, y=160)
    def bus_list():
        global et_logo, ft_win1, ft_win, f1, t1, d1
        f1 = from_title.get()
        t1 = to_title.get()
        d1 = date_entry.get()
        ft_list = []
        ft_list = d1.split('/')
        ft_list[0],ft_list[1] = ft_list[1],ft_list[0]
        date = time.strftime('%d')
        month = time.strftime('%m')
        year = time.strftime('%y')
        Date,Month='',''
        if len(date)==2 and date[0]=='0':
            Date=date[1]
        else:
            Date = date
        if len(month)==2 and month[0]=='0':
            Month=month[1]
        else:
            Month = month
        if f1 == '' and t1 != '':
            messagebox.showerror('Error', 'Choose your departure place')
        elif t1 == '' and f1 != '':
            messagebox.showerror('Error', 'Choose your destination place')
        elif f1 == '' and t1 == '':
            messagebox.showerror('Error', 'All fields are required')
        elif f1 == t1:
            messagebox.showerror('Error', 'Choose correct destination place')
            #print(Month,Date,year,'\n',d1)
        else:
            if int(ft_list[2]) >= int(year):
                if int(ft_list[1]) >= int(Month):
                    if int(ft_list[1]) == int(Month):
                        if int(ft_list[0]) >= int(Date):
                            date_win()
                        else:
                            messagebox.showerror('Error', 'Enter from current date')
                    elif int(ft_list[1]) > int(Month):
                        date_win()
                    else:
                        messagebox.showerror('Error', 'Enter from current month')
            else:
                messagebox.showerror('Error', 'Enter from current year')

    Button(frame1, text='   Search Buses   ', font=('Verdana',12), bg="white smoke", command=bus_list).place(x=400, y=250)
    ft_win.mainloop()

def Book():
    mainfun_var = 2
    book(mainfun_var)
#bi=ImageTk.PhotoImage(file='bi.jpg')
def login(usern,passn):
    global Usern,Passn,b,ycoord1,ycoord2,ycoord3,ycoord4,ycoord5
    Usern = usern
    Passn = passn
    ycoord1 = 130
    ycoord2 = 190
    ycoord3 = 250
    ycoord4 = 310
    ycoord5 = 370

    b = Tk()
    b.geometry('1350x690+0+0')
    b.title('ESCAPE TRAVELS')
    
    b.configure(bg='mint cream')
    b.resizable('False','False')
    
    def history():
        global ycoord1, ycoord2, ycoord3, ycoord4, ycoord5, Usern
        window_history = Tk()
        window_history.geometry('820x500')
        window_history.title('MY HISTORY')
        window_history.configure(bg='aquamarine')
        window_history.resizable(False,False)
        Frame(window_history, bg='mint cream', width=1500, height=1000).place(x=0, y=0)
        con = sql.connect(host = "localhost", user = "root", password = "harshitha", database = "project")
        cr = con.cursor()
        cr.execute("Select * from history_details where username ='"+Usern+"'")
        rows = cr.fetchall()
        con.close()

        history_canvas = Canvas(window_history, width=800)
        history_canvas.pack(side=LEFT, fill=Y)
        scroll = ttk.Scrollbar(window_history, orient='vertical', command=history_canvas.yview)
        scroll.pack(side=RIGHT, fill=Y)
        history_canvas.config(yscrollcommand=scroll.set)
        history_canvas.bind('<Configure>', lambda e: history_canvas.config(scrollregion=history_canvas.bbox('all')))
        s_frame = Frame(history_canvas, bg='aquamarine')
        history_canvas.create_window((0,0), window=s_frame, anchor='nw')

        Frame(s_frame, bg='white', width=780, height=80).pack(padx=10, pady=10)
        Label(s_frame, text='MY HISTORY', bg='white', font=('Verdana bold',15)).place(x=310, y=30)
        if len(rows)==0:
            window_history.geometry('700x370')
            Frame(s_frame, bg='mint cream', width=780, height=250).pack(padx=10, pady=10)
            Label(s_frame, bg='mint cream', font=('Verdana',15), text='Book your seats to view\n\nyour history').place(x=230, y=200)
        if len(rows)==1:
            window_history.geometry('820x420')
        for i in range(len(rows)):
            split = rows[i][6].split(',')
            Frame(s_frame, bg='mint cream', width=780, height=300).pack(padx=10, pady=10)
            Label(s_frame, bg='mint cream', font=('Verdana italic',15), text='Booking details').place(x=70, y=ycoord1)
            Label(s_frame, bg='mint cream', font=('Times',15), text='From').place(x=60, y=ycoord2)
            Label(s_frame, bg='mint cream', font=('Calibri',13), text=rows[i][0], fg='grey50').place(x=120, y=ycoord2)
            Label(s_frame, bg='mint cream', font=('Times',15), text='To').place(x=250, y=ycoord2)
            Label(s_frame, bg='mint cream', font=('Calibri',13), text=rows[i][1], fg='grey50').place(x=300, y=ycoord2)
            Label(s_frame, bg='mint cream', font=('Times',15), text='Date').place(x=400, y=ycoord2)
            Label(s_frame, bg='mint cream', font=('Calibri',13), text=rows[i][2], fg='grey50').place(x=460, y=ycoord2)

            Label(s_frame, bg='mint cream', font=('Times',15), text='No of seats booked').place(x=60, y=ycoord3)
            Label(s_frame, bg='mint cream', font=('Calibri',13), text=rows[i][3], fg='grey50').place(x=250, y=ycoord3)
            Label(s_frame, bg='mint cream', font=('Times',15), text='Seats booked').place(x=320, y=ycoord3)
            Label(s_frame, bg='mint cream', font=('Calibri',13), text=rows[i][4][0:len(rows[i][4])-1], fg='grey50').place(x=450, y=ycoord3)

            Label(s_frame, bg='mint cream', font=('Verdana italic',15), text='Booking Date & time').place(x=70, y=ycoord4)
            Label(s_frame, bg='mint cream', font=('Times',15), text='Booked on').place(x=60, y=ycoord5)
            Label(s_frame, bg='mint cream', font=('Calibri',13), text=split[4:7]+[','], fg='grey50').place(x=160, y=ycoord5)
            Label(s_frame, bg='mint cream', font=('Times',13), text=split[3], fg='grey50').place(x=262, y=ycoord5)
            Label(s_frame, bg='mint cream', font=('Calibri',15), text='at').place(x=320, y=ycoord5)
            Label(s_frame, bg='mint cream', font=('Times',15), text=split[0:3], fg='grey50').place(x=350, y=ycoord5)
            ycoord1 += 320
            ycoord2 += 320
            ycoord3 += 320
            ycoord4 += 320
            ycoord5 += 320
        window_history.mainloop()
    def pro_fil():
        global b
        b.destroy()
        profile.view_profile(usern, passn)
        
    def log_out():
        mg_logout = messagebox.askyesno('Log out', 'Are you sure you want to\nlog out from your account')
        if mg_logout == 1:
            b.destroy()
            win_logout=Tk()
            win_logout.geometry('200x100+400+250')
            win_logout.title('LOG OUT')
            Frame(win_logout, bg='azure', width=1500, height=1000).place(x=0, y=0)
            l1 = Label(win_logout, text='Logging out.  ', bg='azure', font=('Times',20))
            l1.pack(pady=20,expand=True)
            def fun6():
                messagebox.showinfo('Successfully loged out !', 'Thanks for using our system')
                l1.after(0,win_logout.destroy())
            def fun5():
                l1.config(text='Logging out  .')
                l1.after(1000,fun6)
            def fun4():
                l1.config(text='Logging out . ')
                l1.after(1000,fun5)
            def fun3():
                l1.config(text='Logging out.  ')
                l1.after(1000,fun4)
            def fun2():
                l1.config(text='Logging out  .')
                l1.after(1000,fun3)
            def fun1():
                l1.config(text='Logging out . ')
                l1.after(1000,fun2)
            l1.after(1000,fun1)        
    bf=Frame(b, bg='mint cream', width=600, height=250).place(x=350, y=200)
    Button(b, bg='grey90', relief='raised', width=18,height=2, text=' HISTORY ', command=history, cursor='hand2',bd=2,font=('Calibri',15)).place(x=380, y=450)
    Button(b, bg='grey90', relief='raised', width=18,height=2, text=' PROFILE ', command=pro_fil, cursor='hand2',bd=2,font=('Calibri',15)).place(x=800, y=450)
    Button(b, bg='azure', relief='groove', width=9, text='   Log  Out   ', command=log_out, cursor='hand2',font=('Calibri',15)).place(x=1200, y=20)

    def cancel():
        def Back():
            global b
            window_cancel.destroy()
            b.deiconify()
        def selectAll():
            global b
            e = entry.get()
            if e == '':
                messagebox.showerror('Error', 'Enter your registration ID')
            else:
                con = sql.connect(host = "localhost", user = "root", password = "harshitha", database = "project")
                cr = con.cursor()
                cr.execute("Select price,seats from otp where otp ='"+e+"'")
                rows = cr.fetchall()
                if rows == []:
                    messagebox.showerror('Error', "Your registration ID doesn't match")
                else:
                    for r in rows:
                        price_seats = r
                        empty_list = []
                        new_price = price_seats[0]
                        new_seats = price_seats[1].split(',')
                        for some in range(0,len(new_seats)-1):
                            empty_list += [new_seats[some]]
                            #print(empty_list)
                        messagebox.showinfo('Tickets Cancelled', 'Your payment price Rs. '+str(new_price)+' has\nrefunded successfully')
                        con1 = sql.connect(host = "localhost", user = "root", password = "harshitha", database = "project")
                        cr1 = con1.cursor()
                        cr1.execute("Delete from otp where otp ='"+e+"'")
                        cr1.execute('commit')
                        con1.close()
                        window_cancel.destroy()
                        b.deiconify()
                con.close()
        M = messagebox.askyesno('Cancellation', 'Are you sure you want to cancel\nthe tickets you booked?')
        if M == 1:
            b.withdraw()
            window_cancel = Tk()
            window_cancel.geometry('300x200')
            window_cancel.title('CANCELLATION')
            window_cancel.resizable('False','False')
            F = Frame(window_cancel, bg='mint cream', width=1500, height=1000).place(x=0, y=0)
            Label(window_cancel, text='Enter your registration ID\nprovided during your payment process', bg='mint cream', font=('Calibri',13)).place(x=10, y=20)
            entry = Entry(window_cancel, relief='groove', font=('Helvetica',13))
            entry.place(x=30, y=80)
            Button(window_cancel, text='BACK', bg='grey90', width=10, font=('Calibri',12), command=Back).place(x=80, y=150)
            Button(window_cancel, text='OK', bg='grey90', width=10, font=('Calibri',12), command=selectAll).place(x=180, y=150)    
    Label(b, bg='mint cream', text=' Enjoy booking your tickets with ', font=('Times',28,'bold')).place(x=420, y=100)
    Label(b, bg='mint cream', text=' Escape Travels!! ', font=('Times',28,'bold')).place(x=540, y=150)
    Button(b, width=18,height=2, bd=2, relief='raised', command=Book, bg='grey90', font=('Calibri',15), text=' BOOK NOW ').place(x=380, y=300)
    Button(b, width=18,height=2, bd=2, relief='raised', command=cancel, bg='grey90', font=('Calibri',15), text='  CANCELLATION  ').place(x=800, y=300)
#=============================================================================================================================
##def date_fun():
##    elif d1 == Month+'/'+Date+'/'+year or d1 == Month+'/'+str(int(Date)+1)+'/'+year:
##        #MONTH = time.strftime('%B')
##        MoNth = time.strftime('%m')
##        listy = [int('01'),int('03'),int('05'),int('07'),int('08'),10,12]
##        liste = [int('04'),int('06'),int('09'),11]
##        ch = 0
##        if MoNth in listy:
##            if date == '30':
##                DATE = '01'
##                ch = 1
##            elif date == '31':
##                DATE = '02'
##                ch = 1
##            else:
##                DATE = date
##        elif MoNth in liste:
##            if date == '29':
##                DATE = '01'
##                ch = 1
##            elif date == '30':
##                DATE = '02'
##                ch = 1
##            else:
##                DATE = date
##        else:
##            y = time.strftime('%Y')
##            print(y)
##            if y%4 == 0:
##                if date == '28':
##                    DATE = '01'
##                    ch = 1
##                elif date == '29':
##                    DATE = '02'
##                    ch = 1
##                else:
##                    DATE = date
##            else:
##                if date == '27':
##                    DATE = '01'
##                    ch = 1
##                elif date == '28':
##                    DATE = '02'
##                    ch = 1
##                else:
##                    DATE = date
##        if ch == 1:
##            datetime_object = datetime.datetime.strptime(MONTH, "%B")
##            month_number = int(datetime_object.month) + 1
##            datetime_object1 = datetime.datetime.strptime(month_number, "%m")
##            MONTH = datetime_object1.strftime("%B")
##        else:
##            MONTH = time.strftime('%B')
##        messagebox.showerror('Error', 'Booking date starts from '+str(DATE)+' '+str(MONTH))