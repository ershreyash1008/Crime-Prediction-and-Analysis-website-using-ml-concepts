from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

def Relation():

    read_data = pd.read_csv('./Dataset/database.csv', low_memory=False)

    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    state_encoded = le.fit_transform(read_data['State'].unique())  # 1 to 50

    # print(state_encoded)

    crimeType_encoded = le.fit_transform(read_data['Crime_Type'].unique())  # 1
    print(crimeType_encoded)

    victimSex_encoded = le.fit_transform(read_data['Victim_Sex'].unique())  # 0 1
    print(victimSex_encoded)

    victimAge_encoded = le.fit_transform(read_data['Victim_Age'].unique())
    print(victimAge_encoded)

    victimRace_encoded = le.fit_transform(read_data['Victim_Race'].unique())
    print(victimRace_encoded)

    victimCount_encoded = le.fit_transform(read_data['Victim_Count'])  # 0
    print(victimCount_encoded)

    weapon_encoded = le.fit_transform(read_data['Weapon'].unique())
    print(weapon_encoded)

    features = list(zip(state_encoded, crimeType_encoded, victimSex_encoded, victimAge_encoded, victimRace_encoded,
                        victimCount_encoded, weapon_encoded))

    label_output = le.fit_transform(read_data['Perpetrator_Sex'])
    predct1 = dict(zip(read_data.Perpetrator_Sex.unique(), read_data.Relationship.unique()))
    print(predct1)
    return predct1

if __name__ == '__main__':
    Relation()
