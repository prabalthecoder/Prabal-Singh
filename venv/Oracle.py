import cx_Oracle


con = cx_Oracle.connect('SYSTEM/oracle@localhost:1521/orclcdb')
cur = con.cursor()

res = cur.execute('select * from IMDB')
data = res.fetchall()
for row in data:
    print(row)
    