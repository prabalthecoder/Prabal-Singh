import cx_Oracle


con = cx_Oracle.connect('SYSTEM/oracle@localhost:1521/orclcdb')
cur = con.cursor()
sql = ('insert into DEPARTMENT (deptno, name, location) values (:mydeptno, :myname, :mylocation)')
res = cur.execute(sql, ['1', 'Prabal', 'jalandhar'])
con.commit()

res = cur.execute('select * from DEPARTMENT')
print(res.fetchall())
