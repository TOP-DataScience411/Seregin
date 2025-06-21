from numpy import array
from pandas import DataFrame, read_csv, Series
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from pathlib import Path
from sys import path

script_dir = Path(path[0])
model = read_csv(script_dir / "boston.csv", encoding="utf-8")

y = model["MEDV"]
x = model.drop(columns=["MEDV"])

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0
)

models_1st_lvl = [
    KNeighborsRegressor(n_neighbors=3),
    Ridge(),
    DecisionTreeRegressor(max_depth=6),
]
model_2nd_lvl = LinearRegression()
y_trained_preds_1st_lvl = []
y_preds_1st_lvl = []
models_scores = []
for model in models_1st_lvl:
    model.fit(x_train, y_train)
    y_trained_preds_1st_lvl.append(model.predict(x_train))
    q = model.predict(x_test)
    y_preds_1st_lvl.append(q)
    rmse = mean_squared_error(y_test, q)
    models_scores.append(rmse)

y_preds_1st_lvl = DataFrame(
    {
        'knn': y_preds_1st_lvl[0],
        'ridge': y_preds_1st_lvl[1],
        'dec_tree': y_preds_1st_lvl[2],
    }
)

model_2nd_lvl.fit(y_preds_1st_lvl, y_test)

y_preds_all_1st_lvl = array(
    array(y_trained_preds_1st_lvl).T.tolist()
    + y_preds_1st_lvl.values.tolist()
).T
y_preds_all_1st_lvl = DataFrame(
    {
        'knn': y_preds_all_1st_lvl[0],
        'ridge': y_preds_all_1st_lvl[1],
        'dec_tree': y_preds_all_1st_lvl[2],
    }
)

y_preds_all_2nd_lvl = model_2nd_lvl.predict(y_preds_all_1st_lvl)
y_test_all_2nd_lvl = y_train.values.tolist() + y_test.values.tolist()

mae = mean_absolute_error(y_test_all_2nd_lvl, y_preds_all_2nd_lvl)
mse = mean_squared_error(y_test_all_2nd_lvl, y_preds_all_2nd_lvl)
rmse = mse ** 0.5
r2 = r2_score(y_test_all_2nd_lvl, y_preds_all_2nd_lvl)


print(f"MAE= {mae:.2f}")
print(f"MSE= {mse:.2f}")
print(f"RMSE= {rmse:.2f}")
print(f"R2= {r2:.2f}")