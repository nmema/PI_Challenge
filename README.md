## PI Data Engineer Challenge

El [desafio](https://github.com/nmema/PI_Challenge/blob/master/resources/pi-data-challenge.pdf) es recuperar la base de datos, limpiarla y **crear un proceso de carga** que corra los lunes a las 5 am.

Para esto primero corremos el [script](https://github.com/nmema/PI_Challenge/blob/master/scripts/db_setup.sql) que restaura la base de datos, limpia duplicados en dbo.Unificados y crea la tabla dbo.etl_log.
```
sqlcmd -S localhost -U <user> -P <password> -i scripts/db_setup.sql
```

Luego esta el [proceso](https://github.com/nmema/PI_Challenge/blob/master/crontab) que realiza la carga del archivo csv a la base de datos.


