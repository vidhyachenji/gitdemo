import cx_Oracle
import os
os.environ['PATH'] = 'C:\\oracle\\instantclient_19_6'
#create connection
dsn_tns = cx_Oracle.makedsn('localhost', '1523', service_name='orcl3')
conn = cx_Oracle.connect(user='system', password='system', dsn=dsn_tns)
print(conn.version)
query1 = "insert into persons values(101,'Radhika','FQ','London','UK')"
query2 = "update PERSONS set lastname ='eee' where personid =102"
query3 = "delete persons where PERSONID=105"
cur=conn.cursor()
cur.execute(query3)
cur.close()
conn.commit()
conn.close()
print("completed")