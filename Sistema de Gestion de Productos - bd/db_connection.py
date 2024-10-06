import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_DATABASE,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as error:
        raise Exception(f'Error al conectar a la base de datos: {error}')
