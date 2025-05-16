import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
from utils.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from utils.layout import output_layout, format_number

#from pages.indicadores import SobreIndicadoresAvaliacao
from tabs.analises.PerfilEstudantes_tab import PerfilEstudantes
from tabs.analises.AnaliseIndicadoresPorPedra_tab import AnaliseIndicadoresPorPedra
from tabs.analises.MapaCorrelacaoIndicadores_tab import MapaCorrelacaoIndicadores
from tabs.analises.AnaliseTransicaoPedras_tab import AnaliseTransicaoPedras
from tabs.analises.PontoVirada2022_tab import PontoVirada2022
from tabs.analises.AnalisePontoVirada2022Sim_tab import AnalisePontoVirada2022Sim


st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()


with st.container():
    st.header(f":orange[{TITULO_ANALISE_EXPLORATORIA}]")
#            1 - Sobre Indicadores de Avaliação: indicadores internos sobre o perfil de cada jovem

    st.markdown(
        """
        Nesta sessão de análise, detalharemos um pouco sobre: 
        
            1.  Principais Sintomas ao longo das semanas
            2.  Públicos atingidos pela doença
            3.  Trabalho Presencial x Trabalho Remoto: existe influência na propagação?
            4.  Hábitos da população na pandemia
    """
    )
    
    st.header(":blue[Principais Sintomas ao longo das semanas]", divider="blue")
    st.subheader('Sintomas mais comuns apresentados') 
    st.markdown(
                """
                    De acordo com as informações obtidas da base de dados, grande parte dos avaliados apresentou "Algum Sintoma", que pode ser algo fora dos sintomas mais comuns.
                    No caso dos sintomas mais comuns, temos o gráfico abaixo mostrando a evolução dos sintomas nas semanas mapeadas.
                """)

    st.image('assets/imgs/analise_sintomas_semanal.png')
    st.markdown(
                """
                        A quantidade de sintomas reduziu com o passar do tempo.
                """) 
    