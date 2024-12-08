import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import pandas as pd
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib.pyplot as plt #



read_data = pd.read_csv('./Dataset/database.csv', low_memory=False)

#print(matches_cleaned_data.head())

predct = dict(zip(read_data.City.unique(), read_data.Perpetrator_Race.unique()))

print(predct)

"""
predct1 = dict(zip(read_data.Perpetrator_Sex.unique(), read_data.Relationship.unique()))
print(predct1)

#print(read_data['City'].value_counts())


#print(apple_data.head())

print(read_data['Perpetrator_Sex'].value_counts())

male_data=read_data[read_data['Perpetrator_Sex']=='Male']
unknown_data=read_data[read_data['Perpetrator_Sex']=='Unknown']
female_data=read_data[read_data['Perpetrator_Sex']=='Female']


from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
state_encoded=le.fit_transform(read_data['State'])
print(state_encoded)

month_encoded=le.fit_transform(read_data['Month'])
print(month_encoded)
#target variable
label_output=le.fit_transform(read_data['Perpetrator_Sex'])

features=list(zip(state_encoded,month_encoded))

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training sets
model.fit(features,label_output)

#Predict Output
predicted= model.predict([[5,21]])
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

from sklearn import metrics
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

from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

"""