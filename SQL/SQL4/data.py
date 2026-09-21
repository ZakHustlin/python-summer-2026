import pandas as pd
import sqlite3

practices = pd.DataFrame({
    "practice_code": ["P001", "P002", "P003", "P004"],
    "practice_name": ["Riverside", "Oakfield", "Elmwood", "Hillcrest"],
    "list_size":     [8000, 12000, 5000, 9500],
    "region":        ["North", "North", "South", "South"],
})
appointments = pd.DataFrame({
    "appt_id":       range(1, 17),
    "practice_code": ["P001","P001","P001","P002","P002","P002","P002","P003","P003","P003","P004","P004","P004","P004","P001","P002"],
    "hcp_type":      ["GP","GP","Nurse","GP","GP","Nurse","GP","Nurse","GP","GP","GP","Nurse","GP","Nurse","GP","GP"],
    "mode":          ["F2F","Phone","F2F","F2F","Phone","F2F","Phone","F2F","F2F","Phone","F2F","F2F","Phone","F2F","F2F","Phone"],
    "status":        ["Attended","Attended","DNA","Attended","DNA","Attended","Attended","Attended","DNA","Attended","Attended","Attended","Attended","DNA","Attended","Attended"],
    "wait_days":     [0, 3, 14, 2, 21, 0, 7, 5, 28, 1, 0, 9, 15, 3, 6, 12],
})

conn = sqlite3.connect("gp.db")
appointments.to_sql("appointments", conn, if_exists="replace", index=False)