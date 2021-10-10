import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache
def load_model():
       loaded_model = joblib.load("bmw_linear_model_new.sav")
       return loaded_model

def main(model):

       st.title("BMW Price Predictor")

       miles = st.number_input('Enter Miles')
       type = st.selectbox('BMW Model', ['1 Series', '2 Series', 'Active Tourer',
              'Gran Tourer', '3 Series', '4 Series', 'Gran Coupe',
              '5 Series', 'Gran Turismo', '6 Series', '7 Series', '8 Series',
              'M2', 'M3', 'M4', 'M5', 'X1', 'X2',
              'X3', 'X4', 'X5', 'X6', 'Z4', 'I3',])
       year = st.selectbox('Year', ['1986', '1989', '1996', '1999', '2000',
              '2001', '2002', '2003', '2004', '2005',
              '2006', '2007', '2008', '2009', '2010',
              '2011', '2012', '2013', '2014', '2015',
              '2016', '2017', '2018', '2019', '2020',
              '2021'])
       fuel = st.selectbox('Fuel Type', ['Diesel', 'Electric', 'Hybrid',
              'Petrol', 'Petrol/electric', 'Petrol/plugin',
              'Plug_in_hybrid'])
       drive_type = st.selectbox('Drive Type', ['Automatic', 'Manual',
              'Semi', 
              'electric', 'hybri',])




       binary_values = {"miles": 0.01,
              '1 Series ': 0, '2 Series ':0, 'Active Tourer': 0,
              'Gran Tourer': 0, '3 Series ': 0, '4 Series ': 0, 'Gran Coupe': 0,
              '5 Series ': 0, 'Gran Turismo': 0, '6 Series ': 0, '7 Series ': 0, '8 Series ': 0,
              'M2': 0, 'M3': 0, 'M4': 0, 'M5': 0, 'X1': 0, 'X2': 0,
              'X3': 0, 'X4': 0, 'X5': 0, 'X6': 0, 'Z4': 0, 'i3': 0,
              '1986': 0, '1989': 0, '1996': 0, '1999': 0, '2000': 0,
              '2001': 0, '2002': 0, '2003': 0, '2004': 0, '2005': 0,
              '2006': 0, '2007': 0, '2008': 0, '2009': 0, '2010': 0,
              '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0,
              '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0,
              '2021': 0,
              'Diesel': 0, 'Electric': 0, 'Hybrid': 0,
              'Petrol': 0, 'Petrol/electric': 0, 'Petrol/plugin': 0,
              'Plug_in_hybrid': 0,
              'Automatic': 0, 'Manual': 0,
              'Semi': 0, 
              'electric': 0, 'hybri': 0}

       binary_values["miles"] = 1 / miles
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
              
