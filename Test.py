import sqlite3

con = sqlite3.connect('stocks.db')
cur = con.cursor()
# Create table
# cur.execute('''CREATE TABLE stocks
#                (empno, ename,job, mgr, hiredate,sal, comm, deptno)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES (7369,'SMITH','CLERK',7902,'2000-12-17', 800.00, NULL, 20)")
cur.execute("INSERT INTO stocks VALUES (7499,'ALLEN','SALESMAN',7698,'2001-02-20', 1600.00, 300.00, 30)")
cur.execute("INSERT INTO stocks VALUES (7521,'WARD','SALESMAN',7698,'2001-02-22', 1250.00, 500.00, 30)")

# Save (commit) the changes
con.commit()
nominsere = 'empno'
for row in cur.execute('SELECT ' + nominsere +  ' from stocks'):
    print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()