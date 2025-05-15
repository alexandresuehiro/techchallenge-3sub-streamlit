import streamlit as st
#<<<<<<< HEAD
#
#st.title("🎈 My new app")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)
#=======
from utils.constantes import TITULO_PRINCIPAL
from utils.layout import output_layout
import warnings



warnings.filterwarnings("ignore")

st.set_page_config(page_title=TITULO_PRINCIPAL, layout="wide")
output_layout()

st.header(f":orange[{TITULO_PRINCIPAL}]")

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
    Este trabalho tem por finalidade analisar uma faixa de meses do ano de 2020 para analisar os impactos da Covid-19 na população brasileira usando os dados disponíveis no site do IBGE: https://covid19.ibge.gov.br/pnad-covid/
    Tem como intenção auxiliar os médicos a responder algumas perguntas como:
    
    * Quais são os principais sintomas?
    * Qual é o maior público atingido pela doença?
    * Como o trabalho presencial afetou os casos?
    * Quais são as características do comportamento da população?
    """
)



st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """

    Usando a base de dados provida, referente ao período 2020, fizemos uma análise inicial sobre o conteúdo para entender os impactos da Covid-19 sobre a população brasileira ao verificar possíveis estratos da sexo, ocupação, faixa de renda, escolaridade etc.
	A partir disso, esperamos ter um cenário mais claro que responda as questões acima.
 """
)
#>>>>>>> f36f782 (Initial commit)
