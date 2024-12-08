import numpy as np
import pandas as pd
from sklearn import preprocessing
from EncodingValues import Encodings


def knnPrediction(state, crime,sex, age, race,count,weapon):

    read_data = pd.read_csv('./Dataset/database.csv', low_memory=False)

    print(read_data['Perpetrator_Sex'].value_counts())

    male_data=read_data[read_data['Perpetrator_Sex']=='Male']
    unknown_data=read_data[read_data['Perpetrator_Sex']=='Unknown']
    female_data=read_data[read_data['Perpetrator_Sex']=='Female']


    #creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.

    state_encoded=le.fit_transform(read_data['State'])
    crimeType_encoded = le.fit_transform(read_data['Crime_Type'])
    victimSex_encoded = le.fit_transform(read_data['Victim_Sex'])
    victimAge_encoded = le.fit_transform(read_data['Victim_Age'])
    victimRace_encoded = le.fit_transform(read_data['Victim_Race'])
    victimCount_encoded = le.fit_transform(read_data['Victim_Count'])#0
    weapon_encoded = le.fit_transform(read_data['Weapon'])

    #target variable
    label_output=le.fit_transform(read_data['Perpetrator_Sex'])

    features=list(zip(state_encoded,crimeType_encoded,victimSex_encoded,victimAge_encoded,
                      victimRace_encoded,victimCount_encoded,weapon_encoded))

    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors=3)

    # Train the model using the training sets
    model.fit(features,label_output)



    #Predict Output
    predicted= model.predict([[state,crime,sex,age,race,count,weapon]])
    print(predicted)

    from sklearn.model_selection import train_test_split

    from sklearn.neighbors import KNeighborsClassifier

    #Create KNN Classifier
    knn = KNeighborsClassifier(n_neighbors=20)
    X_train, X_test, y_train, y_test = train_test_split(features, label_output, test_size=0.3) # 70% training and 30% test
    #Train the model using the training sets
    knn.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = knn.predict(X_test)

   # from sklearn import metrics
    # Model Accuracy, how often is the classifier correct?
    #print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    #Import knearest neighbors Classifier model
    from sklearn.neighbors import KNeighborsClassifier

    #Create KNN Classifier
    knn = KNeighborsClassifier(n_neighbors=7)

    #Train the model using the training sets
    knn.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = knn.predict(X_test)

    #from sklearn import metrics
    # Model Accuracy, how often is the classifier correct?
    #print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    return predicted

#if __name__ == '__main__':
 #   knnPrediction('Alaska','Murder or Manslaughter','Male',50,'Black',0,'Gun')

