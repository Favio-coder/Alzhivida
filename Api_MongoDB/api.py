from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson.json_util import dumps, ObjectId

app = Flask(__name__)
api = Api(app)

# URI de conexión a la base de datos
uri = "mongodb+srv://alzhivida:RaWKHqs9L9X6vWTg@datasets.zyv34gg.mongodb.net/?retryWrites=true&w=majority&appName=datasets"
#Si no funciona el url, me escriben para pasarles una nueva url actualizado 

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
            return {"message": "Conexión a la base de datos exitosa"}, 200
        except Exception as e:
            return {"message": "Error al conectar a la base de datos", "error": str(e)}, 500
        
class Datos_preguntas(Resource):
    def get(self, id=None):
        if id:
            data = preguntas.find_one({"id_pregunta": ObjectId(id)})
            if data:
                return dumps(data)
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
    def post(self):
        data = request.json
        if data:
            result = preguntas.insert_one(data)
            return {"message": "Datos insertados correctamente", "id": str(result.inserted_id)}, 201
        else:
            return {"message": "No se proporcionaron datos para insertar"}, 400
    def put(self, id):
        data = request.json 
        if data: 
            result = preguntas.update_one({"id_pregunta" : ObjectId(id)}, {"Modificación" : data})
            if result.modified_count:
                return {"message": "Datos actualizados correctamente"}, 200
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        else:
            return {"message": "No se proporcionaron datos para actualizar"}, 400
    def delete(self, id):
        result = preguntas.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return {"message": "Datos eliminados correctamente"}, 200
        else:
            return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        
class Datos_respuestas(Resource):
    def get(self, id=None):
        if id:
            data = respuestas.find_one({"id_pregunta": ObjectId(id)})
            if data:
                return dumps(data)
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
    def post(self):
        data = request.json
        if data:
            result = respuestas.insert_one(data)
            return {"message": "Datos insertados correctamente", "id": str(result.inserted_id)}, 201
        else:
            return {"message": "No se proporcionaron datos para insertar"}, 400
    def put(self, id):
        data = request.json 
        if data: 
            result = respuestas.update_one({"id_pregunta" : ObjectId(id)}, {"Modificación" : data})
            if result.modified_count:
                return {"message": "Datos actualizados correctamente"}, 200
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        else:
            return {"message": "No se proporcionaron datos para actualizar"}, 400
    def delete(self, id):
        result = respuestas.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return {"message": "Datos eliminados correctamente"}, 200
        else:
            return {"message": "No se encontraron datos con el ID proporcionado"}, 404

class Datos_training(Resource):
    def get(self, id=None):
        if id:
            data = training.find_one({"id_pregunta": ObjectId(id)})
            if data:
                return dumps(data)
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
    def post(self):
        data = request.json
        if data:
            result = training.insert_one(data)
            return {"message": "Datos insertados correctamente", "id": str(result.inserted_id)}, 201
        else:
            return {"message": "No se proporcionaron datos para insertar"}, 400
    def put(self, id):
        data = request.json 
        if data: 
            result = training.update_one({"id_pregunta" : ObjectId(id)}, {"Modificación" : data})
            if result.modified_count:
                return {"message": "Datos actualizados correctamente"}, 200
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        else:
            return {"message": "No se proporcionaron datos para actualizar"}, 400
    def delete(self, id):
        result = training.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return {"message": "Datos eliminados correctamente"}, 200
        else:
            return {"message": "No se encontraron datos con el ID proporcionado"}, 404

class Datos(Resource):
    def get(self, id=None):
        if id:
            data = collection.find_one({"_id": ObjectId(id)})
            if data:
                return dumps(data)
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        else:
            data = collection.find()
            return dumps(data)
    
    def post(self):
        data = request.json
        if data:
            result = collection.insert_one(data)
            return {"message": "Datos insertados correctamente", "id": str(result.inserted_id)}, 201
        else:
            return {"message": "No se proporcionaron datos para insertar"}, 400
    
    def put(self, id):
        data = request.json
        if data:
            result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
            if result.modified_count:
                return {"message": "Datos actualizados correctamente"}, 200
            else:
                return {"message": "No se encontraron datos con el ID proporcionado"}, 404
        else:
            return {"message": "No se proporcionaron datos para actualizar"}, 400
    
    def delete(self, id):
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return {"message": "Datos eliminados correctamente"}, 200
        else:
            return {"message": "No se encontraron datos con el ID proporcionado"}, 404

api.add_resource(Conexion, '/conexion')
api.add_resource(Datos, '/pruebas', '/pruebas/<string:id>')
api.add_resource(Datos_preguntas, '/preguntas', '/preguntas/<string:id>')
api.add_resource(Datos_respuestas, '/respuestas', '/respuestas/<string:id>')
api.add_resource(Datos_training, '/training', '/training/<string:id>')


if __name__ == '__main__':
    app.run(debug=True)
