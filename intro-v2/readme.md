- we werent certain that the older model had actually learned useful patterns so we had to give it some data it hadnt seen before, thats why we used the **train_test_split()**
- so were splitting the dataset into 4:
    X_train, Y_train -> training the model with features and correct answers
    X_test, Y_test -> testing the model with unseen examples to check if it will get the correct answers.
X + Y
    X_train + Y_train -> TRAIN MODEL
    X_test + Y_test -> TEST MODEL
- understand that accuracy_score tells us how many the model gets right
- learnt that random_state creates some consistency in the ML model.
- cross-validation