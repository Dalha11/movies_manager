import pymysql
class Dbconnection:
    def __init__(self):
        try:
            self._con = pymysql.connect(host="localhost",user="root",password="Fazith",db="Movies")
        except Exception as e:
            print("Not connected")
            print(e)
