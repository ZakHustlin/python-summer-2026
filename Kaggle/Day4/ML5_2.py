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
from xgboost import XGBClassifier
df = pd.read_csv("trials.csv")
df["phase"] = df["phase"].astype(str)
y = df["terminated"]
x = df.drop(columns=["terminated"])
x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8, random_state=0, stratify=y)

numerical_cols = x_train.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = x_train.select_dtypes(include="object").columns.tolist()

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
    ("model", XGBClassifier(n_estimators=100, random_state=0, scale_pos_weight=4.6))
])

print(numerical_cols)
print(categorical_cols)

pipe.fit(x_train, y_train)
preds = pipe.predict(x_test)
print(categorical_cols)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, preds))

from sklearn.metrics import classification_report
print(classification_report(y_test, preds, digits=3))

from sklearn.metrics import roc_auc_score
proba = pipe.predict_proba(x_test)[:, 1]     # column 1 = P(terminated)
print(roc_auc_score(y_test, proba))