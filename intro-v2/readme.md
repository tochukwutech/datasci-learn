- I wasnt certain that the older model had actually learned useful patterns so we had to give it some data it hadnt seen before, thats why we used the **train_test_split()**
- so were splitting the dataset into 4:
    X_train, Y_train -> training the model with features and correct answers
    X_test, Y_test -> testing the model with unseen examples to check if it will get the correct answers.
X + Y
    X_train + Y_train -> TRAIN MODEL
    X_test + Y_test -> TEST MODEL
- understand that accuracy_score tells us how many the model gets right
- learnt that random_state creates some consistency in the ML model.
- cross-validation
- cross_val_score(
    model,
    features,
    labels,
    number_of_folds
)
- class distribution
- Train/test split evaluates the model on one held-out test set, while 5-fold cross-validation evaluates the model five times using different held-out portions of the dataset.
- ## **stratification** means that we want the classification model folds to contian the same proportion of data as in the original data set:
    for example: in the X and Y dataset that we hardcoded, there are 11 'elements' meaning that there would definitely be some inequality in the data set. eg: 5 males, 6 females, or whatever male and female number that will bond to 11 – it will not be equal. So **stratification** would help us make sure that in the cross validation folds, it would create the folds with the correct proportion of the dataset. in the 
- A validation technique isn’t designed to make your model’s accuracy higher. It’s designed to give you a more appropriate estimate of how the model performs.
- another upgrade that i wanted to factor in was to make the prediction model accept input from users to predict the gender. there is an ML concept that we need to understand which states that the model must be trained before accepting input from users.
- when thinking about the user being able to input details to predict the gender, I had to consider the nature of pythons input. It normally turns input to strings, so i had to typecast the variables to numerical data types. eg: height - int, weight - float, shoe size - int.
- having the input wasnt enough for the model to predict it, becuase the prediction model was taking in list input. Because of that, I had to append each of the input variables after collecting the input, keeping the structure in mind.
- the clf.predict() expects multiple rows in a 2D structure, so even if were only predicting one person, we have to wrap the list inside another list. ***[[user_data]]***