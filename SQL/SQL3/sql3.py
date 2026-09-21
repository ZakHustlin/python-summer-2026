import sqlite3

conn = sqlite3.connect('gp.db')
c = conn.cursor()
import pandas as pd
prac = pd.read_sql("SELECT * FROM practices", conn)
work = pd.read_sql("SELECT * FROM workforce", conn)
appt = pd.read_sql("SELECT * FROM appointments", conn)


c.execute("SELECT AVG(list_size) FROM practices")
#print(c.fetchall())

c.execute("""SELECT p.code, p.name, p.list_size, w.fte_gp
             FROM practices p LEFT JOIN workforce w ON p.code = w.code""")
#for row in c.fetchall(): print(row)

c.execute("SELECT COUNT(*) FROM practices p LEFT JOIN workforce w ON p.code = w.code WHERE w.code IS NULL")
#print(c.fetchall())

for expr in ["COUNT(*)", "COUNT(a.appt_id)"]:
    c.execute(f"""SELECT p.name, {expr}
                  FROM practices p LEFT JOIN appointments a
                    ON p.code = a.code AND a.attended = 1
                  GROUP BY p.code""")
#    print(expr, c.fetchall())

c.execute(f"""SELECT p.name, p.list_size, COUNT(DISTINCT a.appt_id) AS appts, ((COUNT(DISTINCT a.appt_id) * 1000.0) / p.list_size) AS appts_per_1000
            FROM practices p 
            INNER JOIN appointments a ON p.code = a.code
            INNER JOIN workforce w ON p.code = w.code
            WHERE attended = 1 
            GROUP BY p.code




""")
print(c.fetchall())


c.execute("""SELECT (SELECT COUNT(*) FROM practices) AS left_rows,
       (SELECT COUNT(*) FROM workforce) AS right_rows,
       (SELECT COUNT(*) FROM practices p JOIN workforce w ON p.code=w.code) AS joined_rows,
       (SELECT COUNT(*) FROM practices p LEFT JOIN workforce w ON p.code=w.code WHERE w.code IS NULL) AS left_only""")
print(c.fetchall())


m = prac.merge(work, on="code", how="left", indicator=True)
print(m["_merge"].value_counts())