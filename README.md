# API Escuela de Danza Fenix - Documentacion Oficial

## Introducción

El manejo de datos de manera efectiva se ha convertido en un pilar fundamental para el buen funcionamiento de las empresas y su capacidad de crecimiento rápido. No solo busca lograr una claridad interna, sino también permitir un crecimiento efectivo. El manejo adecuado de datos es una característica distintiva de las empresas exitosas.

Llevar registros en papel y lápiz se ha vuelto ineficiente y propenso a errores, especialmente cuando se trata de manejar grandes cantidades de información de los usuarios a los que se les ofrece un servicio. El registro manual de esta cantidad de datos es lento, ineficaz y propenso a errores.

Las empresas necesitan un sistema confiable para registrar la información de manera efectiva y una forma fácil de acceder a ella cuando la necesiten. En la actualidad, las inversiones en el desarrollo de tecnologías que cumplan con los requisitos básicos de manejo de datos son esenciales para las empresas.

* El buen manejo de datos ofrece varios beneficios:

1. Claridad y organización: Permite a las empresas tener una visión clara y organizada de la información que poseen, lo que les ayuda a comprender mejor su negocio y tomar decisiones informadas.

2. Eficiencia y productividad: Utilizar tecnologías adecuadas para el manejo de datos agiliza los procesos, ahorra tiempo y recursos, y aumenta la productividad de la empresa.

3. Toma de decisiones basada en datos: Contar con datos confiables y precisos es fundamental para tomar decisiones fundamentadas y estratégicas.

4. Mejora de la satisfacción del cliente: Un buen manejo de datos permite a las empresas personalizar productos o servicios, anticipar las necesidades de los clientes y brindarles una experiencia satisfactoria.

5. Cumplimiento normativo y seguridad de datos: Las empresas deben cumplir con las regulaciones y normativas de protección de datos para garantizar la confidencialidad y privacidad de la información de los clientes.

En resumen, el manejo efectivo de datos es esencial para el crecimiento y éxito empresarial. Las inversiones en tecnologías adecuadas son necesarias para manejar la gran cantidad de datos de manera confiable y eficiente, y aprovechar al máximo su potencial para impulsar el crecimiento y la toma de decisiones informadas.

## Solución

Escuela de Danza Fénix una API CRUD de alta calidad y accesible para facilitar el manejo empresarial. Esta API proporciona todas las herramientas necesarias para gestionar de manera eficiente la información de la escuela.

La API está diseñada para interactuar con una base de datos MySQL alojada en el localhost, utilizando el puerto 3306, y con las credenciales de usuario "root" y contraseña "admin". Está construida sobre una base de Python 3 y SQLAlchemy, y utiliza FastAPI como estructura principal. FastAPI nos brinda una documentación accesible, detalles completos sobre su funcionamiento y pruebas claras para verificar su correcto funcionamiento.

* Estas son algunas de las características y beneficios clave de nuestra API CRUD:

1. Creación de registros: Permite crear nuevos registros en la base de datos, lo que facilita la captura de información relevante para la escuela de danza, como datos de estudiantes, profesores, horarios de clases, etc.

2. Búsqueda de información: Proporciona la capacidad de buscar y filtrar la información almacenada en la base de datos. Esto permite acceder rápidamente a los datos necesarios según criterios específicos, como buscar estudiantes por nombre, profesores por especialidad, etc.

3. Actualización de registros: Permite actualizar la información existente en la base de datos. Esto es útil cuando se requiere corregir errores, actualizar detalles o realizar cambios en la información almacenada.

4. Eliminación de registros: Proporciona la funcionalidad para eliminar registros de la base de datos cuando ya no sean necesarios. Esto ayuda a mantener una base de datos limpia y actualizada.

5. Documentación clara: FastAPI nos brinda una documentación detallada y accesible, lo que facilita a los desarrolladores y usuarios comprender cómo utilizar la API, qué endpoints están disponibles, qué parámetros se requieren, etc. Esto ayuda a maximizar la eficiencia y la claridad en el manejo de la información.

En resumen, nuestra API CRUD creada en Python 3 y SQLAlchemy, con FastAPI como estructura principal, ofrece una solución de gestión de datos confiable, accesible y de alta calidad para la Escuela de Danza Fénix. Estamos comprometidos con brindar las herramientas necesarias para un manejo empresarial efectivo y eficiente.

## Instalación

### Importante: Es necesario tener instalado Python en tu sistema 

1. Descargar el repositorio en: https://github.com/AI-School-F5-P2/ProyectoFenix_Equipo4.git
2. Descargar e instalar MySQL para crear el servidor
3. Utiliza la terminal o cualquier IDE de código como Visual Studio Code (VSC) y posiciónate en la carpeta.
4. Instala el archivo `requirements.txt` con el comando `pip install -r requirements.txt`.


## Paso a Paso

Con la instalación y configuración de la API y la base de datos, podrás gestionar y navegar fácilmente para lograr una buena administración. A continuación, te proporciono los siguientes pasos que te permitirán comprender rápidamente el funcionamiento:

1. Una vez instalada la API, ejecuta el siguiente comando en la terminal para iniciar el programa: python -m uvicorn main:app --reload. Esto iniciará el servidor y se mostrará en la terminal que ha sido ejecutado correctamente. También se proporcionará una dirección URL, como por ejemplo http://127.0.0.1:8000.

2. Copia la dirección URL proporcionada en la barra de búsqueda de tu navegador y agrega /docs al final de la misma. Por ejemplo, la URL final debería verse así: http://127.0.0.1:8000/docs. Al acceder a esta URL, se abrirá una interfaz que te permitirá trabajar con la API de manera interactiva.

3. En la interfaz de la API, encontrarás diferentes pestañas que hacen referencia a diferentes acciones, identificadas por las palabras clave GET, POST, PUT y DELETE. A continuación, se explica el significado de cada una de estas acciones:

- GET: Permite obtener información de la base de datos.
- POST: Permite agregar nueva información a la base de datos.
- PUT: Permite actualizar información existente en la base de datos.
- DELETE: Permite eliminar información de la base de datos, ya sea de forma específica o completa.

4. Dentro de cada pestaña, encontrarás enlaces que especifican las rutas de los endpoints correspondientes a cada acción. Por ejemplo: /api/user/, /api/user/{user_id}, /api/inscription, entre otros.

5. Para utilizar un servicio específico, accede a la pestaña correspondiente y haz clic en el recuadro "Try it out". Esto abrirá un cuadro donde podrás editar los valores de los parámetros necesarios para ejecutar la acción seleccionada. Por ejemplo, podrás editar los valores de id_user, type_user y password.

6. Para comenzar a administrar los datos, es recomendable registrar a los usuarios primero. Utiliza la opción POST en la pestaña /api/user para registrar los usuarios en la base de datos. Cada usuario debe tener un id_user único. Se sugiere utilizar el rango de códigos del 1000 al 2000 para los registros de usuarios. **RECOMENDACION:** puedes asignar los códigos del 1001 al 1010 para el administrador (manager) y del 1011 al 1050 para los profesores. A partir del código 1051 en adelante hasta el 1999, puedes registrar a los estudiantes.

7. Recomendamos seguir el mismo proceso anterior para registrar la información relacionada con las clases y los descuentos en la base de datos. Utiliza las pestañas POST correspondientes a "/api/classes" y "/api/discounts" con algunas diferencias en los códigos utilizados para los IDs de cada uno. A continuación, te proporciono los códigos sugeridos para cada clase y cada descuento:

- Clases:

* Bachata cero: 100
* Bachata iniciación: 101
* Bachata medio: 102
* Bachata avanzada: 103
* Salsa iniciación: 201
* Salsa medio: 202
* Kizomba iniciación: 301
* Kizomba medio: 302
* Kizomba avanzada: 303
* Estilo para todos: 404
* Lady Style: 504
* Role Rotation iniciación: 601
* Role Rotation medio: 602
* Pilates: 704
* Yoga: 804
* Flamenco: 904
* Zouk iniciación: 911
* Zouk medio: 912

- Descuentos: No es necesario asignar códigos específicos para los descuentos. Solo debes proporcionar el valor del descuento y el tipo de descuento.

8. Para la pestaña de inscripciones, se repetirá el proceso anterior. El ID de inscripciones comenzará a partir del código 4000 en adelante. Los campos a completar serán:

- ID de inscripciones: Se utilizarán los códigos identificadores a partir de 4000.
- ID de usuario: se utilizan el codigo ya registrado
- Status: Indicará si la inscripción está activa o no.
- Día de comienzo: Se ingresará la fecha de inicio de la inscripción.
- ID de clases: Se completará con el código identificador de cada clase.
- Fecha de finalización: Se registrará la fecha en la que la inscripción finaliza.

9. En la pestaña de estudiantes, se utilizará el código 5001 en adelante para el ID de estudiante. Los campos a rellenar serán los 
siguientes:

- ID de estudiante: Se utilizarán los códigos identificadores a partir de 5000.
- Resto de campos solicitados: Se completarán los campos adicionales requeridos, como nombre, apellido, fecha de nacimiento, dirección, correo electrónico, etc.

10. En la pestaña de profesores, se utilizará el código 4001 en adelante para el ID de profesor. Los campos a rellenar serán los siguientes:

- ID de profesor: Se utilizarán los códigos identificadores a partir de 1000.
- Resto de campos solicitados: Se completarán los campos adicionales requeridos, como nombre y apellido.

11. En la pestaña de manager, se utilizará el código 2001 en adelante para el ID de profesor. Los campos a rellenar serán los siguientes:

- ID de profesor: Se utilizarán los códigos identificadores a partir de 2000.
- Resto de campos solicitados: Se completarán los campos adicionales requeridos, como nombre, apellido, fecha de nacimiento, dirección, correo electrónico, etc.

## IMPORTANTE ACLARAR

1. Los códigos de Id de usuario, profesor, estudiante y manager son diferentes entre sí. Es recomendado respetar estos códigos para mantener una organización adecuada.

2. Hay dos formas de acceder a la información. La primera es a través de una vista general donde se muestran todos los valores almacenados. La segunda es utilizando el Id específico en la pestaña de "Get" para obtener información más detallada sobre un usuario en particular.

3. La pestaña "Put" se utiliza para editar o actualizar un dato específico. Primero se debe llamar al dato utilizando su Id y luego se permite realizar los cambios necesarios.

4. El método "Delete" funciona de manera similar a la pestaña "Get", pero en lugar de obtener información, se utiliza para eliminar completamente todos los datos relacionados con un usuario, estudiante, profesor o manager específico.

5. EL PROGRAMA NO CREA LA BASE DE DATOS, SE CREA A TRAVES DEL MYSQL, EJECUTANDO EL QUERY EL SIGUIENTE COMANDO: CREATE DATABASE proyectofenix;

6. El programa cuenta con sistemas de logs y test para registro y la comprobacion del buen funcionamiento. Los test estan por ahora implementados en:

**TEST**
* Crea el motor de SQLAlchemy:

- engine = create_engine(connection_string)

* Crea la base de datos (si no existe)

- engine.execute(f"CREATE DATABASE IF NOT EXISTS mydatabase;")

* Cierra la conexión del motor

- engine.dispose()

**LOGGER**
T

7. Configura la cadena de conexión de MySQL a traves del archivo "example.env". Reemplaza 'username', 'password' y 'database_name' con los valores de tu base de datos:

- MYSQL_DB='database_name'
- MYSQL_USER= 'username'
- MYSQL_PASSWORD= 'password'

**RECORDATORIO:** el cambio de valores se hace en el archivo "example.env", en los valores que se te indican. Por ultimo el nombre del archivo debe ser cambiado de "example.env" a ".env"


