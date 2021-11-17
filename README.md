# Accounts_BUDA

En base a la DB [accounts](accounts.sql), se responden las siguientes preguntas:

- ¿Cuánto se ha transado por país de residencia en los últimos 30 días?
- ¿Cuánto es lo máximo que ha transado un usuario en los últimos 30 días por cada país de residencia?
- ¿Qué día se crearon la mayor cantidad de cuentas para cada país de residencia?
- Cantidad porcentual de usuarios inactivos por cada país, entendiendo como usuario inactivo aquel usuario que no tienen monto transado en los últimos 30 días.
- ¿Cuántos usuarios con verificación básica o avanzada no han operado en los últimos 30 días?

## Su construcción

Para ello utilicé Python y SQLite3, con esto es posible crear la base de datos y realizar las consultas. Cada consulta está dentro de la constante QUERIES, con la pregunta respectiva, en el archivo [constants.py](constants.py).

## Ejecución

> El programa fue hecho con Python v3.9, para ejecutar [main.py](main.py) se aconseja utilizar Python versión >= 3.8.

Antes de ejecutar todo es necesario instalar los requirements:
``` console
$ pip install -r requirements.txt
```

Para ejecutar la creación de la base de datos y las consultas.

```console
$ python3 main.py -f file.sql
```

En el caso de no querer ejecutar el archivo SQL, se debe agregar `-n`.

```console
$ python3 main.py -d file.sqlite3
# Or
$ python3 main.py -nf file.sql
```
