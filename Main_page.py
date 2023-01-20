from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from PIL import ImageTk
import mysql.connector as sql
import booking
from tkcalendar import DateEntry
from tkinter import ttk

fresh = Tk()
fresh.geometry('1350x690+0+0')
fresh.title('Namaste !!')
fresh.resizable('False','False')

image1 = ImageTk.PhotoImage(file='Welcome.jpg')
bt_image = ImageTk.PhotoImage(file='login button.jpg')

Label(fresh, image=image1).place(x=0,y=0)
fresh_frame = Frame(fresh, bg='mint cream', width=650, height=530).place(x=350, y=120)

num1 = StringVar()
num2 = StringVar()

f = Frame(fresh, bg='floral white', height=300, width=400).place(x=470, y=280)

Label(fresh_frame, text='Login here', font=('Impact',30,'bold'), bg='floral white', fg='blue').place(x=570, y=300)
Label(fresh_frame, text='Escape Bus Login Area', font=('Goudy old style',11,'bold'), bg='floral white', fg='blue').place(x=590, y=350)

Label(fresh_frame, text='Username',font=('Goudy old style',13,'bold'), bg='floral white').place(x=500, y=380)
Entry(fresh_frame, font=('Times',20), bd=2, relief='raised', width=20, bg='grey90', textvariable=num1).place(x=500, y=410)

Label(fresh_frame, text='Password',font=('Goudy old style',13,'bold'), bg='floral white').place(x=500, y=450)
Entry(fresh_frame, font=('Times',20), bd=2, relief='raised', width=20, bg='grey90', show='*', textvariable=num2).place(x=500, y=480)

gayathri = 0
a1=ImageTk.PhotoImage(file='reg.jpg')
def forgot_p():
    global n1,a1,fp
    fp = Toplevel()
    fp.geometry('1350x690+0+0')
    fp.title('FORGOT PASSWORD')
    fp.resizable('False','False')
    #a1=ImageTk.PhotoImage(file='reg.jpg')
    Label(fp,image=a1).place(x=0,y=0)
    Frame(fp,bg='mint cream',width=700,height=550).place(x=300,y=100)
    def simplefun1():
        global fresh
        fp.destroy()
        fresh.deiconify()
    #n1 = StringVar()
    Label(fp, text='Enter your username', bg='mint cream', bd=2, relief='flat', font=('Calibri',15)).place(x=350,y=150)
    n1 = Entry(fp,font=('times',20),bg='grey90')
    n1.place(x=350,y=200)

    def Next():
        global n1,n2,n3,rows1,f,gayathri
        f = n1.get()
        con = sql.connect(host = "localhost", user = "root", password = "", database = "project")
        cr = con.cursor()
        cr.execute("Select username from profile_details")
        rows = cr.fetchall()
        con.close()
        
        def n_next():
            global n2,n3,n4,n5,rows1
            f1 = n2.get()
            f2 = n3.get()
            if f1 == rows1[0][1]:
                if f2 == rows1[0][3]:
                    
                    fp_win = Tk()
                    fp_win.title("Change Password")
                    fp_win.geometry('500x400+100+100')
                    def fp_back():
                        global fresh,fp
                        fp_win.destroy()
                        fp.destroy()
                        fresh.deiconify()
                    def fp_next():
                        global n4,n5,rows1,f
                        f4 = n4.get()
                        f5 = n5.get()
                        if len(f4)>=8 and f4.isalnum():
                            if f4==f5:
                                con = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                                cr = con.cursor()
                                cr.execute("UPDATE profile_details SET password='"+str(f5)+"'where username ='"+str(f)+"'")
                                cr.execute('commit')
                                con.close()
                                messagebox.showinfo('Updated','Password successfully changed')
                                Button(fp_win, text='CHANGE', state='disabled', width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=380,y=300)
                            else:
                                messagebox.showerror('Error','Password does not match')
                        else:
                            messagebox.showerror('Error','Enter password correctly')
                            
                    Frame(fp_win, bg='mint cream', width=1500, height=1000).place(x=0,y=0)
                    Label(fp_win, text = 'Enter new password', bg='mint cream', bd=2, relief='flat', font=('Calibri',15)).place(x=40,y=50)
                    n4 = Entry(fp_win,font=('times',20),bg='grey90')
                    n4.place(x=40,y=100)
                    Label(fp_win, text = 'Retype password', bg='mint cream', bd=2, relief='flat', font=('Calibri',15)).place(x=40,y=150)
                    n5 = Entry(fp_win,font=('times',20),bg='grey90')
                    n5.place(x=40,y=200)
                    Button(fp_win, text=' BACK ', command=fp_back, width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=260,y=300)
                    Button(fp_win, text='CHANGE', command=fp_next, width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=380,y=300)
                    
                else:
                    messagebox.showerror('Security question 2','Answer does not match')
            else:
                messagebox.showerror('Security question 1','Answer does not match')

        em_list = []
        for var in range(len(rows)):#rows is a set of usernames
            #em_list += rows[var][0] #em_list is a list of usernames
            if f == rows[var][0]:
                gayathri += 1
                con1 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr1 = con1.cursor()
                cr1.execute("Select sq1,ans1,sq2,ans2 from profile_details where username ='"+str(f)+"'")
                rows1 = cr1.fetchall()
                con1.close()

                n2 = StringVar()
                n3 = StringVar()
                
                Label(fp, text='Security question 1', bg='mint cream', bd=2, relief='flat', font=('Calibri',13)).place(x=350,y=270)
                Label(fp, text=rows1[0][0], bg='mint cream', bd=2, relief='flat', font=('Calibri',15)).place(x=350,y=300)        
                n2 = Entry(fp,font=('times',20),bg='grey90')
                n2.place(x=350,y=340)
                        
                Label(fp, text='Security question 2', bg='mint cream', bd=2, relief='flat', font=('Calibri',13)).place(x=350,y=400)
                Label(fp, text=rows1[0][2], bg='mint cream', bd=2, relief='flat', font=('Calibri',15)).place(x=350,y=440)        
                n3 = Entry(fp,font=('times',20),bg='grey90')
                n3.place(x=350,y=490)
                Button(fp,text='NEXT',command=n_next, width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=830,y=550)
        else:
            if gayathri == 0:
                messagebox.showerror('Error','Username does not exist')
                #print(f)

    
    Button(fp, text='NEXT', command=Next, width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=830,y=550)
    Button(fp, text='BACK', command=simplefun1, width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=710,y=550)
    fp.mainloop()

def forgot():
    global fresh
    fresh.withdraw()
    forgot_p()
Button(fresh_frame, text='Forgot Password ?', font=('Goudy old style',10,'bold'), bg='floral white', fg='blue', relief='flat',command=forgot).place(x=500, y=520)

def about_us():
    window_aboutus = Toplevel(fresh)
    window_aboutus.geometry('830x600+200+30')
    window_aboutus.resizable('False','False')
    
    r1=ImageTk.PhotoImage(file='ab-1.JPG')
    r2=ImageTk.PhotoImage(file='ab-2.JPG')

    Label(window_aboutus, image=r1).place(x=0, y=0)
    Label(window_aboutus, image=r2).place(x=415, y=0)
    window_aboutus.mainloop()
    
def login():
    global num1,num2
    n1=num1.get()
    n2=num2.get()
    con = sql.connect(host = "localhost", user = "root", password = "", database = "project")
    cr = con.cursor()
    cr.execute("Select username,password from profile_details where username ='"+n1+"'")
    rows = cr.fetchall()
    con.close()
    if rows!=[]:
        usern=rows[0][0]
        passn=rows[0][1]        
        if n1 == usern:
            if n2 == passn:
                fresh.destroy()
                booking.login(usern,passn)
            else:
                messagebox.showerror('Error','Incorrect password')
                num2=StringVar()
                Entry(fresh_frame, font=('Times',20), bd=2, relief='raised', width=20, bg='grey90', show='*',textvariable=num2).place(x=500, y=480)            
        else:
            messagebox.showerror('Error','Incorrect username')
            num1=StringVar()
            Entry(fresh_frame, font=('Times',20), bd=2, relief='raised', width=20, bg='grey90',textvariable=num1).place(x=500, y=410)            
    else:
        messagebox.showerror('Error','Username not found')
        num1=StringVar()
        Entry(fresh_frame, font=('Times',20), bd=2, relief='raised', width=20, bg='grey90',textvariable=num1).place(x=500, y=410)
    
Button(fresh, bg='azure', relief='groove', width=7, text=' About Us ', command=about_us, cursor='hand2').place(x=1250, y=20)
Button(fresh, bd=0, image=bt_image, command=login, cursor='hand2', font=('Times',12,'bold'), activebackground='light sky blue').place(x=610, y=540)



def back():
    global fresh, root
    root.destroy()
    fresh.deiconify()

class CustomDateEntry(DateEntry):
    def _select(self, event=None):
        date = self._calendar.selection_get()
        if date is not None:
            self._set_text(date.strftime('%d/%m/%Y'))
            self.event_generate('<<DateEntrySelected>>')
        self._top_cal.withdraw()
        if 'readonly' not in self.state():
            self.focus_set()

def signup():
    global root, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, sq1, sq2, empty, number1, number2, number4, number5, number6, number7, number8, number9, number10, number11, number12, number2_1, number2_2, number2_3, number3_1, number3_2, sq1, sq2, v
    root = Tk()
    root.title('Sign up')
    root.geometry('1350x690+0+0')
    root.configure(bg='light sky blue')
    root.resizable('False','False')    
    
    def check():
        global n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, sq1, sq2, fname, lname, v_radio, ph_num, email, address1, address2, city, pc, state, country, user, pass1, repass, ans1, ans2, empty
        bs="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/\,.-_':;@#%&|*() "
        bs1='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890''.,;":}{[]|\/<>!@#$%^&*()_+=-`~'
        bs2='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
        bs3='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .'
        fname = 0
        s1="select username from profile_details"
        mc=sql.connect(host = "localhost", user = "root", password = "", database = "project")
        cr=mc.cursor()
        cr.execute(s1)
        ur=cr.fetchall()
        emptyn1 = ''
        for aa in n1:
            if aa in bs3:
                emptyn1 += aa
        if emptyn1 == n1:
            fname = 1
        else:
            messagebox.showerror('Error','Enter your firstname correctly')
        if fname==1:    
            lname = 0
            emptyn2 = ''
            for bb in n2:
                if bb in bs3:
                    emptyn2 += bb
            if emptyn2 == n2:
                lname = 1
            else:
                messagebox.showerror('Error','Enter your lastname correctly')
            if lname==1:    
                v_radio = 0
                if n3 == 'Male' or n3 == 'Female' or n3 == 'Others':
                    v_radio = 1
                else:
                    messagebox.showerror('Error','Choose your gender')
                if v_radio==1:                    
                    ph_num = 0
                    if n5.isdigit() and len(n5)==10:
                        ph_num = 1
                    else:
                        messagebox.showerror('Error','Enter your phone number correctly')
                    if ph_num==1:
                        email = 0
                        if (len(n6) >= 16 and n6[-10:] == '@gmail.com') or (len(n6) >= 16 and n6[-10:] == '@yahoo.com') or (len(n6) >= 18 and n6[-12:] == '@hotmail.com') or (len(n6) >= 20 and n6[-15:] == '@rediffmail.com'):
                            email = 1
                        else:
                            messagebox.showerror('Error', 'Enter your valid email ID\nThe local-part of your email ID should be\natleast 6 characters long')
                        if email==1:
                            address1 = 0        
                            emptyn7 = ''
                            for cc in n7:
                                if cc in bs:
                                    emptyn7 += cc
                                    if emptyn7 == n7:
                                        address1 = 1
                                else:
                                    messagebox.showerror('Error','Enter your address1 correctly')
                            if address1==1:
                                address2 = 0
                                emptyn8 = ''
                                for dd in n8:
                                    if dd in bs:
                                        emptyn8 += dd
                                        if emptyn8 == n8:
                                            address2 = 1
                                    else:
                                        messagebox.showerror('Error','Enter your address2 correctly')
                                if address2==1:
                                    city = 0
                                    emptyn9 = ''
                                    for ee in n9:
                                        if ee in bs2:
                                            emptyn9 += ee
                                    if emptyn9 == n9:
                                        city = 1
                                    else:
                                        messagebox.showerror('Error','Enter your city correctly')
                                    if city==1:
                                        pc = 0
                                        if n10.isdigit() and len(n10)==6:
                                            pc = 1
                                        else:
                                            messagebox.showerror('Error','Enter your pincode correctly')
                                        if pc==1:
                                            state = 0
                                            emptyn11 = ''
                                            for ff in n11:
                                                if ff in bs2:
                                                    emptyn11 += ff
                                            if emptyn11 == n11:
                                                state = 1
                                            else:
                                                messagebox.showerror('Error','Enter your state correctly')
                                            if state==1:
                                                country = 0
                                                emptyn12 = ''
                                                for gg in n12:
                                                    if gg in bs2:
                                                        emptyn12 += gg
                                                if emptyn12 == n12:
                                                    country = 1
                                                else:
                                                    messagebox.showerror('Error','Enter your country correctly')
                                                if country == 1:
                                                    user = 0        
                                                    emptyu = ''
                                                    d = 0
                                                    for hh in range(len(ur)):
                                                        if n13 == ur[hh][0]:
                                                            d += 1
                                                    if d >= 1:
                                                        messagebox.showerror('Error','Username already exists')
                                                    else:
                                                        if len(n13) >= 8:
                                                            for ii in n13:
                                                                if ii in bs1:
                                                                    emptyu += ii
                                                                    if emptyu == n13:
                                                                        user = 1
                                                                else:
                                                                    messagebox.showerror('Error','Enter your username correctly')
                                                        else:
                                                            messagebox.showerror('Error','Your username should be minimum 8 characters length')
                                                        
                                                        if user == 1:
                                                            pass1 = 0
                                                            emptyp = ''
                                                            if len(n14) >= 8:
                                                                for x in n14:
                                                                    if x in bs1:
                                                                        emptyp += x
                                                                        if emptyp == n14:
                                                                            pass1 = 1
                                                                    else:
                                                                       messagebox.showerror('Error','Enter your password correctly') 
                                                            else:
                                                                messagebox.showerror('Error','Your password should be minimum 8 characters length')
                                                            if pass1==1:
                                                                repass = 0
                                                                if n14==n15:
                                                                    repass = 1
                                                                else:
                                                                    messagebox.showerror('Error','Password does not match')
                                                                if repass==1:
                                                                    ans1 = 0
                                                                    emptya1 = ''
                                                                    for y in n17:
                                                                        if y in bs:
                                                                            emptya1 += y
                                                                            if emptya1 == n17:
                                                                                ans1 = 1
                                                                        else:
                                                                            messagebox.showerror('Error','Enter your answer1 correctly')
                                                                    if ans1==1:
                                                                        ans2 = 0
                                                                        emptya2 = ''
                                                                        for z in n19:
                                                                            if z in bs:
                                                                                emptya2 += z
                                                                                if emptya2 == n19:
                                                                                    ans2 = 1
                                                                            else:
                                                                                messagebox.showerror('Error','Enter your answer2 correctly')
                        
    def submit():
        global n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, fname, lname, v_radio, ph_num, email, address1, address2, city, pc, state, country, user, pass1, repass, ans1, ans2, empty, number1, number2, number4, number5, number6, number7, number8, number9, number10, number11, number12, number2_1, number2_2, number2_3, number3_1, number3_2, sq1, sq2, v
        n1 = number1.get()        
        n2 = number2.get()
        n3 = g_field.get()
        n4 = number4.get()
        n5 = number5.get()
        n6 = number6.get()
        n7 = number7.get()
        n8 = number8.get()
        n9 = number9.get()
        n10 = number10.get()
        n11 = number11.get()
        n12 = number12.get()
        n13 = number2_1.get()
        n14 = number2_2.get()
        n15 = number2_3.get()       
        n16 = sq1_field.get()
        n17 = number3_1.get()
        n18 = sq2_field.get()
        n19 = number3_2.get()
        if n1 !='' and n2 !='' and n3 !='' and n4 !='' and n5 !='' and n6 !='' and n7 !='' and n8 !='' and n9 !='' and n10 !='' and n11 !='' and n12 !='' and n13 !='' and n14 !='' and n15 !='' and n16 !='' and n17 !='' and n18 !='' and n19 !='':
            check()
            if fname == 1 and lname == 1 and v_radio == 1 and ph_num == 1 and email == 1 and address1 == 1 and address2 == 1 and city == 1 and pc == 1 and state == 1 and country == 1 and user == 1 and pass1 == 1 and repass == 1 and ans1 == 1 and ans2 == 1:
                con = sql.connect(host = "localhost", user = "root", password="", database = "project")
                cr = con.cursor()
                cr.execute("insert into profile_details values('"+str(n1)+"','"+str(n2)+"','"+str(n3)+"','"+str(n4)+"','"+str(n5)+"','"+str(n6)+"','"+str(n7)+"','"+str(n8)+"','"+str(n9)+"',"+n10+",'"+str(n11)+"','"+str(n12)+"','"+str(n16)+"','"+str(n17)+"','"+str(n18)+"','"+str(n19)+"','"+str(n13)+"','"+str(n14)+"')")
                cr.execute("commit")
                con.close()
                messagebox.showinfo('Submitted', 'Hello '+n1+' '+n2+'\nYour details are submitted')
                Button(second, text='SUBMIT', bd=2, relief='raised',state='disabled', width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=560, y=1120)
        else:
            print(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19)
            messagebox.showerror('Error', 'All fields are required')
    
    mycanvas = Canvas(root, bg='light sky blue')
    mycanvas.pack(side=LEFT, fill=Y)
    s = ttk.Scrollbar(root, orient='vertical', command=mycanvas.yview)
    s.pack(side=RIGHT, fill=Y)
    mycanvas.config(yscrollcommand=s.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.config(scrollregion=mycanvas.bbox('all')))
    second = Frame(mycanvas)
    mycanvas.create_window((0,0), window=second, anchor='nw')

    Frame(second, width=1250, height=1200, bg='light sky blue').pack()
    #-------------------------------FIRST LAST NAME-------------------------------
    Label(second, text='REGISTER HERE', bg='light sky blue', font=('Verdana bold',20)).place(x=480, y=40)
    Label(second, font=('Verdana',15), text='FIRST NAME', bg='light sky blue').place(x=55, y=160)
    number1 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number1.place(x=250, y=160)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='LAST NAME').place(x=680, y=160)
    number2 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number2.place(x=900, y=160)

    #-------------------------------DOB GENDER-------------------------------
    Label(second, bg='light sky blue', font=('Verdana',15), text='GENDER').place(x=70, y=240)
    g_field = ttk.Combobox(second, font=('times new roman',12), state='readonly', justify=CENTER)
    g_field['values'] = ['Male','Female','Others']
    g_field.place(x=250, y=240, width=250)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='DATE OF BIRTH').place(x=660, y=240)
    number4 = CustomDateEntry(second, width=22, font=('Helvetica',15))
    number4._set_text(number4._date.strftime('%d/%m/%Y'))
    number4.place(x=900, y=240)
    
    #-------------------------------NUMBER MAIL-------------------------------
    Label(second, bg='light sky blue', font=('Verdana',15), text='PHONE NUMBER').place(x=30, y=320)
    number5 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number5.place(x=250, y=320)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='EMAIL ID').place(x=680, y=320)
    number6 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number6.place(x=900, y=320)
    
    #-------------------------------ADDRESS-------------------------------
    Label(second, bg='light sky blue', font=('Verdana',15), text='ADDRESS1').place(x=55, y=400)
    number7 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number7.place(x=250, y=400)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='ADDRESS2').place(x=680, y=400)
    number8 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number8.place(x=900, y=400)
    Frame(mycanvas, width=1250, bg='light sky blue').pack(pady=100)
    
    #------------------------------CITY PINCODE-------------------------------
    Label(second, bg='light sky blue', font=('Verdana',15), text='CITY').place(x=70, y=480)
    number9 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number9.place(x=250, y=480)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='PIN CODE').place(x=680, y=480)
    number10 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number10.place(x=900, y=480)
    
    #-------------------------------STATE COUNTRY-------------------------------
    Label(second, bg='light sky blue', font=('Verdana',15), text='STATE').place(x=70, y=560)
    number11 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number11.place(x=250, y=560)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='COUNTRY').place(x=680, y=560)
    number12 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number12.place(x=900, y=560)
    
    #-------------------------------USER DETAILS-------------------------------
    Label(second, bg='light sky blue', font=('Verdana',15), text='USERNAME').place(x=50, y=720)
    number2_1 = Entry(second, bd=2, relief='groove', width=30, font=('Helvetica',18))
    number2_1.place(x=250, y=720)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='PASSWORD').place(x=50, y=800)
    number2_2 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number2_2.place(x=250, y=800)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='RETYPE PASSWORD').place(x=660, y=800)
    number2_3 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number2_3.place(x=900, y=800)
    
    #-------------------------------SECURITY QUESTION 1-------------------------------
    Label(second, bg='light sky blue', font=('Verdana',15), text='SECURITY QUESTION 1').place(x=30, y=960)
    sq1_field = ttk.Combobox(second, font=('times new roman',12), state='readonly', justify=CENTER)
    sq1_field['values'] = ['What was your childhood nickname?','What is the name of your favorite sports team?','What is the name of your first teacher?','Who was your childhood hero?','What is the last 3 digits of your phone number?']
    sq1_field.place(x=300, y=960, width=300)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='ANSWER 1').place(x=700, y=960)
    number3_1 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number3_1.place(x=900, y=960)
    
    #-------------------------------SECURITY QUESTION 2-------------------------------
    Label(second, bg='light sky blue', font=('Verdana',15), text='SECURITY QUESTION 2').place(x=30, y=1040)
    sq2_field = ttk.Combobox(second, font=('times new roman',12), state='readonly', justify=CENTER)
    sq2_field['values'] = ['What is your favorite website?','What street did you grow up on?','What high school did you attend?','Which pet would you love to have?','What is the name of your college?']
    sq2_field.place(x=300, y=1040, width=300)
    
    Label(second, bg='light sky blue', font=('Verdana',15), text='ANSWER 2').place(x=700, y=1040)
    number3_2 = Entry(second, bd=2, relief='groove', width=20, font=('Helvetica',18))
    number3_2.place(x=900, y=1040)

    Button(second, text=' BACK ', bd=2, relief='raised', command=back, width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=400, y=1120)
    Button(second, text='SUBMIT', bd=2, relief='raised', command=submit, width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=560, y=1120)
    root.mainloop()

def sign_up():
    global fresh
    fresh.withdraw()
    signup()
    
my_font = Font(family='Times New Roman', size=40, weight='bold')
Label(fresh, text='Welcome to Escape\nTravels', font=my_font, bg='mint cream').place(x=440, y=130)
Label(fresh, text="Don't have an account?", bg='mint cream', fg='blue', font=('Goudy old style',11,'bold')).place(x=720, y=590)
Button(fresh, text='Sign up',width=7, command=sign_up, bg='mint cream', fg='blue', font=('Goudy old style',12,'bold'), cursor='hand2', relief='flat', activebackground='azure').place(x=770, y=610)
