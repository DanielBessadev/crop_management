import streamlit as st
from datetime import datetime, date
import pandas as pd

from functions.functions import species, specimens, names

# Streamlit
st.set_page_config(page_title='Meu Setup', layout='wide')

c1, c2, c3, c4, c5 = st.columns((2,1,2,1,5))
with c1:
    name = st.selectbox('Planta', names)
    selected_species = species.loc[species.name == name]
with c2:
    selected_specimens = specimens.loc[specimens.id_species == int(selected_species.index.values)]
    id_specimen = st.selectbox('Código', selected_specimens.index.sort_values().to_list())
    selected_specimen = selected_specimens.loc[selected_specimens.index == id_specimen]
with c3:
    st.subheader(selected_species['species'].to_string(index=False, header=False))
with c4:
    date_plantation = datetime.strptime(selected_specimen.date_plantation.to_string(index=False, header=False), '%Y-%m-%d').date()
    age = int((date.today() - (date_plantation)).days/365.2425)
    if age == 0:
        st.write('Menos de 1 ano')
    else:
        st.write(str(age), "anos")
with c5:
    st.write(selected_species['popular_names'].to_string(index=False, header=False))

c1, c2 = st.columns((4,6))
with c1:
    subtab_handling, subtab_record = st.tabs(['Manuseio Padrão', 'Histórico de Manuseios'])
    with subtab_handling:
        basic = pd.DataFrame(data=[[f"{selected_species['flowering_month'].to_string(index=False, header=False)}"],
                                    [f"{selected_species['fruiting_month'].to_string(index=False, header=False)}"],
                                    [f"{selected_species['flowering_NPK'].to_string(index=False, header=False)}"],
                                    [f"{selected_species['fruiting_NPK'].to_string(index=False, header=False)}"],
                                    [f"{selected_species['flowering_compost'].to_string(index=False, header=False)}"],
                                    [f"{selected_species['fruiting_compost'].to_string(index=False, header=False)}"],
                                    [f"{selected_species['flowering_calcarium'].to_string(index=False, header=False)}"],
                                    [f"{selected_species['fruiting_calcarium'].to_string(index=False, header=False)}"],
                                    [f"{selected_species['pruning_season'].to_string(index=False, header=False)}"],
                                    [f"{selected_species['harvest_season'].to_string(index=False, header=False)}"]],
                            index=[['Mês de floração','Mês de frutificação', 'NPK de floração', 'NPK de frutificação', 'Adubo de floração', 'Adubo de frutificação', 'Calcário de floração', 'Calcário de frutificação', 'Mês de poda', 'Mês de colheita']], 
                            columns=['Manuseio'])
        st.table(basic)

with c2:
    st.write("Image")

df = pd.DataFrame(data=[[float(selected_specimen.gps_x.to_string(index=False, header=False))], 
                         [float(selected_specimen.gps_y.to_string(index=False, header=False))],
                         [float(10)],
                         [18]],
    columns=['lat', 'lon'])
st.map(df)