import mysql.connector as sql
a = 1

if a == 1:
    con = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
    cr = con.cursor()
    cr.execute("create table profile_details (firstname varchar(40), lastname varchar(40), gender varchar(20), dob varchar(30), ph_num varchar(20), email varchar(50), address varchar(50), address2 varchar(50), city varchar(60), p_c varchar(20), state varchar(60), country varchar(60), sq1 varchar(80), ans1 varchar(80), sq2 varchar(80), ans2 varchar(80), username varchar(80) PRIMARY KEY, password varchar(80))")
    cr.execute("commit")
    con.close()
    b = 1

    if b == 1:
        con1 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
        cr1 = con1.cursor()
        cr1.execute("create table history_details (from_place varchar(50), to_place varchar(50), date_place varchar(50), no_seats int, seats varchar(30), username varchar(50), time varchar(30))")
        cr1.execute("commit")
        con1.close()
        c = 1

        if c == 1:
            con2 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
            cr2 = con2.cursor()
            cr2.execute("create table otp (otp int PRIMARY KEY, price int, seats varchar(70))")
            cr2.execute("commit")
            con2.close()
            d = 1
                      
            if d == 1:
                con3 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
                cr3 = con3.cursor()
                cr3.execute("create table colour1 (seats varchar(100))")
                cr3.execute("commit")
                con3.close()
                e = 1

                if e == 1:
                    con4 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
                    cr4 = con4.cursor()
                    cr4.execute("create table colour2 (seats varchar(100))")
                    cr4.execute("commit")
                    con4.close()
                    f = 1

                    if f == 1:
                        con5 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
                        cr5 = con5.cursor()
                        cr5.execute("create table colour3 (seats varchar(100))")
                        cr5.execute("commit")
                        con5.close()
                        g = 1

                        if g == 1:
                            con6 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
                            cr6 = con6.cursor()
                            cr6.execute("create table colour4 (seats varchar(100))")
                            cr6.execute("commit")
                            con6.close()
                            h = 1

                            if h == 1:
                                con7 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
                                cr7 = con7.cursor()
                                cr7.execute("create table colour5 (seats varchar(100))")
                                cr7.execute("commit")
                                con7.close()
                                i = 1

                                if i == 1:
                                    con8 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
                                    cr8 = con8.cursor()
                                    cr8.execute("create table colour6 (seats varchar(100))")
                                    cr8.execute("commit")
                                    con8.close()
                                    j = 1

                                    if j == 1:
                                        con9 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
                                        cr9 = con9.cursor()
                                        cr9.execute("create table colour7 (seats varchar(100))")
                                        cr9.execute("commit")
                                        con9.close()
                                        k = 1

                                        if k == 1:
                                            con10 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
                                            cr10 = con10.cursor()
                                            cr10.execute("create table colour8 (seats varchar(100))")
                                            cr10.execute("commit")
                                            con10.close()
                                            l = 1

                                            if l == 1:
                                                con11 = sql.connect(host = "localhost", user = "root", password = "harshitha", database =" project")
                                                cr11 = con11.cursor()
                                                cr11.execute("create table colour9 (seats varchar(100))")
                                                cr11.execute("commit")
                                                con11.close()
                                                m = 1
if m == 1:
    print('Mysql - create tables \nSuccessfully created all the tables')