from PIL import Image

# CAMINHO PARA OS DADOS ----------------------------------------------------------------
path1 = "vacina_floripa_limpo.csv"
path2 = "vacina_floripa_pre_limpeza.csv"


path11 = "df_11ABCDEF.csv"
path12 = "df_12GHI.csv"

# - TOPO E RODAPÉ ------------------------------------------------------------------------
html_title="""
<h1 style="font-size:300%; color:#4169e1; font-family:sans-serif;
            text-align:center; ">Explorador de Dados Abertos</h1>
<h3 style="font-size:180%; color:#4169e1;font-family:sans-serif;
            text-align:center; ">Campanha de Vacinação Contra COVID-19 - Florianópolis-SC</h3>
<hr style= "display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
  <p style="color:Gainsboro; text-align: center;">Última atualização: 24/07/2022</p>
"""
html_rodape="""
<hr style= "display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
  <p style="color:Gainsboro; text-align: center;">By: mateus7ortiz@gmail.com</p>
"""

# - OVERVIEW -----------------------------------------------------------------------------
## Overview A:
html_header_0_10="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; 
                                  text-align: center; padding: 10px 0; font-size:200%;"
                                  >Overview dos Dados</h2>
  </div>
</div>
"""

html_subheader_0_30="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 0px; padding-left: 15px;
                                  font-size:150%;" >Explore está Aplicação Web</h3>
  </div>
</div>
"""

html_card_header_0A_1_11="""
<div class="card">
  <div class="card-body" style="border-radius: 25px 25px 0px 0px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 5px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;  
                                width: 100%;height: 40px;">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; 
                                    padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;  
                                    text-align: center; font-size:130%;" 
                                    >Apresentando a Aplicação</h4>
  </div>
</div>
<div class="card" style="border-radius: 0px 0px 20px 20px; background: #F5F5F5; 
                         border:solid; border-color: black; border-width: 0px 1px 1px 1px;
                         padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;  
                         width: 100%; height: 200px;">
    <p class="card-title" style="background-color:#F5F5F5; color:#0d0d0d;font-family:sans-serif; 
                                  text-align: justify; font-size: 100%; padding-top: 10px; padding-bottom: 1px;"
                                  >Nesta Aplicação exploraremos os dados da Campanha de Vacinação Contra
                                  COVID-19, focada nos moradores de Florianópolis-SC. Ao longo da exploração será possível 
                                   análisar os diferentes tipos de variaveis, como as quantidades de cada vacinas e doses aplicada, 
                                   podendo ser segmentar por cacteristicas dos pacientes e visualizados ao longo do tempo<br> 
                                   </p>
</div>"""
html_card_header_0A_1_21="""
<div class="card">
  <div class="card-body" style="border-radius: 25px 25px 0px 0px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 5px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;  
                                width: 100%; height: 40px;">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; 
                                text-align: center;  font-size: 130%;
                                padding-top: 5px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;"  
                                >Descrição dos Dados</h4>
  </div>
</div>
<div class="card" style="border-radius: 0px 0px 25px 25px; background: #F5F5F5;  
                                border:solid; border-color: black; border-width: 0px 1px 1px 1px;
                         padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;  
                         width: 100%; height: 200px;">
    <p class="card-title" style="background-color:#F5F5F5; color:#0d0d0d; font-family:sans-serif; 
                                  text-align: justify; font-size: 80%; padding-top: 10px; padding-bottom: 1px;"
                                  >Está Aplicação é focada nos dados da Campanha de Vacinação Contra COVID-19,
                                  para melhor compeenção sobre o tema e desenvolvimento dos gráficos e tabelas 
                                  também foi utilizado dados do Censo IBGE 2010 e dados do diretorio brasileiro de municipios.<br>
                                   Os links para todos os dados utilizados, assim como o projeto da aplicação completo, 
                                   está disponível ao lado.</p>
</div>"""
html_card_header_0A_1_22="""
<div class="card">
  <div class="card-body" style="border-radius: 25px 25px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 5px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;  
                                width: 100%; height: 40px;">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; 
                                  padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;  
                                    text-align: center; font-size:130%;"
                                    >Links importantes</h4>
  </div>
</div>  
<div class="card" style="border-radius: 0px 0px 25px 25px; background: #F5F5F5;  
                         border:solid; border-color: black; border-width: 0px 1px 1px 1px;
                         padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;  
                         width: 100%; height: 200px;">
    <br>
    <a href="https://github.com/MateusOF5512/TesteHeroku"
    style="background-color:#F5F5F5; color:#0d0d0d; font-family:sans-serif; font-size:90%;"
    >🎲 Código Aberto no Github</a><br>
    <a href="https://cidades.ibge.gov.br/brasil/sc/florianopolis/pesquisa/23/24304?indicador=29455"
    style="background-color:#F5F5F5; color:#0d0d0d; font-family:sans-serif; font-size:90%;"
    >🎲 Dados sobre o CENSO IBGE 2010</a><br>
    <a href="https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao"
    style="background-color:#F5F5F5; color:#0d0d0d; font-family:sans-serif; font-size:90%;"
    >🎲 Dados sobre a Campanha de Vacinação Contra Covid-19 - Original</a><br>
    <a href="https://basedosdados.org/dataset/br-ms-vacinacao-covid19?bdm_table=microdados"
    style="background-color:#F5F5F5; color:#0d0d0d; font-family:sans-serif; font-size:90%;"
    >🎲 Dados sobre a Campanha de Vacinação Contra Covid-19 - Base dos Dados</a><br>
</div>"""

## Overview B:
html_subheader_0_20="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 0px; padding-left: 15px;
                                  font-size:150%;" >🔬  Extração e Tratamento dos Dados  🎲</h3>
  </div>
</div>
"""
html_card_header_0B_1_10="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 5px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; 
                                    text-align: center; padding-top: 5px; ; padding-bottom: 3px;
                                    font-size:100%;" >Extração dos Dados</h4>
  </div>
</div>
<div class="card" style="border-radius: 0px 0px 10px 10px; background: #F5F5F5; 
                         border:solid; border-color: black; border-width: 0px 1px 1px 1px;
                         width: 100%; height: 200px;
                         padding-top: 5px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px;">
    <p class="card-title" style="background-color:#F5F5F5; color:#0d0d0d;
                                  font-family:sans-serif; text-align: justify;
                                  font-size: 90%" >Os Dados foram obtidos no site "Base dos Dados", 
                                  que  é uma organização não-governamental, sem fins lucrativos, open source e colaborativa, 
                                  que dísponibiliza em seu site diversas tabelas de dados dos mais diversos temas,
                                  sendo a forma mais eficiente de utilizar tais informações, o governo Federal 
                                  disponibiliza os dados mas em em 3 tabelas e quase 2GB.</p>
</div>"""

html_body_0B_20="""
<div class="card" style="border-radius: 25px 25px 25px 25px; background: #F5F5F5;   
                         border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                         width: 100%; height: 100px;
                         padding-top: 15px; padding-left: 15px; padding-right:15px;">
    <p class="card-title" style="background-color:#F5F5F5; color:#0d0d0d; font-family:sans-serif; 
                                  text-align: justify; font-size: 100%;"
                                  >Aqui falareos sobre limpeza e tratamento dos dados
                                  </p>
</div>"""

html_card_header_0B_3_31="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1; width: 100%;   
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 5px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                height: 40px;">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; 
                                    text-align: center; padding-top: 5px; ; padding-bottom: 3px;
                                    font-size:100%;" >Dados antes do Tratamento</h4>
  </div>
</div>
"""
html_card_header_0B_3_32="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1; width: 100%;
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 5px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                height: 40px;">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; 
                                    text-align: center; padding-top: 5px; ; padding-bottom: 3px;
                                    font-size:100%;" >Dados depois do Tratamento</h4>
  </div>
</div>
"""


## Overview C:
html_subheader_0C_1="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px;
                                  font-size:150%;" >💉  Análise das Variáveis  👩</h3>
  </div>
</div>
"""
html_body_0C_20="""
<div class="card" style="border-radius: 25px 25px 25px 25px; background: #F5F5F5;  
                         border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                         width: 100%; height: 100px;
                         padding-top: 15px; padding-left: 15px; padding-right:15px">
    <p class="card-title" style="background-color:#F5F5F5; color:#0d0d0d; font-family:sans-serif; 
                                  text-align: justify; font-size: 100%;"
                                  >Nesta seção é possível análisar as colunas dos dados, podendo identificar 
                                  seu tipo, quantidade total, quantidade de valores unicos,de valores faltando,
                                  </p>
</div>
"""
html_card_header_0C_2_11="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 90%;" 
                                  >Identificador Único dos Pacientes (id_paciente)</h5>
  </div>
</div>
"""
html_card_header_0C_2_12="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 90%;" 
                                  >Idade dos Pacientes (idade_paciente)</h5>
  </div>
</div>
"""
html_card_header_0C_2_21="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 90%;" 
                                  >Sexo Biológico dos Pacientes (sexo_paciente)</h5>
  </div>
</div>
"""
html_card_header_0C_2_22="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 90%;" 
                                  >Raça ou Cor dos Pacientes (raca_cor_paciente)</h5>
  </div>
</div>
"""
html_card_header_0C_2_31="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 90%;" 
                                  >Grupos de Atendimento da Vacinação (grupo_atendimento)</h5>
  </div>
</div>
"""
html_card_header_0C_2_32="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 90%;" 
                                  >Fabricantes das Vacinas Aplicadas (nome_fabrica_vacina)</h5>
  </div>
</div>
"""
html_card_header_0C_2_41="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 90%;" 
                                  >Tipo de Doses Aplicadas (dose_vacina)</h5>
  </div>
</div>
"""
html_card_header_0C_2_42="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 80%;" 
                                  >Municipio onde foi Vacinado (nome_municipio_estabelecimento)</h5>
  </div>
</div>
"""
html_card_header_0C_2_51="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 80%;" 
                                  >Estastisticas do Banco de Dados</h5>
  </div>
</div>
"""
html_card_header_0C_2_52="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 80%;" 
                                  >Descrição dos Dados</h5>
  </div>
</div>
"""


# - CAMPANHA DE VACINAÇÃO ------------------------------------------------------------------
## 1.1 - Número de Doses & Vacinas Aplicadas:
html_header_01="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; 
                                  text-align: center; padding: 10px 0; font-size:200%;"
                                  >1 - Descrição da Campanha de Vacinação</h2>
  </div>
</div>
"""
html_subheader_11="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 0px; padding-left: 15px;
                                  font-size:150%;" 
                                  >1.1 - Número de Doses & Vacinas Aplicadas</h3>
  </div>
</div>
"""

html_expanderheader_1_10="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; 
                                  text-align: center; padding: 10px 0; font-size:130%;"
                                  >Selecione o tipo da sua análise:</h2>
  </div>
</div>
"""


html_card_header_1_A_100="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Vacinados com 1° Dose</h5>
  </div>
</div>
"""
html_card_header_1_A_010="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Vacinados com 2° Dose</h5>
  </div>
</div>
"""
html_card_header_1_A_001="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Vacinados com Dose Adicional</h5>
  </div>
</div>
"""

html_card_header_1_B_21="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Quantidade de Vacinas Aplicadas por Dose</h5>
  </div>
</div>  
"""
html_card_header_1_B_22="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Proporção entre as Vacinas Aplicadas</h5>
  </div>
</div>
"""
html_card_header_1_B_23="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Dados dos Pacientes Vacinados</h5>
  </div>
</div>
"""
## 1.2 - Variação das Doses & Vacinas Aplicadas:
html_subheader_12="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 0px; padding-left: 15px;
                                  font-size:150%;" 
                                  >1.2 - Variação das Doses & Vacinas Aplicadas</h3>
  </div>
</div>
"""
html_card_header_1C11="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Variação diária de DOSES aplicadas</h5>
  </div>
</div>
"""
html_card_header_1C12="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Variação diária de VACINAS aplicadas</h5>
  </div>
</div>
"""
html_card_header_1C13="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Dados agrupados por DIA</h5>
  </div>
</div>
"""


## 1.3 -  Grupo Atendimento da Vacinação:

html_subheader_13="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 0px; padding-left: 15px;
                                  font-size:150%;" 
                                  >1.3 - Grupo atendimento da Vacinação</h3>
  </div>
</div>
"""








# - CARACTERISTICAS DOS PACIENTES -----------------------------------------------------------
html_header_20="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; text-align: center; padding: 10px 0;"
    >2 - Características da População Vacinada</h2>
  </div>
</div>
"""

## 2.1 - Análise do Sexo Biológico:
html_subheader_2A_10="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 0px; padding-left: 15px;
                                  font-size:150%;"
                                  >2.1 - Análise do Sexo Biológico</h3>
  </div>
</div>
"""
html_card_header_2A_1_11="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Vacinados do Sexo Masculino</h5>
  </div>
</div>
"""
html_card_header_2A_1_12="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Proporção entre os Sexos</h5>
  </div>
</div>
"""
html_card_header_2A_1_13="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Vacinados do Sexo Feminino</h5>
  </div>
</div>
"""
html_card_header_2A_1_20="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Sexo Biológico - Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2A_1_30="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Variação de Vacinados</h5>
  </div>
</div>
"""


## 2.2 - Análise da Raça ou Cor:
html_subheader_2B_10="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 0px; padding-left: 15px;
                                  font-size:150%;" 
                                  >2.2 - Análise da Raça/Cor</h3>
  </div>
</div>
"""
html_card_header_2B_2_11="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >População Residente x População Vacinada</h5>
  </div>
</div>
"""
html_card_header_2B_2_12="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Raça/Cor - Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2B_2_21="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Raça/Cor - Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2B_2_22="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Raça/Cor - Dados Agrupados</h5>
  </div>
</div>
"""

## 2.3 - Análise da Idade:
html_subheader_2B_30="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 0px; padding-left: 15px;
                                  font-size:150%;" 
                                  >2.3 - Análise da Idade</h3>
  </div>
</div>
"""
html_card_header_2B_3_11="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Quantidade de Vacinados</h5>
  </div>
</div>
"""
html_card_header_2B_3_12="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2B_3_21="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Variação de Vacinados</h5>
  </div>
</div>
"""
html_card_header_2B_3_22="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 10px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 100%;" 
                                  >Companha de Vacinação</h5>
  </div>
</div>
"""


# - POSTOS DE VACINAÇÃO ---------------------------------------------------------------------
## - Geral:

# - IMAGENS ----------------------------------------------------------------------------------

image_vac = Image.open('EDA/logovac.png')
image1 = Image.open('EDA/eda1.png')
image2 = Image.open('EDA/eda2.png')
image3 = Image.open('EDA/3.png')
image4 = Image.open('EDA/4.png')
image5 = Image.open('EDA/5.png')
image6 = Image.open('EDA/6.png')
image7 = Image.open('EDA/7.png')
image8 = Image.open('EDA/8.png')
image9 = Image.open('EDA/9.png')
image10 = Image.open('EDA/10.png')



## - CODIGO -----------------------------------------------------------------------------------

body = '''

# Carregando os Dados via SQL e PYTHON
import basedosdados as bd
df = bd.read_sql("""
     SELECT VAC.id_paciente, VAC.idade_paciente, VAC.sexo_paciente, VAC.raca_cor_paciente, VAC.grupo_atendimento_vacina, VAC.categoria_vacina, VAC.nome_fabricante_vacina, VAC.data_aplicacao_vacina, VAC.dose_vacina,
            UPPER(M1.nome) AS nome_municipio_estabelecimento, VAC.razao_social_estabelecimento, VAC.nome_fantasia_estabelecimento 
     FROM `basedosdados.br_ms_vacinacao_covid19.microdados` AS VAC, `basedosdados.br_bd_diretorios_brasil.municipio` AS M1
     WHERE (VAC.id_municipio_estabelecimento =  M1.id_municipio) AND (VAC.id_municipio_endereco_paciente = '4205407');""", 
     billing_project_id="xxxxx", reauth=False)'''

body2 = '''
# Renomeando valores das colunas para melhor análise:
df['dose_vacina'].replace('Reforço', 'Dose Adicional', inplace = True)
df['dose_vacina'].replace('1º Reforço', 'Dose Adicional', inplace = True)
df['dose_vacina'].replace('3ª Dose', 'Dose Adicional', inplace = True)
df['dose_vacina'].replace('Única', 'Dose Única', inplace = True)

df['sexo_paciente'].replace('F', 'Feminino', inplace = True)
df['sexo_paciente'].replace('M', 'Masculino', inplace = True)

df['raca_cor_paciente'].replace("1", 'Branca', inplace = True)
df['raca_cor_paciente'].replace("2", 'Preta', inplace = True)
df['raca_cor_paciente'].replace("3", 'Parda', inplace = True)
df['raca_cor_paciente'].replace("4", 'Amarela', inplace = True)
df['raca_cor_paciente'].replace("5", 'Indígena', inplace = True)
df['raca_cor_paciente'].replace("99", 'Sem informação', inplace = True)

df['nome_fabricante_vacina'].replace("ASTRAZENECA", 'ASTRAZENECA/FIOCRUZ', inplace = True)

df['data_aplicacao_vacina'].replace("1993-11-08", "2021-11-08", inplace = True)

df['grupo_atendimento_vacina'].replace("101","Anemia Falciforme", inplace = True)
df['grupo_atendimento_vacina'].replace("102","Neoplasias", inplace = True)
df['grupo_atendimento_vacina'].replace("103","Diabetes Mellitus", inplace = True)
df['grupo_atendimento_vacina'].replace("104","Doença Pulmonar Obstrutiva Crônica", inplace = True)
df['grupo_atendimento_vacina'].replace("105","Doença Renal Crônica", inplace = True)
df['grupo_atendimento_vacina'].replace("106","Doenças Cardiovasculares e Cerebrovasculares", inplace = True)
df['grupo_atendimento_vacina'].replace("107","Hipertensão de difícil controle", inplace = True)
df['grupo_atendimento_vacina'].replace("108","Indivíduos Transplantados de Órgão Sólido", inplace = True)
df['grupo_atendimento_vacina'].replace("109","Obesidade Grave (Imc>=40)", inplace = True)
df['grupo_atendimento_vacina'].replace("110","Síndrome de Down", inplace = True)
df['grupo_atendimento_vacina'].replace("111","Outros Imunocomprometidos", inplace = True)
df['grupo_atendimento_vacina'].replace("114","Cirrose Hepática", inplace = True)
df['grupo_atendimento_vacina'].replace("115","Doença Neurológica crônica", inplace = True)
df['grupo_atendimento_vacina'].replace("116","Doença Cardiovascular", inplace = True)
df['grupo_atendimento_vacina'].replace("201","Pessoas de 60 a 64 anos", inplace = True)
df['grupo_atendimento_vacina'].replace("202","Pessoas de 65 a 69 anos", inplace = True)
df['grupo_atendimento_vacina'].replace("203","Pessoas de 70 a 74 anos", inplace = True)
df['grupo_atendimento_vacina'].replace("204","Pessoas de 75 a 79 anos", inplace = True)
df['grupo_atendimento_vacina'].replace("205","Pessoas de 80 anos ou mais", inplace = True)
df['grupo_atendimento_vacina'].replace("301","Pessoas de 60 nos ou mais Institucionalizadas", inplace = True)
df['grupo_atendimento_vacina'].replace("402","Exército Brasileiro - EB", inplace = True)
df['grupo_atendimento_vacina'].replace("403","Força Aérea Brasileira - FAB", inplace = True)
df['grupo_atendimento_vacina'].replace("501","Bombeiro Civil", inplace = True)
df['grupo_atendimento_vacina'].replace("502","Bombeiro Militar", inplace = True)
df['grupo_atendimento_vacina'].replace("503","Guarda Municipal", inplace = True)
df['grupo_atendimento_vacina'].replace("505","Policial Civil", inplace = True)
df['grupo_atendimento_vacina'].replace("506","Policial Federal", inplace = True)
df['grupo_atendimento_vacina'].replace("507","Policial Militar", inplace = True)
df['grupo_atendimento_vacina'].replace("601","Quilombola", inplace = True)
df['grupo_atendimento_vacina'].replace("602","Ribeirinha", inplace = True)
df['grupo_atendimento_vacina'].replace("701","Povos indígenas em terras indígenas", inplace = True)
df['grupo_atendimento_vacina'].replace("801","Ensino Básico", inplace = True)
df['grupo_atendimento_vacina'].replace("802","Ensino Superior", inplace = True)
df['grupo_atendimento_vacina'].replace("901","Auxiliar de Veterinário", inplace = True)
df['grupo_atendimento_vacina'].replace("902","Biólogo", inplace = True)
df['grupo_atendimento_vacina'].replace("903","Biomédico", inplace = True)
df['grupo_atendimento_vacina'].replace("904","Cozinheiro e Auxiliares", inplace = True)
df['grupo_atendimento_vacina'].replace("905","Cuidador de Idosos", inplace = True)
df['grupo_atendimento_vacina'].replace("906","Doula/Parteira", inplace = True)
df['grupo_atendimento_vacina'].replace("907","Enfermeiro(a)", inplace = True)
df['grupo_atendimento_vacina'].replace("908","Farmacêutico", inplace = True)
df['grupo_atendimento_vacina'].replace("909","Fisioterapeutas", inplace = True)
df['grupo_atendimento_vacina'].replace("910","Fonoaudiólogo", inplace = True)
df['grupo_atendimento_vacina'].replace("911","Sistema Funerário", inplace = True)
df['grupo_atendimento_vacina'].replace("912","Médico", inplace = True)
df['grupo_atendimento_vacina'].replace("913","Médico Veterinário", inplace = True)
df['grupo_atendimento_vacina'].replace("914","Motorista de Ambulância", inplace = True)
df['grupo_atendimento_vacina'].replace("915","Nutricionista", inplace = True)
df['grupo_atendimento_vacina'].replace("916","Odontologista", inplace = True)
df['grupo_atendimento_vacina'].replace("917","Pessoal da Limpeza", inplace = True)
df['grupo_atendimento_vacina'].replace("918","Profissionais de Educação Física", inplace = True)
df['grupo_atendimento_vacina'].replace("919","Psicólogo", inplace = True)
df['grupo_atendimento_vacina'].replace("920","Recepcionista", inplace = True)
df['grupo_atendimento_vacina'].replace("921","Segurança", inplace = True)
df['grupo_atendimento_vacina'].replace("922","Assistente Social", inplace = True)
df['grupo_atendimento_vacina'].replace("923","Técnico de Enfermagem", inplace = True)
df['grupo_atendimento_vacina'].replace("924","Técnico Veterinário", inplace = True)
df['grupo_atendimento_vacina'].replace("925","Terapeuta Ocupacional", inplace = True)
df['grupo_atendimento_vacina'].replace("926","Outros Serviços", inplace = True)
df['grupo_atendimento_vacina'].replace("927","Auxiliar de Enfermagem", inplace = True)
df['grupo_atendimento_vacina'].replace("928","Técnico de Odontologia", inplace = True)
df['grupo_atendimento_vacina'].replace("929","Estudante", inplace = True)
df['grupo_atendimento_vacina'].replace("930","Agente de Combate a Endemias - ACE", inplace = True)
df['grupo_atendimento_vacina'].replace("931","Agente Comunitário de Saúde - ACS", inplace = True)
df['grupo_atendimento_vacina'].replace("932","Auxiliar em Saúde Bucal - ASB", inplace = True)
df['grupo_atendimento_vacina'].replace("933","Técnico em Saúde Bucal - TSB", inplace = True)
df['grupo_atendimento_vacina'].replace("1001","Aéreo", inplace = True)
df['grupo_atendimento_vacina'].replace("1002","Caminhoneiro", inplace = True)
df['grupo_atendimento_vacina'].replace("1003","Coletivo Rodoviário Passageiros Urbano e de Longo Curso", inplace = True)
df['grupo_atendimento_vacina'].replace("1004","Ferroviário", inplace = True)
df['grupo_atendimento_vacina'].replace("1005","Metroviário", inplace = True)
df['grupo_atendimento_vacina'].replace("1006","Aquaviário", inplace = True)
df['grupo_atendimento_vacina'].replace("1101","Pessoas com Deficiência Institucionalizadas", inplace = True)
df['grupo_atendimento_vacina'].replace("1102","Pessoas com Deficiências Permanente Grave", inplace = True)
df['grupo_atendimento_vacina'].replace("1301","Trabalhadores Portuários", inplace = True)
df['grupo_atendimento_vacina'].replace("1401","Funcionário do Sistema de Privação de Liberdade", inplace = True)
df['grupo_atendimento_vacina'].replace("1501","População Privada de Liberdade", inplace = True)
df['grupo_atendimento_vacina'].replace("1601","Trabalhadores Industriais", inplace = True)
df['grupo_atendimento_vacina'].replace("1701","Trabalhadores de limpeza urbana e manejo de resíduos sólidos", inplace = True)
df['grupo_atendimento_vacina'].replace("1801","Gestante", inplace = True)
df['grupo_atendimento_vacina'].replace("1901","Puérperas", inplace = True)
df['grupo_atendimento_vacina'].replace("999999","Outros Grupos", inplace = True)

df['grupo_atendimento_vacina'].replace("206","Outros Grupos", inplace = True)
df['grupo_atendimento_vacina'].replace("1201","Outros Grupos", inplace = True)
df['grupo_atendimento_vacina'].replace("401","Outros Grupos", inplace = True)
df['grupo_atendimento_vacina'].replace("504","Outros Grupos", inplace = True)
df['grupo_atendimento_vacina'].replace("112","Outros Grupos", inplace = True)
'''



























