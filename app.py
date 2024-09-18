import pandas as pd
import streamlit as st
import plotly_express as px

st.header('¡Bienvenido a mi primera aplicación web!')

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de precios de venta de coches')
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Construir un gráfico de dispersión para la columna price')
    fig = px.scatter(car_data, x="model_year", y="price")
    fig.show()


