# Importação de Bibliotecas:

from teste_plots import *
from teste_variaveis import *
import streamlit as st


# - TITULO IV - APLICAÇÃO - DASHBOARD FOCADO NA EXPLORAÇÃO E ANÁLISE DOS DADOS
## - Topo e Rodapé da Aplicação:
def topo():
    st.markdown(html_title, unsafe_allow_html=True) #Explorador de Dados Abertos
    st.markdown(""" <style>
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)
    return None

def rodape():
    st.markdown(html_rodape, unsafe_allow_html=True) # ---- by: mateus
    return None


## IV.0 - VISÃO GERAL DOS DADOS:
def overview1():
    st.text("")
    st.markdown(html_subheader_0_30, unsafe_allow_html=True) # Explore está Aplicação Web
    st.text("")
    st.text("")

    col1, col2, col3 = st.columns([50, 1100, 50])
    with col1:
        st.text("")
    with col2:
        st.markdown(html_card_header_0A_1_11, unsafe_allow_html=True)  # Apresentando os Dados
    with col3:
        st.text("")

    st.text("")

    col1A, col2A, col3A, col4A, col5A = st.columns([50, 520, 60, 520, 50])
    with col1A:
        st.text("")
    with col2A:
        st.markdown(html_card_header_0A_1_21, unsafe_allow_html=True)  # Descrição Inicial
    with col3A:
        st.text("")
    with col4A:
        st.markdown(html_card_header_0A_1_22, unsafe_allow_html=True)  # Links importantes
    with col5A:
        st.text("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    st.write("")
    return None

def overview2():
    st.markdown("---")
    st.markdown(html_header_0_10, unsafe_allow_html=True) # Overview dos Dados
    st.markdown("---")
    st.text("")
    st.markdown(html_subheader_0_20, unsafe_allow_html=True) # Extração e Transformação dos Dados
    st.text("")
    st.text("")

    col1, col2, col3 = st.columns([50, 1100, 50])
    with col1:
        st.write("")
    with col2:
        st.image(image_vac)
    with col3:
        st.write("")


    st.text("")

    col1A, col2A, col3A, col4A, col5A = st.columns([50, 520, 60, 520, 50])
    with col1A:
        st.text("")
    with col2A:
        st.code(body, language="python")
    with col3A:
        st.text("")
    with col4A:
        st.markdown(html_card_header_0B_1_10, unsafe_allow_html=True) # Extração dos Dados
    with col5A:
        st.write("")

    st.text("")
    st.text("")

    col1B, col2B, col3B = st.columns([100, 1000, 100])
    with col1B:
        st.write("")
    with col2B:
        st.markdown(html_body_0B_20, unsafe_allow_html=True) # CAIXA DE TEXTO
    with col3B:
        st.text("")

    st.text("")
    st.text("")

    with st.expander("Código da Limpeza dos Dados"):
        st.code(body2, language="python")

    st.text("")
    st.text("")
    col1, col2, col3 = st.columns([20, 1, 20])
    with col1:
        st.markdown(html_card_header_0B_3_31, unsafe_allow_html=True) # Dados antes do Tratamento
        st.dataframe(data=df_old, height=300)
    with col2:
        st.text("")
    with col3:
        st.markdown(html_card_header_0B_3_32, unsafe_allow_html=True) # Dados depois do Tratamento
        st.dataframe(data=df_new, height=300)

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    st.write("")
    return None

def overview3():
    st.text("")
    st.markdown(html_subheader_0C_1, unsafe_allow_html=True) # Análise das variaveis dos Dados
    st.text("")
    st.text("")

    col1, col2, col3 = st.columns([100, 1000, 100])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_body_0C_20, unsafe_allow_html=True) # CAIXA DE TEXTO
    with col3:
        st.text("")

    st.text("")
    st.text("")

    col1A, col2A, col3A, col4A, col5A = st.columns([50, 520, 60, 520, 50])
    with col1A:
        st.text("")
    with col2A:
        st.markdown(html_card_header_0C_2_11, unsafe_allow_html=True)  # Identificador Único dos Pacientes (id_paciente)
        st.image(image2)
        st.text("")
        st.markdown(html_card_header_0C_2_12, unsafe_allow_html=True) # Idade dos Pacientes (idade_paciente)
        st.image(image3)
        st.text("")
        st.markdown(html_card_header_0C_2_21, unsafe_allow_html=True) # Sexo Biológico dos Pacientes (sexo_paciente)
        st.image(image4)
        st.text("")
        st.markdown(html_card_header_0C_2_22, unsafe_allow_html=True) # Raça ou Cor dos Pacientes (raca_cor_paciente)
        st.image(image5)
        st.text("")
        st.markdown(html_card_header_0C_2_51, unsafe_allow_html=True) # Estastisticas do Banco de Dados
        st.image(image1)
        st.text("")

    with col3A:
        st.text("")
    with col4A:
        st.markdown(html_card_header_0C_2_32, unsafe_allow_html=True) # Fabricantes das Vacinas Aplicadas (nome_fabrica_vacina)
        st.image(image7)
        st.text("")
        st.markdown(html_card_header_0C_2_41, unsafe_allow_html=True)  # Tipo de Doses Aplicadas (dose_vacina)
        st.image(image8)
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.markdown(html_card_header_0C_2_31, unsafe_allow_html=True) # Grupos de Atendimento da Vacinação (grupo_atendimento)
        st.image(image6)
        st.text("")
        st.markdown(html_card_header_0C_2_42, unsafe_allow_html=True)  # Municipio onde foi Vacinado (nome_municipio_estabelecimento)
        st.image(image9)
        st.text("")
        st.markdown(html_card_header_0C_2_52, unsafe_allow_html=True)  # Descrição dos Dados
        st.image(image10)
        st.text("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    return None


def campanha1():
    st.markdown("""---""")
    st.markdown(html_header_01, unsafe_allow_html=True) # 1 - Descrição da Campanha de Vacinação
    st.markdown("""---""")
    st.text("")

    with st.expander('⚙ Configurar visualização de gráficos e tabelas 👈'):
        st.markdown("""---""")
        st.markdown(html_expanderheader_1_10, unsafe_allow_html=True) # Selecione o tipo da sua análise:
        st.text("")
        st.text("")

        col1, col2, col3, col4, col5 = st.columns([20, 1, 20, 1, 20])
        with col1:
            status_1 = st.radio("Vacinados por DOSE:",
                                   ('Gráfico Velocimetro - Total e Meta', 'Geáfico de Pizza - Porcentagens'),
                                   key=11, horizontal=False)
        with col2:
            st.write("")
        with col3:
            status_2 = st.radio("Quantidade de VACINAS aplicadas por DOSE",
                                   ('Total', 'Proporção'),
                                   key=12, horizontal=False)
        with col4:
            st.write("")
        with col5:
            status_3 = st.radio("Dados agrupados por PACIENTE:",
                                   ('Campanha de Vacinação', 'Caracteristicas dos Pacientes', 'Posto de Vacinação'),
                                   key=13, horizontal=False)

        st.markdown("""---""")

    st.text("")

    st.markdown(html_subheader_11, unsafe_allow_html=True) # 1.1 - Número de Doses & Vacinas Aplicadas
    st.text("")
    st.text("")

### CAMPANHA 1 - LINHA A -> COM FILTRO --------------------------------------------------------
    if status_1 == 'Gráfico Velocimetro - Total e Meta':
        col1, col2, col3, col4, col5, col6, col7 = st.columns([50, 333, 50, 333, 50, 333, 50])
        with col1:
            st.write("")
        with col2:
            st.markdown(html_card_header_1_A_100, unsafe_allow_html=True) # Vacinados com 1° Dose
            st.plotly_chart(figAA1, use_container_width=True) # VELOCIMETRO
        with col3:
            st.write("")
        with col4:
            st.markdown(html_card_header_1_A_010, unsafe_allow_html=True) # Vacinados com 2° Dose
            st.plotly_chart(figAB1, use_container_width=True) # VELOCIMETRO
        with col5:
            st.write("")
        with col6:
            st.markdown(html_card_header_1_A_001, unsafe_allow_html=True) # Vacinados com Dose Adicional
            st.plotly_chart(figAC1, use_container_width=True) # VELOCIMETRO
        with col7:
            st.write("")

    else:
        col1, col2, col3, col4, col5, col6, col7 = st.columns([50, 333, 50, 333, 50, 333, 50])
        with col1:
            st.write("")
        with col2:
            st.markdown(html_card_header_1_A_100, unsafe_allow_html=True) # Vacinados com 1° Dose
            st.plotly_chart(figAA2, use_container_width=True) # PIZZA
        with col3:
            st.write("")
        with col4:
            st.markdown(html_card_header_1_A_010, unsafe_allow_html=True) # Vacinados com 2° Dose
            st.plotly_chart(figAB2, use_container_width=True) # PIZZA
        with col5:
            st.write("")
        with col6:

            st.markdown(html_card_header_1_A_001, unsafe_allow_html=True) # Vacinados com Dose Adicional
            st.plotly_chart(figAC2, use_container_width=True) # PIZZA
        with col7:
            st.write("")

    st.write("")

### CAMPANHA 1 - LINHA B -------------------------------------------------------
    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([50, 520, 60, 520, 50])
        with col1B:
            st.write("")
        with col2B:
            st.markdown(html_card_header_1_B_21, unsafe_allow_html=True) # Quantidade de Vacinas Aplicadas por Dose
            st.plotly_chart(figAD0, use_container_width=True) # GRÁFICO DE BARRA HORIZONTAL
            st.write("")
            st.markdown(html_card_header_1_B_22, unsafe_allow_html=True) # Proporção entre as Vacinas Aplicadas
            st.plotly_chart(figAE0, use_container_width=True) # GRÁFICO DE FUNIL
        with col3B:
            st.write("")
        with col4B:
            if status_3 == 'Campanha de Vacinação':
                st.markdown(html_card_header_1_B_23, unsafe_allow_html=True)
                st.dataframe(data=df_AF_1, height=200)
            elif status_3 == 'Caracteristicas dos Pacientes':
                st.markdown(html_card_header_1_B_23, unsafe_allow_html=True)
                st.dataframe(data=df_AF_2, height=200)
            elif status_3 == 'Posto de Vacinação':
                st.markdown(html_card_header_1_B_23, unsafe_allow_html=True)
                st.dataframe(data=df_AF_3, height=200)
        with col5B:
            st.write("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    return None

def campanha2():

    col1A, col2A, col3A = st.columns([50, 1100, 50])
    with col1A:
        st.write("")
    with col2A:
        with st.expander('⚙ Configurar visualização de gráficos e tabelas 👈'):
            st.markdown(html_expanderheader_1_10, unsafe_allow_html=True) # Selecione o tipo da sua análise:
            st.markdown("""---""")
            status1 = st.radio("Selecione sua análise temporal:",
                               ('Dia', 'Mês', 'Trimestre', 'Semestre', 'Ano'), key=16, horizontal=True)
    with col3A:
        st.write("")

    st.text("")
    st.markdown(html_subheader_12, unsafe_allow_html=True) # 1.2 - Variação das Doses & Vacinas Aplicadas
    st.write("")
    st.write("")

### CAMPANHA 2 - LINHA 1
    with st.container():
        if status1 == 'Dia':
            col1B, col2B, col3B, col4B, col5B = st.columns([50, 520, 60, 520, 50])
            with col1B:
                st.write("")
            with col2B:
                st.markdown(html_card_header_1C11, unsafe_allow_html=True) # Variação diária de DOSES aplicadas
                st.plotly_chart(figBA0, use_container_width=True) # GRÁFICO DE LINHA AREA (4)
                st.write("")
                st.markdown(html_card_header_1C12, unsafe_allow_html=True)
                st.plotly_chart(figBB0, use_container_width=True)
            with col3B:
                st.write("")
            with col4B:
                st.markdown(html_card_header_1C13, unsafe_allow_html=True)
                st.dataframe(data=df_BC_0, height=200)
            with col5B:
                st.write("")
        else:
            st.write("Ainda nada")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    st.write("")
    return None


# - CARACTERISTICAS DOS PACIENTES -----------------------------------------------------------
def pacientes1():
    st.markdown("""---""")
    st.write("")
    st.markdown(html_header_20, unsafe_allow_html=True) # 2 - Características da População Vacinada
    st.write("")
    st.markdown("""---""")

## 2.1 - Análise do Sexo Biológico:
    col1A, col2A, col3A = st.columns([50, 1100, 50])
    with col1A:
        st.write("")
    with col2A:
        with st.expander('⚙ Configurar gráficos e tabelas 👈'):
            st.markdown(html_expanderheader_1_10, unsafe_allow_html=True)  # Selecione o tipo da sua análise:
            st.markdown("""---""")
            status1 = st.radio("Dados Agrupados por Sexo Biológico:",
                               ('Características dos Pacinados', 'Campanha de Vacinação'), key=21, horizontal=True)
    with col3A:
        st.write("")
    st.write("")
    st.markdown(html_subheader_2A_10, unsafe_allow_html=True) # 2.1 - Análise do Sexo Biológico
    st.write("")
    st.write("")
    st.write("")

    with st.container():
        col1A, col2A, col3A, col4A, col5A, col6A, col7A = st.columns([50, 333, 50, 333, 50, 333, 50])
        with col1A:
            st.write("")
        with col2A:
            st.markdown(html_card_header_2A_1_11, unsafe_allow_html=True) # Vacinados do Sexo Masculino
            st.plotly_chart(fig_CA1_1, use_container_width=True) # GRÁFICO VELOCIMETRO
        with col3A:
            st.write("")
        with col4A:
            st.markdown(html_card_header_2A_1_12, unsafe_allow_html=True) # Proporção entre os Sexos
            st.plotly_chart(fig_CA_20, use_container_width=True) # GRÁFICO DE PIZZA
        with col5A:
            st.write("")
        with col6A:
            st.markdown(html_card_header_2A_1_13, unsafe_allow_html=True) # Vacinados do Sexo Feminino
            st.plotly_chart(fig_CA_30, use_container_width=True) # GRÁFICO VELOCIMETRO
        with col7A:
            st.write("")

    with st.container():
        col1B, col2B, col3B = st.columns([50, 1100, 50])
        with col1B:
            st.write("")
        with col2B:
            if status1 == 'Características dos Pacinados':
                st.markdown(html_card_header_2A_1_20_1, unsafe_allow_html=True)  # Sexo Biológico - Dados Agrupados
                st.dataframe(data=df_CB_01)  # TABELA DADOS AGRUPADOS
            elif status1 == 'Campanha de Vacinação':
                st.markdown(html_card_header_2A_1_20_2, unsafe_allow_html=True)  # Sexo Biológico - Dados Agrupados
                st.dataframe(data=df_CB_02)  # TABELA DADOS AGRUPADOS
        with col3B:
            st.write("")

    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([50, 520, 60, 520, 50])
        with col1B:
            st.write("")
        with col2B:
            st.markdown(html_card_header_2A_1_31, unsafe_allow_html=True) # Variação de Vacinados
            st.plotly_chart(fig_CC_10, use_container_width=True) # GRÁFICO DE LINHA
        with col3B:
            st.write("")
        with col4B:
            st.markdown(html_card_header_2A_1_32, unsafe_allow_html=True)  # Variação de Vacinados
            st.plotly_chart(fig_CC_20, use_container_width=True)  # GRÁFICO DE LINHA
        with col5B:
            st.write("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    return None

## 2.2 - Análise da Raça ou Cor:
def pacientes2():
    st.write("")
    st.markdown(html_subheader_2B_10, unsafe_allow_html=True) # 2.2 - Análise da Raça/Cor
    st.write("")
    st.write("")
    st.write("")


    with st.container():
        col1A, col2A, col3A, col4A, col5A = st.columns([50, 520, 60, 520, 50])
        with col1A:
            st.write("")
        with col2A:
            st.markdown(html_card_header_2B_2_11, unsafe_allow_html=True) # População Residente x População Vacinada
            st.plotly_chart(fig_DA_1, use_container_width=True)
        with col3A:
            st.write("")
        with col4A:
            st.markdown(html_card_header_2B_2_12, unsafe_allow_html=True) # Raça/Cor - Dados Agrupados
            st.dataframe(data=df_DA_2, height=200)
        with col5A:
            st.write("")

    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([50, 520, 60, 520, 50])
        with col1B:
            st.write("")
        with col2B:
            st.markdown(html_card_header_2B_2_21, unsafe_allow_html=True) # Raça/Cor - Dados Agrupados
            st.plotly_chart(fig_DB_1, use_container_width=True) # GRÁFICO VIOLINO
        with col3B:
            st.write("")
        with col4B:
            st.markdown(html_card_header_2B_2_22, unsafe_allow_html=True) # Raça/Cor - Dados Agrupados
            st.plotly_chart(fig_DB_2, use_container_width=True) # GRÁFICO DE LINHA AREA
        with col5B:
            st.write("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    return None

## 2.3 - Análise da Idade:
def pacientes3():
    st.write("")
    st.markdown(html_subheader_2B_30, unsafe_allow_html=True) # 2.3 - Análise da Idade
    st.write("")
    st.write("")
    st.write("")


    with st.container():
        col1A, col2A, col3A, col4A, col5A = st.columns([50, 520, 60, 520, 50])
        with col1A:
            st.write("")
        with col2A:
            st.markdown(html_card_header_2B_3_11, unsafe_allow_html=True) # Quantidade de Vacinados
            st.plotly_chart(fig_EA_1, use_container_width=True) # GRÁFICO DE BARRA
        with col3A:
            st.write("")
        with col4A:
            st.markdown(html_card_header_2B_3_22, unsafe_allow_html=True)  # Companha de Vacinação
            st.plotly_chart(fig_EB_2, use_container_width=True)  # GRÁFICO DE BARRA
        with col5A:
            st.write("")

    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([50, 520, 60, 520, 50])
        with col1B:
            st.write("")
        with col2B:
            st.markdown(html_card_header_2B_3_21, unsafe_allow_html=True) # Variação de Vacinados
            st.plotly_chart(fig_EB_1, use_container_width=True)  # GRÁFICO DE LINHA
        with col3B:
            st.write("")
        with col4B:
            st.markdown(html_card_header_2B_3_12, unsafe_allow_html=True)  # Dados Agrupados
            st.dataframe(data=df_EA_2, height=200)  # TABELA DE DADOS AGRUPADOS
        with col5B:
            st.write("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    return None







