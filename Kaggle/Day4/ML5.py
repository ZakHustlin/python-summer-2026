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
df = pd.read_csv("gp_access.csv")
y = df["pct_same_day"]
x = df.drop(columns=["pct_same_day"])
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=0)

numerical_cols = x_train.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = ["region"]

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
    ("model", XGBRegressor(n_estimators=600, learning_rate=0.02, random_state=0))
])

print(numerical_cols)
print(categorical_cols)

pipe.fit(x_train, y_train)
preds = pipe.predict(x_test)
print(mean_absolute_error(y_test, preds))

baseline_pred = np.full(shape=y_test.shape, fill_value=y_train.mean())
print(mean_absolute_error(y_test, baseline_pred))

print(r2_score(y_test, preds))
