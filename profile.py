from tkinter import *
from tkinter import messagebox
import tkcalendar as tkc
import mysql.connector as sql
import booking

def view_profile(usern,passn):
    global numb1, numb2, numb3, numb4, numb5, numb6, numb7, numb8, numb9, numb10, numb11, numb12, Usern, Passn
    Usern = usern
    Passn = passn
    window_profile = Tk()
    window_profile.geometry('1350x690+0+0')
    window_profile.configure(bg='mint cream')
    window_profile.resizable('False','False')
    window_profile.title('MY PROFILE')
    Frame(window_profile, bg='mint cream', width=1270, height=650).place(x=0, y=0)
    
    con = sql.connect(host = "localhost", user = "root", password = "", database = "project")
    cr = con.cursor()
    cr.execute("Select * from profile_details where username ='"+Usern+"'")
    rows = cr.fetchall()
    con.close()

    Label(window_profile, text='MY PROFILE', bg='mint cream', font=('Verdana bold',15)).place(x=550, y=20)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='FIRST NAME').place(x=55, y=100)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='LAST NAME').place(x=680, y=100)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='GENDER').place(x=70, y=180)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='DATE OF BIRTH').place(x=660, y=180)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='PHONE NUMBER').place(x=30, y=260)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='EMAIL ID').place(x=680, y=260)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='ADDRESS1').place(x=55, y=340)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='ADDRESS2').place(x=680, y=340)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='CITY').place(x=70, y=420)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='PINCODE').place(x=680, y=420)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='STATE').place(x=70, y=500)
    Label(window_profile, bg='mint cream', font=('Verdana',15), text='COUNTRY').place(x=680, y=500)

    numb1 = StringVar()  
    numb2 = StringVar() 
    numb3 = StringVar()
    numb4 = StringVar()
    numb5 = StringVar()
    numb6 = StringVar()
    numb7 = StringVar()
    numb8 = StringVar()
    numb9 = StringVar()
    numb10 = StringVar()
    numb11 = StringVar()
    numb12 = StringVar()

    def button_hover(e):
        Label(window_profile, text=' DD / MM / YYYY ', bg='light yellow', font=('Calibri',13)).place(x=950, y=215)
    def button_hover_leave(e):
        Label(window_profile,text='                                 ', bg='mint cream', font=('Calibri',13)).place(x=950, y=215)

    entry1 = Entry(window_profile, textvariable=numb1, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry1.place(x=280, y=100)
    entry1.insert(0, rows[0][0])
    entry2 = Entry(window_profile, textvariable=numb2, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry2.place(x=905, y=100)
    entry2.insert(0, rows[0][1])
    entry3 = Entry(window_profile, textvariable=numb3, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry3.place(x=280, y=180)
    entry3.insert(0, rows[0][2])
    entry4 = Entry(window_profile, textvariable=numb4, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry4.place(x=905, y=180)
    entry4.insert(0, rows[0][3])
    entry4.bind('<Enter>',button_hover)
    entry4.bind('<Leave>',button_hover_leave)
    entry5 = Entry(window_profile, textvariable=numb5, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry5.place(x=280, y=260)
    entry5.insert(0, rows[0][4])
    entry6 = Entry(window_profile, textvariable=numb6, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry6.place(x=905, y=260)
    entry6.insert(0, rows[0][5])
    entry7 = Entry(window_profile, textvariable=numb7, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry7.place(x=280, y=340)
    entry7.insert(0, rows[0][6])
    entry8 = Entry(window_profile, textvariable=numb8, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry8.place(x=905, y=340)
    entry8.insert(0, rows[0][7])
    entry9 = Entry(window_profile, textvariable=numb9, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry9.place(x=280, y=420)
    entry9.insert(0, rows[0][8])
    entry10 = Entry(window_profile, textvariable=numb10, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry10.place(x=905, y=420)
    entry10.insert(0, rows[0][9])
    entry11 = Entry(window_profile, textvariable=numb11, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry11.place(x=280, y=500)
    entry11.insert(0, rows[0][10])
    entry12 = Entry(window_profile, textvariable=numb12, bd=2, relief='groove', width=20, font=('Helvetica',18))
    entry12.place(x=905, y=500)
    entry12.insert(0, rows[0][11])

    def check():
        global nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9, nb10, nb11, nb12, fname, lname, v_radio, date, ph_num, email, address1, address2, city, pc, state, country, empty
        bs='''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 /\,.-_'":;@#%&|*() '''
        bs1='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'' .,;":}{[]|\/<>!@#$%^&*()_+=-`~ '
        bs2='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
        bs3='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .'
        fname = 0
        emptynb1 = ''
        for aa in nb1:
            if aa in bs3:
                emptynb1 += aa
        if emptynb1 == nb1:
            fname = 1
        else:
            messagebox.showerror('Error','Enter your firstname correctly')
        if fname==1:    
            emptynb2 = ''
            for bb in nb2:
                if bb in bs3:
                    emptynb2 += bb
            if emptynb2 == nb2:
                lname = 1
            else:
                messagebox.showerror('Error','Enter your lastname correctly')
            if lname==1:    
                v_radio = 0
                if nb3=='Female' or nb3=='female' or nb3=='Male' or nb3=='male' or nb3=='Others' or nb3=='others':
                    v_radio = 1
                else:
                    messagebox.showerror('Error','Enter your gender\nMale or Female or Others')
                if v_radio==1:
                    date = 0
                    if len(nb4)==10 and nb4[2]=='/' and nb4[5]=='/':
                        date = 1
                    else:
                        messagebox.showerror('Error','Enter your date of birth correctly\nIt should be of the format DD/MM/YYYY')
                    if date==1:
                        ph_num = 0
                        if nb5.isdigit() and len(nb5)==10:
                            ph_num = 1
                        else:
                            messagebox.showerror('Error','Enter your phone number correctly')
                        if ph_num==1:
                            email = 0
                            if (len(nb6) >= 16 and nb6[-10:] == '@gmail.com') or (len(nb6) >= 16 and nb6[-10:] == '@yahoo.com') or (len(nb6) >= 18 and nb6[-12:] == '@hotmail.com') or (len(nb6) >= 20 and nb6[-15:] == '@rediffmail.com'):
                                email = 1
                            else:
                                messagebox.showerror('Error', 'The local-part of your email ID should be\natleast 6 characters long')
                            if email==1:
                                address1 = 0        
                                emptyn7 = ''
                                for i in nb7:
                                    if i in bs:
                                        emptyn7 += i
                                        if emptyn7 == nb7:
                                            address1 = 1
                                    else:
                                        messagebox.showerror('Error','Enter your address1 correctly')
                                if address1==1:
                                    address2 = 0
                                    emptyn8 = ''
                                    for j in nb8:
                                        if j in bs:
                                            emptyn8 += j
                                            if emptyn8 == nb8:
                                                address2 = 1
                                        else:
                                            messagebox.showerror('Error','Enter your address2 correctly')
                                    if address2==1:
                                        city = 0
                                        emptynb9 = ''
                                        for ee in nb9:
                                            if ee in bs2:
                                                emptynb9 += ee
                                        if emptynb9 == nb9:
                                            city = 1
                                        else:
                                            messagebox.showerror('Error','Enter your city correctly')
                                        if city==1:
                                            pc = 0
                                            if nb10.isdigit() and len(nb10)==6:
                                                pc = 1
                                            else:
                                                messagebox.showerror('Error','Enter your pincode correctly')
                                            if pc==1:
                                                state = 0
                                                emptynb11 = ''
                                                for ff in nb11:
                                                    if ff in bs2:
                                                        emptynb11 += ff
                                                if emptynb11 == nb11:
                                                    state = 1
                                                else:
                                                    messagebox.showerror('Error','Enter your state correctly')
                                                if state==1:
                                                    country = 0
                                                    emptynb12 = ''
                                                    for gg in nb12:
                                                        if gg in bs2:
                                                            emptynb12 += gg
                                                    if emptynb12 == nb12:
                                                        country = 1
                                                    else:
                                                        messagebox.showerror('Error','Enter your country correctly')
                                                   
    def change():
        global rows, user, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9, nb10, nb11, nb12, fname, lname, v_radio, date, ph_num, email, address1, address2, city, pc, state, country, empty, numb1, numb2, numb3, numb4, numb5, numb6, numb7, numb8, numb9, numb10, numb11, numb12, Usern
        nb1 = numb1.get()
        nb2 = numb2.get()
        nb3 = numb3.get()
        nb4 = numb4.get()
        nb5 = numb5.get()
        nb6 = numb6.get()
        nb7 = numb7.get()
        nb8 = numb8.get()
        nb9 = numb9.get()
        nb10 = numb10.get()
        nb11 = numb11.get()
        nb12 = numb12.get()
        if nb1 != '' and nb2 != '' and nb3 != '' and nb4 != '' and nb5 != '' and nb6 != '' and nb7 != '' and nb8 != '' and nb9 != '' and nb10 != '' and nb11 != '' and nb12 != '' :
            check()        
            if fname == 1 and lname == 1 and v_radio == 1 and date == 1 and ph_num == 1 and email == 1 and address1 == 1 and address2 == 1 and city == 1 and pc == 1 and state == 1 and country == 1:
                con1 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr1 = con1.cursor()
                cr1.execute("update profile_details set firstname='"+nb1+"' where username='"+Usern+"'")
                cr1.execute("commit")
                con1.close()
                
                con2 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr2 = con2.cursor()
                cr2.execute("update profile_details set lastname='"+nb2+"' where username='"+Usern+"'")
                cr2.execute("commit")
                con2.close()
                
                con3 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr3 = con3.cursor()
                cr3.execute("update profile_details set gender='"+nb3+"' where username='"+Usern+"'")
                cr3.execute("commit")
                con3.close()

                con4 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr4 = con4.cursor()
                cr4.execute("update profile_details set dob='"+nb4+"' where username='"+Usern+"'")
                cr4.execute("commit")
                con4.close()

                con5 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr5 = con5.cursor()
                cr5.execute("update profile_details set ph_num='"+nb5+"' where username='"+Usern+"'")
                cr5.execute("commit")
                con5.close()

                con6 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr6 = con6.cursor()
                cr6.execute("update profile_details set email='"+nb6+"' where username='"+Usern+"'")
                cr6.execute("commit")
                con6.close()
                
                con7 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr7 = con7.cursor()
                cr7.execute("update profile_details set address='"+nb7+"' where username='"+Usern+"'")
                cr7.execute("commit")
                con7.close()
                
                con8 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr8 = con8.cursor()
                cr8.execute("update profile_details set address2='"+nb8+"' where username='"+Usern+"'")
                cr8.execute("commit")
                con8.close()

                con9 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr9 = con9.cursor()
                cr9.execute("update profile_details set city='"+nb9+"' where username='"+Usern+"'")
                cr9.execute("commit")
                con9.close()

                con10 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr10 = con10.cursor()
                cr10.execute("update profile_details set p_c='"+nb10+"' where username='"+Usern+"'")
                cr10.execute("commit")            
                con10.close()

                con11 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr11 = con11.cursor()
                cr11.execute("update profile_details set state='"+nb11+"' where username='"+Usern+"'")
                cr11.execute("commit")
                con11.close()

                con12 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                cr12 = con12.cursor()
                cr12.execute("update profile_details set country='"+nb12+"' where username='"+Usern+"'")
                cr12.execute("commit")
                con12.close()
                messagebox.showinfo('Changed', 'Your profile has been updated')
            #else:
                #print(fname, lname, v_radio, date, ph_num, email, address1, address2, city, pc, state, country)
        else:
            messagebox.showerror('Error', 'All fields are required')

    def back():
        window_profile.destroy()
        booking.login(Usern,Passn)
    Button(window_profile, text=' BACK ', bd=2, relief='raised', command=back, width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=450, y=580)
    Button(window_profile, text='CHANGE', bd=2, relief='raised', command=change, width=9, bg='grey90', font=('Calibri',13), cursor='hand2').place(x=610, y=580)
#view_profile('qwerqwer','qwerqwer')

