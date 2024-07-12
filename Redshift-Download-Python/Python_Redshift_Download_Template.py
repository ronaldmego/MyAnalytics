import os
import psycopg2
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la conexión
conn_params = {
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT'),
    'dbname': os.getenv('DBNAME'),
    'user': os.getenv('USERNAMES'),
    'password': os.getenv('PASSWORD'),
}

# Consulta SQL
query = """
SELECT * --IDPOL, COUNT(DISTINCT IDCUSTOMER)
FROM INFORMATION_DELIVERY_PROD.MFS_LENDING.INFO_DYN_PY_PREOFFERS --- EN TELCO SOLAMENTE SE TIENEN PREOFFERS, POR LO CUAL ESTA TABLA INPUT ES DISTINTA, AL FINAL YA ESTAN CARGADAS EN OFFERS
WHERE DATE(RECEIVEDAT) = '2024-07-10'
AND IDPOL IN ('SCR_ADM_TELCO')
AND CLASS IN ('08_TELCO_SUSCRIPCION_PREMIUM','09_TELCO_MITIGO','10_TELCO_RESTO')
AND CLASS NOT IN ('01_TM_DIG')
"""

# Función para obtener los datos y guardarlos en un CSV
def get_data():
    conn = None
    try:
        conn = psycopg2.connect(**conn_params)
        print("Conexión exitosa")

        # Crear un cursor
        cursor = conn.cursor()

        # Ejecutar la consulta
        cursor.execute(query)

        # Obtener los resultados y convertirlos a un DataFrame de Pandas
        columns = [desc[0] for desc in cursor.description]
        results = cursor.fetchall()

        # Usar tqdm para mostrar una barra de progreso mientras se cargan los datos
        df = pd.DataFrame(results, columns=columns)
        for _ in tqdm(df.itertuples(), total=len(df), desc="Descargando datos"):
            pass  # La barra de progreso se actualiza aquí

        # Guardar el DataFrame en un archivo CSV
        df.to_csv('datos_descargados.csv', index=False)
        print("Datos guardados en 'datos_descargados.csv'")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexión cerrada")

# Llamar a la función para obtener los datos
get_data()