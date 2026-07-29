import numpy as np

data = np.loadtxt("week4/example.csv", delimiter=",", skiprows=1)
age = data[:, 1]
bmi = data[:, 3]
systolic_bp = data[:, 4]
mean_bp = np.mean(systolic_bp)
for name, col in [("Age", age), ("BMI", bmi), ("BP", systolic_bp)]:
    print(f"{name}: min={col.min()}, max={col.max()}, mean={col.mean():.1f}")

high_bmi = data[bmi > 30]
number_high_bmi = high_bmi.shape[0]
number_high_bmi_bp_mean = np.mean(high_bmi[:, 4])
bp_comparison = number_high_bmi_bp_mean - mean_bp
print(f"Mean systolic BP is {number_high_bmi_bp_mean:.0f} among 30+ BMI individuals. This is {bp_comparison:.0f} higher than the overall average. There are {number_high_bmi} people with a BMI above 30")

result = np.corrcoef(age, systolic_bp)
correlation = result[0, 1]
print(correlation)
