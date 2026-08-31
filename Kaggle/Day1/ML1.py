import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
df = pd.read_csv("data.csv")
y = df["pct_same_day"]

x = df[["list_size", "pct_65plus", "patients_per_gp", "imd_score", "region", "rural"]]
x = pd.get_dummies(x, columns=["region"])





x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
depths = list(range(1, 22))
maes = []
for value in depths:
    model = DecisionTreeRegressor(max_depth=value)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    maes.append(mean_absolute_error(y_test, predictions))

best_depth = depths[maes.index(min(maes))]
print(f"Best depth: {best_depth}, MAE: {min(maes):.2f}")

for i, mae in enumerate(maes):
    print(f"depth {i+1}: {mae:.2f}")