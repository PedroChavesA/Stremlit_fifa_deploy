import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="⚽️",
    layout="wide"
)

df_data = st.session_state["data"]

clubs = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubs)

col1, col2 = st.columns([0.1, 0.9])
col1.image(df_data[df_data["Club"] == club].iloc[0]["Club Logo"])
col2.subheader(f"{club}")

df_filtered = df_data[df_data["Club"] == club].set_index("Name")
columns = ["Age", "Photo", "Flag", "Overall","Value(£)", "Wage(£)", "Joined", "Height(cm.)",
            "Weight(lbs.)", "Nationality","Contract Valid Until", "Release Clause(£)"]


st.dataframe(df_filtered[columns], 
             column_config={
            "Photo": st.column_config.ImageColumn(),
            "Flag": st.column_config.ImageColumn("Country"),
            "Overall": st.column_config.ProgressColumn
            (
            "Overall", min_value=0, max_value=100, format ="%d"
            ),
            "Wage(£)": st.column_config.ProgressColumn
            (
            "Weekly Wage", min_value=0, max_value= df_filtered["Wage(£)"].max(), format ="£%f"
            )
}
)