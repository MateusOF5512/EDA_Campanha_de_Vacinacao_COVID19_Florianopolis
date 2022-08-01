# Importação de Bibliotecas:

from teste import *
from teste_variaveis import *
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from PIL import Image


# TITULO I - EXTRAÇÃO DOS DADOS
## - LENDO OS DADOS:
@st.cache(allow_output_mutation=True)
def get_data_vac( path1 ):
    df = pd.read_csv( path1 , sep=";")
    return df

def get_data_vac_old( path2 ):
    df_old = pd.read_csv( path2 , sep=";")
    return df_old

def get_data_11( path11 ):
    df_11 = pd.read_csv( path11 , sep=";")
    return df_11

def get_data_12( path12 ):
    df_12 = pd.read_csv( path12, sep=";")
    return df_12


# - TITULO II - TRANSFORMAÇÃO DOS DADOS
## CRIANDO NOVAS COLUNAS PARA MELHOR LEITURA DOS GRAFICOS:
def set_feature( df ):
    df['data_aplicacao_vacina'].replace("1993-11-08", "2021-11-08", inplace=True)

    df['1DOSE'] = np.where(df['dose_vacina'] == '1ª Dose', 1, 0)
    df['2DOSE'] = np.where(df['dose_vacina'] == '2ª Dose', 1, 0)
    df['DOSE_UNI'] = np.where(df['dose_vacina'] == 'Dose Única', 1, 0)
    df['DOSE_ADC'] = np.where(df['dose_vacina'] == 'Dose Adicional', 1, 0)

    df['PFIZER'] = np.where(df['nome_fabricante_vacina'] == 'PFIZER', 1, 0)
    df['ASTRAZENECA_FIOCRUZ']      = np.where(df['nome_fabricante_vacina'] == 'ASTRAZENECA/FIOCRUZ', 1, 0)
    df['SINOVAC_BUTANTAN']   = np.where(df['nome_fabricante_vacina'] == 'SINOVAC/BUTANTAN', 1, 0)
    df['JANSSEN']     = np.where(df['nome_fabricante_vacina'] == 'JANSSEN', 1, 0)

    df['FEMININO']  = np.where(df['sexo_paciente'] == 'Feminino', 1, 0)
    df['MASCULINO'] = np.where(df['sexo_paciente'] == 'Masculino', 1, 0)

    df['BRANCA']         = np.where(df['raca_cor_paciente'] == 'Branca', 1, 0)
    df['PRETA']          = np.where(df['raca_cor_paciente'] == 'Preta', 1, 0)
    df['PARDA']          = np.where(df['raca_cor_paciente'] == 'Parda', 1, 0)
    df['AMARELA']        = np.where(df['raca_cor_paciente'] == 'Amarela', 1, 0)
    df['INDIGENA']       = np.where(df['raca_cor_paciente'] == 'Indígena', 1, 0)
    df['SEM INFORMACAO'] = np.where(df['raca_cor_paciente'] == 'Sem informação', 1, 0)

    conditions = [
        (df['idade_paciente'] <= 19),
        (df['idade_paciente'] >= 20) & (df['idade_paciente'] <= 39),
        (df['idade_paciente'] >= 40) & (df['idade_paciente'] <= 59),
        (df['idade_paciente'] >= 60) & (df['idade_paciente'] <= 79),
        (df['idade_paciente'] >= 80)]
    values = ['menos 19 anos', '20 a 39 anos', '40 a 59 anos', '60 a 79 anos', 'mais 80 anos']
    df['faixa_etaria'] = np.select(conditions, values)

    df['menos 19 anos'] = np.where(df['faixa_etaria'] == 'menos 19 anos', 1, 0)
    df['20 a 39 anos'] = np.where(df['faixa_etaria'] == '20 a 39 anos', 1, 0)
    df['40 a 59 anos'] = np.where(df['faixa_etaria'] == '40 a 59 anos', 1, 0)
    df['60 a 79 anos'] = np.where(df['faixa_etaria'] == '60 a 79 anos', 1, 0)
    df['mais 80 anos'] = np.where(df['faixa_etaria'] == 'mais 80 anos', 1, 0)

    df_selection = df

    return df_selection



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

def overview2(df_old, df):
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
        df_old = df_old.drop(columns=['Unnamed: 0'])
        df_old = df_old[["idade_paciente", "sexo_paciente", "raca_cor_paciente", "grupo_atendimento_vacina",
                 "nome_fabricante_vacina", "dose_vacina",
                 "nome_municipio_estabelecimento", "nome_fantasia_estabelecimento",
                 "id_paciente"]]

        st.markdown(html_card_header_0B_3_31, unsafe_allow_html=True) # Dados antes do Tratamento
        st.dataframe(data=df_old, height=300)
    with col2:
        st.text("")
    with col3:
        df = df.drop(columns=['Unnamed: 0'])
        df = df[["idade_paciente", "sexo_paciente", "raca_cor_paciente", "grupo_atendimento_vacina",
                 "nome_fabricante_vacina", "dose_vacina",
                 "nome_municipio_estabelecimento", "nome_fantasia_estabelecimento",
                 "id_paciente"]]
        df1 = df.sample(n=1000)

        st.markdown(html_card_header_0B_3_32, unsafe_allow_html=True) # Dados depois do Tratamento
        st.dataframe(data=df1, height=300)

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


def campanha1( df_11 ):
    st.markdown("""---""")
    st.markdown(html_header_01, unsafe_allow_html=True) # 1 - Descrição da Campanha de Vacinação
    st.markdown("""---""")
    st.text("")

    with st.expander('⚙📊 Configurar visualização de gráficos e tabelas 👈👈'):
        st.markdown("""---""")
        st.markdown(html_expanderheader_1_10, unsafe_allow_html=True)
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

    # DECLARAÇÂO DE VARIAVEIS GERAIS - 1.1A -
    popul_residente = int(516524)
    imun_rebanho = int(387393)
    vacinados_1dose = int(df_11['1DOSE'].sum())
    vacinados_2dose = int(df_11['2DOSE'].sum() + df_11['DOSE_UNI'].sum())
    vacinados_adcdose = int(df_11['DOSE_ADC'].sum())

    pop_sem_1dose = (popul_residente - vacinados_1dose)
    pop_sem_2dose = (popul_residente - vacinados_2dose)
    pop_sem_adcdose = (popul_residente - vacinados_adcdose)


    if status_1 == 'Gráfico Velocimetro - Total e Meta':
        col1, col2, col3, col4, col5, col6, col7 = st.columns([50, 333, 50, 333, 50, 333, 50])
        with col1:
            st.write("")
        with col2:
            fig2 = go.Figure()
            fig2.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=vacinados_1dose,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': imun_rebanho, 'increasing': {'color': "Purple"}},
                gauge={
                    'axis': {'range': [0, 520000], 'tickwidth': 2, 'tickcolor': "#4169E1"},
                    'bordercolor': "#4169E1",
                    'bar': {'color': "#4169E1"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'steps': [
                        {'range': [0, imun_rebanho], 'color': "#ADD8E6"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': imun_rebanho}}))
            fig2.update_layout(autosize=False,
                               height=120, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})

            st.markdown(html_card_header_1_A_100, unsafe_allow_html=True)
            st.plotly_chart(fig2, use_container_width=True)
        with col3:
            st.write("")
        with col4:
            fig3 = go.Figure()
            fig3.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=vacinados_2dose,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': imun_rebanho, 'increasing': {'color': "Purple"}},
                gauge={
                    'axis': {'range': [0, 520000], 'tickwidth': 2, 'tickcolor': "#D70270"},
                    'bordercolor': "#D70270",
                    'bar': {'color': "#D70270"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'steps': [
                        {'range': [0, imun_rebanho], 'color': "#FFC0CB"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.7,
                        'value': imun_rebanho}}))
            fig3.update_layout(autosize=False,
                               height=120, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})

            st.markdown(html_card_header_1_A_010, unsafe_allow_html=True)
            st.plotly_chart(fig3, use_container_width=True)
        with col5:
            st.write("")
        with col6:
            fig4 = go.Figure()
            fig4.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=vacinados_adcdose,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': imun_rebanho, 'increasing': {'color': "Purple"}},
                gauge={
                    'axis': {'range': [0, 520000], 'tickwidth': 2, 'tickcolor': "#D70270"},
                    'bordercolor': "#D70270",
                    'bar': {'color': "#D70270"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'steps': [
                        {'range': [0, imun_rebanho], 'color': "#FFC0CB"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.7,
                        'value': imun_rebanho}}))
            fig4.update_layout(autosize=False,
                               height=120, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})

            st.markdown(html_card_header_1_A_001, unsafe_allow_html=True)
            st.plotly_chart(fig4, use_container_width=True)
        with col7:
            st.write("")

    else:
        col1, col2, col3, col4, col5, col6, col7 = st.columns([50, 333, 50, 333, 50, 333, 50])
        with col1:
            st.write("")
        with col2:
            labels2 = ['População com 1° Dose', "População sem 1° Dose:"]
            colors2 = ['#4169E1', 'gray']
            # PLOTAGEM GRÀFICO DE PIZZA - 1.1B: --------------------------------------------------------------
            fig1 = go.Figure(data=[go.Pie(labels=labels2,
                                          values=[vacinados_1dose, pop_sem_1dose],
                                          textinfo='percent',
                                          showlegend=False,
                                          marker=dict(colors=colors2,
                                                      line=dict(color='#000010', width=2)))])
            fig1.update_traces(hole=.4, hoverinfo="label+percent+value")
            fig1.update_layout(autosize=False,
                               height=120, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})

            st.markdown(html_card_header_1_A_100, unsafe_allow_html=True)
            st.plotly_chart(fig1, use_container_width=True)
        with col3:
            st.write("")
        with col4:
            labels3 = ['Vacinados Completamente', 'Vacinados Incompletamente']
            colors3 = ['#D70270', 'gray']

            # PLOTAGEM GRÀFICO DE PIZZA - 1.1D: ---------------------------------------------------------------
            fig4 = go.Figure(data=[go.Pie(labels=labels3,
                                          values=[vacinados_2dose, pop_sem_2dose],
                                          textinfo='percent', textfont_size=20,
                                          showlegend=False,
                                          marker=dict(colors=colors3,
                                                      line=dict(color=' #000010', width=2)))])
            fig4.update_traces(hole=.4, hoverinfo="label+percent+value")
            fig4.update_layout(autosize=False,
                               height=120, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})

            st.markdown(html_card_header_1_A_010, unsafe_allow_html=True)
            st.plotly_chart(fig4, use_container_width=True)
        with col5:
            st.write("")
        with col6:
            labels3 = ['Vacinados Completamente', 'Vacinados Incompletamente']
            colors3 = ['#D70270', 'gray']

            # PLOTAGEM GRÀFICO DE PIZZA - 1.1D: ---------------------------------------------------------------
            fig5 = go.Figure(data=[go.Pie(labels=labels3,
                                          values=[vacinados_adcdose, pop_sem_adcdose],
                                          textinfo='percent', textfont_size=20,
                                          showlegend=False,
                                          marker=dict(colors=colors3,
                                                      line=dict(color=' #000010', width=2)))])
            fig5.update_traces(hole=.4, hoverinfo="label+percent+value")
            fig5.update_layout(autosize=False,
                               height=120, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})

            st.markdown(html_card_header_1_A_001, unsafe_allow_html=True)
            st.plotly_chart(fig5, use_container_width=True)
        with col7:
            st.write("")

    st.write("")

# - PARTE B - 1 CAMPANHA DE VACINAÇÃO -----------------------------------------------------------------------
    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([50, 520, 60, 520, 50])
        with col1B:
            st.write("")
        with col2B:
            df = df_11
            values = ['1° Dose', '2° Dose','Dose Única', 'Dose Adicional']
            y_PFIZER = [df['1DOSE'][2], df['2DOSE'][2], df['DOSE_UNI'][2], df['DOSE_ADC'][2]]
            y_ASTRAZENECA_FIOCRUZ = [df['1DOSE'][0], df['2DOSE'][0], df['DOSE_UNI'][0], df['DOSE_ADC'][0]]
            y_SINOVAC_BUTANTAN = [df['1DOSE'][3], df['2DOSE'][3], df['DOSE_UNI'][3], df['DOSE_ADC'][3]]
            y_JANSSEN = [df['1DOSE'][1], df['2DOSE'][1], df['DOSE_UNI'][1], df['DOSE_ADC'][1]]

            fig2 = go.Figure()
            fig2.add_trace(go.Bar(name='Pfizer', x=values, y=y_PFIZER,
                                  text=y_PFIZER, textposition='auto',
                                  marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
            fig2.add_trace(go.Bar(name='AstraZeneca/Fiocruz', x=values, y=y_ASTRAZENECA_FIOCRUZ,
                                  text=y_ASTRAZENECA_FIOCRUZ, textposition='auto',
                                  marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
            fig2.add_trace(go.Bar(name='Sinovac/Butantan', x=values, y=y_SINOVAC_BUTANTAN,
                                  text=y_SINOVAC_BUTANTAN, textposition='auto',
                                  marker_color=['#4B0082', '#4B0082', '#4B0082', '#4B0082', '#4B0082']))
            fig2.add_trace(go.Bar(name='Janssen', x=values, y=y_JANSSEN,
                                  text=y_JANSSEN, textposition='auto',
                                  marker_color=['#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF']))
            fig2.update_layout(legend_font_size=12, autosize=False,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"},
                               height=200,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="v",
                                           yanchor="top",
                                           y=0.95,
                                           xanchor="right",
                                           x=0.98),
                               barmode='group')
            fig2.update_xaxes(
                title_text='Doses Aplicadas',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9))
            fig2.update_yaxes(
                title_text="Número de Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_1_B_21, unsafe_allow_html=True)
            st.plotly_chart(fig2, use_container_width=True)

            # PREPARAÇÂO DOS DADOS - 1.3B - Vacinas Aplicadas por Dose: -------------------------------------
            y_PFIZER = int(df_11['TOTAL_DOSES'][2])
            y_ASTRAZENECA_FIOCRUZ = int(df_11['TOTAL_DOSES'][0])
            y_SINOVAC_BUTANTAN = int(df_11['TOTAL_DOSES'][3])
            y_JANSSEN = int(df_11['TOTAL_DOSES'][1])

            values = ["Pfizer", "AstraZeneca/Fiocruz", "Sinovac/Butantan", "Janssen", ]
            y = [y_PFIZER, y_ASTRAZENECA_FIOCRUZ, y_SINOVAC_BUTANTAN, y_JANSSEN, ]

            # ------------------- PLOTAGEM GRÀFICO DE BARRA - 1.3B - Proporção das Vacinas Aplicadas:
            fig2 = go.Figure()
            fig2.add_trace(go.Funnel(
                y=values, x=y,
                textposition="inside",
                textinfo="value+percent total",
                opacity=1, marker={"color": ["#D70270", "#4169E1", "#8A2BE2", "#00FFFF", "#ADFF2F"],
                                   "line": {"width": [2, 2, 2, 2, 2, 2],
                                            "color": ["black", "black", "black", "black", "black"]}},
                connector={"line": {"color": "black", "dash": "solid", "width": 2}}))
            fig2.update_layout(paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"},
                               height=150,
                               margin=dict(l=2, r=2, b=4, t=4))

            st.markdown(html_card_header_1_B_22, unsafe_allow_html=True)
            st.plotly_chart(fig2, use_container_width=True)
            st.write("")
        with col3B:
            st.write("")
        with col4B:
            df_new = df_11

            if status_3 == 'Campanha de Vacinação':
                st.markdown(html_card_header_1_B_23, unsafe_allow_html=True)
                st.dataframe(data=df_new, height=230)

            elif status_3 == 'Caracteristicas dos Pacientes':
                st.markdown(html_card_header_1_B_23, unsafe_allow_html=True)
                st.dataframe(data=df_new, height=230)

            elif status_3 == 'Posto de Vacinação':
                st.markdown(html_card_header_1_B_23, unsafe_allow_html=True)
                st.dataframe(data=df_new, height=230)
        with col5B:
            st.write("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    return None

def campanha2( df_12 ):

    col1A, col2A, col3A = st.columns([50, 1100, 50])
    with col1A:
        st.write("")
    with col2A:
        with st.expander('⚙📊 Configurar visualização de gráficos e tabelas 👈👈'):
            st.markdown(html_expanderheader_1_10, unsafe_allow_html=True)
            st.markdown("""---""")
            status1 = st.radio("Selecione sua análise temporal:",
                               ('Dia', 'Mês', 'Trimestre', 'Semestre', 'Ano'), key=16, horizontal=True)
    with col3A:
        st.write("")

    st.text("")
    st.markdown(html_subheader_12, unsafe_allow_html=True)
    st.write("")
    st.write("")

    # ---------------------------------------------------------------------------------
    with st.container():
        if status1 == 'Dia':
            col1B, col2B, col3B, col4B, col5B = st.columns([50, 520, 60, 520, 50])
            with col1B:
                st.write("")
            with col2B:
                df_12['data_aplicacao_vacina'].replace("1993-11-08", "2021-11-08", inplace=True)
                df_area = df_12

                # 1.2B - Variação Diária da Aplicação das Doses - PLOTAGEM GRÀFICO DE AREA --------------------------------
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(
                    x=df_area['data_aplicacao_vacina'],
                    y=df_area['1DOSE'],
                    name='1° Dose',
                    mode='lines',
                    line=dict(width=1, color='#4169E1'),
                    stackgroup='one'))
                fig2.add_trace(go.Scatter(
                    x=df_area['data_aplicacao_vacina'],
                    y=df_area['2DOSE'],
                    name='2° Dose',
                    mode='lines',
                    line=dict(width=1, color='#D70270'),
                    stackgroup='two'))
                fig2.add_trace(go.Scatter(
                    x=df_area['data_aplicacao_vacina'],
                    y=df_area['DOSE_UNI'],
                    name='Dose Única',
                    mode='lines',
                    line=dict(width=1, color='#00FFFF'),
                    stackgroup='three'))
                fig2.add_trace(go.Scatter(
                    x=df_area['data_aplicacao_vacina'],
                    y=df_area['DOSE_ADC'],
                    name='Dose Adicional',
                    mode='lines',
                    line=dict(width=1, color='#8A2BE2'),
                    stackgroup='four'))
                fig2.update_layout(legend_font_size=10,
                                   paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                                   font={'color': "#4169E1", 'family': "sans-serif"}, height=200,
                                   margin=dict(l=2, r=2, b=4, t=4),
                                   legend=dict(orientation="v",
                                               yanchor="top",
                                               y=0.99,
                                               xanchor="left",
                                               x=0.05))
                fig2.update_xaxes(
                    title_text='Dias da Aplicação da Vacina',
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    rangeslider_visible=True)
                fig2.update_yaxes(
                    title_text="Número de Vacinados",
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

                st.markdown(html_card_header_1C11, unsafe_allow_html=True)
                st.plotly_chart(fig2, use_container_width=True)
                st.write("")

                df_area = df_12

                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(
                    x=df_area['data_aplicacao_vacina'],
                    y=df_area['ASTRAZENECA_FIOCRUZ'],
                    name='ASTRAZENECA/FIOCRUZ',
                    mode='lines',
                    line=dict(width=1, color='#D70270'),
                    stackgroup='one'))
                fig2.add_trace(go.Scatter(
                    x=df_area['data_aplicacao_vacina'],
                    y=df_area['PFIZER'],
                    name='PFIZER',
                    mode='lines',
                    line=dict(width=1, color='#4169E1'),
                    stackgroup='two'))
                fig2.add_trace(go.Scatter(
                    x=df_area['data_aplicacao_vacina'],
                    y=df_area['SINOVAC_BUTANTAN'],
                    name='SINOVAC/BUTANTAN',
                    mode='lines',
                    line=dict(width=1, color='#8A2BE2'),
                    stackgroup='four'))
                fig2.add_trace(go.Scatter(
                    x=df_area['data_aplicacao_vacina'],
                    y=df_area['JANSSEN'],
                    name='JANSSEN',
                    mode='lines',
                    line=dict(width=1, color='#00FFFF'),
                    stackgroup='five'))
                fig2.update_layout(legend_font_size=10,
                                   paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                                   font={'color': "#4169E1", 'family': "sans-serif"}, height=200,
                                   margin=dict(l=2, r=2, b=4, t=4),
                                   legend=dict(orientation="v",
                                               yanchor="top",
                                               y=0.99,
                                               xanchor="left",
                                               x=0.05))
                fig2.update_xaxes(
                    title_text='Dia da Aplicação da Vacina',
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    rangeslider_visible=True)
                fig2.update_yaxes(
                    title_text="Número de Vacinados",
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

                st.markdown(html_card_header_1C12, unsafe_allow_html=True)
                st.plotly_chart(fig2, use_container_width=True)

            with col3B:
                st.write("")
            with col4B:
                df_new = df_12

                st.markdown(html_card_header_1C13, unsafe_allow_html=True)
                st.dataframe(data=df_new, height=220)

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
def pacientes1(df_selection):
    st.markdown("""---""")
    st.write("")
    st.markdown(html_header_20, unsafe_allow_html=True) # 2 - Características da População Vacinada
    st.write("")
    st.markdown("""---""")
    st.write("")

## 2.1 - Análise do Sexo Biológico:
    st.markdown(html_subheader_2A_10, unsafe_allow_html=True) # 2.1 - Análise do Sexo Biológico
    st.write("")
    st.write("")
    st.write("")

    with st.container():
        col1A, col2A, col3A, col4A, col5A, col6A, col7A = st.columns([50, 333, 50, 333, 50, 333, 50])
        with col1A:
            st.write("")
        with col2A:
            df_selection1 = df_selection.drop_duplicates(subset=['id_paciente'], keep="last")

            popul_femi = int(268592)
            rebanho_femi = int(201444)
            popul_masc = int(247931)
            rebanho_masc = int(185948)
            vacinados_femi = int(df_selection1['FEMININO'].sum())
            vacinados_masc = int(df_selection1['MASCULINO'].sum())


            fig3 = go.Figure()
            fig3.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=vacinados_masc,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': rebanho_masc, 'increasing': {'color': "Purple"}},
                gauge={
                    'axis': {'range': [0, popul_masc], 'tickwidth': 2, 'tickcolor': "#4169E1"},
                    'bordercolor': "#4169E1",
                    'bar': {'color': "#4169E1"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'steps': [
                        {'range': [0, rebanho_masc], 'color': "#ADD8E6"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.7,
                        'value': rebanho_masc}}))
            fig3.update_layout(autosize=False,
                               height=120, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})

            st.markdown(html_card_header_2A_1_11, unsafe_allow_html=True) # Vacinados do Sexo Masculino
            st.plotly_chart(fig3, use_container_width=True)
        with col3A:
            st.write("")
        with col4A:
            labels1 = ['Sexo Feminino', 'Sexo Masculino']
            colors1 = ['#D70270', '#4169E1']  # magenta , royalblue

            fig2 = go.Figure(data=[go.Pie(labels=labels1, values=[vacinados_femi, vacinados_masc],
                                          textinfo='percent', textfont_size=20, showlegend=False,
                                          marker=dict(colors=colors1, line=dict(color='black', width=3)))])
            fig2.update_traces(hole=.4, hoverinfo="label+percent+value")
            fig2.update_layout(autosize=False, height=120, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})

            st.markdown(html_card_header_2A_1_12, unsafe_allow_html=True) # Proporção entre os Sexos
            st.plotly_chart(fig2, use_container_width=True)
        with col5A:
            st.write("")
        with col6A:
            fig1 = go.Figure()
            fig1.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=vacinados_femi,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': rebanho_femi, 'increasing': {'color': "Purple"}},
                gauge={
                    'axis': {'range': [0, popul_femi], 'tickwidth': 2, 'tickcolor': "#D70270"},
                    'bordercolor': "#D70270",
                    'bar': {'color': "#D70270"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'steps': [
                        {'range': [0, rebanho_femi], 'color': "#FFC0CB"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.7,
                        'value': rebanho_femi}}))
            fig1.update_layout(autosize=False,
                               height=120, margin=dict(b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 21})

            st.markdown(html_card_header_2A_1_13, unsafe_allow_html=True) # Vacinados do Sexo Feminino
            st.plotly_chart(fig1, use_container_width=True)

        with col7A:
            st.write("")

    with st.container():
        col1B, col2B, col3B = st.columns([50, 1100, 50])
        with col1B:
            st.write("")
        with col2B:
            df_new = df_selection.groupby(['sexo_paciente']).sum().reset_index()

            st.markdown(html_card_header_2A_1_20, unsafe_allow_html=True) # Sexo Biológico - Dados Agrupados
            st.dataframe(data=df_new)
        with col3B:
            st.write("")

    with st.container():
        col1B, col2B, col3B = st.columns([50, 1100, 50])
        with col1B:
            st.write("")
        with col2B:
            df_area = df_selection.groupby(['data_aplicacao_vacina']).sum().reset_index()

            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['MASCULINO'],
                name='Masculino',
                mode='lines',
                line=dict(width=1, color='#4169E1')))
            fig2.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['FEMININO'],
                name='Feminino',
                mode='lines',
                line=dict(width=1, color='#D70270')))
            fig2.update_layout(legend_font_size=12, autosize=False,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=200,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="h",
                                           yanchor="top",
                                           y=0.99,
                                           xanchor="left",
                                           x=0.05))
            fig2.update_xaxes(
                title_text='Dias da Aplicação da Vacina',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                rangeslider_visible=True)
            fig2.update_yaxes(
                title_text="Número de Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2A_1_30, unsafe_allow_html=True) # Variação de Vacinados
            st.plotly_chart(fig2, use_container_width=True)
        with col2B:
            st.write("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    return None

## 2.2 - Análise da Raça ou Cor:
def pacientes2( df_selection ):
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
            dados = df_selection.drop_duplicates(subset=['id_paciente'], keep="last")

            popul_branca = int(436722)
            popul_parda = int(50258)
            popul_preta = int(25568)
            popul_amarela = int(2686)
            popul_indigena = int(1239)
            vacinados_branca = int(dados['BRANCA'].sum())
            vacinados_parda = int(dados['PARDA'].sum())
            vacinados_preta = int(dados['PRETA'].sum())
            vacinados_amarela = int(dados['AMARELA'].sum())
            vacinados_indigena = int(dados['INDIGENA'].sum())
            vacinados_seminfo = int(dados['SEM INFORMACAO'].sum())

            raca_vacina = ['Branca', 'Parda', 'Preta', 'Amarela', 'Indigena', 'Sem Informação']

            y_popul = [popul_branca, popul_preta, popul_parda, popul_amarela, popul_indigena, 0]
            y_vacina = [vacinados_branca, vacinados_preta, vacinados_parda, vacinados_amarela, vacinados_indigena, vacinados_seminfo]

            fig1 = go.Figure()
            fig1.add_trace(go.Bar(name='População Residente (2010)', x=raca_vacina, y=y_popul,
                                  text=y_popul, textposition='outside',
                                  marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
            fig1.add_trace(go.Bar(name='População Vacinada', x=raca_vacina, y=y_vacina,
                                  text=y_vacina, textposition='outside',
                                  marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
            fig1.update_layout(legend_font_size=12, autosize=False,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=200,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="v",
                                           yanchor="top",
                                           y=0.95,
                                           xanchor="right",
                                           x=0.98),
                               barmode='group')
            fig1.update_xaxes(
                title_text='Raça ou Cor',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9))
            fig1.update_yaxes(
                title_text="Número de Residentes/Vacinados",
                title_font=dict(family='Sans-serif', size=9),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2B_2_11, unsafe_allow_html=True) # População Residente x População Vacinada
            st.plotly_chart(fig1, use_container_width=True)

        with col3A:
            st.write("")
        with col4A:
            df_new = df_selection.groupby(['raca_cor_paciente']).sum().reset_index()

            st.markdown(html_card_header_2B_2_12, unsafe_allow_html=True) # Raça/Cor - Dados Agrupados
            st.dataframe(data=df_new, height=200)
        with col5A:
            st.write("")

    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([50, 520, 60, 520, 50])
        with col1B:
            st.write("")
        with col2B:
            fig2 = go.Figure()
            fig2.add_trace(go.Violin(
                x=df_selection['raca_cor_paciente'][df_selection['sexo_paciente'] == 'Masculino'],
                y=df_selection["idade_paciente"][df_selection['sexo_paciente'] == 'Masculino'],
                legendgroup='Masculino', scalegroup='Masculino', name='Masculino',
                side='negative',
                meanline_visible=True,
                line_color='#4169E1',
                fillcolor='#4169E1'))
            fig2.add_trace(go.Violin(
                x=df_selection['raca_cor_paciente'][df_selection['sexo_paciente'] == 'Feminino'],
                y=df_selection["idade_paciente"][df_selection['sexo_paciente'] == 'Feminino'],
                legendgroup='Feminino', scalegroup='Feminino', name='Feminino',
                side='positive',
                meanline_visible=True,
                line_color='#D70270',
                fillcolor='#D70270'))
            fig2.update_layout(violingap=0, violinmode='overlay')
            fig2.update_layout(legend_font_size=12, autosize=False,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=200,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="h",
                                           yanchor="top",
                                           y=0.95,
                                           xanchor="right",
                                           x=0.99))
            fig2.update_xaxes(
                title_text='Raça/Cor',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9))
            fig2.update_yaxes(
                title_text="Idade dos Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=10, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2B_2_21, unsafe_allow_html=True) # Raça/Cor - Dados Agrupados
            st.plotly_chart(fig2, use_container_width=True)

        with col3B:
            st.write("")

        with col4B:
            df_area = df_selection.groupby(['data_aplicacao_vacina']).sum().reset_index()

            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['BRANCA'],
                name='BRANCA',
                mode='lines',
                line=dict(width=1, color='#4169E1'),
                stackgroup='one'))
            fig2.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['SEM INFORMACAO'],
                name='SEM INFORMACAO',
                mode='lines',
                line=dict(width=1, color='#D70270'),
                stackgroup='two'))
            fig2.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['INDIGENA'],
                name='INDIGENAS',
                mode='lines',
                line=dict(width=1, color='#00FFFF'),
                stackgroup='three'))
            fig2.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['PARDA'],
                name='PARDA',
                mode='lines',
                line=dict(width=1, color='#8A2BE2'),
                stackgroup='four'))
            fig2.update_layout(legend_font_size=10,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=200,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="v",
                                           yanchor="top",
                                           y=0.99,
                                           xanchor="left",
                                           x=0.05))
            fig2.update_xaxes(
                title_text='Dias da Aplicação da Vacina',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                rangeslider_visible=True)
            fig2.update_yaxes(
                title_text="Número de Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2B_2_22, unsafe_allow_html=True) # Raça/Cor - Dados Agrupados
            st.plotly_chart(fig2, use_container_width=True)

        with col5B:
            st.write("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    return None

## 2.3 - Análise da Idade:
def pacientes3( df_selection ):
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
            dados = df_selection

            dados1 = dados.drop_duplicates(subset=['id_paciente'], keep="last")
            df = dados1.groupby(['faixa_etaria']).sum().reset_index()

            values = ['menos 19 anos', '20 a 39 anos', '40 a 59 anos', '60 a 79 anos', 'mais 80 anos']
            y_pop = [132402, 191059, 133686, 51058, 8319]
            y_vac = [df['menos 19 anos'][4], df['20 a 39 anos'][0], df['40 a 59 anos'][1], df['60 a 79 anos'][2], df['mais 80 anos'][3]]

            fig1 = go.Figure()
            fig1.add_trace(go.Bar(name='População Residente (2010)',
                                  x=values, y=y_pop,
                                  text=y_pop, textposition='outside',
                                  marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
            fig1.add_trace(go.Bar(name='Vacinados',
                                  x=values, y=y_vac,
                                  text=y_vac, textposition='outside',
                                  marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
            fig1.update_layout(legend_font_size=12, autosize=False,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=200,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="v",
                                           yanchor="top",
                                           y=0.95,
                                           xanchor="right",
                                           x=0.98),
                               barmode='group')
            fig1.update_xaxes(
                title_text='Faixa Etária',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9))
            fig1.update_yaxes(
                title_text="Número de Residentes/Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2B_3_11, unsafe_allow_html=True) # Quantidade de Vacinados
            st.plotly_chart(fig1, use_container_width=True)
        with col3A:
            st.write("")
        with col4A:
            df_new2 = df_selection.groupby('faixa_etaria').sum().reset_index()

            st.markdown(html_card_header_2B_3_12, unsafe_allow_html=True) # Dados Agrupados
            st.dataframe(data=df_new2, height=200)

        with col5A:
            st.write("")

    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([50, 520, 60, 520, 50])
        with col1B:
            st.write("")
        with col2B:
            df = dados.groupby(['faixa_etaria']).sum().reset_index()

            values = ['menos 19 anos', '20 a 39 anos', '40 a 59 anos', '60 a 79 anos', 'mais 80 anos']

            y_1dose = [df['1DOSE'][4], df['1DOSE'][0], df['1DOSE'][1], df['1DOSE'][2], df['1DOSE'][3]]
            y_2dose = [df['2DOSE'][4], df['2DOSE'][0], df['2DOSE'][1], df['2DOSE'][2], df['2DOSE'][3]]
            y_Udose = [df['DOSE_UNI'][4], df['DOSE_UNI'][0], df['DOSE_UNI'][1], df['DOSE_UNI'][2], df['DOSE_UNI'][3]]
            y_Adose = [df['DOSE_ADC'][4], df['DOSE_ADC'][0], df['DOSE_ADC'][1], df['DOSE_ADC'][2], df['DOSE_ADC'][3]]

            df_area = dados.groupby(['data_aplicacao_vacina']).sum().reset_index()

            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['menos 19 anos'],
                name='menos 19 anos',
                mode='lines',
                line=dict(width=1, color='#4169E1'),
                stackgroup='one'))
            fig1.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['20 a 39 anos'],
                name='20 a 39 anos',
                mode='lines',
                line=dict(width=1, color='#D70270'),
                stackgroup='two'))
            fig1.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['40 a 59 anos'],
                name='40 a 59 anos',
                mode='lines',
                line=dict(width=1, color='#00FFFF'),
                stackgroup='three'))
            fig1.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['60 a 79 anos'],
                name='60 a 79 anos',
                mode='lines',
                line=dict(width=1, color='#8A2BE2'),
                stackgroup='four'))
            fig1.add_trace(go.Scatter(
                x=df_area['data_aplicacao_vacina'],
                y=df_area['mais 80 anos'],
                name='mais 80 anos',
                mode='lines',
                line=dict(width=1, color='#8A2BE2'),
                stackgroup='five'))
            fig1.update_layout(legend_font_size=10,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=200,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="v",
                                           yanchor="top",
                                           y=0.99,
                                           xanchor="left",
                                           x=0.01))
            fig1.update_xaxes(
                title_text='Dias da Aplicação da Vacina',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                rangeslider_visible=True)
            fig1.update_yaxes(
                title_text="Número de Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2B_3_21, unsafe_allow_html=True)
            st.plotly_chart(fig1, use_container_width=True)

        with col3B:
            st.write("")
        with col4B:
            fig2 = go.Figure()
            fig2.add_trace(go.Bar(name='1° Dose', x=values, y=y_1dose,
                                  text=y_1dose, textposition='auto',
                                  marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
            fig2.add_trace(go.Bar(name='2° Dose', x=values, y=y_2dose,
                                  text=y_2dose, textposition='auto',
                                  marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
            fig2.add_trace(go.Bar(name='Dose Única', x=values, y=y_Udose,
                                  text=y_Udose, textposition='auto',
                                  marker_color=['#4B0082', '#4B0082', '#4B0082', '#4B0082', '#4B0082']))
            fig2.add_trace(go.Bar(name='Dose Adicional', x=values, y=y_Adose,
                                  text=y_Adose, textposition='auto',
                                  marker_color=['#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF']))
            fig2.update_layout(legend_font_size=12, autosize=False,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=200,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="v",
                                           yanchor="top",
                                           y=0.95,
                                           xanchor="right",
                                           x=0.98),
                               barmode='group')
            fig2.update_xaxes(
                title_text='Faixa Etária',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9))
            fig2.update_yaxes(
                title_text="Doses Aplicadas",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2B_3_22, unsafe_allow_html=True)
            st.plotly_chart(fig2, use_container_width=True)
        with col5B:
            st.write("")

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""---""")
    st.write("")
    return None







