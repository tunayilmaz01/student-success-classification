import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

df = pd.DataFrame({
    "Age": [19, 20, 21, 22, 23, 20, 24, 21, 22, 25, 23, 20],
    "StudyHours": [1, 2, 4, 6, 8, 3, 9, 5, 7, 10, 6, 2],
    "AttendanceRate": [60, 65, 75, 80, 90, 70, 95, 78, 85, 98, 88, 62],
    "Successful": [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0]
})

X = df[["Age", "StudyHours", "AttendanceRate"]]
y = df["Successful"]

model = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

model.fit(X_train, y_train)

train_prediction = model.predict(X_train)
prediction = model.predict(X_test)

prediction_probability = model.predict_proba(X_test)

accuracy = accuracy_score(y_test, prediction)

precision = precision_score(y_test, prediction)

recall = recall_score(y_test, prediction)

f1 = f1_score(y_test, prediction)

cm = confusion_matrix(y_test, prediction)

train_accuracy = accuracy_score(y_train, train_prediction)

print(f"Model train accuracy = {train_accuracy:.2f}")
print(f"Model test accuracy = {accuracy:.2f}")
print(f"Model precision = {precision:.2f}")
print(f"Model recall = {recall:.2f}")
print(f"Model F1 score = {f1:.2f}")
print(f"Model's confusion matrix: \n{cm}")
print(f"Model prediction probabilities = {prediction_probability}")


prediction2 = model.predict(pd.DataFrame({
    "Age": [22],
    "StudyHours": [7],
    "AttendanceRate": [85]
}))

prediction_probability2 = model.predict_proba(pd.DataFrame({
    "Age": [22],
    "StudyHours": [7],
    "AttendanceRate": [85]
}))
print(f"Additional prediction = {prediction2}")
print(f"Additional prediction probabilities = {prediction_probability2}")
