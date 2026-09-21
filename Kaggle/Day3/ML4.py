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
df = pd.read_csv("gp_practices.csv")

y = df["pct_same_day"]
X = df.drop(columns=["pct_same_day"])

# split into train / valid
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, random_state=0)

numerical_cols = X_train.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = X_train.select_dtypes(include="str").columns.tolist()

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))])

preprocessor = ColumnTransformer(transformers=[
    ("nums", numeric_transformer, numerical_cols),
    ("cats", categorical_transformer, categorical_cols)])



pipe = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(n_estimators=100, random_state=0) )
])




pipe.fit(X_train, y_train)
preds = pipe.predict(X_valid)
print(mean_absolute_error(y_valid, preds))


scores = cross_val_score(pipe, X, y,
                         cv=5,
                         scoring="neg_mean_absolute_error")
print("fold MAEs:", -scores)
print("mean MAE:", -scores.mean())



pipe = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", XGBRegressor(n_estimators=500, learning_rate=0.05, random_state=0) )
])


scores = cross_val_score(pipe, X, y,
                         cv=5,
                         scoring="neg_mean_absolute_error")
print("mean MAE:", -scores.mean())



numerical_cols = X_train.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = X_train.select_dtypes(include="str").columns.tolist()

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))

])

preprocessor = ColumnTransformer(transformers=[
    ("nums", numeric_transformer, numerical_cols),
    ("cats", categorical_transformer, categorical_cols)


])

pipe = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", XGBRegressor(n_estimators=600, learning_rate=0.02, random_state=0))



])


scores = cross_val_score(pipe, X, y,
                         cv=6,
                         scoring="neg_mean_absolute_error")

print(-scores.mean())