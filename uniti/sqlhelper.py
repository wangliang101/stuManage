import pymysql

def get_list(sql,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return class_list

def get_one(sql,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    class_list = cursor.fetchone()
    cursor.close()
    conn.close()
    return class_list

def modify(sql,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    conn.commit()
    cursor.close()
    conn.close()

class SqlHelper(object):
    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_one(self,sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def get_list(self,sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def modify(self,sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def multiple_modify(self,sql,args):
        self.cursor.executemany(sql,args)
        self.conn.commit()

    def creat(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()








