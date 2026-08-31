import sqlite3
import random
##Task data from claude
random.seed(42)

conn = sqlite3.connect("gp_surgery.db")
cur = conn.cursor()

# Practices table
cur.execute("""
CREATE TABLE practices (
    practice_code TEXT PRIMARY KEY,
    practice_name TEXT,
    region TEXT,
    list_size INTEGER,
    imd_score REAL,
    patients_per_gp REAL
)
""")

regions = ["North East", "North West", "Yorkshire", "East Midlands", "West Midlands",
           "East of England", "London", "South East", "South West"]

practice_data = []
for i in range(1, 51):
    code = f"P{i:03d}"
    region = random.choice(regions)
    list_size = random.randint(2800, 18000)
    imd = round(random.uniform(5.0, 45.0), 1)
    ppgp = round(random.uniform(1400, 2600), 0)
    name = f"{random.choice(['Oak','Elm','Park','River','Castle','Hill','Valley','Bridge','Meadow','Church'])} {random.choice(['Street','Road','Lane','View','Green'])} Surgery"
    practice_data.append((code, name, region, list_size, imd, ppgp))

cur.executemany("INSERT INTO practices VALUES (?,?,?,?,?,?)", practice_data)

# Appointments table
cur.execute("""
CREATE TABLE appointments (
    appt_id INTEGER PRIMARY KEY,
    practice_code TEXT,
    appt_date TEXT,
    appt_mode TEXT,
    hcp_type TEXT,
    wait_days INTEGER,
    status TEXT,
    patient_age INTEGER,
    FOREIGN KEY (practice_code) REFERENCES practices(practice_code)
)
""")

modes = ["Face-to-Face", "Telephone", "Video", "Home Visit"]
mode_weights = [55, 35, 7, 3]
hcp_types = ["GP", "Nurse", "Pharmacist", "Paramedic", "Other"]
hcp_weights = [50, 30, 10, 5, 5]
statuses = ["Attended", "DNA", "Cancelled"]
status_weights = [82, 8, 10]

appts = []
appt_id = 1
for p_code, _, _, list_size, imd, _ in practice_data:
    # Higher deprivation → slightly more appointments
    n_appts = random.randint(80, 200) + int(imd * 1.5)
    for _ in range(n_appts):
        month = random.choice(["2026-01", "2026-02", "2026-03"])
        day = random.randint(1, 28)
        date = f"{month}-{day:02d}"
        mode = random.choices(modes, mode_weights)[0]
        hcp = random.choices(hcp_types, hcp_weights)[0]
        # Higher deprivation → longer waits on average
        base_wait = max(0, int(random.gauss(imd * 0.3, 5)))
        wait = min(base_wait, 42)
        status = random.choices(statuses, status_weights)[0]
        # DNA more likely in younger patients
        age = random.randint(0, 95)
        if age < 30 and random.random() < 0.12:
            status = "DNA"
        appts.append((appt_id, p_code, date, mode, hcp, wait, status, age))
        appt_id += 1

cur.executemany("INSERT INTO appointments VALUES (?,?,?,?,?,?,?,?)", appts)

conn.commit()
print(f"Built: {len(practice_data)} practices, {len(appts)} appointments")

# Quick sanity check
cur.execute("SELECT COUNT(*) FROM appointments")
print(f"Appointments in DB: {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(DISTINCT practice_code) FROM appointments")
print(f"Practices with appts: {cur.fetchone()[0]}")
cur.execute("SELECT MIN(wait_days), AVG(wait_days), MAX(wait_days) FROM appointments")
row = cur.fetchone()
print(f"Wait days — min: {row[0]}, mean: {row[1]:.1f}, max: {row[2]}")
conn.close()