import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd='Moin@1234'
)
cursor = connection.cursor()

cursor.execute('create database website')
print('done !!')