# this is an improvement on the previous gender classification model which uses hard coded values.
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score

data = pd.read_csv("intro-v2/gender_data.csv")  # read the data from a CSV file
print(data)

X = data[['height', 'weight', 'shoe_size']].values  # features
Y = data['gender'].values  # target variable

# the tree submodule allows us to build a decision tree
# A decision tree is a machine-learning model structured like a flowchart that uses a series of learned questions/splits to arrive at a prediction.

# [height, weight, shoe size]

# X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# Y = ['male', 'female', 'female', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'male']

# clf = tree.DecisionTreeClassifier()  # create a decision tree classifier

# clf = clf.fit(X,Y)

# prediction = clf.predict([[190, 70, 43]])
# # predict the gender of a person with height 190, weight 70, and shoe size 43

# print(prediction)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state=17) # split the data into training and testing sets
clf = tree.DecisionTreeClassifier() # create a decision tree classifier
clf = clf.fit(X_train,Y_train)  # train the model on the training data

prediction = clf.predict(X_test)  # predict the gender of the test data
print(prediction)
accuracy = accuracy_score(Y_test, prediction)
print(accuracy)

scores = cross_val_score(clf, X, Y, cv=5)  # perform cross-validation to evaluate the model's performance
print(scores)
scores = cross_val_score(clf, X, Y, cv=StratifiedKFold(n_splits=5))
print(scores)
print(f"Mean accuracy: {scores.mean()}")  # print the mean accuracy of the model across all folds


# handling user inptu

height = int(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
shoe_size = int(input("Enter your shoe size: "))

user_data = [height, weight, shoe_size] # creating a list of the inputs

# predicting the gender of the user based on their inputs
user_prediction = clf.predict([user_data])
print(f"The predicted gender is: {user_prediction[0]}")  # print the predicted gender of the user