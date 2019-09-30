import pymysql
class Db(object):
    conn=None
    cursor=None
    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='blog',  ##数据库名
        charset='utf8'  ##连接编码
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    @classmethod
    def select(cls,sql,type,data=()):
         Db.link()
         try:
             Db.cursor.execute(sql, data)
             if(type==0):
                 return Db.cursor.fetchone()
             elif(type==1):
                 return Db.cursor.fetchall()
             else:
                 return Db.cursor.rowcount
         except Exception as e:
             return "error"

    @classmethod
    def insert(cls,sql,data):
        try:
            Db.cursor.execute(sql, data)
            return "succer"
        except Exception as e:
            return "error"

    @classmethod
    def query(cls, sql, data):
        Db.link()
        try:
            Db.cursor.execute(sql, data)
            return "succer"
        except Exception as e:
            return "error"

    @classmethod
    def getLastInsertId(cls):
        return  Db.cursor.lastrowid

    @classmethod
    def commit(cls):
        Db.conn.commit()

    @classmethod
    def close(cls):
        Db.conn.close()
        Db.cursor.close()

    @classmethod
    def link(cls):
        if Db.conn!=None and Db.cursor!=None:
            return
        Db.conn = pymysql.Connect(
            host='localhost',  ##mysql服务器地址
            port=3306,  ##mysql服务器端口号
            user='root',  ##用户名
            passwd='123456',  ##密码
            db='blog',  ##数据库名
            charset='utf8'  ##连接编码
        )
        Db.cursor = Db.conn.cursor(cursor=pymysql.cursors.DictCursor)





















