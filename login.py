import pymysql
def logincode():
    try:
        username = input("Username : ")
        password = input("Password : ")
        q="select * from tbllogin where username='{0}' and password='{1}'".format(username,password)
        con = pymysql.connect(host="localhost",user="root",password="Fazith",db="Movies")
        cr =con.cursor()
        cr.execute(q)
        if(cr.rowcount==0): 
            print("Invalid Login Credentials")
            return False
        con.close()
        return True
    except Exception as e:
        print(e)
