import psycopg2

# Database connection parameters
DB_CONFIG = {
    "dbname": "your_database",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}

# Function to get columns from a PostgreSQL table
def get_table_columns(schema, table_name):
    query = """
    SELECT column_name, data_type, character_maximum_length
    FROM information_schema.columns
    WHERE table_schema = %s AND table_name = %s;
    """

    try:
        # Connect to PostgreSQL database
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Execute query with schema and table name as parameters
        cursor.execute(query, (schema, table_name))
        
        # Fetch and display results
        columns = cursor.fetchall()
        
        if not columns:
            print(f"No columns found for {schema}.{table_name}")
            return
        
        print(f"Columns in {schema}.{table_name}:")
        for col in columns:
            col_name, col_type, col_length = col
            col_length = col_length if col_length is not None else "N/A"
            print(f"- {col_name}: {col_type} (Max Length: {col_length})")

        # Close cursor and connection
        cursor.close()
        connection.close()

    except psycopg2.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    schema_name = "public"  # Change if your table is in a different schema
    table_name = "employees"  # Replace with your table name
    get_table_columns(schema_name, table_name)