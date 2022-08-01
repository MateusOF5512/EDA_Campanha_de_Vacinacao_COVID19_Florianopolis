# BIBLIOTECAS USADAS
from teste_functions import *
from teste import *
from teste_variaveis import *

st.set_page_config(page_title="Explorador de Dados Abertos", page_icon=":mag_right:",
                   layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/


# APLICANDO FUNÇÕES PARA CARREGAR E TRATAR OS DADOS
df_11 = get_data_11(path11)
df_12 = get_data_12(path12)


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
    campanha1( df_11 )
    campanha2( df_12 )

elif menu == '2 - Características da População Vacinada':
    overview1()

elif menu == "3 - Informações dos Postos de Vacinação":
    overview1()


rodape()



