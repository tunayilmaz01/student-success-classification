# student-success-classification

  This project develops a machine learning model to predict whether a student will be successful based on their age, study hours, and attendance rate.

## Model

  Logistic Regression was used to predict whether a student would be successful based on the available student data.

## Evaluation

- The model was evaluated using the following metrics:

- Accuracy

- Precision

- Recall

- F1 Score

- Confusion Matrix

  These metrics were used to evaluate the model's classification performance and understand how well it predicts student success.

## Dataset

- The dataset contains 12 student records with the following features:

- Age

- Study Hours

- Attendance Rate

- Successful

  The Successful column is the target variable. A value of 1 represents a successful student, while 0 represents an unsuccessful student.

## Example Prediction

  The trained model was also used to predict the outcome of a new student using:

- Age: 22

- Study Hours: 7

- Attendance Rate: 85

  The model returns both the predicted class and the probability of each class.

## Results

  The model was evaluated on a separate test set using Accuracy, Precision, Recall, F1 Score, and a Confusion Matrix.

  The model achieved:

- Train Accuracy: 1.00
- Test Accuracy: 0.67
- Precision: 0.67
- Recall: 1.00
- F1 Score: 0.80

  The confusion matrix showed that the model correctly identified the successful students in the test set, while one unsuccessful student was incorrectly classified as successful.

  Because the dataset is small, these results should not be considered representative of real-world model performance. The project is intended to demonstrate the basic machine learning classification workflow.
