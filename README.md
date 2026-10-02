# student-success-classification

This is a small machine learning project I made to predict whether a student will be successful or not using their age, study hours, and attendance rate.

## Model

I used Logistic Regression for this project to predict whether a student would be successful based on the given student data.

## Evaluation

I evaluated the model using the following metrics:

- Accuracy

- Precision

- Recall

- F1 Score

- Confusion Matrix

I used these metrics to see how well the model was making predictions and where it was making mistakes.

## Dataset

- The dataset contains 12 student records with the following features:

- Age

- Study Hours

- Attendance Rate

- Successful

The Successful column is the target variable. A value of 1 means the student was successful, while 0 means the student was unsuccessful.

## Example Prediction

I also tested the model with a new student using:

- Age: 22

- Study Hours: 7

- Attendance Rate: 85

The model gives a prediction for the student and also shows the probability for each class.

## Results

The model was tested using a separate test set with Accuracy, Precision, Recall, F1 Score, and a Confusion Matrix.

The model achieved:

- Train Accuracy: 1.00
- Test Accuracy: 0.67
- Precision: 0.67
- Recall: 1.00
- F1 Score: 0.80

The confusion matrix showed that the model correctly predicted the successful students, but one unsuccessful student was predicted as successful.

Since the dataset is small, these results should not be taken as real-world performance. I mainly made this project to practice the basic machine learning classification workflow and get more familiar with Logistic Regression and evaluation metrics.
