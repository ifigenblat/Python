import mysql.connector as mysql

def connect(db_name, db_password):
	try:
		return mysql.connect(
			host="localhost",
			user="root",
			password= db_password,
			database=db_name)
	except Error as e:
		print(e)


if __name__ == '__main__':
	db_name = input("Which database would you like to connect to: ")
	db_password = input("Please enter the database password: ")
	db = connect(db_name, db_password)
	if(db):
		print(f'Successfuly connected to {db_name}')
	while True:
		quary = input('What quary would you like to run? (type exit to quit) '.strip())
		if quary == 'exit':
			print('Exiting ...')
			break
		cursor = db.cursor()
		cursor.execute(quary)
		project_records = cursor.fetchall()
		print(project_records)
	db.close()