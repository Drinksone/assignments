# Provide a program to create tables (Employee, Department, Project) in database Sqlite and insert the data.

import sqlite3                                                 #import sqlite
conn = sqlite3.connect('777.db')                               #import database file

#print("Connection established ..........")
cursor=conn.cursor()                                             #cursor object

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")                  #drop table

#create table
sql ='''CREATE TABLE EMPLOYEE
(    EMPLOYEE_NAME CHAR(50) NOT NULL,
    EMP_ID INT,
    EMP_PROJECT CHAR(50),
    EMP_DEPT CHAR(50)
    )'''

cursor.execute(sql)
#insert data in table
cursor.execute('''INSERT INTO EMPLOYEE
("EMPLOYEE_NAME","EMP_ID","EMP_DEPT","EMP_PROJECT")
values ("SURAJ KUMAR",111,"OPERATION","AMEZON")''')
cursor.execute('''INSERT INTO EMPLOYEE
("EMPLOYEE_NAME","EMP_ID","EMP_DEPT","EMP_PROJECT")
values ("DISHA PATIL",112,"DEVELPOEMENT","ECLIPSE")''')
cursor.execute('''INSERT INTO EMPLOYEE
("EMPLOYEE_NAME","EMP_ID","EMP_DEPT","EMP_PROJECT")
values ("AKASH MODE",113,"RESEARCH","PYTHON")''')

cursor.execute('''SELECT * from EMPLOYEE''')
result = cursor.fetchall();
print(result)                        #show result
conn.commit()                        #commit connection
conn.close()                         #close connection