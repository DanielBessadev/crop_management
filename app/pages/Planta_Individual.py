import streamlit as st
from datetime import datetime, date

from functions.functions import species, specimens, names

# Streamlit
st.set_page_config(page_title='Meu Setup', layout='wide')

c1, c2, c3 = st.columns((1,1,6))
with c1:
    name = st.selectbox('Planta', names)
    selected_species = species.loc[species.name == name]
with c2:
    st.subheader(selected_species['species'].to_string(index=False, header=False))
with c3:
    st.write("Image")
    # Image columns #st.image

c1, c2, c3 = st.columns((1,1,6))
with c1:
    selected_specimens = specimens.loc[specimens.id_species == int(selected_species.index.values)]
    id_specimen = st.selectbox('Código', selected_specimens['id_specimen'].sort_values().to_list())
    selected_specimen = selected_specimens.loc[selected_specimens.id_specimen == id_specimen]
with c2:
    # Age calculation
    date_plantation = datetime.strptime(selected_specimen.date_plantation.to_string(index=False, header=False), '%Y-%m-%d').date()
    age = int((date.today() - (date_plantation)).days/365.2425)
    st.write("Idade:", age)
with c3:
    st.write(selected_species['popular_names'].to_string(index=False, header=False))