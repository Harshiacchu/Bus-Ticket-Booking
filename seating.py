from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as sql
from PIL import ImageTk
import random
import time
import booking

def third_win(str_viewseats, girl, f1 ,t1 ,d1, Usern, Passn):    
    global window, variable, List, Str_viewseats, time_list, v, i, def_age, Name, Age, Price, v, r, R, otp, dc_no, def_dcno, cvv, def_cvv, cr_no, def_crno, Cvv, def_Cvv, F1, T1, D1, usern, passn
    Str_viewseats = str_viewseats
    GIRL = girl
    F1 = f1
    T1 = t1
    D1 = d1
    usern = Usern
    passn = Passn
   
    window = Tk()
    window.title('Escape Bus Travels')
    window.geometry('870x690+0+0')
    window.resizable(width='False', height='False')
    #imag = ImageTk.PhotoImage(file='D:\\Gayathri Srinivasan\\Python programs\\Project\\Images\\bus.jpg')
    #Label(window, image=imag).place(x=0, y=0)
    Frame(window, bg='mint cream', width=870, height=630).place(x=0, y=0)
    window.configure(bg='mint cream')

    Label(window, text='Book your seats..', bg='mint cream', font=('Verdana',20)).place(x=210, y=20)
    variable = 0
    v = IntVar()
    List = []
    time_list=[]
    colour_list = []

    con1 = sql.connect(host = "localhost", user = "root", password = "", database =" project")
    cr1 = con1.cursor()
    cr1.execute("select * from colour"+str(GIRL))
    #cr1.execute("commit")
    rows1 = cr1.fetchall()
    con1.close()
    for some in range(len(rows1)):
        some1 = rows1[some][0].split(',')
        some2 = some1[0:len(some1)-1]
        colour_list += some2
    #print(colour_list)
    def row1_1():
        global variable, List, colour_list        
        Button(window, text='A1', width=4, bg='grey90', font=('Calibri',13), command=click_1_1).place(x=100, y=90)
        List.remove('A1')
        variable -= 1
    def row1_2():
        global variable, List, colour_list
        Button(window, text='A2', width=4, bg='grey90', font=('Calibri',13), command=click_1_2).place(x=180, y=90)
        List.remove('A2')
        variable -= 1
    def row1_3():
        global variable, List, colour_list
        Button(window, text='A3', width=4, bg='grey90', font=('Calibri',13), command=click_1_3).place(x=340, y=90)
        List.remove('A3')
        variable -= 1
    def row1_4():
        global variable, List, colour_list
        Button(window, text='A4', width=4, bg='grey90', font=('Calibri',13), command=click_1_4).place(x=420, y=90)
        List.remove('A4')
        variable -= 1 
    def row1_5():
        global variable, List, colour_list
        Button(window, text='A5', width=4, bg='grey90', font=('Calibri',13), command=click_1_5).place(x=500, y=90)
        List.remove('A5')
        variable -= 1

    def row2_1():
        global variable, List, colour_list
        Button(window, text='B1', width=4, bg='grey90', font=('Calibri',13), command=click_2_1).place(x=100, y=160)
        List.remove('B1')
        variable -= 1     
    def row2_2():
        global variable, List, colour_list
        Button(window, text='B2', width=4, bg='grey90', font=('Calibri',13), command=click_2_2).place(x=180, y=160)
        List.remove('B2')
        variable -= 1
    def row2_3():
        global variable, List, colour_list
        Button(window, text='B3', width=4, bg='grey90', font=('Calibri',13), command=click_2_3).place(x=340, y=160)
        List.remove('B3')
        variable -= 1
    def row2_4():
        global variable, List, colour_list
        Button(window, text='B4', width=4, bg='grey90', font=('Calibri',13), command=click_2_4).place(x=420, y=160)
        List.remove('B4')
        variable -= 1
    def row2_5():
        global variable, List, colour_list
        Button(window, text='B5', width=4, bg='grey90', font=('Calibri',13), command=click_2_5).place(x=500, y=160)
        List.remove('B5')
        variable -= 1

    def row3_1():
        global variable, List, colour_list
        Button(window, text='C1', width=4, bg='grey90', font=('Calibri',13), command=click_3_1).place(x=100, y=230)
        List.remove('C1')
        variable -= 1     
    def row3_2():
        global variable, List, colour_list
        Button(window, text='C2', width=4, bg='grey90', font=('Calibri',13), command=click_3_2).place(x=180, y=230)
        List.remove('C2')
        variable -= 1
    def row3_3():
        global variable, List, colour_list
        Button(window, text='C3', width=4, bg='grey90', font=('Calibri',13), command=click_3_3).place(x=340, y=230)
        List.remove('C3')
        variable -= 1
    def row3_4():
        global variable, List, colour_list
        Button(window, text='C4', width=4, bg='grey90', font=('Calibri',13), command=click_3_4).place(x=420, y=230)
        List.remove('C4')
        variable -= 1
    def row3_5():
        global variable, List, colour_list
        Button(window, text='C5', width=4, bg='grey90', font=('Calibri',13), command=click_3_5).place(x=500, y=230)
        List.remove('C5')
        variable -= 1

    def row4_1():
        global variable, List, colour_list
        Button(window, text='D1', width=4, bg='grey90', font=('Calibri',13), command=click_4_1).place(x=100, y=300)
        List.remove('D1')
        variable -= 1     
    def row4_2():
        global variable, List, colour_list
        Button(window, text='D2', width=4, bg='grey90', font=('Calibri',13), command=click_4_2).place(x=180, y=300)
        List.remove('D2')
        variable -= 1
    def row4_3():
        global variable, List, colour_list
        Button(window, text='D3', width=4, bg='grey90', font=('Calibri',13), command=click_4_3).place(x=340, y=300)
        List.remove('D3')
        variable -= 1
    def row4_4():
        global variable, List, colour_list
        Button(window, text='D4', width=4, bg='grey90', font=('Calibri',13), command=click_4_4).place(x=420, y=300)
        List.remove('D4')
        variable -= 1
    def row4_5():
        global variable, List, colour_list
        Button(window, text='D5', width=4, bg='grey90', font=('Calibri',13), command=click_4_5).place(x=500, y=300)
        List.remove('D5')
        variable -= 1

    def row5_1():
        global variable, List, colour_list
        Button(window, text='E1', width=4, bg='grey90', font=('Calibri',13), command=click_5_1).place(x=100, y=370)
        List.remove('E1')
        variable -= 1     
    def row5_2():
        global variable, List, colour_list
        Button(window, text='E2', width=4, bg='grey90', font=('Calibri',13), command=click_5_2).place(x=180, y=370)
        List.remove('E2')
        variable -= 1
    def row5_3():
        global variable, List, colour_list
        Button(window, text='E3', width=4, bg='grey90', font=('Calibri',13), command=click_5_3).place(x=340, y=370)
        List.remove('E3')
        variable -= 1
    def row5_4():
        global variable, List, colour_list
        Button(window, text='E4', width=4, bg='grey90', font=('Calibri',13), command=click_5_4).place(x=420, y=370)
        List.remove('E4')
        variable -= 1
    def row5_5():
        global variable, List, colour_list
        Button(window, text='E5', width=4, bg='grey90', font=('Calibri',13), command=click_5_5).place(x=500, y=370)
        List.remove('E5')
        variable -= 1

    def row6_1():
        global variable, List, colour_list
        Button(window, text='F1', width=4, bg='grey90', font=('Calibri',13), command=click_6_1).place(x=100, y=440)
        List.remove('F1')
        variable -= 1     
    def row6_2():
        global variable, List, colour_list
        Button(window, text='F2', width=4, bg='grey90', font=('Calibri',13), command=click_6_2).place(x=180, y=440)
        List.remove('F2')
        variable -= 1
    def row6_3():
        global variable, List, colour_list
        Button(window, text='F3', width=4, bg='grey90', font=('Calibri',13), command=click_6_3).place(x=340, y=440)
        List.remove('F3')
        variable -= 1
    def row6_4():
        global variable, List, colour_list
        Button(window, text='F4', width=4, bg='grey90', font=('Calibri',13), command=click_6_4).place(x=420, y=440)
        List.remove('F4')
        variable -= 1
    def row6_5():
        global variable, List, colour_list
        Button(window, text='F5', width=4, bg='grey90', font=('Calibri',13), command=click_6_5).place(x=500, y=440)
        List.remove('F5')
        variable -= 1

    def row7_1():
        global variable, List, colour_list
        Button(window, text='G1', width=4, bg='grey90', font=('Calibri',13), command=click_7_1).place(x=100, y=510)
        List.remove('G1')
        variable -= 1     
    def row7_2():
        global variable, List, colour_list
        Button(window, text='G2', width=4, bg='grey90', font=('Calibri',13), command=click_7_2).place(x=180, y=510)
        List.remove('G2')
        variable -= 1
    def row7_3():
        global variable, List, colour_list
        Button(window, text='G3', width=4, bg='grey90', font=('Calibri',13), command=click_7_3).place(x=260, y=510)
        List.remove('G3')
        variable -= 1
    def row7_4():
        global variable, List, colour_list
        Button(window, text='G4', width=4, bg='grey90', font=('Calibri',13), command=click_7_4).place(x=340, y=510)
        List.remove('G4')
        variable -= 1 
    def row7_5():
        global variable, List, colour_list
        Button(window, text='G5', width=4, bg='grey90', font=('Calibri',13), command=click_7_5).place(x=420, y=510)
        List.remove('G5')
        variable -= 1
    def row7_6():
        global variable, List, colour_list
        Button(window, text='G6', width=4, bg='grey90', font=('Calibri',13), command=click_7_6).place(x=500, y=510)
        List.remove('G6')
        variable -= 1


    def click_1_1():
        global variable, List, colour_list        
        Button(window, text='A1', width=4, bg='green2', font=('Calibri',13), command=row1_1).place(x=100, y=90)
        List += ['A1']
        variable += 1  
    def click_1_2():
        global variable, List, colour_list
        Button(window, text='A2', width=4, bg='green2', font=('Calibri',13), command=row1_2).place(x=180, y=90)
        List += ['A2']
        variable += 1
    def click_1_3():
        global variable, List, colour_list
        Button(window, text='A3', width=4, bg='green2', font=('Calibri',13), command=row1_3).place(x=340, y=90)
        List += ['A3']
        variable += 1
    def click_1_4():
        global variable, List, colour_list
        Button(window, text='A4', width=4, bg='green2', font=('Calibri',13), command=row1_4).place(x=420, y=90)
        List += ['A4']
        variable += 1
    def click_1_5():
        global variable, List, colour_list
        Button(window, text='A5', width=4, bg='green2', font=('Calibri',13), command=row1_5).place(x=500, y=90)
        List += ['A5']
        variable += 1
        
    def click_2_1():
        global variable, List, colour_list
        Button(window, text='B1', width=4, bg='green2', font=('Calibri',13), command=row2_1).place(x=100, y=160)
        List += ['B1']
        variable += 1
    def click_2_2():
        global variable, List, colour_list
        Button(window, text='B2', width=4, bg='green2', font=('Calibri',13), command=row2_2).place(x=180, y=160)
        List += ['B2']
        variable += 1
    def click_2_3():
        global variable, List, colour_list
        Button(window, text='B3', width=4, bg='green2', font=('Calibri',13), command=row2_3).place(x=340, y=160)
        List += ['B3']
        variable += 1
    def click_2_4():
        global variable, List, colour_list
        Button(window, text='B4', width=4, bg='green2', font=('Calibri',13), command=row2_4).place(x=420, y=160)
        List += ['B4']
        variable += 1
    def click_2_5():
        global variable, List, colour_list
        Button(window, text='B5', width=4, bg='green2', font=('Calibri',13), command=row2_5).place(x=500, y=160)
        List += ['B5']
        variable += 1
        
    def click_3_1():
        global variable, List, colour_list
        Button(window, text='C1', width=4, bg='green2', font=('Calibri',13), command=row3_1).place(x=100, y=230)
        List += ['C1']
        variable += 1
    def click_3_2():
        global variable, List, colour_list
        Button(window, text='C2', width=4, bg='green2', font=('Calibri',13), command=row3_2).place(x=180, y=230)
        List += ['C2']
        variable += 1
    def click_3_3():
        global variable, List, colour_list
        Button(window, text='C3', width=4, bg='green2', font=('Calibri',13), command=row3_3).place(x=340, y=230)
        List += ['C3']
        variable += 1
    def click_3_4():
        global variable, List, colour_list
        Button(window, text='C4', width=4, bg='green2', font=('Calibri',13), command=row3_4).place(x=420, y=230)
        List += ['C4']
        variable += 1
    def click_3_5():
        global variable, List, colour_list
        Button(window, text='C5', width=4, bg='green2', font=('Calibri',13), command=row3_5).place(x=500, y=230)
        List += ['C5']
        variable += 1
        
    def click_4_1():
        global variable, List, colour_list
        Button(window, text='D1', width=4, bg='green2', font=('Calibri',13), command=row4_1).place(x=100, y=300)
        List += ['D1']
        variable += 1
    def click_4_2():
        global variable, List, colour_list
        Button(window, text='D2', width=4, bg='green2', font=('Calibri',13), command=row4_2).place(x=180, y=300)
        List += ['D2']
        variable += 1
    def click_4_3():
        global variable, List, colour_list
        Button(window, text='D3', width=4, bg='green2', font=('Calibri',13), command=row4_3).place(x=340, y=300)
        List += ['D3']
        variable += 1
    def click_4_4():
        global variable, List, colour_list
        Button(window, text='D4', width=4, bg='green2', font=('Calibri',13), command=row4_4).place(x=420, y=300)
        List += ['D4']
        variable += 1
    def click_4_5():
        global variable, List, colour_list
        Button(window, text='D5', width=4, bg='green2', font=('Calibri',13), command=row4_5).place(x=500, y=300)
        List += ['D5']
        variable += 1
        
    def click_5_1():
        global variable, List, colour_list
        Button(window, text='E1', width=4, bg='green2', font=('Calibri',13), command=row5_1).place(x=100, y=370)
        List += ['E1']
        variable += 1
    def click_5_2():
        global variable, List, colour_list
        Button(window, text='E2', width=4, bg='green2', font=('Calibri',13), command=row5_2).place(x=180, y=370)
        List += ['E2']
        variable += 1
    def click_5_3():
        global variable, List, colour_list
        Button(window, text='E3', width=4, bg='green2', font=('Calibri',13), command=row5_3).place(x=340, y=370)
        List += ['E3']
        variable += 1
    def click_5_4():
        global variable, List, colour_list
        Button(window, text='E4', width=4, bg='green2', font=('Calibri',13), command=row5_4).place(x=420, y=370)
        List += ['E4']
        variable += 1
    def click_5_5():
        global variable, List, colour_list
        Button(window, text='E5', width=4, bg='green2', font=('Calibri',13), command=row5_5).place(x=500, y=370)
        List += ['E5']
        variable += 1
        
    def click_6_1():
        global variable, List, colour_list
        Button(window, text='F1', width=4, bg='green2', font=('Calibri',13), command=row6_1).place(x=100, y=440)
        List += ['F1']
        variable += 1
    def click_6_2():
        global variable, List, colour_list
        Button(window, text='F2', width=4, bg='green2', font=('Calibri',13), command=row6_2).place(x=180, y=440)
        List += ['F2']
        variable += 1
    def click_6_3():
        global variable, List, colour_list
        Button(window, text='F3', width=4, bg='green2', font=('Calibri',13), command=row6_3).place(x=340, y=440)
        List += ['F3']
        variable += 1
    def click_6_4():
        global variable, List, colour_list
        Button(window, text='F4', width=4, bg='green2', font=('Calibri',13), command=row6_4).place(x=420, y=440)
        List += ['F4']
        variable += 1
    def click_6_5():
        global variable, List, colour_list
        Button(window, text='F5', width=4, bg='green2', font=('Calibri',13), command=row6_5).place(x=500, y=440)
        List += ['F5']
        variable += 1
        
    def click_7_1():
        global variable, List, colour_list
        Button(window, text='G1', width=4, bg='green2', font=('Calibri',13), command=row7_1).place(x=100, y=510)
        List += ['G1']
        variable += 1
    def click_7_2():
        global variable, List, colour_list
        Button(window, text='G2', width=4, bg='green2', font=('Calibri',13), command=row7_2).place(x=180, y=510)
        List += ['G2']
        variable += 1
    def click_7_3():
        global variable, List, colour_list
        Button(window, text='G3', width=4, bg='green2', font=('Calibri',13), command=row7_3).place(x=260, y=510)
        List += ['G3']
        variable += 1
    def click_7_4():
        global variable, List, colour_list
        Button(window, text='G4', width=4, bg='green2', font=('Calibri',13), command=row7_4).place(x=340, y=510)
        List += ['G4']
        variable += 1
    def click_7_5():
        global variable, List, colour_list
        Button(window, text='G5', width=4, bg='green2', font=('Calibri',13), command=row7_5).place(x=420, y=510)
        List += ['G5']
        variable += 1
    def click_7_6():
        global variable, List, colour_list
        Button(window, text='G6', width=4, bg='green2', font=('Calibri',13), command=row7_6).place(x=500, y=510)
        List += ['G6']
        variable += 1


    if 'A1' in colour_list:
        Button(window, text='A1', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=100, y=90)
    else:
        Button(window, text='A1', width=4, bg='grey90', font=('Calibri',13), command=click_1_1).place(x=100, y=90)
        
    if 'A2' in colour_list:
        Button(window, text='A2', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=180, y=90)
    else:
        Button(window, text='A2', width=4, bg='grey90', font=('Calibri',13), command=click_1_2).place(x=180, y=90)

    if 'A3' in colour_list:
        Button(window, text='A3', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=340, y=90)
    else:
        Button(window, text='A3', width=4, bg='grey90', font=('Calibri',13), command=click_1_3).place(x=340, y=90)
        
    if 'A4' in colour_list:
        Button(window, text='A4', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=420, y=90)
    else:
        Button(window, text='A4', width=4, bg='grey90', font=('Calibri',13), command=click_1_4).place(x=420, y=90)
        
    if 'A5' in colour_list:
        Button(window, text='A5', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=500, y=90)
    else:
        Button(window, text='A5', width=4, bg='grey90', font=('Calibri',13), command=click_1_5).place(x=500, y=90)


    if 'B1' in colour_list:
        Button(window, text='B1', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=100, y=160)
    else:        
        Button(window, text='B1', width=4, bg='grey90', font=('Calibri',13), command=click_2_1).place(x=100, y=160)
    
    if 'B2' in colour_list:
        Button(window, text='B2', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=180, y=160)
    else:
        Button(window, text='B2', width=4, bg='grey90', font=('Calibri',13), command=click_2_2).place(x=180, y=160)

    if 'B3' in colour_list:
        Button(window, text='B3', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=340, y=160)
    else:
        Button(window, text='B3', width=4, bg='grey90', font=('Calibri',13), command=click_2_3).place(x=340, y=160)

    if 'B4' in colour_list:
        Button(window, text='B4', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=420, y=160)
    else:
        Button(window, text='B4', width=4, bg='grey90', font=('Calibri',13), command=click_2_4).place(x=420, y=160)

    if 'B5' in colour_list:
        Button(window, text='B5', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=500, y=160)
    else:
        Button(window, text='B5', width=4, bg='grey90', font=('Calibri',13), command=click_2_5).place(x=500, y=160)


    if 'C1' in colour_list:
        Button(window, text='C1', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=100, y=230)
    else:
        Button(window, text='C1', width=4, bg='grey90', font=('Calibri',13), command=click_3_1).place(x=100, y=230)

    if 'C2' in colour_list:
        Button(window, text='C2', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=180, y=230)
    else:
        Button(window, text='C2', width=4, bg='grey90', font=('Calibri',13), command=click_3_2).place(x=180, y=230)

    if 'C3' in colour_list:
        Button(window, text='C3', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=340, y=230)
    else:
        Button(window, text='C3', width=4, bg='grey90', font=('Calibri',13), command=click_3_3).place(x=340, y=230)

    if 'C4' in colour_list:
        Button(window, text='C4', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=420, y=230)
    else:
        Button(window, text='C4', width=4, bg='grey90', font=('Calibri',13), command=click_3_4).place(x=420, y=230)

    if 'C5' in colour_list:
        Button(window, text='C5', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=500, y=230)
    else:
        Button(window, text='C5', width=4, bg='grey90', font=('Calibri',13), command=click_3_5).place(x=500, y=230)


    if 'D1' in colour_list:
        Button(window, text='D1', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=100, y=300)
    else:
        Button(window, text='D1', width=4, bg='grey90', font=('Calibri',13), command=click_4_1).place(x=100, y=300)

    if 'D2' in colour_list:
        Button(window, text='D2', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=180, y=300)
    else:
        Button(window, text='D2', width=4, bg='grey90', font=('Calibri',13), command=click_4_2).place(x=180, y=300)

    if 'D3' in colour_list:
        Button(window, text='D3', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=340, y=300)
    else:
        Button(window, text='D3', width=4, bg='grey90', font=('Calibri',13), command=click_4_3).place(x=340, y=300)

    if 'D4' in colour_list:
        Button(window, text='D4', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=420, y=300)
    else:
        Button(window, text='D4', width=4, bg='grey90', font=('Calibri',13), command=click_4_4).place(x=420, y=300)

    if 'D5' in colour_list:
        Button(window, text='D5', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=500, y=300)
    else:
        Button(window, text='D5', width=4, bg='grey90', font=('Calibri',13), command=click_4_5).place(x=500, y=300)


    if 'E1' in colour_list:
        Button(window, text='E1', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=100, y=370)
    else:
        Button(window, text='E1', width=4, bg='grey90', font=('Calibri',13), command=click_5_1).place(x=100, y=370)

    if 'E2' in colour_list:
        Button(window, text='E2', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=180, y=370)
    else:
        Button(window, text='E2', width=4, bg='grey90', font=('Calibri',13), command=click_5_2).place(x=180, y=370)

    if 'E3' in colour_list:
        Button(window, text='E3', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=340, y=370)
    else:
        Button(window, text='E3', width=4, bg='grey90', font=('Calibri',13), command=click_5_3).place(x=340, y=370)

    if 'E4' in colour_list:
        Button(window, text='E4', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=420, y=370)
    else:
        Button(window, text='E4', width=4, bg='grey90', font=('Calibri',13), command=click_5_4).place(x=420, y=370)

    if 'E5' in colour_list:
        Button(window, text='E5', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=500, y=370)
    else:
        Button(window, text='E5', width=4, bg='grey90', font=('Calibri',13), command=click_5_5).place(x=500, y=370)


    if 'F1' in colour_list:
        Button(window, text='F1', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=100, y=440)
    else:
        Button(window, text='F1', width=4, bg='grey90', font=('Calibri',13), command=click_6_1).place(x=100, y=440)

    if 'F2' in colour_list:
        Button(window, text='F2', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=180, y=440)
    else:
        Button(window, text='F2', width=4, bg='grey90', font=('Calibri',13), command=click_6_2).place(x=180, y=440)

    if 'F3' in colour_list:
        Button(window, text='F3', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=340, y=440)
    else:
        Button(window, text='F3', width=4, bg='grey90', font=('Calibri',13), command=click_6_3).place(x=340, y=440)

    if 'F4' in colour_list:
        Button(window, text='F4', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=420, y=440)
    else:
        Button(window, text='F4', width=4, bg='grey90', font=('Calibri',13), command=click_6_4).place(x=420, y=440)

    if 'F5' in colour_list:
        Button(window, text='F5', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=500, y=440)
    else:
        Button(window, text='F5', width=4, bg='grey90', font=('Calibri',13), command=click_6_5).place(x=500, y=440)


    if 'G1' in colour_list:
        Button(window, text='G1', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=100, y=510)
    else:
        Button(window, text='G1', width=4, bg='grey90', font=('Calibri',13), command=click_7_1).place(x=100, y=510)

    if 'G2' in colour_list:
        Button(window, text='G2', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=180, y=510)
    else:
        Button(window, text='G2', width=4, bg='grey90', font=('Calibri',13), command=click_7_2).place(x=180, y=510)

    if 'G3' in colour_list:
        Button(window, text='G3', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=260, y=510)
    else:
        Button(window, text='G3', width=4, bg='grey90', font=('Calibri',13), command=click_7_3).place(x=260, y=510)

    if 'G4' in colour_list:
        Button(window, text='G4', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=340, y=510)
    else:
        Button(window, text='G4', width=4, bg='grey90', font=('Calibri',13), command=click_7_4).place(x=340, y=510)

    if 'G5' in colour_list:
        Button(window, text='G5', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=420, y=510)
    else:
        Button(window, text='G5', width=4, bg='grey90', font=('Calibri',13), command=click_7_5).place(x=420, y=510)

    if 'G6' in colour_list:
        Button(window, text='G6', width=4, bg='IndianRed1', font=('Calibri',13), state='disabled').place(x=500, y=510)
    else:
        Button(window, text='G6', width=4, bg='grey90', font=('Calibri',13), command=click_7_6).place(x=500, y=510)


    Button(window, bd=2, relief='raised', width=8, bg='grey90', font=('Calibri',13), text='BACK', state='disabled', cursor='hand2').place(x=600, y=570)
    Button(window, bd=2, relief='raised', width=8, bg='grey90', font=('Calibri',13), text='NEXT', state='disabled', cursor='hand2').place(x=700, y=570)

    i=1
    def_age = 0
    Name = []
    Age = []
    Price = 0
    v = IntVar()
    r=''
    R=''
    otp = str(random.randrange(100000,1000000))

    dc_no = 0
    def_dcno = 0
    cvv = 0
    def_cvv = 0
    cr_no = 0
    def_crno = 0
    Cvv = 0
    def_Cvv = 0
    def Back_to_book():
        global window
        window.destroy()
        var_fun = 3
        booking.book(var_fun)
    def Next():
        global variable
        window.geometry('600x500+20+20')
        window.title('PASSENGER DETAILS')
        def submit():
            global Price,Pp
            Pp = 'Your total Booking Price is Rs.'+str(Price)+'/-'
            messagebox.askokcancel('Total Price', Pp)
            window.geometry('1050x500+30+30')
            window.title('PAYMENT OPTIONS')
            def Pay():
                global Price, otp, variable, time_list, F1, T1, D1, usern
                window.geometry('400x300+20+20')
                window.title('PAYMENT WINDOW')
                s=''
                for l in range(0,len(List)):
                    s += (str(List[l])+',')
                hour = time.strftime('%I')
                time_list += [hour]
                minute = time.strftime('%M')
                time_list += [minute]
                am_pm = time.strftime('%p')
                time_list += [am_pm]
                day = time.strftime('%a')
                time_list += [day]
                date = time.strftime('%d')
                time_list += [date]
                month = time.strftime('%b')
                time_list += [month]
                year = time.strftime('%Y')
                time_list += [year]
                S=''
                for L in range(0,len(time_list)):
                    S += (str(time_list[L])+',')
                con = sql.connect(host = "localhost", user = "root", password = "", database =" project")
                cr = con.cursor()
                cr.execute("insert into history_details values('"+F1+"','"+T1+"','"+D1+"','"+str(variable)+"','"+s+"','"+usern+"','"+S+"')")
                cr.execute("commit")
                con.close()
                def insert():
                    global Price,otp,List
                    s=''
                    for l in range(0,len(List)):
                        s += (str(List[l])+',')
                    con = sql.connect(host = "localhost", user = "root", password = "", database =" project")
                    cr = con.cursor()
                    cr.execute("insert into otp values('"+otp+"','"+str(Price)+"','"+s+"')")
                    cr.execute("commit")
                    con.close()
                    abcdef=0
                    con1 = sql.connect(host = "localhost", user = "root", password = "", database =" project")
                    cr1 = con1.cursor()
                    cr1.execute("insert into colour"+str(GIRL)+" values('"+s+"')")
                    cr1.execute("commit")
                    con1.close()
                insert()
                def close():
                    global otp, usern, passn,bi
                    messagebox.showinfo('Remainder', 'NOTE : Your registration ID is '+str(otp)+'\nUse this registration ID to cancel your tickets')
                    m = messagebox.askyesno('Exit', 'Are you sure you want to return to main window?')
                    if m==1: # YES - 1
                        window.destroy()
                        
                        booking.login(usern,passn)
                        
                def cancel():
                    def back():
                        window_cancel.destroy()
                        window.deiconify()
                    def CLose():
                        messagebox.showinfo('Escape travels', 'Thanks for using our system')
                        window_cancel.destroy()                    
                    def selectAll():
                        e = entry.get()
                        if e == '':
                            messagebox.showerror('Error', 'Enter your registration ID')
                        else:
                            con = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                            cr = con.cursor()
                            cr.execute("Select price,seats from otp where otp ='"+e+"'")
                            rows = cr.fetchall()
                            if rows == []:
                                messagebox.showerror('Error', "Your registration ID doesn't match")
                            else:
                                for r in rows:
                                    price_seats = r
                                    new_price = price_seats[0]
                                    new_seats = price_seats[1].split(',')
                                    for some in range(0,len(new_seats)-1):
                                        print(new_seats[some])
                                    messagebox.showinfo('Tickets Cancelled', 'Your payment price Rs. '+str(new_price)+' has\nrefunded successfully')
                                    b1.destroy()
                                    b2.destroy()
                                    con1 = sql.connect(host = "localhost", user = "root", password = "", database = "project")
                                    cr1 = con1.cursor()
                                    cr1.execute("Delete from otp where otp ='"+e+"'")
                                    con1.close()
                                    Button(window_cancel, text='CLOSE', bg='grey90', width=10, font=('Calibri',12), command=CLose, cursor='hand2').place(x=130, y=150)
                            con.close()
                    M = messagebox.askyesno('Cancellation', 'Are you sure you want to cancel\nthe tickets you booked?')
                    if M == 1:
                        window.withdraw()
                        window_cancel = Tk()
                        window_cancel.geometry('300x200+500+500')
                        window_cancel.title('CANCELLATION')
                        Frame(window_cancel, bg='mint cream', width=300, height=200).place(x=0, y=0)
                        Label(window_cancel, text='Enter your registration ID\nprovided during your payment process', bg='mint cream', font=('Calibri',13)).place(x=10, y=20)
                        entry = Entry(window_cancel, font=('Helvetica',13))
                        entry.place(x=30, y=80)
                        b1 = Button(window_cancel, text='BACK', bg='grey90', width=10, font=('Calibri',12), command=back, cursor='hand2')
                        b1.place(x=80, y=150)
                        b2 = Button(window_cancel, text=' OK ', bg='grey90', width=10, font=('Calibri',12), command=selectAll, cursor='hand2')
                        b2.place(x=180, y=150)

                Frame(window, bg='mint cream', width=400, height=300).place(x=0, y=0)
                Label(window, text='Payment Successful !!', bg='mint cream', fg='green4', font=('Calibri',15)).place(x=30, y=30)
                #Label(window, text="You've paid Rs."+str(Price)+'/-', bg='mint cream', fg='green4', font=('Calibri',15)).place(x=40, y=60)
                #Label(window, text='Thank You', bg='mint cream', fg='grey60', font=('Calibri',12)).place(x=70, y=100)
                Label(window, text='HAPPY JOURNEY :)', bg='mint cream', fg='deep pink', font=('Verdana',18)).place(x=60, y=100)

                Label(window, text='Your registration ID is '+str(otp), bg='mint cream', fg='brown4', font=('Calibri',12)).place(x=100, y=180)
                Label(window, text='You can cancel your tickets\n48 hours before your journey', bg='mint cream', font=('Calibri',11)).place(x=100, y=210)
                Button(window, text='BACK', bg='grey90', width=10, font=('Calibri',12), cursor='hand2', command=close).place(x=280, y=255)
                #Button(window, text='CANCEL', bg='grey90', width=10, font=('Calibri',12), cursor='hand2', command=cancel).place(x=280, y=255)
                messagebox.showinfo('Remainder', 'Your registration ID is sent to your\nregistered mobile number or mail ID')
            def debit():
                global d_number1,d_number2,d_number3
                def dc_no():
                    global d_number1
                    try:
                        d1 = d_number1.get()
                        if len(d1)== 19 and (d1[0:4].isdigit() and d1[5:9].isdigit() and d1[10:14].isdigit() and d1[15:].isdigit()) and((d1[4] == ' ' and d1[9] == ' ' and d1[14] == ' ')or(d1[4] == '-' and d1[9] == '-' and d1[14] == '-')):
                            dc_no = 1
                            return dc_no
                        else:
                            messagebox.showerror('Error!','Enter your card number correctly with spaces')
                    except IndexError:
                        messagebox.showerror('Error!','Enter your card number correctly with spaces')
                def cvv():
                    global d_number2
                    d2 = d_number2.get()
                    if d2.isdigit() and len(d2) == 3:
                        cvv = 1
                        return cvv
                    else:
                        messagebox.showerror('Error!','Enter CVV correctly')
                def pay():
                    if dc_no() == 1 and cvv() == 1:
                        Pay()
                
                Frame(window, height=500, width=850, bg='mint cream').place(x=300, y=0)
                ex_month = StringVar()
                ex_year = StringVar()

                em = ttk.Combobox(window, textvariable=ex_month, width=24, font=('Calibri',15))
                em['values'] = ['January','February','March','April','May','June','July','August','September','October','November','December']
                em.place(x=700, y=155)

                ey = ttk.Combobox(window, textvariable=ex_year, width=24, font=('Calibri',15))
                ey['values'] = ['2022','2023','2024','2025','2026','2027','2028','2029','2030']
                ey.place(x=700, y=210)

                Label(window, bg='mint cream', font=('Verdana bold',13), text='DEBIT CARD PAYMENT').place(x=540, y=30)
                Label(window, bg='mint cream', font=('Verdana',12), text='DEBIT CARD NUMBER').place(x=400, y=105)
                Label(window, bg='mint cream', font=('Verdana',12), text='EXPIRY MONTH').place(x=400, y=160)
                Label(window, bg='mint cream', font=('Verdana',12), text='EXPIRY YEAR').place(x=400, y=215)
                Label(window, bg='mint cream', font=('Verdana',12), text='CVV').place(x=400, y=270)
                Label(window, bg='mint cream', font=('Verdana',12), text="CARD HOLDER'S NAME").place(x=400, y=325)

                def button_hover_de(e):
                    Label(window, text='Enter the number with spaces or hyphen(-)', bg='light yellow').place(x=700, y=134)
                def button_hover_dl(e):
                    Label(window,text='                                                                                                        ', bg='mint cream').place(x=700, y=134)
                
                d_number1 = Entry(window, bd=2, relief='raised', width=22, font=('Calibri',18))
                d_number1.place(x=700, y=100)
                d_number1.bind('<Enter>',button_hover_de)
                d_number1.bind('<Leave>',button_hover_dl)
                d_number2 = Entry(window, bd=2, relief='raised', width=22, font=('Calibri',18))
                d_number2.place(x=700, y=265)
                d_number3 = Entry(window, bd=2, relief='raised', width=25, font=('Calibri',18))
                d_number3.place(x=700, y=320)

                Button(window, bd=2, relief='raised', width=12, bg='grey90', font=('Calibri',13), cursor='hand2', text='PAY', command=pay).place(x=700, y=420)
                
            def credit():
                global c_number1,c_number2,c_number3
                def cr_no():
                    global c_number1
                    try:
                        c1 = c_number1.get()
                        if len(c1)== 19 and ((c1[4] == ' ' and c1[9] == ' ' and c1[14] == ' ')or(c1[4] == '-' and c1[9] == '-' and c1[14] == '-')):
                            cr_no = 1
                            return cr_no
                        else:
                            messagebox.showerror('Error!','Enter your card number correctly with spaces')
                    except IndexError:
                        messagebox.showerror('Error!','Enter your card number correctly with spaces')
                def Cvv():
                    global c_number2
                    c2 = c_number2.get()
                    if c2.isdigit() and len(c2) == 3:                        
                        Cvv = 1
                        return Cvv
                    else:
                        messagebox.showerror('Error!','Enter CVV correctly')
                def pay():
                    if cr_no() == 1 and Cvv() == 1:
                        Pay()
                
                Frame(window, height=1500, width=1000, bg='mint cream').place(x=300, y=0)  
                ex_month = StringVar()
                ex_year = StringVar()

                em = ttk.Combobox(window, textvariable=ex_month, width=24, font=('Calibri',15))
                em['values'] = ['January','February','March','April','May','June','July','August','September','October','November','December']
                em.place(x=700,y=155)

                ey = ttk.Combobox(window, textvariable=ex_year, width=24, font=('Calibri',15))
                ey['values'] = ['2022','2023','2024','2025','2026','2027','2028','2029','2030']
                ey.place(x=700,y=210)

                Label(window, bg='mint cream', font=('Verdana bold',13), text='CREDIT CARD PAYMENT').place(x=540,y=30)
                Label(window, bg='mint cream', font=('Verdana',12), text='CREDIT CARD NUMBER').place(x=400,y=105)
                Label(window, bg='mint cream', font=('Verdana',12), text='EXPIRY MONTH').place(x=400,y=160)
                Label(window, bg='mint cream', font=('Verdana',12), text='EXPIRY YEAR').place(x=400,y=215)
                Label(window, bg='mint cream', font=('Verdana',12), text='CVV').place(x=400,y=270)
                Label(window, bg='mint cream', font=('Verdana',12), text="CARD HOLDER'S NAME").place(x=400,y=325)

                def button_hover_ce(e):
                    Label(window, text='Enter the number with spaces or hyphen(-)', bg='light yellow').place(x=700, y=134)
                def button_hover_cl(e):
                    Label(window,text='                                                                                                        ', bg='mint cream').place(x=700, y=134)

                c_number1 = Entry(window, bd=2, relief='raised', width=22, font=('Calibri',18))
                c_number1.place(x=700,y=100)
                c_number1.bind('<Enter>',button_hover_ce)
                c_number1.bind('<Leave>',button_hover_cl)
                c_number2 = Entry(window, bd=2, relief='raised', width=22, font=('Calibri',18))
                c_number2.place(x=700,y=265)
                c_number3 = Entry(window, bd=2, relief='raised', width=25, font=('Calibri',18))
                c_number3.place(x=700,y=320)

                Button(window, bd=2, relief='raised', width=12, bg='grey90', font=('Calibri',13), cursor='hand2', text='PAY', command=pay).place(x=700, y=420)
                
            def google():
                global g_number1
                def pay():
                    global g_number1
                    n1 = str(g_number1.get())
                    if len(n1) == 10 and n1.isdigit:
                        Pay()
                    else:
                        messagebox.showerror('Error!','Enter your phone number correctly')
                Frame(window, height=500, width=850, bg='mint cream').place(x=300, y=0)

                Label(window, text='GOOGLE PAY', bg='mint cream', font=('Verdana bold',13)).place(x=570, y=30)
                Label(window, text='Enter your phone number registered with google pay', bg='mint cream', font=('Verdana',12)).place(x=350, y=150)

                g_number1 = Entry(window, bd=2, relief='raised', width=25, font=('Calibri',18))
                g_number1.place(x=350,y=220)

                Button(window, bd=2, relief='raised', width=12, bg='grey90', font=('Calibri',13), cursor='hand2', text='PAY', command=pay).place(x=700, y=420)
                
            def phone_pay():
                global p_number1,p_number2
                def pay():
                    global p_number1,p_number2
                    p_n1 = str(p_number1.get())
                    if len(p_n1) == 10 and p_n1.isdigit:
                        try:
                            p_n2 = int(p_number2.get())
                        except ValueError:
                            messagebox.showerror('Error!','Enter your UPI pin correctly\nin digits')
                        if len(str(p_n2))==4 or len(str(p_n2))==5 or len(str(p_n2))==6:
                            Pay()
                        else:
                            messagebox.showerror('Error!', 'Enter your UPI pin correctly')    
                    else:
                        messagebox.showerror('Error!', 'Enter your phone number correctly')
                    
                Frame(window, height=500, width=850, bg='mint cream').place(x=300, y=0)
                Label(window, text='PHONE PE', bg='mint cream', font=('Verdana bold',13)).place(x=570, y=30)
                Label(window, text='Enter your phone number registered with phone pe', bg='mint cream', font=('Verdana',12)).place(x=350, y=150)
                Label(window, text='Enter your UPI pin', bg='mint cream', font=('Verdana',12)).place(x=350, y=250)

                p_number1 = Entry(window, bd=2, relief='raised', width=25, font=('Calibri',18))
                p_number1.place(x=350,y=200)
                p_number2 = Entry(window, bd=2, relief='raised', width=15, font=('Calibri',18))
                p_number2.place(x=350,y=300)

                Button(window, bd=2, relief='raised', width=12, bg='grey90', font=('Calibri',13), cursor='hand2', text='PAY', command=pay).place(x=700, y=420)
                
            def amazon():
                global a_number1,a_number2
                def pay():
                    global a_number1,a_number2
                    a_n1 = str(a_number1.get())
                    a_n2 = str(a_number2.get())
                    if (len(a_n1) >= 16 and a_n1[-10:] == '@gmail.com') or (len(a_n1) >= 16 and a_n1[-10:] == '@yahoo.com') or (len(a_n1) >= 18 and a_n1[-12:] == '@hotmail.com') or (len(a_n1) >= 20 and a_n1[-15:] == '@rediffmail.com'):
                        if len(a_n2) >=8 and a_n2.isalnum():
                            Pay()
                        else:
                            messagebox.showerror('Error!', 'Enter your Amazon password correctly')
                    else:
                        messagebox.showerror('Error!', 'Enter your email address correctly')
                Frame(window, height=500, width=850, bg='mint cream').place(x=300, y=0)
                Label(window, text='AMAZON PAY', bg='mint cream', font=('Verdana bold',13)).place(x=570, y=30)
                Label(window, text='Enter your email address registered with amazon pay', bg='mint cream', font=('Verdana',12)).place(x=350, y=150)
                Label(window, text='Enter your Amazon password', bg='mint cream', font=('Verdana',12)).place(x=350, y=250)

                a_number1 = Entry(window, bd=2, relief='raised', width=25, font=('Calibri',18))
                a_number1.place(x=350,y=200)
                a_number2 = Entry(window, bd=2, relief='raised', width=15, font=('Calibri',18))
                a_number2.place(x=350,y=300)

                Button(window, bd=2, relief='raised', width=12, bg='grey90', font=('Calibri',13), text='PAY', cursor='hand2', command=pay).place(x=700, y=420)
                
            def upi():
                u = Frame(window, height=500, width=850, bg='mint cream').place(x=300, y=0)
                Label(window, text='UPI', bg='mint cream', font=('Verdana bold',13)).place(x=570, y=30)
                Label(window, text='Virtual address ex : CustomerName@BankName', bg='mint cream', font=('Verdana',12)).place(x=350, y=150)

                entryupi = Entry(window, bd=2, relief='raised', width=30, font=('Helvetica',18)).place(x=350, y=220)

                Button(window, bd=2, relief='raised', width=12, bg='grey90', font=('Calibri',13), cursor='hand2', text='PAY', command=Pay).place(x=700, y=420)
                
            def net_banking():
                global cd,ifsc
                Frame(window, height=500, width=850, bg='mint cream').place(x=300, y=0)
                def pay():
                    global cd,ifsc
                    CD = cd.get()
                    IFSC = ifsc.get()
                    if len(CD)== 19 and ((CD[4] == ' ' and CD[9] == ' ' and CD[14] == ' ')or(CD[4] == '-' and CD[9] == '-' and CD[14] == '-')):
                        if len(IFSC)==4 and IFSC.isdigit():
                            Pay()
                        else:
                            messagebox.showerror('Error','Enter IFSC code correctly')
                    else:
                        messagebox.showerror('Error','Enter card number correctly')
                        
                b = StringVar()
                Label(window, text='NET BANKING', bg='mint cream', font=('Verdana bold',13)).place(x=570, y=30)
                Label(window, text='Select any bank', bg='mint cream', font=('Verdana',12)).place(x=360, y=150)
                bn = ttk.Combobox(window, textvariable=b, width=20, font=('Calibri',15))
                bn['values'] = ['Axis Bank','Andhra Bank','Bank of Baroda','Canara Bank','City Union Bank','Corporation Bank','Dena Bank','Federal Bank','HDFC','ICICI','Indian Bank','Indusland Bank','Jammu & Kashmir Bank','Karur Vysya Bank','Kotak Mahindra Bank','Lakshmi Vilas Bank','Punjab National Bank','South Indian Bank','State Bank Of India','TamilNad Mercantile Bank','Union Bank','Vijaya Bank']
                bn.place(x=350,y=200)

                def button_hover_ue(e):
                    Label(window, text='Enter the number with spaces or hyphen(-)', bg='light yellow').place(x=360, y=360)
                def button_hover_ul(e):
                    Label(window,text='                                                                                                        ', bg='mint cream').place(x=360, y=360)
                
                Label(window, text='Enter your card no\n(credit/debit)', bg='mint cream', font=('Verdana',12)).place(x=360, y=260)            
                cd = Entry(window, bd=2, relief='raised', width=30, font=('Helvetica',18))
                cd.bind('<Enter>',button_hover_ue)
                cd.bind('<Leave>',button_hover_ul)
                cd.place(x=350, y=320)
                
                Label(window, text='Enter your IFSC code', bg='mint cream', font=('Verdana',12)).place(x=710, y=150)
                ifsc = Entry(window, bd=2, relief='raised', width=20, font=('Helvetica',18))
                ifsc.place(x=700, y=200)
                
                Button(window, bd=2, relief='raised', width=12, bg='grey90', font=('Calibri',13), cursor='hand2', text='PAY', command=pay).place(x=700, y=420)
                
            Frame(window, height=500, width=300, bg='pink').place(x=0, y=0)
            Label(window, bg='pink', fg='black', font=('Verdana bold',13), text='PAYMENT OPTIONS').place(x=50, y=30)
            default_frame = Frame(window, height=500, width=850, bg='mint cream').place(x=300, y=0)
            Label(window, text='Select any one option', bg='mint cream', font=('Verdana',30)).place(x=470, y=190)

            Button(window, width=32, bg='white', font=('Calibri',13), cursor='hand2', text='DEBIT CARD', command=debit).place(x=0, y=125)
            Button(window, width=32, bg='white', font=('Calibri',13), cursor='hand2', text='CREDIT CARD', command=credit).place(x=0, y=170)
            Button(window, width=32, bg='white', font=('Calibri',13), cursor='hand2', text='GOOGLE PAY', command=google).place(x=0, y=215)
            Button(window, width=32, bg='white', font=('Calibri',13), cursor='hand2', text='PHONE PAY', command=phone_pay).place(x=0, y=260)
            Button(window, width=32, bg='white', font=('Calibri',13), cursor='hand2', text='AMAZON', command=amazon).place(x=0, y=305)
            Button(window, width=32, bg='white', font=('Calibri',13), cursor='hand2', text='UPI', command=upi).place(x=0, y=350)
            Button(window, width=32, bg='white', font=('Calibri',13), cursor='hand2', text='NET BANKING', command=net_banking).place(x=0, y=395)
        def Back():
            pass
        def age():
            global l_age, def_age, entry3
            age = 0
            n3 = entry3.get() 
            if n3.isdigit() and (len(n3)==1 or len(n3)==2):
                if def_age == 1:
                    l_age.destroy()
                    def_age = 0
                if def_age == 0:
                    age = 1
                    return age
            else:
                l_age = Label(window, text='Enter your age in numerals', bg='mint cream', fg='red')
                l_age.place(x=400, y=280)
                def_age = 1
        def NEXT():
            global P, def_age, entry1, entry3, i, Name, Age, Price, variable, l_age, Str_viewseats
            Price += int(Str_viewseats)
            n1 = entry1.get()
            if n1 == '':
                messagebox.showerror('Error!','Enter your Name')
            elif len(n1) < 2:
                messagebox.showerror('Error!','Enter your Name correctly')
            else:
                try:
                    n3 = int(entry3.get())
                except ValueError:
                    messagebox.showerror('Error!','Enter your age')
                if age()==1:                    
                    Name += [str(n1)]
                    Age += [int(n3)]
                    message = 'Price for '+str(R)+str(n1)+' is Rs.'+Str_viewseats+'/-'
                    messagebox.askokcancel('Your Price', message)
                    i+=1
                    if i < variable+1:
                        mul_frames()
                    else:
                        Button(window, bd=2, relief='groove', width=15, bg='grey90', font=('Calibri',12), cursor='hand2', text='PROCEED TO PAY', command=submit).place(x=320, y=400)
                        Label(window, text='You are now ready to pay', bg='mint cream', fg='green4', font=('Calibri',12)).place(x=310, y=370)
                        Button(window, bd=2, relief='groove', width=10, bg='grey90', font=('Calibri',12), cursor='hand2', text='NEXT', state='disabled').place(x=480, y=400)

        def mul_frames():
            global entry1, entry3, i, List, v
            if List==[]:
                window.geometry('870x630+40+40')
                messagebox.showerror('Error', 'Book your tickets')
            else:
                Frame(window, height=650, width=900, bg='mint cream').place(x=0, y=0)

                Label(window, bg='mint cream', font=('Verdana bold',11), text='PASSENGER DETAILS').place(x=200, y=20)
                Label(window, bg='mint cream', fg='grey20', font=('Verdana bold',11), text='Passenger '+str(i)).place(x=60, y=65)
                Label(window, bg='mint cream', fg='grey20', font=('Verdana bold',11), text='Seat no : '+List[i-1]).place(x=60, y=95)

                Label(window, bg='mint cream', font=('Calibri',12), text='NAME').place(x=50, y=150)
                Label(window, bg='mint cream', font=('Calibri',12), text='GENDER').place(x=50, y=200)
                Label(window, bg='mint cream', font=('Calibri',12), text='AGE').place(x=50, y=250)

                entry1 = Entry(window, bd=2, relief='groove', width=35, font=('Helvetica',13))
                entry1.place(x=200, y=150)
                Radiobutton(window, text='Male', variable=v, value=1, bd=2, relief='groove', width=7).place(x=200, y=200)
                Radiobutton(window, text='Female', variable=v, value=2, bd=2, relief='groove', width=7).place(x=330, y=200)
                Radiobutton(window, text='Others', variable=v, value=3, bd=2, relief='groove', width=7).place(x=460, y=200)
                entry3 = Entry(window, bd=2, relief='groove', width=35, font=('Helvetica',13))
                entry3.place(x=200, y=250)
            
                Button(window, bd=2, relief='groove', width=15, bg='grey90', font=('Calibri',12), cursor='hand2', text='PROCEED TO PAY', state='disabled').place(x=320, y=400)
                Button(window, bd=2, relief='groove', width=10, bg='grey90', font=('Calibri',12), cursor='hand2', text='NEXT', command=NEXT).place(x=480, y=400)
        mul_frames()

    def submit():
        count = 200
        Label(window, font=('Calibri',16), bg='mint cream', text='      \n      \n      \n      \n      \n      \n      \n      \n      \n      \n      ').place(x=690, y=200)
        Label(window, font=('Verdana',15), bg='mint cream', text='Number of seats booked').place(x=600, y=50)
        Label(window, font=('Calibri',16), bg='mint cream', text=variable).place(x=690, y=80)
        
        Label(window, font=('Verdana',15), bg='mint cream', text='Seats booked').place(x=620, y=170)
        for a in range(len(List)):
            Label(window, font=('Calibri',16), bg='mint cream', text=List[a]).place(x=690, y=count)
            count += 40
        Button(window, bd=2, relief='raised', width=8, bg='grey90', font=('Calibri',13), text='BACK', command=Back_to_book).place(x=600, y=570)
        Button(window, bd=2, relief='raised', width=8, bg='grey90', font=('Calibri',13), text='NEXT', command=Next).place(x=700, y=570)
    Button(window, text='BOOK', bg='ivory2', width=7, font=('Calibri',16), command=submit, bd=2, relief='groove', cursor='hand2').place(x=280, y=575)
#third_win()
