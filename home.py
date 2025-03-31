import streamlit as st
import pandas as pd

df = pd.read_excel('Siniestros Notificados(Respuestas).xlsx', sheet_name='Rtas -Notificacion Siniestro', usecols=[0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

df['N° Legajo (EJ)'] = df['N° Legajo (EJ)'].astype(str)
df['N° POLIZA (EJ)'] = df['N° POLIZA (EJ)'].astype(str)
df['N° DOMINIO (EJ)'] = df['N° DOMINIO (EJ)'].astype(str)

st.set_page_config(page_icon="logo1.png", page_title="Dashboard RGA", layout='wide', initial_sidebar_state="expanded")

st.markdown("""
    <style>
            .st-emotion-cache-1xf0csu > img{
                border-radius: 100%;
            }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image('logo1.png', caption="")
    st.title(body='Ingrese los filtros a aplicar: ')
    efector = st.sidebar.multiselect(
        "Hospital/Caps", 
        options=df['(ING/DEST) Centro de Salud'].unique(),
    )

    aseguradora = st.sidebar.multiselect(
        "Aseguradora", 
        options=df['Compañia (EJ)'].unique(),
    )
    check =st.button(label='CONSULTAR')
    if check:
        # Filtrar los datos según las opciones seleccionadas en el sidebar
        if efector:
            df = df[df['(ING/DEST) Centro de Salud'].isin(efector)]
        if aseguradora:
            df = df[df['Compañia (EJ)'].isin(aseguradora)]
        
        
st.subheader('Listado de Siniestros')        
st.write("-----")

st.dataframe(df, height=800)