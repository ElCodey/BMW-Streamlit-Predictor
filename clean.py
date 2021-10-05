import pandas as pd
import datetime

def car_type_clean(df):
    df["car"] = df["car"].str.replace("BMW", "")
    df["car"] = df["car"].str.replace("Bmw","")
    df["car"] = df["car"].str.replace("bmw", "")
    df["car"] = df["car"].str.replace("Series", "")
    df["car"] = df["car"].str.replace("SERIES", "")
    
    counts = df['car'].value_counts()
    df = df[~df['car'].isin(counts[counts < 10].index)]

    return df

def specs_clean(df):
    df["specs"] = df["specs"].str.split()
    df["year"] = df["specs"].str[0]
    df["miles"] = df["specs"].str[2]
    df["miles"] = df["miles"].str.replace(",", "")
    df["fuel"] = df["specs"].str[5]
    df["drive_type"] = df["specs"].str[7]
    df = df.drop("specs", axis=1)
    df = df.dropna()

    return df

def split_remove_was_price(x):
    y = x.rsplit("\n") 
    return y[0]

def price_clean(df):
    df["price"] = df["price"].str.replace("£", "")
    df["price"] = df["price"].str.replace(",", "")  
    df["price"] = df["price"].apply(lambda x: split_remove_was_price(x))
    df["price"] = df["price"].apply(lambda x: int(x))

    return df

def miles_clean(df):
    df["miles"] = df["miles"].apply(lambda x: int(x))
    return df

def make_dummies(df):
    return pd.get_dummies(df)

def complete_clean(df):
    df = car_type_clean(df)
    df = specs_clean(df)
    df = price_clean(df)
    df = miles_clean(df)
    df = make_dummies(df)
    return df