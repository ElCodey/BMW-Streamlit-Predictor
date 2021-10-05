import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def split(df):
    X = df.drop("price", axis=1)
    y = df["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, random_state=1)

    return X_train, X_test, y_train, y_test

def lin_model(X_train, X_test, y_train):
    model = LinearRegression()
    model = model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return model, y_pred
    
def model_results(y_true, y_pred):
    r_score = r2_score(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)

    return r_score, mse, mae

