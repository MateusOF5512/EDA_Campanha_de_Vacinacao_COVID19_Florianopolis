# BIBLIOTECAS USADAS

import streamlit as st

st.set_page_config(page_title="App Web", page_icon=":mag_right:", layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

from pages import *
from plots import *


# APLICAÇÃO
topo()

tab1, tab2, tab3 = st.tabs(["💉 Campanha de Vacinação", "😎 Pacientes Vacinados", "🎲 Overview dos Dados"])

with tab1:
    campanha1()
    campanha2()

with tab2:
    pacientes1()
    pacientes2()
    pacientes3()

with tab3:
    overview2()
    overview3()
    overview1()

rodape()



