# Urban Routes

## Descripción del proyecto

Este proyecto contiene pruebas automatizadas para la aplicación **Urban Routes**.

El objetivo es comprobar diferentes funcionalidades relacionadas con la configuración y solicitud de un viaje, utilizando pruebas independientes para validar cada escenario.

## Tecnologías y técnicas utilizadas

* **Python**: lenguaje utilizado para escribir las pruebas automatizadas.
* **Selenium WebDriver**: herramienta utilizada para automatizar las interacciones con el navegador.
* **Pytest**: framework utilizado para ejecutar las pruebas.
* **Page Object Model (POM)**: patrón utilizado para organizar los localizadores y métodos de la página.
* **WebDriverWait**: utilizado para esperar de forma explícita a que los elementos de la página estén disponibles.
* **Git y GitHub**: utilizados para controlar y almacenar el código del proyecto.

## Pruebas realizadas

El proyecto contiene 9 pruebas automatizadas:

1. **Establecer la ruta**: comprueba que las direcciones de origen y destino sean correctas.
2. **Seleccionar la tarifa Comfort**: comprueba que la tarifa Comfort quede seleccionada.
3. **Agregar número de teléfono**: comprueba que el número de teléfono sea confirmado y aparezca en la aplicación.
4. **Agregar tarjeta**: comprueba que la tarjeta quede seleccionada como método de pago.
5. **Agregar mensaje para el conductor**: comprueba que el mensaje ingresado sea correcto.
6. **Seleccionar manta y pañuelos**: comprueba que esta opción quede seleccionada.
7. **Agregar dos helados**: comprueba que el contador de helados llegue a 2.
8. **Buscar automóvil**: comprueba que aparezca la ventana de búsqueda de automóvil.
9. **Comprobar información del vehículo**: comprueba que aparezca el número del automóvil asignado.

## Cómo ejecutar las pruebas

### 1. Clonar el proyecto

Clona el repositorio desde GitHub y abre el proyecto en PyCharm.

### 2. Activar el entorno virtual

En la terminal de PyCharm, activa el entorno virtual:

```bash
.venv\Scripts\activate
```

### 3. Instalar las dependencias

Instala Selenium y Pytest:

```bash
python -m pip install selenium pytest
```

### 4. Ejecutar todas las pruebas

Para ejecutar las 9 pruebas:

```bash
python -m pytest main.py -v
```

También puedes ejecutar una prueba específica. Por ejemplo:

```bash
python -m pytest main.py::TestUrbanRoutes::test_set_route -v
```

## Estructura principal del proyecto

* `main.py`: contiene la clase de la página, los localizadores, los métodos y las pruebas automatizadas.
* `data.py`: contiene los datos utilizados durante las pruebas.
* `README.md`: contiene la información y las instrucciones del proyecto.
