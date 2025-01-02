import csv

path = 'C:\\python code\\Python_essential_Training\\Exercise Files\\exercise_files\\10_02_us.csv'


with open(path,'r') as f:
	# use delimiter if the seperater in the file is not comma, use csv.reader(f) when comma
	reader = csv.reader(f, delimiter='\t') 
	# use next(reader) to skip the header if you like to
	next(reader)
	for row in reader:
		print(row)

# you can use list to avoid calling next like:
with open(path,'r') as f:
	# use delimiter if the seperater in the file is not comma, use csv.reader(f) when comma
	reader = list(csv.reader(f, delimiter='\t')) 
	for row in reader[1:]:
		print(row)

# you can also use Dictionery to access key / Value:
with open(path,'r') as f:
	# use delimiter if the seperater in the file is not comma, use csv.reader(f) when comma
	reader = csv.DictReader(f, delimiter='\t') 
	for row in reader:
		print(row)


def readCSVFile(path):
	with open(path,'r') as f:
		reader = csv.reader(f)
		for row in reader:
			print(row)


# Filtering data

def allPrimesUpTo(num):
    my_list = []
    for number in range(2,num):
        for factor in range(2, int(number**0.5)+1):
            if number % factor == 0:
                break
        else:
             my_list.append(number)
    return my_list

with open(path,'r') as f:
	data = list(csv.DictReader(f, delimiter = '\t'))
	# now that we have data, let's filter all the prime number based on zip code

primes = allPrimesUpTo(99999)

print(len(primes))
filtered_data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']
print(len(filtered_data)) 

'''
Another solution - more efficient and making sure to handle no value or not digit

# File path
path = 'C:\\python code\\Python_essential_Training\\Exercise Files\\exercise_files\\10_02_us.csv'

# Function to generate primes using Sieve of Eratosthenes
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    return {num for num, is_prime in enumerate(sieve) if is_prime}

# Generate primes up to 99999
primes = generate_primes(99999)

print(len(primes))

# Read and filter data
with open(path, 'r') as f:
    data = list(csv.DictReader(f, delimiter='\t'))

# Filter rows based on prime postal codes and state code
filtered_data = [
    row for row in data
    if row['postal code'].isdigit() and int(row['postal code']) in primes and row['state code'] == 'MA'
]

# Output result
print(len(filtered_data))
'''

# Writing back to a CSV file
file_path = 'C:\\python code\\Python_essential_Training\\Exercise Files\\exercise_files\\10_02_ma_prime.csv'
with open(file_path, 'w') as f:
	writer = csv.writer(f)
	for row in filtered_data:
		writer.writerow([row['postal code'], row['place name'], row['county']])

readCSVFile(file_path)