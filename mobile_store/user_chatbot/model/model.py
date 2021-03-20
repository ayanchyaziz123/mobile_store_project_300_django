import pandas
from sklearn import linear_model
import numpy as np
import pickle

df = pandas.read_csv("mobile.csv")

X = df[[ 'Main_cammera', 'ROM', 'RAM']]
y = df['Price']

regr = linear_model.LinearRegression()
regr.fit(X, y)


pickle.dump(regr, open('mobilee.pkl','wb'))

model = pickle.load(open('mobilee.pkl','rb'))
print(model.predict([[48, 64, 4]]))
