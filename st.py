import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# import cars data 

cars = pd.read_csv('mtcars.csv')
st.write(cars)

st.sidebar.header("Pick two variables for your scatterplot")
x_val = st.sidebar.selectbox("Pick your X axis",cars.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your Y axis",cars.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(cars,title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(x_val,title=f"{y_val}"),
    tooltip=[x_val,y_val]
)
st.altair_chart(scatter, use_container_width=True)

# Calculate the correlation
corr = round(cars[x_val].corr(cars[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")