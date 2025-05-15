import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]

players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)
player_status = df_data[df_data["Name"] == player].iloc[0]

col1, col2 = st.columns([0.1, 0.9])
col1.image(player_status["Photo"])
col2.title(player_status["Name"])

col3, col4, col5 = st.columns(3)
col6, col7, col8 = st.columns(3)
col3.markdown(f"**Posição**: {player_status['Position']}")
col4.markdown(f"**Idade**: {player_status['Age']}")
col5.markdown(f"**Altura**: {player_status['Height(cm.)'] / 100} m")
col6.markdown(f"**Peso**: {player_status['Weight(lbs.)'] * 0.453:.2f} kg")
col7.markdown(f"**Nacionalidade**: {player_status['Nationality']}")
col8.markdown(f"**Clube**: {player_status['Club']}")

st.markdown("___" * 50)
st.subheader(f"Overall: {player_status['Overall']}")

st.progress(int(player_status["Overall"]) / 100)

col9, col10, col11 = st.columns(3)
col9.metric(label= "Valor de mercado", value= f"£ {player_status["Value(£)"]:,}")
col10.metric(label= "Remuneração Semanal", value= f"£ {player_status["Wage(£)"]:,}")
col11.metric(label= "Cláusula de recisão", value= f"£ {player_status["Release Clause(£)"]:,}")