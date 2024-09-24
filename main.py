from Leerubi import leer_ubicacion
from GoogleMaps import obtener_coordenadas
from Carpetaubi import crear_carpeta_ubicacion
from NasaLarc import descargar_datos_nasa_api
from NasaLarc2 import descargar_datos_nasa_api_monthly
from ProExc import procesar_y_pegar_datos_horarios  
from ProExc2 import procesar_y_pegar_datos_mensuales

def main():
    # Definir la ruta del archivo
    ruta_archivo = r'C:\Users\adamonte\Desktop\AGUSTIN\Python\NASA AUTOM Prueba - Modelo Gen ee.xlsx'

    # Llamar a la función para leer la ubicación
    ubicacion = leer_ubicacion(ruta_archivo)
    print(f"Ubicación retornada: {ubicacion}")

    # Llamar a la función para obtener latitud y longitud de Google Maps
    latitud, longitud = obtener_coordenadas(ubicacion)
    print(f"Latitud: {latitud}, Longitud: {longitud}")

    # Llamar a la función para crear la carpeta con la ubicación
    ruta_carpeta = crear_carpeta_ubicacion(ubicacion)
    print(f"Carpeta creada en: {ruta_carpeta}")

    # Descargar los datos horarios de la NASA usando la API
    ruta_archivo_csv_hourly = descargar_datos_nasa_api(latitud, longitud, ruta_carpeta, ubicacion)
    print(f"Archivo horario descargado: {ruta_archivo_csv_hourly}")

    # Descargar los datos mensuales de la NASA usando la API
    ruta_archivo_csv_monthly = descargar_datos_nasa_api_monthly(latitud, longitud, ruta_carpeta, ubicacion)
    print(f"Archivo mensual descargado: {ruta_archivo_csv_monthly}")

    # Procesar y pegar los datos horarios en el archivo Excel
    procesar_y_pegar_datos_horarios(ruta_carpeta, ubicacion)

    # Procesar y pegar los datos mensuales en el archivo Excel
    procesar_y_pegar_datos_mensuales(ruta_carpeta, ubicacion)

if __name__ == "__main__":
    main()
