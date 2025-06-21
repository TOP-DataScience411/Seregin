from pandas import read_csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
    
from sklearn.model_selection import train_test_split

from pandas import read_csv
from pathlib import Path
from sys import path

script_dir = Path(path[0])
model = read_csv(script_dir / "boston.csv", encoding="utf-8")

y = model["MEDV"]
x = model.drop(columns=["MEDV"])

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1
)

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    n_jobs=-1,
    random_state=1
)

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
rmse = mse ** 0.5  
r2 = r2_score(y_test, y_predict)

print(f"MAE= {mae:.2f}")
print(f"MSE= {mse:.2f}")
print(f"RMSE= {rmse:.2f}")
print(f"R2= {r2:.2f}")

# model = RandomForestRegressor(
    # n_estimators=100,
    # max_depth=5,
    # n_jobs=-1,
    # random_state=1
# )
# MAE= 2.45
# MSE= 9.70
# RMSE= 3.11
# R2= 0.90
# ---------------------
# model = RandomForestRegressor(
    # n_estimators=100,
    # max_depth=3,
    # n_jobs=-1,
    # random_state=1
# MAE= 2.82
# MSE= 12.36
# RMSE= 3.52
# R2= 0.87
# --------------------
# model = RandomForestRegressor(
    # n_estimators=100,
    # max_depth=7,
    # n_jobs=-1,
    # random_state=1
#MAE= 2.39
# MSE= 9.03
# RMSE= 3.00
# R2= 0.91
