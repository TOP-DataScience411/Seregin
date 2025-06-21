from pandas import read_csv
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from pathlib import Path
from sys import path

script_dir = Path(path[0])
model = read_csv(script_dir / "boston.csv")

y = model["MEDV"]
x = model.drop(columns=["MEDV"])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

bagging_model = BaggingRegressor(
    estimator=DecisionTreeRegressor(),
    n_estimators=75,
    n_jobs=-1,
    random_state=0
)
bagging_model.fit(x_train, y_train)

y_predict = bagging_model.predict(x_test)

mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_predict)

print(f"MAE= {mae:.2f}")
print(f"MSE= {mse:.2f}")
print(f"RMSE= {rmse:.2f}")
print(f"R2= {r2:.2f}")





# bagging_model = BaggingRegressor(
    # estimator=DecisionTreeRegressor(),
    # n_estimators=54,
    # n_jobs=-1,
    # random_state=0
# )
# MAE= 2.47
# MSE= 14.79
# RMSE= 3.85
# R2= 0.82
# ---------------------------


# bagging_model = BaggingRegressor(
    # estimator=DecisionTreeRegressor(),
    # n_estimators=75,
    # n_jobs=-1,
    # random_state=0
# )
# MAE= 2.46
# MSE= 14.35
# RMSE= 3.79
# R2= 0.83


    
    