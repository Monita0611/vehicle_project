import pandas as pd
import plotly.express as px
import streamlit as st
        
# Leer los datos
df = pd.read_csv('vehicles_us.csv')

# Crear el botón
hist_button = st.button('Construir histograma')

# Al hacer clic en el botón
if hist_button:
    st.write('🎯 **Creación de un histograma para el kilometraje de vehículos usados en EE. UU.**')

    # Crear histograma con mejoras
    fig = px.histogram(
        df,
        x="odometer",
        nbins=50,
        color="condition",  # Colorear por condición del vehículo
        title="Distribución del kilometraje según la condición del vehículo",
        labels={"odometer": "Kilometraje (millas)", "count": "Cantidad de vehículos"},
        template="plotly_dark"  # Estilo visual oscuro
    )

    # Ajustes de diseño del histograma
    fig.update_layout(
        bargap=0.2,
        title_font_size=22,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        legend_title="Condición",
        legend=dict(x=0.8, y=0.95)
    )

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)
