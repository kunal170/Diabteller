from numpy import double
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.naive_bayes import GaussianNB as gnb
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier as ada
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.linear_model import Perceptron
from sklearn.ensemble import ExtraTreesClassifier as etc
from sklearn.ensemble import BaggingClassifier as bc
from sklearn.linear_model import LogisticRegression as lr
from sklearn.ensemble import GradientBoostingClassifier as gbc
def data_training(result):
    df = pd.read_csv("diabetes.csv")    
    x = df.iloc[:,[0,1,2,3,4,5,6,7]]
    y = df.iloc[:,[8]]
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)
    mn = [knn(),gnb(),LDA(),ada(),rfc(),Perceptron(),etc(),bc(),lr(),gbc()]
    max_accuracy=0
    index=-1
    for i in range(10):
        model=mn[i]
        model.fit(xtrain,ytrain)
        accuracy = accuracy_score(ytest, model.predict(xtest))
        print(str(accuracy)+" "+ str(i))
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            index = i
    print(max_accuracy)
    print(mn[index])
    glucose_default=df['Glucose'].mean()
    if result['glucose']=='':
        glucose=glucose_default
    else: 
        glucose=double(result['glucose'])
    print(glucose)
    skin_default = df['SkinThickness'].mean()
    if result['skin_thickness']=='':
        skin_thickness=skin_default
    else: 
        skin_thickness=double(result['skin_thickness'])
    print(skin_thickness)
    serum_default=df['Insulin'].mean()
    if result['insulin']=='':
        insulin=serum_default
    else: 
        insulin=double(result['insulin'])
    print(insulin)
    height=int(result['height'])
    weight=int(result['weight'])
    bmi=(weight/(height*height))*10000
    print(bmi)
    
    if result['pregnancies']=='5' :
        no_of_pregnancy=0
    elif result['pregnancies']=='4':                    
        no_of_pregnancy=4
    else:
        no_of_pregnancy=int(result['pregnancies'])
    print(no_of_pregnancy)
    if result['family_history']=='yes':
        pedigree=1.0
    else :
        pedigree=0.0
    print(pedigree)

    blood_pressure=double(result['blood_pressure'])
    
    age=int(result['age'])
     

    sample_data=np.array([no_of_pregnancy,glucose,blood_pressure,skin_thickness,insulin,bmi,pedigree,age])
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    print(sample_data)
    sample_data=sample_data.reshape(1,-1)
    print(sample_data)
    predictionProbability = mn[index].predict_proba(sample_data)
    prediction=mn[index].predict(sample_data)
    print(predictionProbability)
    print(prediction)
    data = {'Pregnancies':no_of_pregnancy,'Glucose':glucose,'BloodPressure':blood_pressure,'SkinThickness':skin_thickness,'Insulin':insulin,'BMI':bmi,'DiabetesPedigreeFunction':pedigree,'Age':age, 'Outcome': prediction[0]}
    df1 = pd.DataFrame(data, index=[0])
    df1.to_csv('diabetes.csv', mode='a',index=False, header=False)
    return [round(predictionProbability[0][1]*100,2),prediction[0]]

      #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome