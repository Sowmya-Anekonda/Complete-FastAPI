import joblib
import pandas as pd 
from sklearn.linear_model import LinearRegression


df = pd.read_csv('/Users/smanjunatha/Documents/Personal/My_Projects/FastAPI_Advance/Complete_FastAPI/data/housing.csv')
df = df.iloc[:, :-1].dropna()
print('Read the dataset')

X = df.drop(columns='median_house_value')
y = df['median_house_value'].copy()
print('Split dataset')

model = LinearRegression().fit(X, y)
print("Trained the model")

joblib.dump(model, 'model.joblib')
print('Saved the model')

