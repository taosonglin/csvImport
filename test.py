import pymysql
from tools import *

conn=pymysql.connect('localhost','root','dld2019!',"dldDB")
cur=conn.cursor()
t1=now()
sql="select * from TSO where Shares_Amount>100000000;"
cur.execute(sql)
conn.commit()
result = cur.fetchall()
t2=now()
print t1,t2
print(len(result))
conn.close()
