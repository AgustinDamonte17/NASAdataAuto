import os
import requests
import re
import unicodedata

def descargar_datos_nasa_api(latitud, longitud, ruta_carpeta, ubicacion):
    # Definir los parámetros para la API de la NASA
    api_url = "https://power.larc.nasa.gov/api/temporal/hourly/point"
    params = {
        "latitude": latitud,
        "longitude": longitud,
        "start": "20120101",  # Formato: YYYYMMDD (01/01/2012)
        "end": "20221231",    # Formato: YYYYMMDD (31/12/2022)
        "parameters": "ALLSKY_SFC_SW_DWN,T2M",  # Radiación y temperatura a 2 metros
        "community": "RE",
        "format": "CSV",
        "header": "true",     # Incluir el encabezado en el archivo CSV
        "time-standard": "UTC"
    }

    # Realizar la solicitud HTTP a la API de la NASA
    response = requests.get(api_url, params=params)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Sanitizar el nombre de la ubicación para que sea válido en un nombre de archivo
        ubicacion_sanitizada = re.sub(r'[<>:"/\\|?*]', '', ubicacion)
        ubicacion_sanitizada = ubicacion_sanitizada.replace(' ', '_')

        # Eliminar acentos y caracteres especiales
        ubicacion_sanitizada = unicodedata.normalize('NFD', ubicacion_sanitizada).encode('ascii', 'ignore').decode('utf-8')

        # Crear el nombre del archivo CSV indicando que son datos Hourly
        nombre_archivo = f"nasa_data_hourly_{ubicacion_sanitizada}.csv"
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

        # Guardar el archivo CSV en la carpeta indicada
        with open(ruta_archivo, "w", encoding='utf-8') as archivo_csv:
            archivo_csv.write(response.text)

        print(f"Datos descargados correctamente en: {ruta_archivo}")
    else:
        print(f"Error al descargar los datos de la NASA: {response.status_code}")

    return ruta_archivo
