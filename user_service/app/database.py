import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DATABASE_HOST", "localhost"),
            database=os.getenv("DATABASE_NAME", "user_service"),
            user=os.getenv("DATABASE_USER", "user_service_user"),
            password=os.getenv("DATABASE_PASSWORD", "password"),
            port=os.getenv("DATABASE_PORT", "5432"),
            cursor_factory=RealDictCursor
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        raise




'''

import psycopg2
from psycopg2.extras import RealDictCursor

# Database credentials
DATABASE = {
    "host": "localhost",
    "database": "user_service",
    "user": "user_service_user",
    "password": "password",
}

def get_connection():
    try:
        conn = psycopg2.connect(
            host=DATABASE["host"],
            database=DATABASE["database"],
            user=DATABASE["user"],
            password=DATABASE["password"],
            cursor_factory=RealDictCursor
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        raise
'''