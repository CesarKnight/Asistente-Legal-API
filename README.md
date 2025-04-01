# Asistente Legal API

Aplicación RAG y API para Asistente Legal de tránsito Bolivia.

## Requisitos Previos

- Python 3.13 o superior
- Poetry (Gestor de paquetes)

## Instalación

1. Clonar el repositorio:
```sh
git clone [url-del-repositorio]
cd asistente-api
```

2. Configurar Poetry para crear el entorno virtual en el proyecto:
```sh
poetry config virtualenvs.in-project true
```

3. Instalar dependencias:
```sh
poetry install --no-root
```

4. Configurar variables de entorno:
   - Copiar el archivo `.env example` a `.env`
   - Actualizar las variables en `.env` con tus credenciales:
     - `DEEPSEEK_API_KEY`: Tu clave API de DeepSeek
     - `DEEPSEEK_API_URL`: URL base de la API

## Activar el Entorno Virtual

```sh
poetry shell
```

## Ejecutar la Aplicación

[Instrucciones pendientes para ejecutar la aplicación]

## Desarrollo

Para agregar nuevas dependencias:
```sh
poetry add [nombre-del-paquete]
```