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
    max_depth=7,
    n_jobs=-1,
)

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
rmse = mse ** 0.5  
r2 = r2_score(y_test, y_predict)

print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2: {r2:.2f}")

# model = RandomForestRegressor(
    # n_estimators=100,
    # max_depth=5,
    # n_jobs=-1,
# MAE: 2.45
# MSE: 9.73
# RMSE: 3.12
# R2: 0.90

# -------------


# model = RandomForestRegressor(
    # n_estimators=100,
    # max_depth=3,
    # n_jobs=-1,
# MAE: 2.68
# MSE: 11.84
# RMSE: 3.44
# R2: 0.88

    
# ---------------
# model = RandomForestRegressor(
    # n_estimators=100,
    # max_depth=7,
    # n_jobs=-1,

# MAE: 2.35
# MSE: 9.12
# RMSE: 3.02
# R2: 0.91

# -------------
# model = RandomForestRegressor(
    # n_estimators=25,
    # max_depth=7,
    # n_jobs=-1,
# )
# MAE: 2.45
# MSE: 9.61
# RMSE: 3.10
# R2: 0.90



# ------------------
# model = RandomForestRegressor(
    # n_estimators=50,
    # max_depth=7,
    # n_jobs=-1,
# 

# MAE: 2.42
# MSE: 9.18
# RMSE: 3.03
# R2: 0.91



# ------------------
# model = RandomForestRegressor(
    # n_estimators=100,
    # max_depth=7,
    # n_jobs=-1,
    
# MAE: 2.42
# MSE: 9.75
# RMSE: 3.12
# R2: 0.90
    