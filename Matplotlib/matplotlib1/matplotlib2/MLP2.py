import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

monthly = pd.read_csv("monthly.csv", parse_dates=["month"])
regional = pd.read_csv("regional.csv")
practices2 = pd.read_csv("practices2.csv")


##Exercise 1


fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Data")

axes[0, 0].set_title("PCT Same-Day")
axes[0, 0].hist(practices2["pct_same_day"], bins=30, alpha=0.5)
axes[0, 0].set_xlabel("% Appointments")
axes[0, 0].set_ylabel("Frequency")


axes[0, 1].hist(practices2["dna_rate"], bins=30, alpha=0.5)
axes[0, 1].set_xlabel("Appointments")
axes[0, 1].set_ylabel("Frequency")
axes[0, 1].set_title("dna rate")


axes[1, 0].set_title("workload vs same-day")
axes[1, 0].scatter(practices2["patients_per_gp"], practices2["pct_same_day"], c=practices2["imd_score"])
axes[1, 0].set_ylabel("same-day")
axes[1, 0].set_xlabel("workload")

axes[1, 1].scatter(practices2["imd_score"], practices2["dna_rate"])
axes[1, 1].set_title("IMD Score vs DNA rate")
axes[1, 1].set_xlabel("IMD Score")
axes[1, 1].set_ylabel("DNA Rate")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("MLP2_1.png")


##Exercise 2

fig, ax = plt.subplots()
ax.bar(regional["region"], regional["mean_same_day"], yerr=regional["se_same_day"])
plt.savefig("MLP2_2.png")

##exercise 3
fig, ax = plt.subplots()
ax.set_title("workload vs same-day")
ax.scatter(practices2["patients_per_gp"], practices2["pct_same_day"], c=practices2["imd_score"])
ax.set_ylabel("same-day")
ax.set_xlabel("workload")
best_idx = practices2["pct_same_day"].idxmax()
best = practices2.loc[best_idx]
ax.annotate("Highest PCT Same-Day",
            xy=(best["patients_per_gp"], best["pct_same_day"]),
            xytext=(best["patients_per_gp"] + 100, best["pct_same_day"] - 1),
            arrowprops=dict(arrowstyle="->"))
worst_idx = practices2["pct_same_day"].idxmin()
worst = practices2.loc[worst_idx]
ax.annotate("Lowest PCT Same-Day",
            xy=(worst["patients_per_gp"], worst["pct_same_day"]),
            xytext=(worst["patients_per_gp"] + 100, worst["pct_same_day"] + 3),
            arrowprops=dict(arrowstyle="->"))
plt.savefig("MLP2_3.png")


##exercise 4
fig, axes = plt.subplots(1, 3, figsize=(18, 7))

sns.boxplot(data=practices2, x="pct_same_day", y="region", ax=axes[0])
sns.violinplot(data=practices2, x="dna_rate", y="region", ax=axes[1])

sns.heatmap(practices2.select_dtypes("number").corr(), ax=axes[2], annot=True)
plt.savefig("MLP2_4.1.png")



## exercise 5


fig, axes = plt.subplots(1, 2, figsize=(14, 7))

sns.heatmap(practices2.select_dtypes("number").corr(), ax=axes[1], annot=True)




sns.scatterplot(data = practices2, x="patients_per_gp", y="pct_same_day", hue="imd_score", ax=axes[0])
axes[0].set_ylabel("same-day access")
axes[0].set_xlabel("workload")
axes[0].set_title("How does GP workload affect same-day access for patient?")
best_idx = practices2["pct_same_day"].idxmax()
best = practices2.loc[best_idx]
axes[0].annotate("Highest PCT Same-Day",
            xy=(best["patients_per_gp"], best["pct_same_day"]),
            xytext=(best["patients_per_gp"] + 50, best["pct_same_day"] - 1),
            arrowprops=dict(arrowstyle="->"))
worst_idx = practices2["pct_same_day"].idxmin()
worst = practices2.loc[worst_idx]
axes[0].annotate("Lowest PCT Same-Day",
            xy=(worst["patients_per_gp"], worst["pct_same_day"]),
            xytext=(worst["patients_per_gp"] + 100, worst["pct_same_day"] + 3),
            arrowprops=dict(arrowstyle="->"))
axes[1].set_title("Correlations between patient types, workload and accessibility")
axes[1].tick_params(axis='x', rotation=45)
fig.savefig("gp_access_summary.png", dpi=300, bbox_inches="tight")