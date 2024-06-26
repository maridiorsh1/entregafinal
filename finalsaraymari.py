import streamlit as st
import pandas as pd
from PIL import Image

# Cambia el color de la página a gris y la tipografía
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    body {
        background-color: #638270;
        font-family: 'Montserrat', sans-serif;
 }
    h1 {
        color: #57a16e;
        font-family: 'Montserrat', sans-serif;
    }
    h2 {
        color: #79a8a0;
        font-family: 'Montserrat', sans-serif;
    }
    h3 {
        color: #5c9fab;
        font-family: 'Montserrat', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title(' Supervisión para Huertas Urbanas')
image = Image.open('temperatura.png')
st.image(image)

uploaded_file = st.file_uploader('Selecciona un archivo')

if uploaded_file is not None:
   df1 = pd.read_csv(uploaded_file)

   st.header('Gráfico de la variable monitoreada')
   df1 = df1.set_index('Time')
   st.line_chart(df1)
   
   st.write(df1)
   st.header('Estadísticas básicas de los sensores')
   st.dataframe(df1["temperatura ESP32"].describe())
   
   min_temp = st.slider('Elige el valor mínimo del filtro', min_value=-10, max_value=45, value=23, key=1)
   # Filtrar el DataFrame utilizando query
   filtrado_df_min = df1.query(f"`temperatura ESP32` > {min_temp}")
   # Mostrar el DataFrame filtrado
   st.header("Temperaturas mayores al valor configurado")
   st.write('Dataframe Filtrado')
   st.write(filtrado_df_min)
   
   max_temp = st.slider('Elige el valor máximo del filtro', min_value=-10, max_value=45, value=23, key=2)
   # Filtrar el DataFrame utilizando query
   filtrado_df_max = df1.query(f"`temperatura ESP32` < {max_temp}")
   # Mostrar el DataFrame filtrado
   st.header("Temperaturas menores al valor configurado")
   st.write('Dataframe Filtrado')
   st.write(filtrado_df_max)
else:
   st.warning('Es necesario cargar un archivo CSV o Excel.')

