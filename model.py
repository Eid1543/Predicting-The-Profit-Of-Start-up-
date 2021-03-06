# Importing the libraries
import numpy as np
import pandas as pd
import pickle 


# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Training the Multiple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train) 




# Predicting the Test set results
#y_pred = regressor.predict(X_test)



#Evaluatiing the model 
#from sklearn.metrics import r2_score 
#from sklearn.metrics import mean_squared_error
#from sklearn.metrics import mean_absolute_error

#print ("R2 : " , r2_score(y_test,y_pred))
#print ("RMSE : " , mean_squared_error(y_test, y_pred, squared=False) )
#print ("MAE : " , mean_absolute_error(y_test, y_pred) )



pickle.dump(regressor, open ('model.pkl' , 'wb'))














