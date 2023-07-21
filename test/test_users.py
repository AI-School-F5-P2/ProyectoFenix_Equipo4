from fastapi.testclient import TestClient
from main import app

client = TestClient(app=app)

#Traer lista de usuarios
def test_get_users():
    response = client.get("/api/user")
    assert response.status_code == 200
    assert response.json() == []
    
#Crear usuario
def test_create_user():
    user_data = {
        "id_user": "1",
        "type_user": "admin",
        "password": "mypassword"
    }
    response = client.post("/api/user", json=user_data)
    assert response.status_code == 201

#Traer usuario por ID
def test_get_user():
    response = client.get("/api/user/1")
    assert response.status_code == 200
    assert response.json() == {
        "id_user": "1",
        "type_user": "admin"
    }

#Actualizar usuario
def test_update_user():
    user_data = {
        "id_user": "1",
        "type_user": "user",
        "password": "newpassword"
    }
    response = client.put("/api/user/1", json=user_data)
    assert response.status_code == 200
    assert response.json() == {
        "id_user": "1",
        "type_user": "user"
    }

#Eliminar usuario
def test_delete_user():
    response = client.delete("/api/user/1")
    assert response.status_code == 204