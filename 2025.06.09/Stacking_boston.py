
from pandas import read_csv
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np  

from sys import path
from pathlib import Path

path_dir = Path(path[0])

data = read_csv(path_dir / "boston.csv")

target = data["MEDV"]

data = data.drop("MEDV", axis=1)

x_train, x_test, y_train, y_test = train_test_split(data, target, train_size=0.3, random_state=1)

model = StackingRegressor(
    estimators=[
        ('ridge', RidgeCV()),
        ('lr', LinearRegression()),
        ('svr', LinearSVR(random_state=1))
    ],
    final_estimator=RandomForestRegressor(n_estimators=30, random_state=1)
)

model.fit(x_train, y_train)

pred = model.predict(x_test)

mae = mean_absolute_error(y_test, pred) 
mse = mean_squared_error(y_test, pred)   
rmse = np.sqrt(mse)                       
r2 = r2_score(y_test, pred)               


print(f"MAE: {mae:.4f}")  
print(f"MSE: {mse:.4f}")  
print(f"RMSE: {rmse:.4f}")  
print(f"R2: {r2:.4f}") 


# MAE: 3.6303
# MSE: 26.2475
# RMSE: 5.1232
# R2: 0.6795