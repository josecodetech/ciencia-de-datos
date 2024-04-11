import geopandas as gpd
import matplotlib.pyplot as plt
mundo = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
mundo.plot(column='pop_est', figsize=(10,6), cmap='OrRd',legend=True)
plt.title('Poblacion mundial')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.show()