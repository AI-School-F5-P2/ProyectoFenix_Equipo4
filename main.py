from fastapi import FastAPI
from router import download_router
from router.router import user
from router.inscriptions_router import inscriptions_router
from router.class_router import classes_router
from router.professors_router import professor_router
from router.manager_router import manager_router
from router.students_router import student_router
from router.descuentos_router import descuentos_router
from router.descuentos_alumnos_router import descuentos_alumnos_router
from tags import tags_metadata
from router import download_router

description = """
Bienvenido a la API de Danza Fénix. 

## Crear, buscar, actualizar y eliminar.

Con esta API podrás:

* **Crear usuarios e indicar su rol dentro de la academia: managers, alumnos, profesores** 
* **Crear y modificar fichas de inscripción para los alumnos** 
* **Crear y modificar las clases ofrecidas**
* **Obtener rápidamente el precio final según las inscripciones del alumno**
* **Agregar o modificar los descuentos ofrecidos**



"""


app = FastAPI(openapi_tags=tags_metadata, title="Danza Fénix API",
    description=description,
    summary="Sistema de gestión de Danza Fénix",
    version="0.0.1",
   )

app.include_router(download_router.router)
app.include_router(user)
app.include_router(inscriptions_router)
app.include_router(classes_router)
app.include_router(professor_router)
app.include_router(manager_router)
app.include_router(student_router)
app.include_router(descuentos_router)
app.include_router(descuentos_alumnos_router)
app.include_router(download_router.router)
