# Urban Routes

## Descripción del proyecto

Este proyecto contiene pruebas automatizadas para la aplicación **Urban Routes**.

El objetivo es comprobar que un usuario pueda configurar un viaje correctamente, incluyendo la selección de la ruta, la tarifa, el número de teléfono, el método de pago y diferentes opciones del viaje.

## Tecnologías y técnicas utilizadas

* **Python**: lenguaje utilizado para escribir las pruebas automatizadas.
* **Selenium WebDriver**: herramienta utilizada para automatizar las interacciones con el navegador.
* **Pytest**: framework utilizado para ejecutar las pruebas.
* **Page Object Model (POM)**: patrón utilizado para organizar los localizadores y métodos de la página.
* **WebDriverWait**: utilizado para esperar de forma explícita a que los elementos de la página estén disponibles.
* **Git y GitHub**: utilizados para controlar y almacenar el código del proyecto.

## Pruebas realizadas

Las pruebas automatizadas comprueban, entre otros aspectos:

* Introducción de la dirección de origen y destino.
* Selección de la tarifa Comfort.
* Introducción y confirmación del número de teléfono.
* Agregado de una tarjeta bancaria.
* Introducción de un mensaje para el conductor.
* Selección de manta y pañuelos.
* Agregado de dos helados.
* Solicitud del taxi.
* Comprobación de la búsqueda del automóvil.
* Comprobación de la información del vehículo después de la asignación del conductor.

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

### 4. Ejecutar las pruebas

Para ejecutar todas las pruebas:

```bash
python -m pytest -v
```

También puedes ejecutar específicamente la prueba de Urban Routes:

```bash
python -m pytest main.py::TestUrbanRoutes::test_set_route -v
```

## Estructura principal del proyecto

* `main.py`: contiene la clase de la página, los localizadores, los métodos y la prueba automatizada.
* `data.py`: contiene los datos utilizados durante la prueba.
* `README.md`: contiene la información y las instrucciones del proyecto.
