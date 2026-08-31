import sqlite3

conn = sqlite3.connect("gp_surgery.db")
cur = conn.cursor()



cur.execute("SELECT patient_age, practice_code, appt_date FROM appointments WHERE appt_mode = 'Home Visit' ORDER BY patient_age LIMIT 5")
rows = cur.fetchall()
for row in rows:
    print(row)