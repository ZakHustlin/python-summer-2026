import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
df = pd.read_csv("data.csv")
y = df["pct_same_day"]

x = df[["list_size", "pct_65plus", "patients_per_gp", "imd_score", "region", "rural"]]
x = pd.get_dummies(x, columns=["region"])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=100)
model.fit(x_train, y_train)
predictions = model.predict(x_test)

contributors = model.feature_importances_
print(pd.Series(contributors, x.columns).sort_values(ascending=False))