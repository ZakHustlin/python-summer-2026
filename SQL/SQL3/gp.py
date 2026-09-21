import sqlite3
con = sqlite3.connect("gp.db"); c = con.cursor()
c.executescript("""
DROP TABLE IF EXISTS practices; DROP TABLE IF EXISTS appointments; DROP TABLE IF EXISTS workforce;
CREATE TABLE practices (code TEXT, name TEXT, list_size INT, region TEXT);
CREATE TABLE workforce (code TEXT, fte_gp REAL, fte_nurse REAL);
CREATE TABLE appointments (appt_id INT, code TEXT, hcp TEXT, wait_band TEXT, attended INT);

INSERT INTO practices VALUES
 ('P001','Riverside',8200,'North East'),('P002','Kirk Lane',4100,'North East'),
 ('P003','Marsh Road',12500,'London'),('P004','Ash Grove',6700,'London'),
 ('P005','Hill Top',2300,'South West'),('P006','Fen End',9900,'East');

INSERT INTO workforce VALUES
 ('P001',4.5,3.0),('P002',2.0,1.5),('P002',1.0,0.5),
 ('P003',7.2,5.0),('P004',3.1,2.0),('P006',5.0,4.0);

INSERT INTO appointments VALUES
 (1,'P001','GP','Same Day',1),(2,'P001','Nurse','2-7 Days',1),(3,'P001','GP','15-21 Days',0),
 (4,'P002','GP','Same Day',1),(5,'P002','GP','8-14 Days',1),
 (6,'P003','GP','Same Day',1),(7,'P003','Nurse','Same Day',1),(8,'P003','GP','22-28 Days',1),
 (9,'P004','GP','2-7 Days',0),(10,'P005','GP','Same Day',1),
 (11,'P099','GP','Same Day',1),(12,'P099','Nurse','2-7 Days',1);
""")
con.commit()