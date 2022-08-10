# BIBLIOTECAS USADAS

import streamlit as st

st.set_page_config(page_title="Explorador de Dados Abertos", page_icon=":mag_right:", layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

from teste_pages import *
from teste_plots import *


# APLICAÇÃO
topo()

menu = st.selectbox("Começar a Explorar os Dados!",
                        ("0 - Overview dos Dados",
                         "1 - Descrição da Campanha de Vacinação",
                         "2 - Características da População Vacinada",
                         "3 - Informações dos Postos de Vacinação"
                         ))


if menu == '0 - Overview dos Dados':
    overview2()
    overview3()
    overview1()

elif menu == '1 - Descrição da Campanha de Vacinação':
    campanha1()
    campanha2()

elif menu == '2 - Características da População Vacinada':
    pacientes1()
    pacientes2()
    pacientes3()

elif menu == "3 - Informações dos Postos de Vacinação":
    overview1()


rodape()



