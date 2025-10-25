#Archivo inicial de graficacion 

import panda as pd
import matplotlib.pyplot as plt

url ='https://github.com/Twoeme/dataanalysis/raw/refs/heads/main/ANM_Vol%C3%BAmen_de_Explotaci%C3%B3n_de_Minerales_Asociados_a_Pagos_de_Regal%C3%ADas_20251025.csv'

df=pd.read_csv(url)
df_2=df_2.dropna()
