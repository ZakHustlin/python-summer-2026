import numpy as np, pandas as pd
rng = np.random.default_rng(42)
n = 1200

region = rng.choice(["North East","North West","Midlands","East","London","South East","South West"],
                    n, p=[.07,.15,.18,.12,.14,.20,.14])
rurality = rng.choice(["Urban","Suburban","Rural"], n, p=[.55,.30,.15])
pcn = np.array([f"PCN_{i:03d}" for i in rng.integers(0, 180, n)])   # high cardinality

list_size      = rng.lognormal(8.9, 0.45, n).round()
imd_score      = np.clip(rng.normal(22, 11, n), 1, 60)              # higher = more deprived
pct_65_plus    = np.clip(rng.normal(18, 5, n) - imd_score*0.12, 3, 40)
patients_per_gp = np.clip(rng.normal(1900, 380, n) + imd_score*9, 900, 4200)
appts_per_1000  = np.clip(rng.normal(370, 60, n) - imd_score*1.2, 150, 600)

pct_same_day = (58
    - 0.0042*(patients_per_gp - 1900)
    - 0.28*(imd_score - 22)
    + 0.15*(pct_65_plus - 18)
    + np.where(rurality=="Rural", 6, 0)
    + rng.normal(0, 6, n))
pct_same_day = np.clip(pct_same_day, 5, 95)

df = pd.DataFrame(dict(practice_code=[f"P{i:05d}" for i in range(n)],
    region=region, rurality=rurality, pcn=pcn, list_size=list_size,
    imd_score=imd_score, pct_65_plus=pct_65_plus,
    patients_per_gp=patients_per_gp, appts_per_1000=appts_per_1000,
    pct_same_day=pct_same_day.round(2)))

# missingness — three different mechanisms, deliberately
miss_p = 1/(1+np.exp(-(0.05*(df.patients_per_gp-1900)/380 + 0.9*(df.imd_score-22)/11 - 2.0)))
df.loc[rng.random(n) < miss_p, "patients_per_gp"] = np.nan     # (a)
df.loc[rng.random(n) < 0.06, "imd_score"] = np.nan             # (b)
df["pct_under_5"] = np.where(rng.random(n) < 0.88, np.nan,
                             np.clip(rng.normal(6, 1.5, n), 1, 12))  # (c)

df.to_csv("gp_access.csv", index=False)
print(df.isna().mean().round(3))