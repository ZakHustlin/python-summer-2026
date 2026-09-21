import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("gp_features.csv")

print(df[["list_size","patients_per_gp","imd_score","pct_same_day"]].corr())

plt.scatter(df["list_size"], df["pct_same_day"], alpha=0.3)
plt.savefig("list_size_scatter.png", dpi=120)

from sklearn.feature_selection import mutual_info_regression
X = df[["list_size","patients_per_gp","imd_score"]]
mi = mutual_info_regression(X, df["pct_same_day"], random_state=0)
print({name: score for name, score in zip(X.columns, mi)})

from sklearn.preprocessing import LabelEncoder
reg_codes = LabelEncoder().fit_transform(df["region"])
X2 = df[["list_size","patients_per_gp"]].copy()
X2["region"] = reg_codes
mi2 = mutual_info_regression(
          X2, df["pct_same_day"],
          discrete_features=[False, False, True],
          random_state=0)
print(mi2)

print(df.groupby("pcn")["pct_same_day"].mean().std())
print(df["pct_same_day"].std())


g = df.groupby("pcn")["pct_same_day"]
pcn_sum = df["pcn"].map(g.sum())
pcn_cnt = df["pcn"].map(g.count())
df["pcn_loo"] = (pcn_sum - df["pct_same_day"]) / (pcn_cnt - 1)
print(df["pcn_loo"].corr(df["pct_same_day"]))

print(df[["pcn_loo","pct_same_day"]].describe())
print(df["pcn_loo"].dropna().corr(df["pct_same_day"]))