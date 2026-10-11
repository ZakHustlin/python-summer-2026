import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("gp_practices.csv")
df["patients_per_gp"] = df["list_size"] / df["fte_gps"]  
y = df["pct_same_day"]
x = df.drop(columns=["practice_code", "pct_same_day", "same_day_appts_3m", "total_appts_3m"])                             

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=0)

numerical_cols = x_train.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = x_train.select_dtypes(exclude=[np.number]).columns.tolist()

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))])

preprocessor = ColumnTransformer(transformers=[
    ("nums", numeric_transformer, numerical_cols),
    ("cats", categorical_transformer, categorical_cols)
])


pipe = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", XGBRegressor(random_state=0, learning_rate=0.05, max_depth=3))
])

pipe.fit(x_train, y_train)
preds = pipe.predict(x_test)
#print("mae: ", mean_absolute_error(y_test, preds))

baseline_pred = np.full(shape=y_test.shape, fill_value=y_train.mean())
#print("baseline mae: ", mean_absolute_error(y_test, baseline_pred))
scores = -cross_val_score(pipe, x_train, y_train, cv=5, scoring="neg_mean_absolute_error")
#print("crossval: ", scores)
print("crossval mean: ", scores.mean())
#print("crossval std: ", scores.std())

from sklearn.inspection import permutation_importance

result = permutation_importance(pipe, x_test, y_test,
                                n_repeats=10, random_state=0,
                                scoring="neg_mean_absolute_error")

imp = pd.Series(result.importances_mean, index=x_test.columns)
print(imp.sort_values(ascending=False))

import seaborn as sns
sns.regplot(data=df, x="pct_65plus", y="pct_same_day", scatter_kws={"alpha": 0.2})
plt.savefig("scatter")