from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models

def fetchlist():
    connection = conne()
    cursor = connection.cursor(DictCursor)

    sql ='''
        select 	no,
			    name,
			    message,
			    date_format(times, '%Y-%m-%d %h:%i:%s') as times
			    from mysite
        order by no desc
    '''
    cursor.execute(sql)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results

def insert(name, password, message):
    connection = conne()
    cursor = connection.cursor()

    sql ='''
        insert
            into mysite 
        values(null, %s, %s, %s, now())
    '''
    cursor.execute(sql,(name,password,message))
    connection.commit()


    cursor.close()
    connection.close()

def delete(no, password):
    connection = conne()
    cursor = connection.cursor()

    sql ='''
    delete
         from mysite
         where no=%s and password=%s
    '''
    cursor.execute(sql,(no, password))
    connection.commit()

    cursor.close()
    connection.close()


def conne():
    return connect(
        user= 'mysite',
        password='mysite',
        host='192.168.1.111',
        db= 'mysite',
        port = 3307,
        charset='utf8')
