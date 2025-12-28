import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------
# Configuración inicial
# -------------------------
st.set_page_config(
    page_title="Análisis de anuncios de coches",
    layout="wide"
)

# -------------------------
# Encabezado de la app
# -------------------------
st.header("🚗 Análisis Exploratorio de Anuncios de Coches")

st.write(
    """
    Esta aplicación permite explorar de forma interactiva un conjunto de datos
    de anuncios de venta de coches en Estados Unidos.
    """
)

# -------------------------
# Cargar datos
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/vehicles_us.csv")


car_data = load_data()

st.write("Vista previa del conjunto de datos:")
st.dataframe(car_data.head())

# -------------------------
# Checkboxes para gráficos
# -------------------------
build_histogram = st.checkbox("Construir histograma del odómetro")
build_scatter = st.checkbox("Construir gráfico de dispersión (precio vs odómetro)")

# -------------------------
# Histograma
# -------------------------
if build_histogram:
    st.write("📊 Distribución del odómetro")

    fig_hist = go.Figure(
        data=[go.Histogram(x=car_data["odometer"])]
    )

    fig_hist.update_layout(
        title="Distribución del Odómetro",
        xaxis_title="Kilometraje",
        yaxis_title="Frecuencia"
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# -------------------------
# Gráfico de dispersión
# -------------------------
if build_scatter:
    st.write("📈 Relación entre precio y kilometraje")

    fig_scatter = go.Figure(
        data=go.Scatter(
            x=car_data["odometer"],
            y=car_data["price"],
            mode="markers"
        )
    )

    fig_scatter.update_layout(
        title="Precio vs Odómetro",
        xaxis_title="Kilometraje",
        yaxis_title="Precio (USD)"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)
