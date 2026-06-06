# Actividad 6 – Desarrollo de Servidor MCP para Gestión de Inventario

## Integrantes
- Edwin Leonardo Rocha
- Viviana Caterine Lopez

## Descripción
Se desarrolló un servidor MCP utilizando FastMCP y SQLite 
para la gestión de inventario de productos, implementando 
operaciones CRUD y herramientas analíticas que permiten 
a un modelo de lenguaje interactuar con datos reales.


## Tecnologías utilizadas
- Python 3.12
- FastMCP
- SQLite
- Git
- GitHub

## Estructura del proyecto
| Archivo | Descripción |
|---------|-------------|
| `server.py` | Servidor MCP con herramientas CRUD y analíticas |
| `database.py` | Inicialización de la base de datos SQLite |
| `test_server.py` | Script de pruebas funcionales |
| `requirements.txt` | Dependencias del proyecto |
| `inventory.db` | Base de datos (se genera automáticamente) |
| `README.md` | Este archivo |

## Requisitos previos
- Python 3.8 o superior
- Git instalado

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/erochac2/Computacion-Cognitiva.git
cd Computacion-Cognitiva
```

### 2. Crear el entorno virtual
```bash
python3.12 -m venv venv
```

### 3. Activar el entorno virtual
```bash
# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Ejecución

### Ejecutar las pruebas funcionales
```bash
python test_server.py
```

### Iniciar el servidor MCP
```bash
python server.py
```

## Funcionalidades

### Operaciones CRUD
- Crear productos
- Consultar productos por ID
- Actualizar cantidad de productos
- Eliminar productos
- Listar todos los productos

### Herramientas analíticas
- Calcular valor total del inventario
- Consultar productos agotados
- Identificar producto más costoso
- Estadísticas generales del inventario

## Repositorio
https://github.com/erochac2/Computacion-Cognitiva