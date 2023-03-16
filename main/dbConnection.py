import psycopg2
import os

DB_NAME = os.getenv('DB_NAME', 'database_name')
DB_USER = os.getenv('DB_USER', 'database_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'database_password')
DB_HOST = os.getenv('DB_HOST', 'database_host')
DB_PORT = os.getenv('DB_PORT', 'database_port')

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
