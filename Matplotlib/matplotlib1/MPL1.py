"""
MATPLOTLIB 1: CORE PLOTS
=========================
Session: ~90 min
Data: Three synthetic GP CSVs (monthly_appointments.csv, practices.csv, mode_by_region.csv)
You need: matplotlib, pandas, numpy. Seaborn for Part 5.

Work through each exercise in order. Write your code, run it, then move on.
If a plot looks wrong, fix it before continuing — the styling exercises build on earlier plots.

Import block (start here):
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

monthly = pd.read_csv("appointments.csv", parse_dates=["month"])
practices = pd.read_csv("practices.csv")
modes = pd.read_csv("mode.csv")


# ══════════════════════════════════════════════════════════════
# PART 1 — LINE PLOT
# ══════════════════════════════════════════════════════════════
# Plot total_appointments over month.
# Just get a line on screen first. Don't style it yet.
#
# Then: add face_to_face and telephone as separate lines on the SAME axes.
# Three lines, one figure.
#
# MY CODE:
plt.plot(monthly["month"], monthly["total_appointments"])
plt.plot(monthly["month"], monthly["face_to_face"])
plt.plot(monthly["month"], monthly["telephone"])
plt.savefig("part1.png")



# ══════════════════════════════════════════════════════════════
# PART 2 — BAR PLOT
# ══════════════════════════════════════════════════════════════
# Using `modes`, make a bar chart: one bar per region, showing face_to_face %.
#
# Then: try a GROUPED bar chart — face_to_face, telephone, and online_other
# side by side for each region. This is harder. You'll need to offset the
# x-positions manually. Think about what np.arange and bar width buy you.
#
# MY CODE:

x = np.arange(len(modes))
plt.bar(x, modes["face_to_face"], width=0.25)
plt.bar(x - 0.25, modes["telephone"], width=0.25)
plt.bar(x + 0.25, modes["online_other"], width=0.25)
plt.savefig("part2.png")


# ══════════════════════════════════════════════════════════════
# PART 3 — SCATTER PLOT
# ══════════════════════════════════════════════════════════════
# Using `practices`: scatter patients_per_gp (x) vs pct_same_day (y).
#
# Question before you plot: what relationship do you EXPECT to see,
# and why? Write your prediction as a comment.
#
# Then: try colouring the dots by imd_decile. You'll want the `c` parameter
# and a colormap. What does the colour add to the story?
#
# YOUR CODE:

plt.scatter(practices["patients_per_gp"], practices["pct_same_day"], c=practices["imd_decile"])
plt.colorbar()
plt.savefig("part3.png")



# ══════════════════════════════════════════════════════════════
# PART 4 — HISTOGRAM
# ══════════════════════════════════════════════════════════════
# Plot the distribution of pct_same_day across all 800 practices.
# Start with default bins, then try bins=30 and bins=50. Which tells
# the clearest story?
#
# Then: plot pct_same_day and pct_wait_15plus as TWO overlapping histograms
# on the same axes. You'll need the `alpha` parameter (transparency).
# The point: these two metrics are NOT mirror images. Can you see that?
#
# MY CODE:

plt.hist(practices["pct_same_day"], bins=30, alpha=0.5)
plt.hist(practices["pct_wait_15plus"], bins=30, alpha=0.5)
plt.savefig("part4.png")



# ══════════════════════════════════════════════════════════════
# PART 5 — STYLING (apply to any plot above)
# ══════════════════════════════════════════════════════════════
# Pick your best plot from Parts 1–4 and add ALL of these:
#   - plt.figure(figsize=(...))  — pick a sensible size
#   - plt.title()
#   - plt.xlabel(), plt.ylabel()
#   - plt.legend()  (if multiple series)
#   - plt.tight_layout()
#   - plt.savefig("my_plot.png", dpi=150)
#
# Rule from the project bible: "Every chart gets a sentence."
# After saving, write a one-line interpretation as a comment.
#
# YOUR CODE:
plt.figure(figsize=(10, 6))  
plt.hist(practices["pct_same_day"], bins=35, alpha=0.5)
plt.hist(practices["pct_wait_15plus"], bins=35, alpha=0.5)
plt.title("Same Day Access vs 15 Day Wait Distribution")
plt.xlabel("% Appointments")
plt.ylabel("Frequency")
plt.legend(["Same-Day", "15-Day"])   # one label per series, in order
plt.tight_layout()                 # stops labels getting clipped
plt.savefig("part5.png", dpi=250)  # higher dpi = sharper image
plt.savefig("part5.png")

## These distributions have different shapes and centers, which means
## they are measuring different things. 
# ══════════════════════════════════════════════════════════════
# PART 6 — SEABORN TASTER
# ══════════════════════════════════════════════════════════════
# Uncomment the seaborn import at the top.
#
# 6a) sns.histplot(practices["pct_same_day"], kde=True)
#     What does the kde=True line add? When would it mislead?
#
# 6b) sns.scatterplot(data=practices, x="patients_per_gp", y="pct_same_day",
#                     hue="region", alpha=0.6)
#     Compare this to your Part 3 scatter. What did Seaborn do for free
#     that you had to do manually?
#
# 6c) sns.boxplot(data=practices, x="region", y="pct_same_day")
#     New plot type. What do the box, whiskers, and dots represent?
#     (If you're not sure, look at it and reason from the data.)
#
# YOUR CODE:
sns.histplot(practices["pct_same_day"], kde=True)
plt.savefig("part6a.png")

sns.scatterplot(data=practices, x="patients_per_gp", y="pct_same_day",
                hue="region", alpha=0.6)
plt.savefig("part6b.png")

sns.boxplot(data=practices, x="region", y="pct_same_day")
plt.savefig("part6c.png")


# ══════════════════════════════════════════════════════════════
# CHALLENGE (if time remains)
# ══════════════════════════════════════════════════════════════
# Make a 2x2 subplot grid using plt.subplots(2, 2, figsize=(12, 10)):
#   Top-left:     line plot (monthly appointments)
#   Top-right:    bar chart (mode by region)
#   Bottom-left:  scatter (workload vs same-day access)
#   Bottom-right: histogram (same-day distribution)
#
# Title the whole figure. Save it. This is the "publication quality"
# preview — Matplotlib 2 will go deeper.
#
# YOUR CODE:
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].set_title("total_appointments")
axes[0, 0].plot(monthly["month"], monthly["total_appointments"], alpha=0.5)
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Appointments")


axes[0, 1].bar(modes["region"], modes["face_to_face"])
axes[0, 1].set_xlabel("region")
axes[0, 1].set_ylabel("mode")


axes[1, 0].set_title("workload vs same-day")
axes[1, 0].scatter(practices["patients_per_gp"], practices["pct_same_day"], c=practices["imd_decile"])
axes[1, 0].set_ylabel("same-day")
axes[1, 0].set_xlabel("workload")

axes[1, 1].hist(practices["pct_same_day"], bins=30, alpha=0.5)
axes[1, 1].set_title("Same-Day Access Distribution")
axes[1, 1].set_xlabel("% Same-Day")
axes[1, 1].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("part7.png")