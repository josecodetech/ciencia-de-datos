import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
europa = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
europa = europa[europa['continent'] == 'Europe']
paises_europeos = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herz.', 'Bulgaria', 
                   'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 
                   'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 
                   'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 
                   'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 
                   'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 
                   'United Kingdom', 'Vatican City']
renta_per_capita = np.random.randint(20000, 80000, size=len(paises_europeos))
datos_renta = pd.DataFrame({'Pais': paises_europeos, 'Renta per capita': renta_per_capita})
europa = europa.merge(datos_renta,how='left', left_on='name', right_on='Pais') 
europa.plot(column='Renta per capita', figsize=(10,6), cmap='OrRd',legend=True)
plt.title('Renta per capita en Europa')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.show()
