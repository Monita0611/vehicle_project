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
    fig = px.histogram(
    df,
    x="odometer",
    nbins=50,  # número de barras
    color="condition",  # color por condición del vehículo
    title="Distribución del kilometraje por condición del vehículo",
    labels={"odometer": "Kilometraje (millas)", "count": "Número de vehículos"},
    template="plotly_dark"  # estilo visual
)

fig.update_layout(
    bargap=0.2,  # espacio entre barras
    title_font_size=22,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    legend_title="Condición",
    legend=dict(x=0.8, y=0.95)
)

fig.show()

# Checkbox para mostrar diagrama de dispersión
if st.checkbox('Mostrar gráfico de dispersión precio vs. odómetro'):
    filtered_df = df[['model_year', 'price', 'type', 'odometer', 'model', 'condition']].dropna()

    fig = px.scatter(
    filtered_df,
    x="model_year",
    y="price",
    color="type",
    size="odometer",
    hover_data=["model", "condition"],
    title="Precio de vehículos según el año del modelo y tipo",
    labels={"model_year": "Año del modelo", "price": "Precio (USD)"},
    template="plotly_dark"
    )

    fig.update_layout(
    title_font_size=22,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    legend_title="Tipo de vehículo",
    legend=dict(x=0.8, y=0.95)
    )

fig.show()





