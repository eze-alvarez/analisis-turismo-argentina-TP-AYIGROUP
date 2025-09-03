import pandas as pd
import numpy as np

def cargar_y_limpiar_vuelos(ruta_archivo):
    """
    Carga el dataset de vuelos, selecciona columnas relevantes,
    convierte tipos de datos, maneja nulos y filtra por el año 2024.
    
    Args:
        ruta_archivo (str): La ruta al archivo CSV del dataset de vuelos.
    
    Returns:
        pd.DataFrame: Un DataFrame de pandas con los datos de vuelos limpios y filtrados.
    """
    # Cargar el dataset
    df_vuelos_original = pd.read_csv(ruta_archivo)
    
    # Renombrar la columna de tiempo para mayor claridad
    df_vuelos_original.rename(columns={'indice_tiempo': 'fecha_vuelos'}, inplace=True)
    
    # Seleccionar solo las columnas que necesitas para el análisis
    columnas_a_mantener = [
        'fecha_vuelos',
        'origen_provincia',
        'destino_provincia',
        'origen_pais',
        'pasajeros',
        'asientos',
        'vuelos'
    ]
    
    df_vuelos = df_vuelos_original[columnas_a_mantener].copy()

    # Convertir a formato de fecha y filtrar por 2024
    df_vuelos['fecha_vuelos'] = pd.to_datetime(
        df_vuelos['fecha_vuelos'],
        format='%Y-%m-%d',
        errors='coerce'
    )

    filtro_2024 = df_vuelos['fecha_vuelos'].dt.year
    df_vuelos = df_vuelos[filtro_2024 == 2024]

    # Manejar valores nulos en columnas de provincia
    # Los valores nulos en estas columnas indican que el vuelo es internacional
    df_vuelos['origen_provincia'] = df_vuelos['origen_provincia'].fillna('Internacional')
    df_vuelos['destino_provincia'] = df_vuelos['destino_provincia'].fillna('Internacional')

    # Manejar nulos en columnas numéricas y asegurarse de que sean de tipo entero
    for col in ['pasajeros', 'asientos', 'vuelos']:
        df_vuelos[col] = df_vuelos[col].fillna(0).astype(int)

    # Calcular la tasa de ocupación, evitando la división por cero
    # Se reemplaza np.inf por 0
    df_vuelos['ocupacion'] = np.where(
    df_vuelos['asientos'] > 0,
    (df_vuelos['pasajeros'] / df_vuelos['asientos']) * 100,
    0
    )

    # Redondea la columna 'ocupacion' a 2 decimales
    df_vuelos['ocupacion'] = df_vuelos['ocupacion'].round(2)



    return df_vuelos


def cargar_y_limpiar_feriados(ruta_archivo):
    # Tu función original, no necesita cambios
    df_feriados = pd.read_excel(ruta_archivo)


    # Renombrar la columna 'indice_tiempo' a 'fecha_fin_largo'
    df_feriados.rename(columns={'indice_tiempo': 'fecha_fin_largo'}, inplace=True)

    df_feriados['fecha_fin_largo'] = pd.to_datetime(df_feriados[ 'fecha_fin_largo'])
    return df_feriados


def unir_datasets(df_vuelos, df_feriados):
    # Tu función original, no necesita cambios
    df_vuelos['es_feriado_largo'] = df_vuelos['indice_tiempo'].isin(df_feriados['indice_tiempo'])
    return df_vuelos


def unir_datasets(df_vuelos, df_feriados):
    """
    Une el DataFrame de vuelos con el de feriados para identificar los días de feriado largo.
    """
    # Usar las nuevas columnas de fecha para la unión
    df_vuelos['es_feriado_largo'] = df_vuelos['fecha_vuelos'].isin(df_feriados['fecha_fin_largo'])
    return df_vuelos


def normalizar_provincias(df_vuelos):
    """
    Crea una tabla de provincias únicas y asigna IDs, luego reemplaza los nombres
    de las provincias en el DataFrame de vuelos por sus IDs.
    
    Args:
        df_vuelos (pd.DataFrame): DataFrame de vuelos limpio.

    Returns:
        tuple: Una tupla que contiene (df_vuelos_normalizado, df_provincias).
    """
    # 1. Extraer las provincias únicas de las columnas de origen y destino
    provincias_origen = df_vuelos[['origen_provincia']].rename(columns={'origen_provincia': 'provincia'})
    provincias_destino = df_vuelos[['destino_provincia']].rename(columns={'destino_provincia': 'provincia'})
    
    # Unir las provincias de origen y destino y eliminar duplicados
    df_provincias = pd.concat([provincias_origen, provincias_destino]).drop_duplicates().reset_index(drop=True)
    
    # 2. Asignar un ID único a cada provincia
    df_provincias['id_provincia'] = df_provincias.index + 1
    
    # Crear un diccionario para mapear el nombre de la provincia a su ID
    provincia_map = df_provincias.set_index('provincia')['id_provincia'].to_dict()
    
    # 3. Reemplazar los nombres de las provincias por sus IDs en el DataFrame de vuelos
    df_vuelos['id_origen_provincia'] = df_vuelos['origen_provincia'].map(provincia_map)
    df_vuelos['id_destino_provincia'] = df_vuelos['destino_provincia'].map(provincia_map)
    
    # 4. Eliminar las columnas originales con los nombres completos
    df_vuelos = df_vuelos.drop(columns=['origen_provincia', 'destino_provincia'])
    
    # Devolver el DataFrame de vuelos normalizado y la nueva tabla de provincias
    return df_vuelos, df_provincias

