import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pandas as pd

import PythonCode.predict

st.title("Seoul Bike Trip Duration Prediction")
image = Image.open('img\cover.jpg')
st.image(image, 'Bike Trip')
st.write("""Trip duration is the most fundamental measure in all modes of transportation. Hence, it is crucial to predict the trip-time precisely for the advancement of Intelligent Transport Systems (ITS) and traveller information systems. In order to predict the trip duration, data mining techniques are employed in this paper to predict the trip duration of rental bikes in Seoul Bike sharing system. The prediction is carried out with the combination of Seoul Bike data and weather data. The Data used include trip duration, trip distance, pickup-drop-off latitude and longitude, temperature, precipitation, wind speed, humidity, solar radiation, snowfall, ground temperature and 1-hour average dust concentration.""")

Distance = st.slider('Distance', min_value=0, max_value=100)
PLong = st.slider('PLong', min_value=0, max_value=100)
PLatd = st.slider('PLatd', min_value=0, max_value=100)
DLong = st.slider('DLong', min_value=0, max_value=100)
DLatd = st.slider('DLatd', min_value=0, max_value=100)
Haversine = st.slider('Haversine', min_value=0, max_value=100)
Pmonth = st.slider('Pmonth', min_value=1, max_value=12)
Pday = st.slider('Pday', min_value=1, max_value=31)
Phour = st.slider('Phour', min_value=1, max_value=24)
Pmin = st.slider('Pmin', min_value=1, max_value=60)
PDweek = st.slider('PDweek', min_value=1, max_value=5)
Dmonth = st.slider('Dmonth', min_value=1, max_value=12)
Dday = st.slider('Dday', min_value=1, max_value=31)
Dhour = st.slider('Dhour', min_value=1, max_value=24)
Dmin = st.slider('Dmin', min_value=1, max_value=60)
DDweek = st.slider('DDweek', min_value=1, max_value=5)
Temp = st.slider('Temp', min_value=0, max_value=50)
Precip = st.slider('Precip', min_value=0, max_value=40)
Wind = st.slider('Wind', min_value=0, max_value=10)
Humid = st.slider('Humid', min_value=0, max_value=100)
Solar = st.slider('Solar', min_value=0, max_value=5)
Snow = st.slider('Snow', min_value=0, max_value=10)
GroundTemp = st.slider('GroundTemp', min_value=0, max_value=100)
Dust = st.slider('Dust', min_value=0, max_value=1500)

y = st.button('Predict')

if y == True:
   data = [[Distance, PLong, PLatd, DLong, DLatd, Haversine, Pmonth, Pday, Phour, Pmin, PDweek, 
   Dmonth, Dday, Dhour, Dmin, DDweek, Temp, Precip, Wind, Humid, Solar, Snow, GroundTemp, Dust]]
   
   df = pd.DataFrame(data, columns = ['Distance', 'PLong', 'PLatd', 'DLong', 'DLatd', 'Haversine', 
   'Pmonth', 'Pday', 'Phour', 'Pmin', 'PDweek','Dmonth', 'Dday', 'Dhour', 'Dmin', 'DDweek', 'Temp', 
   'Precip', 'Wind', 'Humid', 'Solar', 'Snow', 'GroundTemp', 'Dust'])

   pred = PythonCode.predict.Predictor(df)

   st.write("Prediction", round(pred[0],4))
   y = False