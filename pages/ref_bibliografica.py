import streamlit as st
from utils.constantes import TITULO_PRINCIPAL, TITULO_REFERENCIAS
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_REFERENCIAS} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_REFERENCIAS}]")
    
    st.markdown(
        """
        1. 
        2. 
        3. 
        4. 
    """
    )
