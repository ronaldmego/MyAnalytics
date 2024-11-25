import os
import psycopg2
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

# Función para crear una tabla en un esquema específico
def create_table():
    conn = None
    try:
        conn = psycopg2.connect(**conn_params)
        print("Conexión exitosa")

        # Crear un cursor
        cursor = conn.cursor()

        # Comando SQL para crear una tabla en el esquema específico usando IDENTITY en lugar de SERIAL
        create_table_query = """
        CREATE TABLE IF NOT EXISTS INFORMATION_DELIVERY_PROD.MFS_MARKETING.ejemplo_tabla (
            id INT IDENTITY(1,1) PRIMARY KEY,
            nombre VARCHAR(50),
            edad INT,
            ciudad VARCHAR(50)
        );
        """

        # Ejecutar el comando
        cursor.execute(create_table_query)
        conn.commit()
        print("Tabla creada exitosamente en INFORMATION_DELIVERY_PROD.MFS_MARKETING")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexión cerrada")

# Función para insertar datos en la tabla
def insert_data():
    conn = None
    try:
        conn = psycopg2.connect(**conn_params)
        print("Conexión exitosa")

        # Crear un cursor
        cursor = conn.cursor()

        # Comando SQL para insertar datos en la tabla en el esquema específico
        insert_data_query = """
        INSERT INTO INFORMATION_DELIVERY_PROD.MFS_MARKETING.ejemplo_tabla (nombre, edad, ciudad) VALUES
        ('Juan', 28, 'Lima'),
        ('Maria', 32, 'Bogotá'),
        ('Carlos', 25, 'Ciudad de México');
        """

        # Ejecutar el comando
        cursor.execute(insert_data_query)
        conn.commit()
        print("Datos insertados exitosamente en INFORMATION_DELIVERY_PROD.MFS_MARKETING.ejemplo_tabla")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexión cerrada")

# Llamar a las funciones para crear la tabla e insertar los datos
create_table()
insert_data()