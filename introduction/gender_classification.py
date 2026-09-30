from sklearn import tree

# the tree submodule allows us to build a decision tree
# A decision tree is a machine-learning model structured like a flowchart that uses a series of learned questions/splits to arrive at a prediction.

# [height, weight, shoe size]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()  # create a decision tree classifier

clf = clf.fit(X,Y)

prediction = clf.predict([[190, 70, 43]])
# predict the gender of a person with height 190, weight 70, and shoe size 43

print(prediction)