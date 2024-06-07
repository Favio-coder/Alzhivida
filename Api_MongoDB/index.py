from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, jsonify
import json
import os

# Crear la aplicación Flask
app = Flask(__name__)

# URI de conexión a la base de datos (mejor usar variables de entorno para mayor seguridad)
uri = os.getenv("MONGO_URI", "mongodb+srv://alzhivida:RaWKHqs9L9X6vWTg@datasets.zyv34gg.mongodb.net/?retryWrites=true&w=majority&appName=datasets")

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

# Ruta relativa para el directorio que contiene los archivos JSON
directorio_json = os.path.join(os.getcwd(), "prueba")

# Verificar si el directorio existe
if not os.path.exists(directorio_json):
    raise FileNotFoundError(f"El directorio '{directorio_json}' no existe.")

# Lista de archivos JSON en el directorio
archivos_json = os.listdir(directorio_json)

# Ruta para insertar datos desde cada archivo JSON
@app.route("/insertar-datos", methods=["GET"])
def insertar_datos():
    for archivo in archivos_json:
        ruta_archivo = os.path.join(directorio_json, archivo)
        datos_json = cargar_datos_desde_json(ruta_archivo)
        
        try:
            resultado = pruebas.insert_many(datos_json)
            print(f"Datos insertados desde '{archivo}' con éxito. IDs:", resultado.inserted_ids)
        except Exception as e:
            print(f"Error al insertar datos desde '{archivo}':")
            print(e)
    return jsonify({"mensaje": "Datos insertados con éxito."})

# Función para mandar registros a la colección 'training'
@app.route("/insertar-training", methods=["GET"])
def cargar_json_training():
    for archivo in archivos_json:
        ruta_archivo = os.path.join(directorio_json, archivo)
        datos_json = cargar_datos_desde_json(ruta_archivo)

        try:
            resultado = training.insert_many(datos_json)
            print(f"Datos insertados desde '{archivo}' con éxito. IDs:", resultado.inserted_ids)
        except Exception as e:
            print(f"Error al insertar datos a la colección training desde '{archivo}':")
            print(e)
    return jsonify({"mensaje": "Datos insertados en training con éxito."})

# Inicio de la aplicación
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
