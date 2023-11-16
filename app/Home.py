import streamlit as st
from PIL import Image

# Streamlit
st.set_page_config(page_title='Crop Management', layout='wide')

st.title("Crop Management")

# Description
st.write("""
    """)


# Links of bibliography
st.subheader("Bibliography")
st.write("""
    Ativos listados na [**B3**](https://www.b3.com.br/pt_br/);
    
    Dados de mercado baixados da [**API Yahoo! de Finanças**](https://pypi.org/project/yfinance/);

    Maioria dos Setups divulgados pelo trader **Stormer** da [**L&S**](https://ls.com.vc).""")

# Import file with modifications
st.write("Import file")


# My github link
c1, c2, c3 = st.columns((2,6,2))
with c2:
    st.write("Isenção de responsabilidade: Não é uma recomendação de compra ou venda de ativos no mercado financeiro.")