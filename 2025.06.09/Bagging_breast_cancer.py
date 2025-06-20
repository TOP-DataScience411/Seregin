from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import fbeta_score, confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier

data_raw = load_breast_cancer()
X = data_raw.data
y = data_raw.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = BaggingClassifier(
    estimator=LogisticRegression(),
    n_estimators=7,
    bootstrap=True,
    n_jobs=-1
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

conf_matr = confusion_matrix(y_test, pred)
(TN, FP), (FN, TP) = conf_matr

accuracy = accuracy_score(y_test, pred)
specificity = TN / (TN + FP)
precision = precision_score(y_test, pred)
recall = recall_score(y_test, pred)
f1 = 2 * precision * recall / (precision + recall)
fbeta = fbeta_score(y_test, pred, beta=0.5)

print(
    f'accuracy: {accuracy:.1%}',
    f'specificity: {specificity:.1%}',
    f'precision: {precision:.1%}',
    f'recall: {recall:.1%}',
    f'f1: {f1:.1%}',
    f'fbeta: {fbeta:.1%}',
    sep='\n'
)



# accuracy: 98.2%
# specificity: 97.6%
# precision: 98.6%
# recall: 98.6%
# f1: 98.6%
# fbeta: 98.6%
