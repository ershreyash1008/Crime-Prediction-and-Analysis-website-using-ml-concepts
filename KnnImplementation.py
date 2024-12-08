from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier


def knnPrediction(state,sex,age,race,weapon):
#def knnPrediction(state, crimeType, victimSex, victimAge,victimRace,victimCount,weapon):
    read_data = pd.read_csv('./Dataset/database.csv', low_memory=False)
    predct = dict(zip(read_data.City.unique(), read_data.Perpetrator_Race.unique()))



    predct1 = dict(zip(read_data.Perpetrator_Sex.unique(), read_data.Relationship.unique()))
    print(predct1)


    print(read_data['Perpetrator_Sex'].value_counts())

    male_data=read_data[read_data['Perpetrator_Sex']=='Male']
    unknown_data=read_data[read_data['Perpetrator_Sex']=='Unknown']
    female_data=read_data[read_data['Perpetrator_Sex']=='Female']


    # creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    state_encoded = le.fit_transform(read_data['State'].unique())#1 to 50

    #print(state_encoded)

    crimeType_encoded = le.fit_transform(read_data['Crime_Type'].unique())#1
    print(crimeType_encoded)

    victimSex_encoded = le.fit_transform(read_data['Victim_Sex'].unique())# 0 1
    print(victimSex_encoded)

    victimAge_encoded = le.fit_transform(read_data['Victim_Age'].unique())
    print(victimAge_encoded)

    victimRace_encoded = le.fit_transform(read_data['Victim_Race'].unique())
    print(victimRace_encoded)

    victimCount_encoded = le.fit_transform(read_data['Victim_Count'])#0
    print(victimCount_encoded)

    weapon_encoded = le.fit_transform(read_data['Weapon'].unique())
    print(weapon_encoded)


    features = list(zip(state_encoded, crimeType_encoded, victimSex_encoded,victimAge_encoded, victimRace_encoded,
                    victimCount_encoded, weapon_encoded))

    label_output = le.fit_transform(read_data['Perpetrator_Sex'])

    from sklearn.neighbors import KNeighborsClassifier
    #Create KNN Classifier
    knn = KNeighborsClassifier(n_neighbors=7)
    X_train, X_test, y_train, y_test = train_test_split(features, label_output, test_size=0.30) # 70% training and 30% test
    #Train the model using the training sets
    knn.fit(X_train, y_train)

#Predict the response for test dataset
    y_pred = knn.predict(X_test)


    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    #Import knearest neighbors Classifier model

    from sklearn.neighbors import KNeighborsClassifier
    #Create KNN Classifier
    knn = KNeighborsClassifier(n_neighbors=7)

    #Train the model using the training sets
    knn.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = knn.predict(X_test)


    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    from sklearn.neighbors import KNeighborsClassifier

    model = KNeighborsClassifier(n_neighbors=3)

    # Train the model using the training sets
    model.fit(features,label_output)

    #Predict Output

    predicted = model.predict([[5,1,0,50,1,0,2]])
    print(predicted)
   # return predicted



if __name__ == '__main__':
     knnPrediction()
