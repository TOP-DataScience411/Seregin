from pandas import read_csv
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix, 
    ConfusionMatrixDisplay,
    recall_score,
    precision_score,
)
from pathlib import Path

from sys import path
from matplotlib import pyplot as plt

script_dir = Path(path[0])
data = read_csv(script_dir / "banknote-auth.csv", encoding="utf-8")

x = data.drop(columns=["class"])
y = data["class"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=1
)
model = BaggingClassifier(
    estimator=DecisionTreeClassifier(max_depth=5),
    n_estimators=50,
    n_jobs=-1,
    random_state=1
)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
pre = precision_score(y_test, y_pred)


print(f"\nаccuracy = {acc:.2f}\n")
print(f"\nrecall   = {rec:.2f}\n")
print(f"\npresicion= {pre:.2f}\n")

# аccuracy = 0.99


# recall   = 0.99


# presicion= 0.99