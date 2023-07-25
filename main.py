from fastapi import FastAPI
from router.router import user
from router.inscriptions_router import inscriptions_router
from router.class_router import classes_router
from router.professors_router import professor_router
from router.manager_router import manager_router
from router.students_router import student_router
from router.descuentos_router import descuentos_router
from router.descuentos_alumnos_router import descuentos_alumnos_router


app = FastAPI()

app.include_router(user)
app.include_router(inscriptions_router)
app.include_router(classes_router)
app.include_router(professor_router)
app.include_router(manager_router)
app.include_router(student_router)
app.include_router(descuentos_router)
app.include_router(descuentos_alumnos_router)
