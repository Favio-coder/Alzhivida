from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson.json_util import ObjectId

app = Flask(__name__)
api = Api(app)

# URI de conexión a la base de datos
uri = "mongodb+srv://alzhivda_juan:FDKLUg8wd2N4rXHk@datasets.zyv34gg.mongodb.net/?retryWrites=true&w=majority&appName=datasets"

# Crear una conexión a la base de datos
client = MongoClient(uri)
db = client["datasets_Alzheimer"]
collection = db["pruebas"]
preguntas = db["preguntas"]
respuestas = db["respuestas"]
training = db["training"]

class Conexion(Resource):
    def get(self):
        try:
            # Verificar la conexión a la base de datos
            client.server_info()
            return {"message": "Conexión a la base de datos exitosa c:"}, 200
        except Exception as e:
            return {"message": "Error al conectar a la base de datos", "error": str(e)}, 500
        
##########################################################
class Datos_training(Resource):
    def get(self, id=None):
        try:
            if id:
                data = training.find_one({"id_training": ObjectId(id)})
                if data:
                    data['_id'] = str(data['_id'])  # Convertir ObjectId a cadena
                    return jsonify(data)
                else:
                    return {"message": "No se encontraron datos con el ID proporcionado"}, 404
            else:
                data = training.find()
                data_list = [item for item in data]  # Convertir a lista de diccionarios
                for item in data_list:
                    item['_id'] = str(item['_id'])  # Convertir ObjectId a cadena en cada documento
                return jsonify(data_list)
        except Exception as e:
            return {"message": "Error al buscar datos en la base de datos", "error": str(e)}, 500

    def post(self):
        try:
            data = request.json
            if data:
                if isinstance(data, list):  # Verificar si se proporciona una lista de documentos JSON
                    result = training.insert_many(data)
                    return {"message": "Datos insertados correctamente", "ids": [str(id) for id in result.inserted_ids]}, 201
                else:
                    result = training.insert_one(data)
                    return {"message": "Datos insertados correctamente", "id": str(result.inserted_id)}, 201
            else:
                return {"message": "No se proporcionaron datos para insertar"}, 400
        except Exception as e:
            return {"message": "Error al insertar datos en la base de datos", "error": str(e)}, 500

    def put(self, id):
        try:
            data = request.json 
            if data: 
                result = training.update_one({"id_training" : ObjectId(id)}, {"Modificación" : data})
                if result.modified_count:
                    return {"message": "Datos actualizados correctamente"}, 200
                else:
                    return {"message": "No se encontraron datos con el ID proporcionado"}, 404
            else:
                return {"message": "No se proporcionaron datos para actualizar"}, 400
        except Exception as e:
            return {"message": "Error al actualizar datos en la base de datos", "error": str(e)}, 500

    def delete(self, id):
        try:
            result = training.delete_one({"_id": ObjectId(id)})
            if result.deleted_count:
                return {"message": "Datos eliminados correctamente"}, 200
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        except Exception as e:
            return {"message": "Error al eliminar datos en la base de datos", "error": str(e)}, 500

################################################################
class Datos_preguntas(Resource):
    def get(self, id=None):
        try:
            if id:
                data = preguntas.find_one({"id_pregunta": ObjectId(id)})
                if data:
                    data['_id'] = str(data['_id'])  # Convertir ObjectId a cadena
                    return jsonify(data)
                else:
                    return {"message": "No se encontraron datos con el ID proporcionado"}, 404
            else:
                data = preguntas.find()
                data_list = [item for item in data]  # Convertir a lista de diccionarios
                for item in data_list:
                    item['_id'] = str(item['_id'])  # Convertir ObjectId a cadena en cada documento
                return jsonify(data_list)
        except Exception as e:
            return {"message": "Error al buscar datos en la base de datos", "error": str(e)}, 500

    def post(self):
        try:
            data = request.json
            if data:
                if isinstance(data, list):  # Verificar si se proporciona una lista de documentos JSON
                    result = preguntas.insert_many(data)
                    return {"message": "Datos insertados correctamente", "ids": [str(id) for id in result.inserted_ids]}, 201
                else:
                    result = preguntas.insert_one(data)
                    return {"message": "Datos insertados correctamente", "id": str(result.inserted_id)}, 201
            else:
                return {"message": "No se proporcionaron datos para insertar"}, 400
        except Exception as e:
            return {"message": "Error al insertar datos en la base de datos", "error": str(e)}, 500

    def put(self, id):
        try:
            data = request.json 
            if data: 
                result = preguntas.update_one({"id_pregunta" : ObjectId(id)}, {"Modificación" : data})
                if result.modified_count:
                    return {"message": "Datos actualizados correctamente"}, 200
                else:
                    return {"message": "No se encontraron datos con el ID proporcionado"}, 404
            else:
                return {"message": "No se proporcionaron datos para actualizar"}, 400
        except Exception as e:
            return {"message": "Error al actualizar datos en la base de datos", "error": str(e)}, 500

    def delete(self, id):
        try:
            result = preguntas.delete_one({"_id": ObjectId(id)})
            if result.deleted_count:
                return {"message": "Datos eliminados correctamente"}, 200
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        except Exception as e:
            return {"message": "Error al eliminar datos en la base de datos", "error": str(e)}, 500
##############################################################################
class Datos_respuestas(Resource):
    def get(self, id=None):
        try:
            if id:
                data = respuestas.find_one({"id_respuesta": ObjectId(id)})
                if data:
                    data['_id'] = str(data['_id'])  # Convertir ObjectId a cadena
                    return jsonify(data)
                else:
                    return {"message": "No se encontraron datos con el ID proporcionado"}, 404
            else:
                data = respuestas.find()
                data_list = [item for item in data]  # Convertir a lista de diccionarios
                for item in data_list:
                    item['_id'] = str(item['_id'])  # Convertir ObjectId a cadena en cada documento
                return jsonify(data_list)
        except Exception as e:
            return {"message": "Error al buscar datos en la base de datos", "error": str(e)}, 500

    def post(self):
        try:
            data = request.json
            if data:
                if isinstance(data, list):  # Verificar si se proporciona una lista de documentos JSON
                    result = respuestas.insert_many(data)
                    return {"message": "Datos insertados correctamente", "ids": [str(id) for id in result.inserted_ids]}, 201
                else:
                    result = respuestas.insert_one(data)
                    return {"message": "Datos insertados correctamente", "id": str(result.inserted_id)}, 201
            else:
                return {"message": "No se proporcionaron datos para insertar"}, 400
        except Exception as e:
            return {"message": "Error al insertar datos en la base de datos", "error": str(e)}, 500


    def put(self, id):
        try:
            data = request.json 
            if data: 
                result = respuestas.update_one({"id_respuesta" : ObjectId(id)}, {"Modificación" : data})
                if result.modified_count:
                    return {"message": "Datos actualizados correctamente"}, 200
                else:
                    return {"message": "No se encontraron datos con el ID proporcionado"}, 404
            else:
                return {"message": "No se proporcionaron datos para actualizar"}, 400
        except Exception as e:
            return {"message": "Error al actualizar datos en la base de datos", "error": str(e)}, 500

    def delete(self, id):
        try:
            result = respuestas.delete_one({"_id": ObjectId(id)})
            if result.deleted_count:
                return {"message": "Datos eliminados correctamente"}, 200
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        except Exception as e:
            return {"message": "Error al eliminar datos en la base de datos", "error": str(e)}, 500

###############################################
class Datos(Resource):
    def get(self, id=None):
        try:
            if id:
                data = collection.find_one({"_id": ObjectId(id)})
                if data:
                    # Convertir todos los valores a cadenas
                    for key, value in data.items():
                        data[key] = str(value)
                    return jsonify(data)
                else:
                    return {"message": "No se encontraron datos con el ID proporcionado"}, 404
            else:
                data = collection.find()
                data_list = []
                for item in data:
                    # Convertir todos los valores a cadenas en cada documento
                    document = {key: str(value) for key, value in item.items()}
                    data_list.append(document)
                return jsonify(data_list)
        except Exception as e:
            return {"message": "Error al buscar datos en la base de datos", "error": str(e)}, 500


    def post(self):
        try:
            data = request.json
            if data:
                if isinstance(data, list):  # Verificar si se proporciona una lista de documentos JSON
                    result = collection.insert_many(data)
                    return {"message": "Datos insertados correctamente", "ids": [str(id) for id in result.inserted_ids]}, 201
                else:
                    result = collection.insert_one(data)
                    return {"message": "Datos insertados correctamente", "id": str(result.inserted_id)}, 201
            else:
                return {"message": "No se proporcionaron datos para insertar"}, 400
        except Exception as e:
            return {"message": "Error al insertar datos en la base de datos", "error": str(e)}, 500


    def put(self, id):
        try:
            data = request.json
            if data:
                result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
                if result.modified_count:
                    return {"message": "Datos actualizados correctamente"}, 200
                else:
                    return {"message": "No se encontraron datos con el ID proporcionado"}, 404
            else:
                return {"message": "No se proporcionaron datos para actualizar"}, 400
        except Exception as e:
            return {"message": "Error al actualizar datos en la base de datos", "error": str(e)}, 500

    def delete(self, id):
        try:
            result = collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count:
                return {"message": "Datos eliminados correctamente"}, 200
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        except Exception as e:
            return {"message": "Error al eliminar datos en la base de datos", "error": str(e)}, 500

api.add_resource(Conexion, '/conexion')
api.add_resource(Datos, '/pruebas', '/pruebas/<string:id>')
api.add_resource(Datos_preguntas, '/preguntas', '/preguntas/<string:id>')
api.add_resource(Datos_respuestas, '/respuestas', '/respuestas/<string:id>')
api.add_resource(Datos_training, '/training', '/training/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
