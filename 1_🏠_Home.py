import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

if "data" not in st.session_state: 
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv")
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown('# FIFA 2023 OFFICIAL DATASET! ⚽')

st.sidebar.markdown("Desenvolvido por [Pedro Henrique](https://www.linkedin.com/in/pedro-henrique-chaves)")

btn = st.link_button('Acesse os dados no Kaggle',"https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    "O conjunto de dados de jogadores de futebol, abrangendo o período de 2017 a 2023 e contendo mais de **17.000 registros**, " \
    "apresenta um panorama detalhado do futebol profissional. Este rico conjunto de informações engloba uma vasta gama de " \
    "atributos cruciais para a compreensão do esporte, desde dados demográficos e características físicas dos atletas até " \
    "estatísticas detalhadas de suas partidas, informações sobre contratos e seus respectivos clubes."
,  )