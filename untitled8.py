# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st

st.title("Buscador de Jugadores")

df = pd.read_excel("jugadores.xlsx")

rut = st.text_input("Ingrese RUT")

if st.button("Buscar"):
    resultado = df[df['DNI'].astype(str) == rut]

    if not resultado.empty:
        st.write("Datos del jugador:")
        st.dataframe(resultado)
    else:
        st.warning("No encontrado")
