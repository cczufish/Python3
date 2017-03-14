
#  Ih.<3iibF=O!

#2017-03-13T09:55:04.693239Z 1 [Note] A temporary password is generated for root@localhost: hH.zekzdW1w!

#If you lose this password, please consult the section How to Reset the Root Password in the MySQL reference manual.
#!/usr/bin/env pytho
# -*- coding:utf-8 -*-

import pymysql
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='123456', db='test')

#import mysql.connector
#conn = mysql.connector.connect(user='root',password='123456',database='test')
cursor = conn.cursor()
effect_row = cursor.excute('select * from student')


#cursor.excute('create table user (id varchar(20) primary key,name varchar(20))')
#cursor.excute('insert into user (id,name) values (%s,%s)',['1','Michael'])

#print(cursor.rowcount)

conn.commit()
cursor.close()

#cursor = conn.cursor()
#cursor.excute('select * from user where id = %s',('1',))

#values = cursor.fetchall()
#print(values)

#cursor.close()

conn.close()

