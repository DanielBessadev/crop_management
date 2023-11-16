import streamlit as st

from functions.functions import species, specimens, names

# Streamlit
st.set_page_config(page_title='Meu Setup', layout='wide')

c1, c2, c3 = st.columns(3)
with c1:
    name = st.selectbox('Planta', names)
    selected_species = species.loc[species.name == name]
with c2:
    st.write("(", selected_species['species'],")")
with c3:
    st.write("Image")
    # Image columns #st.image

c1, c2, c3 = st.columns(3)
with c1:
    st.write(selected_species['popular_names'])
with c2:
    selected_specimens = specimens.loc[specimens.id_species == int(selected_species.index.values)]
    gps = st.selectbox('Localização', selected_specimens['gps_x'].sort_values().to_list())
    selected_specimen = selected_specimens.loc[selected_specimens.gps_x == gps]
with c3:
    # Age calculation
    age = selected_specimen['date_plantation']
    st.write("Idade:", age)

