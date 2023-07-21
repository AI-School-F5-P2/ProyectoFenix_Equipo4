from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Traer lista de clases
def test_get_classes():
    response = client.get("/api/classes")
    assert response.status_code == 200
    assert response.json() == []

# Crear una clase
def test_create_class():
    class_data = {
        "name_class": "Salsa",
        "level": "Intermediate",
        "price": 40.0,
        "pack": "1",
        "id_prof": 1
    }
    response = client.post("/api/classes", json=class_data)
    assert response.status_code == 201
    assert response.json() == {"message": "Class created successfully"}

# Traer una clase por ID
def test_get_class():
    response = client.get("/api/classes/1")
    assert response.status_code == 200
    assert response.json() == {
        "id_class": 1,
        "name_class": "Salsa",
        "level": "Intermediate",
        "price": 40.0,
        "pack": "1",
        "id_prof": 1
    }

# Actualizar una clase
def test_update_class():
    class_data = {
        "name_class": "Fouk",
        "level": "Advanced",
        "price": 35.0,
        "pack": "2",
        "id_prof": 2
    }
    response = client.put("/api/classes/1", json=class_data)
    assert response.status_code == 200
    assert response.json() == class_data

# Asignar un profesor a una clase
def test_assign_professor_to_class():
    response = client.put("/api/classes/1/assign_professor/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Professor assigned to class successfully"}

# Eliminar una clase
def test_delete_class():
    response = client.delete("/api/classes/1")
    assert response.status_code == 204
    assert response.text == ""
