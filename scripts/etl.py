import datetime
import pandas as pd
from sqlalchemy import create_engine
from secrets import connection


URL = 'https://adlschallenge.blob.core.windows.net/challenge/nuevas_filas.csv?sp=r&st=2022-06-20T14:51:53Z&se=2022-12-31T22:51:53Z&spr=https&sv=2021-06-08&sr=b&sig=y9hLJFCVvGh1Ej58SXqsXTSVC6ABoVuQgfECDOd83Lw%3D'

engine = create_engine(connection)

df = pd.read_csv(URL)
df['FECHA_COPIA'] = datetime.datetime.now()
df.to_sql("Unificado", con=engine, if_exists='append', index=False)
