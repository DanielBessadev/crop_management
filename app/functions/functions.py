import pandas as pd

# Dataframes
species = pd.read_excel('/database/roca_andiroba.xlsx', sheet_name='Species', index_col='id_species')
names = species['name'].sort_values().to_list()

specimens = pd.read_excel('/database/roca_andiroba.xlsx', sheet_name='Specimen', index_col='id_specimen')

# Retornar somente uma planta
