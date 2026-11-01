"""Página de muestra del registro de partidos, servida con Streamlit.
Arranque local:  streamlit run app.py
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Registro de Partidos", page_icon="🏛️", layout="wide")

# Oculta el menú y el pie de Streamlit para que se vea solo el formulario
st.markdown(
    "<style>#MainMenu, header, footer {visibility: hidden;} .block-container {padding: 0 1rem;}</style>",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "registro.html").read_text(encoding="utf-8")
components.html(html, height=2900, scrolling=True)
