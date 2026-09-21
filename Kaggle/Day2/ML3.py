import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("gp_access.csv")
df = df.drop(columns=["practice_code", "pcn", "pct_under_5"])
X = pd.get_dummies(df.drop(columns=["pct_same_day"]))   # region + rurality
y = df["pct_same_day"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = RandomForestRegressor(n_estimators=100, random_state=0)

##A
X_train_a = X_train.copy()
X_test_a = X_test.copy()
X_train_a = X_train_a.dropna(axis=1)
X_test_a = X_test_a[X_train_a.columns]
model.fit(X_train_a, y_train)
preds = model.predict(X_test_a)
print(mean_absolute_error(y_test, preds))
##B
X_train_b = X_train.copy()
X_test_b = X_test.copy()
imputer = SimpleImputer(strategy="mean")   # create and save
X_train_b = imputer.fit_transform(X_train_b)  # fit on train, transform train
X_test_b = imputer.transform(X_test_b)         # transform test (no fit!)
model.fit(X_train_b, y_train)
predsb = model.predict(X_test_b)
print(mean_absolute_error(y_test, predsb))


##C


X_train_c = X_train.copy()
X_test_c = X_test.copy()

X_train_c["patients_per_gp_was_missing"] = X_train_c["patients_per_gp"].isna()
X_test_c["patients_per_gp_was_missing"] = X_test_c["patients_per_gp"].isna()
# now impute, fit, predict
imputer = SimpleImputer(strategy="mean")   # create and save
X_train_c = imputer.fit_transform(X_train_c)  # fit on train, transform train
X_test_c = imputer.transform(X_test_c)

model.fit(X_train_c, y_train)
predsc = model.predict(X_test_c)
print(mean_absolute_error(y_test, predsc))


from sklearn.pipeline import Pipeline



numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])
preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer,     numerical_cols),
    ("cat", categorical_transformer, categorical_cols),
])

pipe = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(n_estimators=100, random_state=0) )
])

pipe.fit(X_train, y_train)
preds = pipe.predict(X_test)
print(mean_absolute_error(y_test, preds))


