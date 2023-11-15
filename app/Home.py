import streamlit as st
from PIL import Image

# Streamlit
st.set_page_config(page_title='Crop Management', layout='wide')

st.title("Crop Management")

# Description
st.write("""
    """)

c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16 = st.columns(16)
c5.image(Image.open('app/images/b3_logo.png'))
c6.image(Image.open('app/images/Python.png'))
c7.image(Image.open('app/images/Selenium.png'))
c8.image(Image.open('app/images/Pandas.png'))
c9.image(Image.open('app/images/Numpy.png'))
c10.image(Image.open('app/images/Plotly.png'))
c11.image(Image.open('app/images/Streamlit.png'))
c12.image(Image.open('app/images/Yahoo.png'))

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