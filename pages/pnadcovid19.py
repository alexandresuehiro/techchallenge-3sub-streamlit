import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from utils.constantes import TITULO_COVID, TITULO_PRINCIPAL
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_COVID} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
            st.header(f":orange[Pnad Covid-19]")
            st.subheader(":blue[O Trabalho do IBGE]", divider="blue")
            st.markdown(
                """
    Neste canal, o IBGE reúne as iniciativas realizadas e as ações em desenvolvimento em relação a seus estudos e pesquisas para apoiar os esforços no combate à Covid-19.

No novo cenário vivido pelo País, torna-se fundamental a rápida geração de informações que possam basear e sustentar decisões dos segmentos de governo e da sociedade civil, para que possamos prosseguir no enfrentamento da pandemia e contribuir para o bem comum.

Dessa forma, o IBGE vem adaptando suas atividades e a forma de trabalho de suas equipes para que as informações de que o Brasil necessita continuem a ser produzidas.

Além disso, o IBGE antecipou a divulgação de alguns resultados de pesquisas com temas relacionados à saúde e está preparando novos estudos que permitam mapear e conhecer com mais detalhe e precisão as condições de vida da população e do desenvolvimento do país durante esse período.
                """)


