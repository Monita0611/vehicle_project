import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Título de la app
st.header('Explorador de Vehículos Usados en EE.UU.')

# Mostrar una vista previa de los datos
st.write("Vista previa de los datos:")
st.dataframe(df.head())

# Checkbox para mostrar histograma
if st.checkbox('Mostrar histograma del precio'):
    fig_hist = px.histogram(df, x='price', nbins=50, title='Distribución de precios')
    st.plotly_chart(fig_hist)

# Checkbox para mostrar diagrama de dispersión
if st.checkbox('Mostrar gráfico de dispersión precio vs. odómetro'):
    fig_scatter = px.scatter(df, x='odometer', y='price', color='type',
                             title='Precio vs. Odómetro por tipo de vehículo',
                             labels={'odometer': 'Odómetro', 'price': 'Precio'})
    st.plotly_chart(fig_scatter)
