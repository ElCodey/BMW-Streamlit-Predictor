import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache
def load_model():
       loaded_model = joblib.load("bmw_linear_model.sav")
       return loaded_model

def main(model):

       st.title("BMW Price Predictor")

       miles = st.number_input('Enter Miles')
       type = st.selectbox('BMW Model', ['car_ 1_series ', 'car_ 2_series ', 'car_ 2  Active Tourer',
              'car_ 2  Gran Tourer', 'car_ 3_series ', 'car_ 4_series ', 'car_ 4  Gran Coupe',
              'car_ 5_series ', 'car_ 5  Gran Turismo', 'car_ 6_series ', 'car_ 7_series ', 'car_ 8_series ',
              'car_ M2', 'car_ M3', 'car_ M4', 'car_ M5', 'car_ X1', 'car_ X2',
              'car_ X3', 'car_ X4', 'car_ X5', 'car_ X6', 'car_ Z4', 'car_ i3',])
       year = st.selectbox('Year', ['year_1986', 'year_1989', 'year_1996', 'year_1999', 'year_2000',
              'year_2001', 'year_2002', 'year_2003', 'year_2004', 'year_2005',
              'year_2006', 'year_2007', 'year_2008', 'year_2009', 'year_2010',
              'year_2011', 'year_2012', 'year_2013', 'year_2014', 'year_2015',
              'year_2016', 'year_2017', 'year_2018', 'year_2019', 'year_2020',
              'year_2021'])
       fuel = st.selectbox('Fuel Type', ['fuel_Diesel', 'fuel_Electric', 'fuel_Hybrid',
              'fuel_Petrol', 'fuel_Petrol/electric', 'fuel_Petrol/plugin',
              'fuel_Plug_in_hybrid'])
       drive_type = st.selectbox('Drive Type', ['drive_type_Automatic', 'drive_type_Manual',
              'drive_type_Semi', 
              'drive_type_electric', 'drive_type_hybri',])




       binary_values = {"miles": 0,
              'car_ 1_series ': 0, 'car_ 2_series ':0, 'car_ 2  Active Tourer': 0,
              'car_ 2  Gran Tourer': 0, 'car_ 3_series ': 0, 'car_ 4_series ': 0, 'car_ 4  Gran Coupe': 0,
              'car_ 5_series ': 0, 'car_ 5  Gran Turismo': 0, 'car_ 6_series ': 0, 'car_ 7_series ': 0, 'car_ 8_series ': 0,
              'car_ M2': 0, 'car_ M3': 0, 'car_ M4': 0, 'car_ M5': 0, 'car_ X1': 0, 'car_ X2': 0,
              'car_ X3': 0, 'car_ X4': 0, 'car_ X5': 0, 'car_ X6': 0, 'car_ Z4': 0, 'car_ i3': 0,
              'year_1986': 0, 'year_1989': 0, 'year_1996': 0, 'year_1999': 0, 'year_2000': 0,
              'year_2001': 0, 'year_2002': 0, 'year_2003': 0, 'year_2004': 0, 'year_2005': 0,
              'year_2006': 0, 'year_2007': 0, 'year_2008': 0, 'year_2009': 0, 'year_2010': 0,
              'year_2011': 0, 'year_2012': 0, 'year_2013': 0, 'year_2014': 0, 'year_2015': 0,
              'year_2016': 0, 'year_2017': 0, 'year_2018': 0, 'year_2019': 0, 'year_2020': 0,
              'year_2021': 0,
              'fuel_Diesel': 0, 'fuel_Electric': 0, 'fuel_Hybrid': 0,
              'fuel_Petrol': 0, 'fuel_Petrol/electric': 0, 'fuel_Petrol/plugin': 0,
              'fuel_Plug_in_hybrid': 0,
              'drive_type_Automatic': 0, 'drive_type_Manual': 0,
              'drive_type_Semi': 0, 
              'drive_type_electric': 0, 'drive_type_hybri': 0}

       binary_values["miles"] = miles
       for i in binary_values:
              if type == i:
                     binary_values[i] = 1
              if year == i:
                     binary_values[i] = 1
              if fuel == i:
                     binary_values[i] = 1
              if drive_type == i:
                     binary_values[i] = 1


       if st.button("Predict Price"):
              result = model.predict(np.array(list(binary_values.values())).reshape(1,-1)).round(2)
              st.text("Predicted price is £{}".format(result[0]))

if __name__ == "__main__":
       model = load_model()
       main(model)
              