from fastapi.testclient import TestClient
import json
from main import app
from config.db import engine, meta_data
from model.inscriptions import inscriptions
from model.users import users
from model.classes import classes
from schema.class_schema import ClassSchema

client = TestClient(app=app)


#Crear usuario
def test_create_user():
    user_data = {
        "id_user": "982828",
        "type_user": "prueba",
        "password": "password"
    }
    response = client.post("/api/user", json=user_data)
    assert response.status_code == 201

def test_create_class():
    # Datos de prueba para la clase
    class_data = ClassSchema(
        id_class=982,
        name_class="Tango",
        level="Intermediate",
        price=45,
        pack="99"
    )

    # Realizamos la solicitud POST para crear una clase
    response = client.post("/api/classes", json=class_data.dict())

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 201
    assert response.json() == {"message": "Class created successfully"}


def test_create_inscription():
    # Datos de prueba para la inscripción
    inscription_data = {
        "id_inscription": 9999,
        "id_user": 982828,  
        "id_class": 982,  
        "type_inscription": "alumno",
        "status": True,
        "start_date": "2023-07-24",
        "finish_date": "2023-12-31"
    }

    # Realizamos la solicitud POST para crear una inscripción
    response = client.post("/api/inscriptions", json=inscription_data)

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 201
    assert response.json() == {"message": "Inscription created successfully"}



def test_get_inscriptions():
    # Realizamos la solicitud GET para obtener todas las inscripciones
    response = client.get("/api/inscriptions")

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 200



def test_delete_inscription():
    # Realizamos la solicitud DELETE para eliminar una inscripción
    response = client.delete("/api/inscriptions/9999")

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 204



#Eliminar clase
def test_delete_class():
    response = client.delete("/api/classes/982")
    assert response.status_code == 204

#Eliminar usuario
def test_delete_user():
    response = client.delete("/api/user/982828")
    assert response.status_code == 204
