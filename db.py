import pymysql as pd
class DBHelper:
    def __init__(self):
        conn = pd.connect(host='localhost', user='root', passwd='mirim', charset='utf8') # mysql 접속
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS bit_db")   #db생성
        #mysql 로그아웃 후
        cur.close()
        conn.close()
        #db로 다시접속 (접속한 데이터 베이스 이름 : database='famous_vegetables_db')
        conn = pd.connect(host='localhost', user='root', passwd='mirim',database='bit_db', charset='utf8')
        cur = conn.cursor()
        #테이블 생성
        cur.execute("CREATE TABLE IF NOT EXISTS bit(Name VARCHAR(20), Score INT)")
        cur.close()
        conn.close()

    def insert(self, Name, Score):
        conn = pd.connect(host='localhost', user='root', passwd='mirim', database='bit_db', charset='utf8')
        cur = conn.cursor()

        cur.execute("INSERT INTO bit (Name, Score)VALUES( %s, %s)", (Name, Score))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM bit WHERE 이름 = '이예진';"
        self.cur.execute(sql)
        self.bit_db.commit()

    def select(self):
        conn = pd.connect(host='localhost', user='root', passwd='mirim',database='bit_db', charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM bit")
        return cur.fetchall()