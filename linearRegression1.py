import pandas as pd
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression # to build linear regression model


def predictAge(state, crime,sex, age, race,count,weapon):

    read_data = pd.read_csv('./Dataset/database.csv', low_memory=False)
    df= read_data.loc[(read_data!=0).any(axis=1)]
    print(df)
    drop_A=df.index[df["Perpetrator_Age"] != 0].tolist()
    print(drop_A)
    from sklearn import preprocessing
    #creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    #state_encoded=le.fit_transform(read_data['State'])
    #print(state_encoded)

    #month_encoded=le.fit_transform(read_data['Month'])
    #print(month_encoded)
    #target variable

    state_encoded=le.fit_transform(read_data['State'])
    crimeType_encoded = le.fit_transform(read_data['Crime_Type'])
    victimSex_encoded = le.fit_transform(read_data['Victim_Sex'])
    victimAge_encoded = le.fit_transform(read_data['Victim_Age'])
    victimRace_encoded = le.fit_transform(read_data['Victim_Race'])
    victimCount_encoded = le.fit_transform(read_data['Victim_Count'])#0
    weapon_encoded = le.fit_transform(read_data['Weapon'])

    #features=list(zip(state_encoded,month_encoded))
    features = list(zip(state_encoded, crimeType_encoded, victimSex_encoded, victimAge_encoded,
                        victimRace_encoded, victimCount_encoded, weapon_encoded))

    label_output=le.fit_transform(read_data['Perpetrator_Age'])
    X_train, X_test, y_train, y_test = train_test_split(features, label_output, test_size=0.3)
    linearModel = LinearRegression()
    linearModel.fit(X_train, y_train)

    ypred = linearModel.predict(X_test)
    agepredict= linearModel.predict([[state,crime,sex,age,race,count,weapon]])
    Y_Optimal_Pred=ypred[:3]
    print(ypred)
    print(Y_Optimal_Pred)
    age_optimal= agepredict[:3]
    print(agepredict[:3])
    return agepredict[:3]

if __name__ == '__main__':
    predictAge('Alaska', 'Murder or Manslaughter', 'Male', 50, 'Black', 0, 'Gun')