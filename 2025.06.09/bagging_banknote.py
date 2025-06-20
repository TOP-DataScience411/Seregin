from pandas import read_csv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import fbeta_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier

from sys import path
from pathlib import Path

path_dir = Path(path[0])
data = read_csv(path_dir / "banknote-auth.csv")

target = data["class"]
data = data.drop("class", axis=1)

x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=1)

model = BaggingClassifier(
    estimator=LogisticRegression(),
    n_estimators=8,
    bootstrap=True,
    n_jobs=-1,
    random_state=1  
)

model.fit(x_train, y_train)

pred = model.predict(x_test)

conf_matr = confusion_matrix(y_test, pred)
(TN, FP), (FN, TP) = conf_matr
accuracy = (TN + TP) / (TN + FP + FN + TP)
specificity = TN / (TN + FP)
precision = TP / (FP + TP) if (FP + TP) > 0 else 0
recall = TP / (FN + TP) if (FN + TP) > 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
fbeta = fbeta_score(y_test, pred, beta=0.5)

print(f'Accuracy: {accuracy:.1%}')
print(f'specificity: {specificity:.1%}')
print(f'Precision: {precision:.1%}')
print(f'recall: {recall:.1%}')
print(f'F1: {f1:.1%}')
print(f'F-beta: {fbeta:.1%}')


# Accuracy: 99.3%
# specificity: 99.4%
# Precision: 99.2%
# recall: 99.2%
# F1: 99.2%
# F-beta: 99.2%