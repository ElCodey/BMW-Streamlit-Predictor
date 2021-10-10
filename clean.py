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
    df["drive_type"] = df["drive_type"].str.replace("Semi-automatic", "Semi")
    df["drive_type"] = df["drive_type"].str.replace("Semiauto", "Semi")
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
    df["miles"] = df["miles"].apply(lambda x: 1/x)
    return df

def make_dummies(df):
    df_dum =  pd.get_dummies(df)
    df_dum = df_dum.drop(["drive_type_rex", "drive_type_•", "drive_type_h"], axis=1)
    return df_dum

def complete_clean(df):
    df = car_type_clean(df)
    df = specs_clean(df)
    df = price_clean(df)
    df = miles_clean(df)
    df = make_dummies(df)
    return df