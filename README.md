# vehicle_project

# Explorador de Vehículos Usados

Esta aplicación web interactiva fue desarrollada con [Streamlit](https://streamlit.io/) y permite explorar datos de vehículos usados en Estados Unidos. El conjunto de datos utilizado contiene información como año del modelo, precio, tipo de vehículo, kilometraje, condición, entre otros.

## 🚗 ¿Qué hace esta app?

Con esta app puedes:

- 📊 **Visualizar un histograma del kilometraje** (`odometer`) agrupado por condición del vehículo.
- 📉 **Explorar un gráfico de dispersión interactivo** que muestra la relación entre el año del modelo y el precio, diferenciando por tipo de vehículo y tamaño según el kilometraje.
- 🧾 **Examinar una tabla interactiva** con los primeros registros del conjunto de datos.

## ⚙️ Tecnologías usadas

- Python
- Streamlit
- Plotly Express
- Pandas

## 🚀 Despliegue en Render

Esta aplicación está configurada para desplegarse fácilmente en [Render](https://render.com). Asegúrate de incluir estos archivos:

- `Procfile`: indica cómo iniciar la app.
- `requirements.txt`: contiene las dependencias.
- `streamlit/config.toml`: configura el puerto necesario para Render.

### 🛠️ Comandos usados por Render

```bash
web: streamlit run app.py --server.port 10000 --server.address 0.0.0.0


# Used Vehicles Explorer

This is an interactive web application built with [Streamlit](https://streamlit.io/) that allows users to explore data on used vehicles in the United States. The dataset includes details such as model year, price, vehicle type, mileage (odometer), condition, and more.

## 🚗 What Can You Do with This App?

With this app, you can:

- 📊 **Visualize a histogram of vehicle mileage** (`odometer`), grouped by vehicle condition.
- 📉 **Explore an interactive scatter plot** showing the relationship between model year and price, differentiated by vehicle type and scaled by mileage.
- 🧾 **Preview a data table** with the first few records of the dataset.

## ⚙️ Technologies Used

- Python
- Streamlit
- Plotly Express
- Pandas

## 🚀 Deployment on Render

This app is ready to deploy on [Render](https://render.com). Make sure you include the following configuration files:

- `Procfile`: specifies how to start the app.
- `requirements.txt`: lists the dependencies.
- `streamlit/config.toml`: sets up the required port for Render.

### 🛠️ Render Start Command

```bash
web: streamlit run app.py --server.port 10000 --server.address 0.0.0.0


