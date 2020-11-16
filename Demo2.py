import cx_Oracle
import os
os.environ['PATH'] = 'C:\\oracle\\instantclient_19_6'
#create connection
dsn_tns = cx_Oracle.makedsn('localhost','1523',service_name='orcl3')
conn = cx_Oracle.connect(user='system',password='system',dsn=dsn_tns)
print(conn.version)
cur=conn.cursor()
query="select * from users2"
cur.execute(query)
for cols in cur:
    print(cols[0],"  ",cols[1])
cur.close()
conn.close()
