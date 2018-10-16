import sqlite3
connection = sqlite3.connect("etc.db")
query = 'create table if not exists etc (username , password , userid , groupid , fullname , home , shell);'
connection.execute(query)

if connection.execute(query):
    print("Table Created")

for line in list(open("passwd.txt","r").readlines()):
    element = line.rstrip().split(":")
    connection.execute('insert into etc values(?,?,?,?,?,?,?)',element)

cursor = connection.execute('select * from etc')

for line in cursor:
    print("Username : " + line[0] + "Password : " + line[1] + "User ID : " + line[2] + "Group ID : " + line[3])
    print("Description : " + line[4] + "Home Directory : " + line[5] + "Default Shell : " + line[6])
    print("-------------------------------------------------------------------------------------------------------------------------")
