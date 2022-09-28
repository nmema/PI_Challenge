-- Restore BackUp
RESTORE DATABASE [pidata] 
FROM DISK = N'/<path_to_backup>/Testing_ETL.bak'
WITH
    MOVE 'Testing_ETL' TO N'/var/opt/mssql/data/Testing_ETL.mdf', 
    MOVE 'Testing_ETL_log' TO N'/var/opt/mssql/data/Testing_ETL_log.ldf';
GO

-- Clean DataBase
USE pidata;
GO

WITH cte AS (
    SELECT 
        *,
        ROW_NUMBER() OVER(
            PARTITION BY ID, MUESTRA, RESULTADO
            ORDER BY FECHA_COPIA DESC
        ) AS row_number
    FROM dbo.Unificado
)
DELETE
FROM cte
WHERE row_number > 1;
GO

-- Log Table
CREATE TABLE etl_log (
    table_name varchar(100),
    rows_uploaded int,
    date_uploaded datetime NOT NULL DEFAULT (GETDATE())
);
GO