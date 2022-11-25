import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px

from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

from variaveis import *

# CARREGANDO OS DADOS:
@st.cache(allow_output_mutation=True)
def get_data_11( path11 ):
    df_11 = pd.read_csv( path11 , sep=";")
    return df_11

def get_data_12( path12 ):
    df_12 = pd.read_csv( path12, sep=";")
    return df_12

def get_data_13_1( path13_1 ):
    df_13_1 = pd.read_csv( path13_1, sep=";")
    return df_13_1
def get_data_13_2( path13_2 ):
    df_13_2 = pd.read_csv( path13_2, sep=";")
    return df_13_2

def get_data_14_1( path14_1 ):
    df_14_1 = pd.read_csv( path14_1, sep=";")
    return df_14_1
def get_data_14_2( path14_2 ):
    df_14_2 = pd.read_csv( path14_2, sep=";")
    return df_14_2
def get_data_14_3_1( path14_3_1 ):
    path14_3_1 = pd.read_csv( path14_3_1, sep=";")
    return path14_3_1
def get_data_14_3_2( path14_3_2 ):
    path14_3_2 = pd.read_csv( path14_3_2, sep=";")
    return path14_3_2
def get_data_14_3_3( path14_3_3 ):
    path14_3_3 = pd.read_csv( path14_3_3, sep=";")
    return path14_3_3
def get_data_14_3_4( path14_3_4 ):
    path14_3_4 = pd.read_csv( path14_3_4, sep=";")
    return path14_3_4

def get_data_15_1( path15_1 ):
    df_15_1 = pd.read_csv( path15_1, sep=";")
    return df_15_1
def get_data_15_2( path15_2 ):
    df_15_2 = pd.read_csv( path15_2, sep=";")
    return df_15_2



# CARREGANDO BASE DE DADOS PARA ALIMENTAÇÃO DOS GRÁFICOS
df_11 = get_data_11(path11) # DADOS AGRUPADOS PELA TIPO DE VACINA APLICADA
df_12 = get_data_12(path12) # DADOS AGRUPADOS PELA DIA DA VACINAÇÃO

df_13_1 = get_data_13_1(path13_1) # DADOS AGRUPADOS POR SEXO (PACIENTES UNICOS)
df_13_2 = get_data_13_2(path13_2) # DADOS AGRUPADOS POR SEXO (PACIENTES UNICOS)

df_14_1 = get_data_14_1(path14_1) # DADOS AGRUPADOS POR RAÇA/COR (PACIENTES UNICOS)
df_14_2 = get_data_14_2(path14_2) # DADOS AGRUPADOS POR RAÇA/COR (PACIENTES UNICOS)


df_15_1 = get_data_15_1(path15_1) # DADOS AGRUPADOS POR FAIXA ETARIA (PACIENTES UNICOS)
df_15_2 = get_data_15_2(path15_2) # DADOS AGRUPADOS POR FAIXA ETARIA (PACIENTES UNICOS)

# Introdução:

df_old = df_14_1
df_new = df_14_2


# - CAMPANHA DE VACINAÇÃO ------------------------------------------------------------------
## 1.1 - Número de Doses & Vacinas Aplicadas:

### AA1 - GRÁFICO VELOCIMETRO - Vacinados com 1° Dose
popul_residente = int(516524)
imun_rebanho = int(popul_residente * 0.75)
vacinados_1dose = int(df_11['1DOSE'].sum())

figAA1 = go.Figure()
figAA1.add_trace(go.Indicator(
    mode="gauge+number+delta",
    value=vacinados_1dose,
    domain={'x': [0, 1], 'y': [0, 1]},
    delta={'reference': imun_rebanho, 'increasing': {'color': "Purple"}},
    gauge={
        'axis': {'range': [0, popul_residente], 'tickwidth': 2, 'tickcolor': "#4169E1"},
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
figAA1.update_layout(autosize=True, height=120, margin=dict(l=20, r=20, b=20, t=30),
                   paper_bgcolor="#F8F8FF", font={'size': 20})

### AA2 - GRÁFICO PIZZA - Vacinados com 1° Dose
vacinados_1dose = int(df_11['1DOSE'].sum())
pop_sem_1dose = (popul_residente - vacinados_1dose)
labels = ['População com 1° Dose', "População sem 1° Dose:"]
colors = ['#4169E1', 'gray']

figAA2 = go.Figure(data=[go.Pie(labels=labels,
                              values=[vacinados_1dose, pop_sem_1dose],
                              textinfo='percent',
                              showlegend=False,
                              marker=dict(colors=colors,
                                          line=dict(color='#000010', width=2)))])
figAA2.update_traces(hole=.4, hoverinfo="label+percent+value")
figAA2.update_layout(autosize=True,
                   height=120, margin=dict(l=20, r=20, b=20, t=30),
                   paper_bgcolor="#F8F8FF", font={'size': 20})

### AB1 - GRÁFICO VELOCIMETRO - Vacinados com 2° Dose
popul_residente = int(516524)
imun_rebanho = int(popul_residente * 0.75)
vacinados_2dose = int(df_11['2DOSE'].sum() + df_11['DOSE_UNI'].sum())

figAB1 = go.Figure()
figAB1.add_trace(go.Indicator(
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
figAB1.update_layout(autosize=True,
                   height=120, margin=dict(l=20, r=20, b=20, t=30),
                   paper_bgcolor="#F8F8FF", font={'size': 20})


### AB2 - GRÁFICO PIZZA - Vacinados com 2° Dose
vacinados_2dose = int(df_11['2DOSE'].sum() + df_11['DOSE_UNI'].sum())
pop_sem_2dose = (popul_residente - vacinados_2dose)

labels = ['Vacinados Completamente', 'Vacinados Incompletamente']
colors = ['#D70270', 'gray']
figAB2 = go.Figure(data=[go.Pie(labels=labels,
                              values=[vacinados_2dose, pop_sem_2dose],
                              textinfo='percent', textfont_size=20,
                              showlegend=False,
                              marker=dict(colors=colors,
                                          line=dict(color=' #000010', width=2)))])
figAB2.update_traces(hole=.4, hoverinfo="label+percent+value")
figAB2.update_layout(autosize=True,
                   height=120, margin=dict(l=20, r=20, b=20, t=30),
                   paper_bgcolor="#F8F8FF", font={'size': 20})

### AC1 - GRÁFICO VELOCIMETRO - Vacinados com Dose Adicional
popul_residente = int(516524)
imun_rebanho = int(popul_residente * 0.75)
vacinados_adcdose = int(df_11['DOSE_ADC'].sum())

figAC1 = go.Figure()
figAC1.add_trace(go.Indicator(
    mode="gauge+number+delta",
    value=vacinados_adcdose,
    domain={'x': [0, 1], 'y': [0, 1]},
    delta={'reference': imun_rebanho, 'increasing': {'color': "Green"}},
    gauge={
        'axis': {'range': [0, 520000], 'tickwidth': 2, 'tickcolor': "#4B0082"},
        'bordercolor': "#4B0082",
        'bar': {'color': "#4B0082"},
        'bgcolor': "lightgray",
        'borderwidth': 2,
        'steps': [
            {'range': [0, imun_rebanho], 'color': "#ecd9ec"}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.7,
            'value': imun_rebanho}}))
figAC1.update_layout(autosize=True, height=120, margin=dict(l=20, r=20, b=20, t=30),
                   paper_bgcolor="#F8F8FF", font={'size': 20})


### AC2 - GRÁFICO PIZZA - Vacinados com Dose Adicional
vacinados_adcdose = int(df_11['DOSE_ADC'].sum())
pop_sem_adcdose = (popul_residente - vacinados_adcdose)
labels = ['Vacinados Completamente', 'Vacinados Incompletamente']
colors = ['#D70270', 'gray']

figAC2 = go.Figure(data=[go.Pie(labels=labels,
                              values=[vacinados_adcdose, pop_sem_adcdose],
                              textinfo='percent', textfont_size=20,
                              showlegend=False,
                              marker=dict(colors=colors,
                                          line=dict(color=' #000010', width=2)))])
figAC2.update_traces(hole=.4, hoverinfo="label+percent+value")
figAC2.update_layout(autosize=True,
                   height=120, margin=dict(l=20, r=20, b=20, t=30),
                   paper_bgcolor="#F8F8FF", font={'size': 20})

### AD0 - GRÁFICO DE BARRA VERTICAL - Quantidade de Vacinas Aplicadas por Dose
values = ['1° Dose', '2° Dose', 'Dose Única', 'Dose Adicional']
y_PFIZER = [df_11['1DOSE'][2], df_11['2DOSE'][2], df_11['DOSE_UNI'][2], df_11['DOSE_ADC'][2]]
y_ASTRAZENECA_FIOCRUZ = [df_11['1DOSE'][0], df_11['2DOSE'][0], df_11['DOSE_UNI'][0], df_11['DOSE_ADC'][0]]
y_SINOVAC_BUTANTAN = [df_11['1DOSE'][3], df_11['2DOSE'][3], df_11['DOSE_UNI'][3], df_11['DOSE_ADC'][3]]
y_JANSSEN = [df_11['1DOSE'][1], df_11['2DOSE'][1], df_11['DOSE_UNI'][1], df_11['DOSE_ADC'][1]]

figAD0 = go.Figure()
figAD0.add_trace(go.Bar(
    name='Pfizer', x=values, y=y_PFIZER,
    hovertemplate ="<br>Aplicação: %{x} </br>Vacinados: %{y}",
    textposition='none', marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
figAD0.add_trace(go.Bar(
    name='AstraZeneca/Fiocruz', x=values, y=y_ASTRAZENECA_FIOCRUZ,
    hovertemplate="<br>Aplicação: %{x} </br>Vacinados: %{y}",
    textposition='none', marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
figAD0.add_trace(go.Bar(
    name='Sinovac/Butantan', x=values, y=y_SINOVAC_BUTANTAN,
    hovertemplate="<br>Aplicação: %{x} </br>Vacinados: %{y}",
    textposition='none', marker_color=['#4B0082', '#4B0082', '#4B0082', '#4B0082', '#4B0082']))
figAD0.add_trace(go.Bar(
    name='Janssen', x=values, y=y_JANSSEN,
    hovertemplate="<Aplicação: %{x} </br>N° Vacinados: %{y}",
    textposition='none', marker_color=['#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF']))
figAD0.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=11, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=200, barmode='group', margin=dict(l=1, r=1, b=1, t=1), autosize=True)
figAD0.update_yaxes(
    title_text="Número de Vacinados",title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')


### AE1 - GRÁFICO DE FUNIL - Proporção entre as Vacinas Aplicadas
y_PFIZER = int(df_11['TOTAL_DOSES'][2])
y_ASTRAZENECA_FIOCRUZ = int(df_11['TOTAL_DOSES'][0])
y_SINOVAC_BUTANTAN = int(df_11['TOTAL_DOSES'][3])
y_JANSSEN = int(df_11['TOTAL_DOSES'][1])
values = ["Pfizer", "AstraZeneca/Fiocruz", "Sinovac/Butantan", "Janssen", ]
y = [y_PFIZER, y_ASTRAZENECA_FIOCRUZ, y_SINOVAC_BUTANTAN, y_JANSSEN, ]

figAE1 = go.Figure()
figAE1.add_trace(go.Funnel(
    y=values, x=y, textposition="inside", textinfo="percent total",
    marker={"color": ["#D70270", "#4169E1", "#8A2BE2", "#00FFFF", "#ADFF2F"],
            "line": {"width": [2, 2, 2, 2, 2, 2],
                     "color": ["black", "black", "black", "black", "black"]}},
    connector={"line": {"color": "black", "dash": "solid", "width": 2}}))
figAE1.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    height=200, margin=dict(l=1, r=1, b=1, t=1))

### AE2 - GRÁFICO DE BARRA - Grupo Atendimento Vacinado por Dose

values = ['Pfizer', 'AstraZeneca/Fiocruz', 'Sinovac/Butantan', 'Jansen']
y_1dose = [df_11['1DOSE'][2], df_11['1DOSE'][0], df_11['1DOSE'][3], df_11['1DOSE'][1]]
y_2dose = [df_11['2DOSE'][2], df_11['2DOSE'][0], df_11['2DOSE'][3], df_11['2DOSE'][1]]
y_Udose = [df_11['DOSE_UNI'][2], df_11['DOSE_UNI'][0], df_11['DOSE_UNI'][3], df_11['DOSE_UNI'][1]]
y_Adose = [df_11['DOSE_ADC'][2], df_11['DOSE_ADC'][0], df_11['DOSE_ADC'][3], df_11['DOSE_ADC'][1]]

figAE2 = go.Figure()
figAE2.add_trace(go.Bar(
    name='Dose Adicional', x=values, y=y_Adose,
    hovertemplate="<Aplicação: %{x} </br>N° Vacinados: %{y}",
    textposition='none', marker_color=['#4B0082', '#4B0082', '#4B0082', '#4B0082', '#4B0082']))
figAE2.add_trace(go.Bar(
    name='Dose Única', x=values, y=y_Udose,
    hovertemplate="<br>Aplicação: %{x} </br>Vacinados: %{y}",
    textposition='none', marker_color=['#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF']))
figAE2.add_trace(go.Bar(
    name='2° Dose', x=values, y=y_2dose,
    hovertemplate="<br>Aplicação: %{x} </br>Vacinados: %{y}",
    textposition='none', marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
figAE2.add_trace(go.Bar(
    name='1° Dose', x=values, y=y_1dose,
    hovertemplate="<br>Aplicação: %{x} </br>Vacinados: %{y}",
    textposition='none', marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
figAE2.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=11, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=200, barmode='stack', margin=dict(l=1, r=1, b=1, t=1), autosize=True)
figAE2.update_yaxes(
    title_text="Número de Vacinados",title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')


### AF0 -
df_AF_1 = df_11
df_AF_2 = df_11
df_AF_3 = df_11

## 1.2 - Variação das Doses & Vacinas Aplicadas
### BA0 - GRÁFICO DE LINHA (4) - Variação diária de DOSES aplicadas:
df_12['data_aplicacao_vacina'].replace("1993-11-08", "2021-11-08", inplace=True)

figBA0 = go.Figure()
figBA0.add_trace(go.Scatter(
    x=df_12['data_aplicacao_vacina'], y=df_12['1DOSE'],
    name='1° Dose', mode='lines', line=dict(width=1, color='#4169E1'), stackgroup='one'))
figBA0.add_trace(go.Scatter(
    x=df_12['data_aplicacao_vacina'], y=df_12['2DOSE'],
    name='2° Dose', mode='lines', hovertemplate=None, line=dict(width=1, color='#D70270'), stackgroup='two'))
figBA0.add_trace(go.Scatter(
    x=df_12['data_aplicacao_vacina'], y=df_12['DOSE_UNI'],
    name='Dose Única', mode='lines', hovertemplate=None, line=dict(width=1, color='#00FFFF'), stackgroup='three'))
figBA0.add_trace(go.Scatter(
    x=df_12['data_aplicacao_vacina'], y=df_12['DOSE_ADC'],
    name='Dose Adicional', mode='lines', hovertemplate=None, line=dict(width=1, color='#8A2BE2'), stackgroup='four'))
figBA0.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=12, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=220, hovermode="x unified", margin=dict(l=1, r=1, b=1, t=1))
figBA0.update_xaxes(
    rangeslider_visible=True)
figBA0.update_yaxes(
    title_text="Número de Vacinados", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

###-------------------------------------------------------------------
### BB0 - GRÁFICO DE LINHA (4) - Variação diária de VACINAS aplicadas:
figBB0 = go.Figure()
figBB0.add_trace(go.Scatter(
    x=df_12['data_aplicacao_vacina'], y=df_12['ASTRAZENECA_FIOCRUZ'], name='ASTRAZENECA/FIOCRUZ',
    mode='lines', hovertemplate=None, line=dict(width=1, color='#D70270'), stackgroup='one'))
figBB0.add_trace(go.Scatter(
    x=df_12['data_aplicacao_vacina'], y=df_12['PFIZER'],
    name='PFIZER', mode='lines', hovertemplate=None, line=dict(width=1, color='#4169E1'), stackgroup='two'))
figBB0.add_trace(go.Scatter(
    x=df_12['data_aplicacao_vacina'], y=df_12['SINOVAC_BUTANTAN'],
    name='SINOVAC/BUTANTAN', mode='lines', hovertemplate=None, line=dict(width=1, color='#8A2BE2'), stackgroup='four'))
figBB0.add_trace(go.Scatter(
    x=df_12['data_aplicacao_vacina'], y=df_12['JANSSEN'],
    name='JANSSEN', mode='lines', hovertemplate=None, line=dict(width=1, color='#00FFFF'), stackgroup='five'))
figBB0.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    height=220, hovermode="x unified", margin=dict(l=1, r=1, b=1, t=1),
    legend=dict(font_size=8, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5))
figBB0.update_xaxes(
    rangeslider_visible=True)
figBB0.update_yaxes(
    title_text="Número de Vacinados", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')


### BC0 -

df_BC_0 = df_12

###-----------------------------------------------------------------------------
### BD0 - GRÁFICO DE LINHA (4) - Variação diária de Grupo Atendimento vacinado:



## 1.3 -  Grupo Atendimento da Vacinação:

# - CARACTERISTICAS DOS PACIENTES -----------------------------------------------------------
## 2.1 - Análise do Sexo Biológico:

### CA1_1 - GRÁFICO VELOCIMETRO - Vacinados do Sexo Masculino
df_selection1 = df_13_1

popul_masc = int(247931)
rebanho_masc = int(185948)
vacinados_masc = int(df_13_1['MASCULINO'].sum())

fig_CA1_1 = go.Figure()
fig_CA1_1.add_trace(go.Indicator(
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
fig_CA1_1.update_layout(
    paper_bgcolor="#F8F8FF", font={'size': 20},
    height=120, autosize=True, margin=dict(l=20, r=20, b=20, t=30))


### CA_20 - GRÁFICO DE PIZZA - Proporção entre os Sexos
vacinados_femi = int(df_13_1['FEMININO'].sum())
vacinados_masc = int(df_13_1['MASCULINO'].sum())
labels1 = ['Sexo Feminino', 'Sexo Masculino']
colors1 = ['#D70270', '#4169E1']  # magenta , royalblue

fig_CA_20 = go.Figure(data=[go.Pie(labels=labels1, values=[vacinados_femi, vacinados_masc],
                              textinfo='percent', textfont_size=20, showlegend=False,
                              marker=dict(colors=colors1, line=dict(color='black', width=3)))])
fig_CA_20.update_traces(hole=.4, hoverinfo="label+percent+value")
fig_CA_20.update_layout(autosize=True, height=120, margin=dict(l=20, r=20, b=20, t=30),
                        paper_bgcolor="#F8F8FF", font={'size': 20})


### CA_30 - GRAFICO VELOCIMETRO - Vacinados do Sexo Feminino
popul_femi = int(268592)
rebanho_femi = int(201444)
vacinados_femi = int(df_13_1['FEMININO'].sum())

fig_CA_30 = go.Figure()
fig_CA_30.add_trace(go.Indicator(
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
fig_CA_30.update_layout(autosize=True,
                   height=120, margin=dict(b=20, t=30),
                   paper_bgcolor="#F8F8FF", font={'size': 21})

### CB_01 - TABELA DE DADOS AGRUPADOS
df_13_1 = df_13_1.drop(columns=['Unnamed: 0'])
df_CB_01 = df_13_1
### CB_02 - TABELA DE DADOS AGRUPADOS
df_13_2 = df_13_2.drop(columns=['Unnamed: 0'])
df_CB_02 = df_13_2

### CC_10 - GRAFICO DE LINHA - Variação de Vacinados
df_area = df_12

fig_CC_10 = go.Figure()
fig_CC_10.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['MASCULINO'], name='Masculino',
    mode='lines', hovertemplate=None, line=dict(width=1, color='#4169E1')))
fig_CC_10.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['FEMININO'], name='Feminino',
    mode='lines', hovertemplate=None, line=dict(width=1, color='#D70270')))
fig_CC_10.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=12, orientation="h", yanchor="top", y=1.2, xanchor="center", x=0.5),
    height=200, hovermode="x unified", autosize=True, margin=dict(l=1, r=1, b=1, t=1))
fig_CC_10.update_xaxes(
    rangeslider_visible=True)
fig_CC_10.update_yaxes(
    title_text="Número de Vacinados", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

### CC_20 - GRAFICO DE LINHA - Variação de Vacinados

values = ['Masculino', 'Feminino']
y_1dose = [df_13_2['1DOSE'][1], df_13_2['1DOSE'][0]]
y_2dose = [df_13_2['2DOSE'][1], df_13_2['2DOSE'][0]]
y_Udose = [df_13_2['DOSE_UNI'][1], df_13_2['DOSE_UNI'][0]]
y_Adose = [df_13_2['DOSE_ADC'][1], df_13_2['DOSE_ADC'][0]]

fig_CC_20 = go.Figure()
fig_CC_20.add_trace(go.Bar(
    x=values, y=y_1dose, name='1° Dose', hovertemplate="<br>Sexo: %{x} </br>Vacinados: %{y}",
    textposition='none', marker_color=['#4169E1', '#4169E1']))
fig_CC_20.add_trace(go.Bar(
    x=values, y=y_2dose, name='2° Dose', hovertemplate ="<br>Sexo: %{x} </br>Vacinados: %{y}",
    textposition='auto', marker_color=['#D70270', '#D70270']))
fig_CC_20.add_trace(go.Bar(
    x=values, y=y_Udose, name='Dose Única', hovertemplate ="<br>Sexo: %{x} </br>Vacinados: %{y}",
    textposition='auto', marker_color=['#4B0082', '#4B0082']))
fig_CC_20.add_trace(go.Bar(
    x=values, y=y_Adose, name='Dose Adicional', hovertemplate ="<br>Sexo: %{x} </br>Vacinados: %{y}",
    textposition='auto', marker_color=['#00FFFF', '#00FFFF']))
fig_CC_20.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=12, orientation="h", yanchor="top", y=1.2, xanchor="center", x=0.5),
    barmode='group', height=200, autosize=True, margin=dict(l=1, r=1, b=1, t=1))
fig_CC_20.update_yaxes(
    title_text="Doses Aplicadas", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')



## 2.2 - Análise da Raça ou Cor:
### DA_1 - GRÁFICO DE BARRA -
dados = df_14_1

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
y_vacina = [vacinados_branca, vacinados_preta, vacinados_parda, vacinados_amarela, vacinados_indigena,  vacinados_seminfo]

fig_DA_1 = go.Figure()
fig_DA_1.add_trace(go.Bar(
    name='População Residente (2010)', x=raca_vacina, y=y_popul, hovertemplate ="<br>Cor / Raça: %{x} </br>Vacinados: %{y}",
    textposition='none', marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
fig_DA_1.add_trace(go.Bar(
    name='População Vacinada', x=raca_vacina, y=y_vacina, hovertemplate ="<br>Cor / Raça: %{x} </br>Vacinados: %{y}",
    textposition='none', marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
fig_DA_1.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    height=200, barmode='group', margin=dict(l=1, r=1, b=1, t=1), autosize=True,
    legend=dict(font_size=12, orientation="h", yanchor="top", y=1.2, xanchor="center", x=0.5))
fig_DA_1.update_yaxes(
    title_text="Número de Residentes/Vacinados", title_font=dict(family='Sans-serif', size=9),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

### DA_2 - TABELA DADOS AGRUPOADOS -
df_DA_2 = df_14_2

### DB_1 - GRÁFICO DE VIOLINO -
values = ['Sem informação', 'Branca', 'Parda', 'Preta', 'Amarela', 'Indígena']
y_1dose = (df_14_2.loc[1, "1DOSE"], df_14_2.loc[0, "1DOSE"], df_14_2.loc[2, "1DOSE"],
           df_14_2.loc[3, "1DOSE"], df_14_2.loc[4, "1DOSE"], df_14_2.loc[5, "1DOSE"])
y_2dose = (df_14_2.loc[1, "2DOSE"], df_14_2.loc[0, "2DOSE"], df_14_2.loc[2, "2DOSE"],
           df_14_2.loc[3, "2DOSE"], df_14_2.loc[4, "2DOSE"], df_14_2.loc[5, "2DOSE"])
y_Udose = (df_14_2.loc[1, "DOSE_UNI"], df_14_2.loc[0, "DOSE_UNI"], df_14_2.loc[2, "DOSE_UNI"],
           df_14_2.loc[3, "DOSE_UNI"], df_14_2.loc[4, "DOSE_UNI"], df_14_2.loc[5, "DOSE_UNI"])
y_Adose = (df_14_2.loc[1, "DOSE_ADC"], df_14_2.loc[0, "DOSE_ADC"], df_14_2.loc[2, "DOSE_ADC"],
           df_14_2.loc[3, "DOSE_ADC"], df_14_2.loc[4, "DOSE_ADC"], df_14_2.loc[5, "DOSE_ADC"])

fig_DB_1 = go.Figure()
fig_DB_1.add_trace(go.Bar(
    x=values, y=y_1dose, text=y_1dose, name='1° Dose', hovertemplate="1° Dose: <br>%{y}</br> %{x}",
    textposition='none', marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
fig_DB_1.add_trace(go.Bar(
    x=values, y=y_2dose, text=y_2dose, name='2° Dose', hovertemplate ="2° Dose: <br>%{y} </br> %{x}",
    textposition='none', marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
fig_DB_1.add_trace(go.Bar(
    x=values, y=y_Udose, text=y_Udose, name='Dose Única', hovertemplate ="Dose Única: <br>%{y} </br> %{x}",
    textposition='none', marker_color=['#4B0082', '#4B0082', '#4B0082', '#4B0082', '#4B0082', '#4B0082']))
fig_DB_1.add_trace(go.Bar(
    x=values, y=y_Adose, text=y_Adose, name='Dose Adicional', hovertemplate ="Dose Adicional:<br> %{y}</br> %{x}",
    textposition='none', marker_color=['#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF']))
fig_DB_1.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=12, orientation="h", yanchor="top", y=1.2, xanchor="center", x=0.5),
    barmode='group', height=200, autosize=True, margin=dict(l=1, r=1, b=1, t=1))
fig_DB_1.update_yaxes(
    title_text="Doses Aplicadas", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')



### DB_1
df_area = df_12

fig_DB_2 = go.Figure()
fig_DB_2.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['BRANCA'], name='BRANCA',
    mode='lines', stackgroup='one', hovertemplate=None, line=dict(width=1, color='#4169E1')))
fig_DB_2.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['SEM INFORMACAO'], name='SEM INFORMACAO',
    mode='lines', stackgroup='two', hovertemplate=None, line=dict(width=1, color='#D70270')))
fig_DB_2.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['INDIGENA'], name='INDIGENAS',
    mode='lines', stackgroup='three', hovertemplate=None, line=dict(width=1, color='#00FFFF')))
fig_DB_2.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['PARDA'], name='PARDA',
    mode='lines', stackgroup='four', hovertemplate=None, line=dict(width=1, color='#8A2BE2')))
fig_DB_2.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=10, orientation="h", yanchor="top", y=1.25, xanchor="center", x=0.5),
    height=200, hovermode="x unified", margin=dict(l=1, r=1, b=1, t=1))
fig_DB_2.update_xaxes(
    rangeslider_visible=True)
fig_DB_2.update_yaxes(
    title_text="Número de Vacinados", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')




## 2.3 - Análise da Idade:
### EA_1 - GRÁFICO DE BARRA - População residente x População vacinada

df = df_15_1

values = ['menos 19 anos', '20 a 39 anos', '40 a 59 anos', '60 a 79 anos', 'mais 80 anos']
y_pop = [132402, 191059, 133686, 51058, 8319] # DADOS RETIRADOS DO CENSO DE 2010 IBGE
y_vac = [df['menos 19 anos'][4], df['20 a 39 anos'][0], df['40 a 59 anos'][1], df['60 a 79 anos'][2], df['mais 80 anos'][3]]

fig_EA_1 = go.Figure()
fig_EA_1.add_trace(go.Bar(
    x=values, y=y_pop, name='População residente (2010)', hovertemplate ="<br>Faixa Etária: %{x} </br>N° Vacinados: %{y}",
    textposition='none', marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
fig_EA_1.add_trace(go.Bar(
    x=values, y=y_vac, name='População vacinada', hovertemplate ="<br>Faixa Etária: %{x} </br>N° Vacinados: %{y}",
    textposition='none', marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
fig_EA_1.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=14, orientation="h", yanchor="top", y=1.22, xanchor="center", x=0.44),
    height=200, barmode='group', margin=dict(l=1, r=1, b=1, t=1), autosize=True)
fig_EA_1.update_yaxes(
    title_text="Número de Residentes/Vacinados", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')


### EA_2 - TABELA DADOS AGRUPADOS - Dados Agrupados:
df_EA_2 = df_15_2


### EB_1 - GRÁFICO DE LINHA - Variação de Vacinados:
df_area = df_12

fig_EB_1 = go.Figure()
fig_EB_1.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['menos 19 anos'], name='menos 19 anos',
    mode='lines', hovertemplate=None, line=dict(width=1, color='#4169E1'), stackgroup='one'))
fig_EB_1.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['20 a 39 anos'], name='20 a 39 anos',
    mode='lines', hovertemplate=None, line=dict(width=1, color='#D70270'), stackgroup='two'))
fig_EB_1.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['40 a 59 anos'],name='40 a 59 anos',
    mode='lines', hovertemplate=None, line=dict(width=1, color='#00FFFF'), stackgroup='three'))
fig_EB_1.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['60 a 79 anos'], name='60 a 79 anos',
    mode='lines', hovertemplate=None, line=dict(width=1, color='#8A2BE2'), stackgroup='four'))
fig_EB_1.add_trace(go.Scatter(
    x=df_area['data_aplicacao_vacina'], y=df_area['mais 80 anos'], name='mais 80 anos',
    mode='lines', hovertemplate=None, line=dict(width=1, color='#8A2BE2'), stackgroup='five'))
fig_EB_1.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=10, orientation="h", yanchor="top", y=1.2, xanchor="center", x=0.5),
    height=200, hovermode="x unified", margin=dict(l=1, r=1, b=1, t=1))
fig_EB_1.update_xaxes(
    rangeslider_visible=True)
fig_EB_1.update_yaxes(
    title_text="Número de Vacinados", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')


### EB_2 - GRÁFICO DE BARRA - Companha de Vacinação:
df = df_15_2

values = ['menos 19 anos', '20 a 39 anos', '40 a 59 anos', '60 a 79 anos', 'mais 80 anos']
y_1dose = [df['1DOSE'][4], df['1DOSE'][0], df['1DOSE'][1], df['1DOSE'][2], df['1DOSE'][3]]
y_2dose = [df['2DOSE'][4], df['2DOSE'][0], df['2DOSE'][1], df['2DOSE'][2], df['2DOSE'][3]]
y_Udose = [df['DOSE_UNI'][4], df['DOSE_UNI'][0], df['DOSE_UNI'][1], df['DOSE_UNI'][2], df['DOSE_UNI'][3]]
y_Adose = [df['DOSE_ADC'][4], df['DOSE_ADC'][0], df['DOSE_ADC'][1], df['DOSE_ADC'][2], df['DOSE_ADC'][3]]

fig_EB_2 = go.Figure()
fig_EB_2.add_trace(go.Bar(
    x=values, y=y_1dose, name='1° Dose', hovertemplate ="<br>Faixa Etária: %{x} </br>N° Vacinados: %{y}",
    textposition='none', marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
fig_EB_2.add_trace(go.Bar(
    x=values, y=y_2dose, name='2° Dose', hovertemplate ="<br>Faixa Etária: %{x} </br>N° Vacinados: %{y}",
    textposition='none', marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
fig_EB_2.add_trace(go.Bar(
    x=values, y=y_Udose, name='Dose Única', hovertemplate ="<br>Faixa Etária: %{x} </br>N° Vacinados: %{y}",
    textposition='none', marker_color=['#4B0082', '#4B0082', '#4B0082', '#4B0082', '#4B0082']))
fig_EB_2.add_trace(go.Bar(
    x=values, y=y_Adose, name='Dose Adicional', hovertemplate ="<br>Faixa Etária: %{x} </br>N° Vacinados: %{y}",
    textposition='none', marker_color=['#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF']))
fig_EB_2.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=12, orientation="h", yanchor="top", y=1.15, xanchor="center", x=0.5),
    barmode='group', height=200, autosize=True, margin=dict(l=1, r=1, b=1, t=1))
fig_EB_2.update_yaxes(
    title_text="Doses Aplicadas", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')





# - POSTOS DE VACINAÇÃO ---------------------------------------------------------------------


def tabela_aggrid(df, enabled, height):
    gd = GridOptionsBuilder.from_dataframe(df)

    gd.configure_pagination(enabled=enabled)
    #gd.configure_selection(use_checkbox=True, selection_mode='multiple')
    gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
    gd.configure_side_bar()
    gridOptions = gd.build()

    df = AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=True,
                height=height, width='100%', editable=True)

    return df