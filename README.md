<p align="center">
    <img src="https://python-poetry.org/images/logo-origami.svg" width="80" alt="Poetry Logo" style="display: inline-block; margin-right: 10px;"/>
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="350" alt="FastAPI Logo" style="display: inline-block; margin-left: 10px;"/>
</p>

# FAST API ARQUITECTURA HEXAGONAL TEMPLATE

Bienvenido al template de **FAST API ARQUITECTURA HEXAGONAL**.

## Requisitos Previos

Para trabajar en este proyecto, necesitarás:

- ![Python](https://img.shields.io/badge/Python-3.11.8-blue.svg)
- [![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-blueviolet.svg)](https://python-poetry.org/docs/#installation)

## Instalación

Sigue los pasos a continuación para iniciar tu entorno de desarrollo:

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/BrayansStivens/fastapi_template.git
   ```

2. **Navegar a la carpeta del backend:**

   ```bash
   cd fastapi_template
   ```

3. **Instalar las dependencias con Poetry:**

   ```bash
   poetry install
   ```

4. **Activar el entorno virtual:**
   ```bash
   poetry shell
   ```

## Uso

Para poner en marcha el servidor de desarrollo:

1. **Iniciar FastAPI:**

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

   El flag `--reload` permite que el servidor se reinicie automáticamente al realizar cambios en el código.

## Testing

Para ejecutar los tests del proyecto:

1. **Correr pruebas:**
   ```bash
   poetry run pytest
   ```

---

Para más información sobre cómo usar **FastAPI** y **Poetry**, visita la [documentación de FastAPI](https://fastapi.tiangolo.com/) y la [documentación de Poetry](https://python-poetry.org/docs/).

## Arquitectura Hexagonal y Vertical Slicing

La arquitectura hexagonal, también conocida como patrón de puertos y adaptadores, es un marco de diseño que promueve la separación entre la lógica de negocio de una aplicación y los mecanismos por los cuales esa lógica es accesible tanto desde fuera como desde dentro. La 'forma hexagonal' se deriva de la idea de que se pueden tener múltiples puntos de interacción (puertos) alrededor de la aplicación, a los cuales se conectan diversos adaptadores, sin afectar el núcleo central de la lógica de negocio.

El vertical slicing, en el contexto de esta arquitectura, se refiere a la creación de características o módulos que atraviesan todas las capas necesarias, desde la interfaz de usuario o el punto de entrada hasta la persistencia de datos. Cada 'slice' representa una funcionalidad completa y es vertical en el sentido de que conecta todas las capas lógicas necesarias para completar una operación o proceso.


## Estructura del Proyecto

```bash
my_fastapi_app/
│
├── app/                                 # Carpeta principal de la aplicación
│   ├── api/                             # Capa de adaptadores de entrada para la API
│   │   ├── common/                      # Funcionalidades comunes a todas las versiones
│   │   │   ├── health/                  # Endpoints de chequeos de salud
│   │   │   │   └── health_controller.py # Controladores para los endpoints de salud
│   │   │   ├── dashboard/               # Endpoints del dashboard de administración
│   │   │   │   └── dashboard_controller.py # Controladores para el dashboard
│   │   │   └── main_common.py           # Punto de entrada para funcionalidades comunes (opcional)
│   │   │
│   │   ├── v1/                          # Versión 1 de la API
│   │   │   ├── <feature>/               # Módulo de una característica específica
│   │   │   │   ├── application/         # Capa de aplicación con servicios y casos de uso
│   │   │   │   ├── domain/              # Capa de dominio con entidades y reglas de negocio
│   │   │   │   ├── infrastructure/      # Capa de infraestructura con detalles de implementación
│   │   │   │   └ <feature>_controller.py #Controladores de FastAPI para las rutas de la característica
│   │   │   └── main_v1.py               # Punto de entrada de la versión 1 de la API
│   │   │
│   │   ├── v2/                          # Versión 2 de la API
│   │   │   ├── <feature>/                   # Ejemplo de característica actualizada
│   │   │   │   ├── application/
│   │   │   │   ├── domain/
│   │   │   │   ├── infrastructure/
│   │   │   │   └── <feature>_controller.py
│   │   │   └── main_v2.py               # Punto de entrada de la versión 2 de la API
│   │   │
│   │   └── main.py                      # Archivo principal que podría redirigir a versiones específicas
│   │
│   ├── core/                            # Configuración central y componentes compartidos de la aplicación
│   │   ├── config.py                    # Configuración central de la aplicación
│   │   └── security.py                  # Utilidades de seguridad comunes
│   │
│   └── main.py                          # Punto de entrada general de la aplicación FastAPI
│
├── tests/
│   ├── api_tests/                       # Pruebas para los endpoints de la API
│   │   ├── common/                      # Tests para funcionalidades comunes
│   │   │   ├── health_tests/
│   │   │   └── dashboard_tests/
│   │   ├── v1/                          # Pruebas para la versión 1 de la API
│   │   │   ├── <feature>_tests/         # Pruebas específicas para una característica
│   │   │   └── ...
│   │   ├── v2/                          # Pruebas para la versión 2 de la API
│   │   │   ├── <feature>_tests/
│   │   │   └── ...
│   │   └── ...
│   └── ...
│
├── requirements.txt                     # Dependencias del proyecto
└── README.md                            # Documentación del proyecto
```

## Explicación de la Estructura

- `api/`: Contiene módulos individuales y el archivo main.py. Cada módulo encapsula su propia lógica distribuida en capas de application, domain, e infrastructure.
- `api/<feature_name>/`: Cada subdirectorio dentro de api/ corresponde a una característica específica, como auth para autenticación. Dentro de este módulo, se encuentran:
  - `application/`: Contiene servicios que orquestan las operaciones de dominio y coordinan la lógica de negocio.
  - `domain/`: Define las entidades y las reglas de negocio fundamentales de la característica.
  - `infrastructure/`: Gestiona los detalles de implementación técnica, como la interacción con la base de datos.
  - `api/<feature_name>_controller.py`: Actúa como adaptador de entrada, manejando las solicitudes HTTP y delegándolas a la capa de aplicación.
- `api/main.py`: Agrega y configura las rutas de todos los módulos de la API, estableciendo sus prefijos y etiquetas.
- `app/main.py`: Punto de entrada de la aplicación FastAPI que integra api_router y configura aspectos globales como middleware y CORS.
- `core/`: Configuraciones y componentes compartidos que son fundamentales para la operación de la aplicación pero no están vinculados a una característica específica.
- `core/config/`: Se utiliza para centralizar toda la configuración de la aplicación, facilita la gestión del comportamiento de la aplicacióne en diferentes entornos como (develop, testing y production). Incluyendo configuraciónes de bases de datos, claves secretas y parámetros de API externas.
- `core/security/`: Gestionar y almacenar todos los utilitarios y configuraciones relacionadas con la seguridad de la aplicación.
- `common/`: Incluyen las funcionalidades que son comunes y reutilizables independiente de la versión.

Con esta estructura, la aplicación aprovecha una organización modular y clara. Esta disposición no solo facilita la escalabilidad y el mantenimiento, sino que también favorece prácticas de desarrollo como la integración y entrega continuas (CI/CD), permitiendo colaboraciones paralelas y eficientes entre equipos en diferentes características.