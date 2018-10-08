import sqlite3
connection = sqlite3.connect("etc.db")
query = 'create table if not exists etc (username , password , userid , groupid , fullname , home , shell);'
connection.execute(query)

if connection.execute(query):
    print("Table Created")

for line in list(open("passwd.txt","r").readlines()):
    element = line.split(":")
    connection.execute('insert into etc values(?,?,?,?,?,?,?)',element)

cursor = connection.execute('select * from etc')

for line in cursor:
    print(line[0]  + line[1] + line[2] + line[3] + line[4] + line[5] + line[6])
