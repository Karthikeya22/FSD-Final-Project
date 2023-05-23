from django.shortcuts import render
from KISSAN.models import crops
from math import ceil
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from KISSAN.utiles import get_plot, get_plot1


# Create your views here.
def home(request) :
    return render(request, 'home.html')

def index(request) :
    Crops = crops.objects.all()
    n = len(Crops)
    nslides = n//3 + ceil((n/3)-(n//3))
    params = {'no_of_slides':nslides ,'crop':Crops}
    return render(request, 'index.html', params)

def analyse(request) :
    Crops = crops.objects.all()
    n = len(Crops)
    params = {'no_of_slides':n,'crop':Crops}
    return render(request, 'analysis.html', params)

def Predict(request) :
    Crop_name = str(request.GET['crop_Name'])
    return render(request, 'prediction.html', {'name':Crop_name})

def result(request) :
    df=pd.read_csv(r"static\Sheet1.csv")
    # df.drop(df.columns[[5]],axis = 1,inplace=True)
    df['orderdate'].astype(str)
    df['orddate']=df['orderdate'].apply(lambda x: x.split(' ')[0])
    df['Day']=df['orderdate'].apply(lambda x: x.split('-')[1]).astype(int)
    df['Month']=df['orderdate'].apply(lambda x: x.split('-')[0]).astype(int)
    df['Year']=df['orderdate'].apply(lambda x: x.split('-')[2]).astype(int)
    df1=df[['prod_id','avg price','ordercount','Day','Month','Year']]
    x=df1.drop(df1[['avg price','ordercount']],axis=1)
    y=df1['avg price']
    y2=df1['ordercount']
    X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size = 0.2, random_state = 2)
    X_train1, X_test1, Y_train1, Y_test1 = train_test_split(x,y2, test_size = 0.2, random_state = 2)
    model1=XGBRegressor()
    model2=XGBRegressor()
    model1.fit(X_train,Y_train)
    model2.fit(X_train1,Y_train1)
    
    crop_name = str(request.GET['Crop_Name'])
    day = float(request.GET['Day'])
    month = float(request.GET['Month'])
    year = float(request.GET['Year'])
    prod = {'Onion': 1110, 'Tomato': 996, 'Potato': 1150, 'Sugercane': 1120, 'Brinjal': 1011, 'Okra': 1071}
    dict1 = {'prod_id':[prod[crop_name]],'Day':[day],'Month':[month],'Year':[year]}
    df2=pd.DataFrame(dict1)
    df3=pd.DataFrame(dict1)
    train1=model1.predict(df2)
    train2 = model2.predict(df3)
    a = []
    b = []
    c = []
    d = []
    for i in range(0,6) :
        if (month != 12) :
            dict2 = {'prod_id':[prod[crop_name]],'Day':[day],'Month':[month+i],'Year':[year]}
        else :
            month = 1
            dict2 = {'prod_id':[prod[crop_name]],'Day':[day],'Month':[month],'Year':[year+1]}
        df4 = pd.DataFrame(dict2)
        train3 = model1.predict(df4)
        a.append(train3)
        b.append(i)
    
    for i in range(0,6) :
        if (month != 12) :
            dict3 = {'prod_id':[prod[crop_name]],'Day':[day],'Month':[month+i],'Year':[year]}
        else :
            month = 1
            dict3 = {'prod_id':[prod[crop_name]],'Day':[day],'Month':[month],'Year':[year+1]}
        df5 = pd.DataFrame(dict3)
        train4 = model2.predict(df5)
        c.append(train4)
        d.append(i)
    chart = get_plot(b, a)
    chart1 = get_plot1(d, c)
    return render(request, 'result1.html', {'price':train1, 'demand':train2, 'chart':chart, 'chart1': chart1})