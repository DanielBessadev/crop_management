from datetime import datetime, date

from functions.functions import all_reports_by_stock
from functions.graphs import graph_compare_report
from functions.report import report_columns
from functions.setups import frequency, setups_info
from functions.tickers import tickers

import streamlit as st

# Streamlit
st.set_page_config(page_title='Meu Setup', layout='wide')

st.subheader("Performance de setups por Ativo")