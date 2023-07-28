from fastapi import APIRouter, Response
import pandas as pd
from config.db import engine
from logger.logger import log_info

router = APIRouter()

@router.get('/descargar_alumnos', tags=["descargas"], response_class=Response, status_code=200)
def descargar_alumnos():
    # Realiza la consulta para obtener los datos relevantes de los alumnos desde la base de datos
    with engine.connect() as connection:
        query = "SELECT * FROM students;"
        results = connection.execute(query).fetchall()
    # Convierte los resultados en un DataFrame de pandas
    column_names = results[0].keys()  # Obtener los nombres de las columnas desde los resultados
    df = pd.DataFrame(results, columns=column_names)
    # Convierte el DataFrame a CSV en formato texto
    csv_data = df.to_csv(index=False)
    # Devuelve el CSV como una respuesta HTTP con el encabezado adecuado
    response = Response(content=csv_data, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=alumnos.csv"
    log_info("descargada con exito los alumnos en un csv")
    return response

@router.get('/descargar_inscripciones', tags=["descargas"],  response_class=Response, status_code=200)
def descargar_inscripciones():
    with engine.connect() as connection:
        query = "SELECT * FROM inscriptions;"
        results = connection.execute(query).fetchall()

    column_names = results[0].keys()   
    df = pd.DataFrame(results, columns=column_names) 

    csv_data = df.to_csv(index=False)

    response = Response(content=csv_data, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=inscripciones.csv"
    log_info("descargada con exito las inscripciones en un csv")

    return response