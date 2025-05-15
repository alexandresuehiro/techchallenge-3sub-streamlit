
import streamlit as st
from st_pages import show_pages, Page
import locale

from utils.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_COVID, TITULO_INDICADORES, TITULO_BIGQUERY, TITULO_REFLEXOES, TITULO_INSTRUCTIONS, TITULO_REFERENCIAS

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

def output_layout():
    show_pages(
        [
            Page("./streamlit_app.py", "Tech Challenge 3 Sub", use_relative_hash=True),                 
            Page("./pages/pnadcovid19.py", TITULO_COVID, use_relative_hash=True),     
            Page("./pages/indicadores.py", TITULO_INDICADORES, use_relative_hash=True),         
            Page("./pages/bigquery.py", TITULO_BIGQUERY, use_relative_hash=True),
            Page("./pages/analise.py", TITULO_ANALISE_EXPLORATORIA, use_relative_hash=True),
            Page("./pages/reflexoes.py", TITULO_REFLEXOES, use_relative_hash=True),         
            Page("./pages/instructions.py", TITULO_INSTRUCTIONS, use_relative_hash=True),         
            Page("./pages/ref_bibliografica.py", TITULO_REFERENCIAS, use_relative_hash=True)             
        ]
    )

    with st.sidebar:
        st.subheader("Aluno")
        st.text("Alexandre Suehiro de Paula e Silva")
        st.text("RM 352798 - 3DTAT")

        st.divider()

        st.subheader("Repositórios do projeto")
        st.link_button(
            "Repositório Streamlit",
            "https://github.com/alexandresuehiro/techchallenge-3sub-streamlit",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )