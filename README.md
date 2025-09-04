# Flying to the moon

## Requisitos

- python 3.13
- uv (https://github.com/astral-sh/uv)
- task (https://taskfile.dev)

  Nota: puedes correr los comandos que se encuentran en el archivo `Taskfile.yml` en lugar de los comandos que en este readme aparecen.

## Cómo correrlo

### En local

```pwsh
task run
```

### Con docker-compose

```pwsh
task docker-compose
```

## Configuraciones

Los valores que aparecen son los configurados por defecto.

```ini
DB__HOST=localhost
DB__PORT=28015
DB__NAME=test

MISC__LOG_LEVEL=DEBUG
```
