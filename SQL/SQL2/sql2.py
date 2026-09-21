import sqlite3
conn = sqlite3.connect('gp_surgery.db')
c = conn.cursor()

c.execute("SELECT appt_mode, COUNT(appt_mode) FROM appointments WHERE appt_status='DNA' GROUP BY appt_mode HAVING COUNT(appt_mode) > 100")

print(c.fetchall())


