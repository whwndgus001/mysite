from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models

def insert(name, email, password, gender):
    connection = conne()
    cursor = connection.cursor()

    sql ='''
            insert
            into user
        values(null, %s, %s, password(%s), %s, now())
    '''
    cursor.execute(sql,(name,email,password,gender))
    connection.commit()


    cursor.close()
    connection.close()


def fetchone(email, password):
    connection = conne()
    cursor = connection.cursor(DictCursor)

    sql = '''
        select no,
               name
               from user
               where email = %s 
               and password = password(%s)
       
    '''
    cursor.execute(sql, (email, password))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result








def conne():
        return connect(
            user='mysite',
            password='mysite',
            host='192.168.1.111',
            db='mysite',
            port=3307,
            charset='utf8')
