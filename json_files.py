import json
from json import JSONDecodeError, JSONEncoder

#Reading and Processing JSON file

def read_and_process(json_file):
    # Read data from the JSON file
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    
        # Process the JSON data
        for item in data:
            print(f"Processed item: {item}")
    except JSONDecodeError:
        print(f"Error: Could not decode JSON from {json_file}")
    except FileNotFoundError:
        print(f"Error: File {json_file} not found")

# File path
json_path = 'output.json'

# Execute the function
read_and_process(json_path)


# Loading JSON

jsonString = '{"a": "appale", "b": "bear", "c": "cat"}' # this is not pyton dictionary, it json string
try:
	# loading JSON into dictionary 
	print(json.loads(jsonString))
except JSONDecodeError:
	print('Could not parse JSON!')


# Dumping JSON

pythonDict = {'a': 'appale', 'b': 'bear', 'c': 'cat'}
json.dumps(pythonDict)


# Custom JSON Decoders 

class Animal:
	def __init__(self, name):
		self.name = name

class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Animal):  # Use isinstance for type checking
            return o.name
        return super().default(o)  # Fix typo here

# dumping python disctinary into JSON using custom JSON encoder 
pythonDict = {'a': Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('cat')}
print(json.dumps(pythonDict, cls=AnimalEncoder))


# Example of Read from text and Write in JSON

# File paths
text_path = 'data.txt'
json_path = 'output.json'

# Read and parse text file
data = []
with open(text_path, 'r') as file:
    record = {}
    for line in file:
        line = line.strip()
        if line:  # Process non-empty lines
            key, value = line.split(': ', 1)
            record[key] = value
        else:
            if record:  # Add record to list when a blank line is encountered
                data.append(record)
                record = {}
    if record:  # Add the last record if the file doesn't end with a blank line
        data.append(record)

# Write data to JSON file
with open(json_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Output result
print(f"Data written to {json_path}")

##################################################################################

# Sample encodeString function
def encodeString(stringVal):
    # Example encoding logic: reverse the string (replace with your actual logic)
    return stringVal[::-1]

def process_and_save(input_file, output_file):
    # Read data from the text file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Initialize an empty list to hold encoded lines
    encoded_lines = []

    # Process each line using the encodeString function
    for line in lines:
        stripped_line = line.strip()  # Remove leading/trailing whitespace
        if stripped_line:  # Only process non-empty lines
            encoded_line = encodeString(stripped_line)
            encoded_lines.append(encoded_line)

    # Write the processed data to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(encoded_lines, json_file, indent=4)

    print(f"Encoded data has been written to {output_file}")

# File paths
input_path = 'file.txt'
output_path = 'output.json'

# Execute the function
process_and_save(input_path, output_path)