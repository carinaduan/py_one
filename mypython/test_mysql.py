#coding=utf-8
import mysql.connector

mydb = mysql.connector.connect(
    host="10.200.24.77",       # 数据库主机地址
    user="root",    # 数据库用户名
    passwd="dcos",   # 数据库密码
    database="ppcloud"
)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("select * from user limit 0,10")
# for x in mycursor:       #循环输出结果
#     print(x)

#mydb.commit()    # 数据表内容有更新，必须使用到该语句   增删改是需要提交执行

#myresult = mycursor.fetchall()     获取一个结果
myresult = mycursor.fetchall()      #获取全部结果
print(myresult)