# Flying to the moon

## Requisitos

- python 3.13
- uv (https://github.com/astral-sh/uv)
- task (https://taskfile.dev)

  Nota: puedes correr los comandos que se encuentran en el archivo `Taskfile.yml` en lugar de los comandos que en este readme aparecen.

Las tres herramientas deben estar en el PATH.

## Cómo correrlo

### En local

```bash
task run
```

### Con docker-compose

```bash
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

## Decisiones de diseño y lineamientos

### Modelo

En el documento de cada vuelo, viene información de los pasajeros. Estos, a priori y al tener un id, podríamos separarlos en una tabla distinta y simplemente referenciarlos en la tabla de los vuelos, pero se contemplaron los siguientes casos:

- Pasa el tiempo y el mismo pasajero vuelve a viajar, pero su edad es ahora mayor.
- Por algún error en otro sistema, nos llegan dos pasajeros con el mismo id.

En el primer caso, no queremos actualizar la edad porque podría dificultar la búsqueda y se perderían registros (dada la información que tenemos), mientras que en el segundo, no queremos sobreescribir la data de un pasajero con la data de otro.

Y para terminar, los únicos datos que sí son "propios" del pasajero como tal y que no dependen del vuelo son su nombre y edad.

### Sobre idiomas

Código y comentarios en inglés, documentación en español.

Sólo en casos en que sea imprescindible que todos entiendan perfectamente un comentario, se agregará una versión del mismo en español además del original en inglés.
