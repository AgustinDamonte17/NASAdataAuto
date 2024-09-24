import openpyxl

def leer_ubicacion(ruta_archivo):
    # Abrir el archivo Excel
    libro = openpyxl.load_workbook(ruta_archivo, data_only=True)
    
    # Seleccionar la hoja llamada "Ubicación"
    hoja = libro['Ubicación']
    
    # Leer el valor de la celda B2
    ubicacion = hoja['B2'].value
    
    # Mostrar la ubicación leída para verificar
    print(f"Ubicación leída: {ubicacion}")
    
    # Cerrar el archivo Excel
    libro.close()
    
    # Retornar la ubicación leída
    return ubicacion