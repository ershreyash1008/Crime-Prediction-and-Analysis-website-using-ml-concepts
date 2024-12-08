import tkinter
import pandas as pd
from sklearn.linear_model import LinearRegression  # to build linear regression model
from sklearn.model_selection import train_test_split


def predictAge(state, crime, sex, age, race, count, weapon):
    read_data = pd.read_csv('./Dataset/database.csv', low_memory=False)
    read_data = read_data.loc[~(read_data == 0).all(axis=1)]
    print(read_data)
    from sklearn import preprocessing
    # creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    state_encoded = le.fit_transform(read_data['State'])
    crimeType_encoded = le.fit_transform(read_data['Crime_Type'])
    victimSex_encoded = le.fit_transform(read_data['Victim_Sex'])
    victimAge_encoded = le.fit_transform(read_data['Victim_Age'])
    victimRace_encoded = le.fit_transform(read_data['Victim_Race'])
    victimCount_encoded = le.fit_transform(read_data['Victim_Count'])  # 0
    weapon_encoded = le.fit_transform(read_data['Weapon'])
    # target variable
    # features=list(zip(state_encoded,month_encoded))

    features = list(zip(state_encoded, crimeType_encoded, victimSex_encoded, victimAge_encoded,
                        victimRace_encoded, victimCount_encoded, weapon_encoded))

    label_output = le.fit_transform(read_data['Perpetrator_Age'])
    X_train, X_test, y_train, y_test = train_test_split(features, label_output, test_size=0.3)
    linearModel = LinearRegression()
    linearModel.fit(X_train, y_train)
    ypred = linearModel.predict(X_test)

    Y_Optimal_Pred = ypred[:3]
    # print(ypred)
    print(Y_Optimal_Pred)
    # predicttest = linearModel.predict([[state, crime,sex, age, race,count,weapon]])

    # print(predicttest)
    # finalpre= Y_Optimal_Pred[0]+','+Y_Optimal_Pred[1]+','+Y_Optimal_Pred[2]

    tkinter.messagebox._show("Age Prediction1", Y_Optimal_Pred[0])
    tkinter.messagebox._show("Age Prediction1", Y_Optimal_Pred[1])
    tkinter.messagebox._show("Age Prediction1", Y_Optimal_Pred[2])


# return Y_Optimal_Pred[0],Y_Optimal_Pred[1],Y_Optimal_Pred[2]
##return  ypred


# if __name__ == '__main__':
# predictAge()
#   predictAge('Alaska', 'Murder or Manslaughter', 'Male', 50, 'Black', 0, 'Gun')
# def predictAge(state, crime,sex, age, race,count,weapon):
