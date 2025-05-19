import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
from utils.constantes import TITULO_INDICADORES, TITULO_PRINCIPAL
from utils.layout import output_layout, format_number


from tabs.tab import TabInterface


st.set_page_config(
     page_title=f"{TITULO_INDICADORES} | {TITULO_PRINCIPAL}",
     layout="wide",
)
output_layout()


with st.container():
        st.header(f":orange[{TITULO_INDICADORES}]")

        st.markdown(
            """
            Nesta sessão de análise, detalharemos sobre alguns sintomas do Covid-19, registrados na base do Pnad Covid-19:

            *	Febre
            *	Tosse
            *   Dor de garganta
            *   Dificuldade de respirar
            *   Dor de cabeça
            *   Dor no peito
            *   Náusea
            *   Nariz entupido ou escorrendo
            *   Fadiga
            *   Dor nos olhos
            *   Pedra de olfato ou paladar
            *   Dor muscular
            *   Febre, Tosse e dificuldade de respirar
            *   Febre, Tosse e dor no peito
        """
        )
        # # Criando 8 expanders

        # # Se você tiver muitas seções, pode utilizar um loop for para simplificar:
        # for i in range(1, 9):
        #     with st.expander(f"INDE"):
        #         chamarINDE = SobreINDE()
        #         st.write(chamarINDE)
                
        #     with st.expander(f"IAA"):
        #         chamarIAA = SobreIAA()
        #         st.write(chamarIAA)

        #     with st.expander(f"IAN"):
        #         chamarIAN = SobreIAN()
        #         st.write(chamarIAN)

        #     with st.expander(f"IDA"):
        #         chamarIDA = SobreIDA()
        #         st.write(chamarIDA)

        #     with st.expander(f"IEG"):
        #         chamarIEG = SobreIEG()
        #         st.write(chamarIEG)

        #     with st.expander(f"IPS"):
        #         chamarIPS = SobreIPS()
        #         st.write(chamarIPS)

        #     with st.expander(f"IPP"):
        #         chamarIPP = SobreIPP()
        #         st.write(chamarIPP)

        #     with st.expander(f"IPV"):
        #         chamarIPV = SobreIPV()
        #         st.write(chamarIPV)
       
    
