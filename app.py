import streamlit as st
from pages/UTI_Evolucao import evolucao_uti_interface

st.set_page_config(page_title="SmartRound UTI", layout="wide")

st.sidebar.title("SmartRound UTI")
st.sidebar.markdown("Versão estruturada de evolução para pacientes críticos.")

evolucao_uti_interface()
