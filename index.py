from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import os

# URI de conexión a la base de datos
uri = "mongodb+srv://alzhivida:RaWKHqs9L9X6vWTg@datasets.zyv34gg.mongodb.net/?retryWrites=true&w=majority&appName=datasets"

# Crear un cliente y conectarse al servidor
client = MongoClient(uri, server_api=ServerApi('1'))

# Seleccionar la base de datos y la colección
db = client["datasets_Alzheimer"]
pruebas = db["pruebas"]
preguntas = db["preguntas"]
respuestas = db["respuestas"]
training = db["training"]

# Función para cargar datos desde un archivo JSON
def cargar_datos_desde_json(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        datos = json.load(archivo)
    return datos

# Directorio que contiene los archivos JSON
directorio_json = r"D:\Alzhivida\Datos de entrenamiento\Mongodb\prueba"

# Lista de archivos JSON en el directorio
archivos_json = os.listdir(directorio_json)

# Insertar datos desde cada archivo JSON
for archivo in archivos_json:
    ruta_archivo = os.path.join(directorio_json, archivo)
    datos_json = cargar_datos_desde_json(ruta_archivo)
    
    # Insertar datos en la colección de pruebas
    try:
        resultado = pruebas.insert_many(datos_json)
        print(f"Datos insertados desde '{archivo}' con éxito. IDs:", resultado.inserted_ids)
    except Exception as e:
        print(f"Error al insertar datos desde '{archivo}':")
        print(e)

#Función para mandar registros a training
def cargar_json_training():
    for archivo in archivos_json:
        ruta_archivo = os.path.join(directorio_json, archivo)
        datos_json = cargar_datos_desde_json(ruta_archivo)

        #Insertar datos en la colección de training
        try:
            resultado = training.insert_many(datos_json)
            print(f"Datos insertados desde '{archivo}' con éxito. IDs:", resultado.inserted_ids)
        except Exception as e:
            print(f"Error al insertar datos a la colección training desde '{archivo }':")
            print(e)