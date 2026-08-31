import pandas as pd
import numpy as np
import re
df = pd.read_csv("messy.csv")

df["clinician"] = df["clinician"].str.replace("  +", " ", regex=True).str.title().str.strip()


df["appointment_type"] = df["appointment_type"].str.replace("-", " ", regex=True).str.lower().str.strip()

df["reason"] = df["reason"].str.lower().str.strip().replace("", np.nan)


df["status"] = df["status"].str.lower().replace({"dna": "did not attend", "cancelled by patient": "cancelled", "cancelled by practice": "cancelled"})


def parse_duration(val):
    if pd.isna(val):
        return np.nan
    else:
        val = re.sub("[^0-9.]", "", val)
        if val == "":
            return np.nan 
        else:
            val = float(val)
            return val

df["duration_mins"] = df["duration_mins"].apply(parse_duration)
##print(df["duration_mins"].mean(), df["duration_mins"].median())

df["wait_days"] = pd.to_numeric(df["wait_days"], errors="coerce")
df.loc[df["wait_days"] < 0, "wait_days"] = np.nan
proportion = df["wait_days"].count() / df.shape[0]

df["patient_age"] = df["patient_age"].str.strip()
df["patient_age"] = pd.to_numeric(df["patient_age"], errors="coerce")
##print(df["patient_age"].describe())

df["appointment_date"] = pd.read_csv("messy.csv", usecols=["appointment_date"])["appointment_date"]
mask = df["appointment_date"].str.startswith("2026/")
df.loc[mask, "appointment_date"] = df.loc[mask, "appointment_date"].str.replace("/", "-")
df["appointment_date"] = pd.to_datetime(df["appointment_date"], format="mixed", dayfirst=True)
###print(df["appointment_date"].min(), df["appointment_date"].max())
##print(mask.sum())
##print(df.loc[mask, "appointment_date"].head(10))

df.duplicated().sum()
df = df.drop_duplicates()


result = df.groupby(["practice_code"]).agg({"practice_code": "count", "patient_id": "nunique", "clinician": "nunique"})
result["repeat_rate"] = result["practice_code"] / result["patient_id"]


table = pd.pivot_table(df, index="practice_code", columns="appointment_type", values="patient_id", aggfunc="count", fill_value=0)
total = table.sum(axis=1)
p_telephone = table["telephone"] / total
##print(p_telephone.sort_values(ascending=False))

 
df["quarter"] = df["appointment_date"].dt.quarter
table3 = pd.pivot_table(df, index="region", columns="quarter", values="wait_days", aggfunc="mean", fill_value=0)
print(table3)
