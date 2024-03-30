import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de películas
peliculas = {
    'Título': ['Pelicula A', 'Pelicula B', 'Pelicula C', 
               'Pelicula D', 'Pelicula E'],
    'Género': ['Drama', 'Comedia', 'Acción', 'Thriller', 
               'Aventura'],
    'Calificación': [7.5, 8.2, 6.9, 7.8, 8.5]
}
df_peliculas = pd.DataFrame(peliculas)

# Visualizar distribución de calificaciones de películas
plt.figure(figsize=(8, 6))
plt.hist(df_peliculas['Calificación'], bins=5, color='green', 
         alpha=0.7)
plt.title('Distribución de Calificaciones de Películas')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
