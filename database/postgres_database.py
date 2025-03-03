import psycopg2
from psycopg2 import sql, OperationalError, DatabaseError

def connect(db_name = 'company_db', db_user = 'ifigenblat', db_password = 'Magic8ball'):
	try:
		return psycopg2.connect(
			database=db_name,
			user=db_user,
			password= db_password,
			host="localhost",
			port="5432"
			)
	except Error as e:
		print(e)

# Database connection parameters
DB_CONFIG = {
    "dbname": "company_db",
    "user": "ifigenblat",
    "password": "Magic8ball",
    "host": "localhost",
    "port": "5432"
}

def connect_and_execute():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Attempt to execute an SQL command
        try:
            cursor.execute("SELECT * FROM hr.employees;")  # Example query

            # Fetch results
            records = cursor.fetchall()
            for row in records:
                print(row)

        except psycopg2.ProgrammingError as e:
            print(f"SQL Execution Error: {e}")

        except psycopg2.IntegrityError as e:
            print(f"Data Integrity Error: {e}")

        except psycopg2.DatabaseError as e:
            print(f"General Database Error: {e}")

        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()

    except OperationalError as e:
        print(f"Error connecting to the database: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
	'''	
	db_name = input("Which database would you like to connect to: ")
	db_user = input("Please enter the database user: ")
	db_password = input("Please enter the database password: ")
	db = connect(db_name, db_user, db_password)'''
	connect_and_execute()
	db = connect()
	if(db):
		print(f'Successfuly connected')# to {db_name}')
	cursor = db.cursor()
	while True:
		quary = input('What quary would you like to run? (type exit to quit):  '.strip())
		if quary == 'exit':
			print('Exiting ...')
			break
		try:
			cursor.execute(quary)
			project_records = cursor.fetchall()
			print(project_records)
		except psycopg2.ProgrammingError as e:
			print(f"SQL Execution Error: {e}")
	cursor.close()
	db.close()