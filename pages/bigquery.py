import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from utils.constantes import TITULO_BIGQUERY, TITULO_PRINCIPAL
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_BIGQUERY} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
            st.header(f":orange[Usando o Bigquery]")
            st.subheader(":blue[Queries usadas]", divider="blue")
            st.markdown(
                """
                    st.image('assets/imgs/02_query_bigquery.png')
    
                """)


