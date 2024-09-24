import os

def crear_carpeta_ubicacion(ubicacion):
    # Definir la ruta base donde se creará la carpeta modelo
    ruta_base = r'C:\Users\adamonte\Desktop\AGUSTIN\Python\NASA auto download temp irrad'

    # Crear el nombre de la carpeta modelo
    nombre_carpeta_modelo = f"Modelo ({ubicacion})"

    # Crear la ruta completa de la carpeta modelo
    ruta_carpeta_modelo = os.path.join(ruta_base, nombre_carpeta_modelo)

    # Verificar si la carpeta modelo ya existe; si no, crearla
    if not os.path.exists(ruta_carpeta_modelo):
        os.makedirs(ruta_carpeta_modelo)
        print(f"Carpeta modelo creada: {ruta_carpeta_modelo}")
    else:
        print(f"La carpeta modelo ya existe: {ruta_carpeta_modelo}")

    # Crear el nombre de la carpeta de datos Nasa dentro de la carpeta modelo
    nombre_carpeta_datos_nasa = f"Datos Nasa ({ubicacion})"

    # Crear la ruta completa de la carpeta de datos Nasa
    ruta_carpeta_datos_nasa = os.path.join(ruta_carpeta_modelo, nombre_carpeta_datos_nasa)

    # Verificar si la carpeta de datos Nasa ya existe; si no, crearla
    if not os.path.exists(ruta_carpeta_datos_nasa):
        os.makedirs(ruta_carpeta_datos_nasa)
        print(f"Carpeta de datos Nasa creada: {ruta_carpeta_datos_nasa}")
    else:
        print(f"La carpeta de datos Nasa ya existe: {ruta_carpeta_datos_nasa}")

    return ruta_carpeta_datos_nasa
