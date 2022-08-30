# BIBLIOTECAS USADAS

import streamlit as st

st.set_page_config(page_title="App Web", page_icon=":mag_right:", layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

from teste_pages import *
from teste_plots import *


# APLICAÇÃO
topo()

tab1, tab2 = st.tabs(["Dashbords", "Overview dos Dados"])


with tab1:
    campanha1()
    campanha2()
    pacientes1()
    pacientes2()
    pacientes3()

with tab2:
    overview2()
    overview3()
    overview1()


rodape()



