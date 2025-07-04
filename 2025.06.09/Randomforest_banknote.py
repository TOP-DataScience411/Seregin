from matplotlib import pyplot as plt
from pandas import read_csv
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix, 
    ConfusionMatrixDisplay,
    recall_score,
    precision_score,
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from pathlib import Path
from sys import path

script_dir = Path(path[0])
data = read_csv(script_dir / "banknote-auth.csv", encoding="utf-8")

y = data["class"]
x = data.drop(columns=["class"])

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    n_jobs=-1,
)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# conf = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
pre = precision_score(y_test, y_pred)

# print("ConfMatrix:\n", conf)
print(f"\nаccuracy = {acc:.2f}\n")
print(f"\nrecall   = {rec:.2f}\n")
print(f"\npresicion= {pre:.2f}\n")

