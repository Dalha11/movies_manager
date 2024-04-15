from dbconnect import Dbconnection
class StudentCode(Dbconnection):
    def __init__(self):
        super().__init__()

    def insert(self,num,name,director,year,genre,Language):
        try:
             q="insert into movies_collection(num,name,director,year,genre,Language) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(num,name,director,year,genre,Language)
  
             cr = self._con.cursor()
             cr.execute(q)
             self._con.commit()
             print("Saved")
        except Exception as e:
            print(e)

    def delete(self,num):
        try:
            q="delete from movies_collection where num={0}".format(num)
            cr = self._con.cursor()
            cr.execute(q)
            if cr.rowcount==0:
                print("Data Not Found")
            else:
                print("Deleted")    
            self._con.commit()
        except Exception as e:
            print(e)
        

    def update(self,num,director,year,genre,Language):
        try:
            q="update movies_collection set director='{2}', year={3}, genre={4}, Language={5} where num={0}".format(num,director,year,genre,Language)
            cr = self._con.cursor()
            cr.execute(q)
            if cr.rowcount==0:
                print("Data Not Found")
            else:
                print("Updated")    
            self._con.commit()
        except Exception as e:
            print(e)

    def select(self):
        try:
            q="select * from movies_collection"
            cr = self._con.cursor()
            cr.execute(q)
            if(cr.rowcount==0):
                print("No data found")
                return
            print("-----------------------------------------------------------------------------------------------")
            print(" NUM             NAME           DIRECTOR              YEAR           GENRE         LANGUAGE ")
            print("--------------------------------------------------------------------------------------------------")
            for row in cr:
                print(row[0],row[1],row[2],row[3],row[4],row[5],sep=" \t\t")
            print("----------------------------------------------------------------------------------------------")    
        except Exception as e:
            print(e)

    def selectbydirector(self,director):
        try:
            q="select * from movies_collection where director like '%{0}%' ".format(director)
            cr = self._con.cursor()
            cr.execute(q)
            if(cr.rowcount==0):
                print("No data found")
                return False
            print("----------------------------------------------------------------------------------------------")
            print(" NUM           NAME           DIRECTOR                YEAR           GENRE          LANGUAGE")
            print("-----------------------------------------------------------------------------------------------")
            for row in cr:
                print(row[0],row[1],row[2],row[3],row[4],row[5],sep=" \t\t")
            print("------------------------------------------------------------------------------------------------")     
            return True
        except Exception as e:
            print(e)

    def selectbynum(self,num):
        try:
            q="select * from movies_collection where num={0} ".format(num)
            cr = self._con.cursor()
            cr.execute(q)
            if(cr.rowcount==0):
                print("No data found")
                return False
            print("-------------------------------------------------------------------------------------------")
            print(" NUM            NAME           DIRECTOR               YEAR          GENRE            LANGUAGE")
            print("--------------------------------------------------------------------------------------------")
            for row in cr:
                print(row[0],row[1],row[2],row[3],row[4],row[5],sep=" \t\t")
            print("---------------------------------------------------------------------------------------------")     
            return True
        except Exception as e:
            print(e)        
