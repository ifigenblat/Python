'''
file_path: The location of the file (e.g., C:\\Users\\YourName\\Documents\\file.txt) (windows).
mode: The mode in which you want to open the file. Common modes:
'r': Read (default).
'w': Write (overwrites file if it exists, creates a new file if it doesn’t).
'a': Append (add to the end of the file).
'rb': Read in binary mode.
'wb': Write in binary mode.
'''
# Reading a file
f = open('C:\\python code\\Python_essential_Training\\Exercise Files\\exercise_files\\10_01_file.txt', 'r')
# print(f) - file object 
# print(f.readline()) - read the content of the file, one line at a time
# print(f.readlines()) - read all content 

for line in f.readlines():
	print(line.strip())

# Read File Function
def fileReader(path):
	f = open(path, 'r')
	for line in f.readlines():
		print(line.strip())

# Writing a file
path = 'C:\\python code\\Python_essential_Training\\Exercise Files\\exercise_files\\10_01_output.txt'
f = open(path, 'w')
f.write('Line 1\n')
f.write('Line 2\n')
f.close()
fileReader(path)

# Appending Files
path = 'C:\\python code\\Python_essential_Training\\Exercise Files\\exercise_files\\10_01_output.txt'
f = open(path, 'a')
f.write('Line 3\n')
f.write('Line 4\n')
f.close()
fileReader(path)

# Closing a file is best practice and prevent strange behavior, 
# most commen way to do that is by using the with statement
path = 'C:\\python code\\Python_essential_Training\\Exercise Files\\exercise_files\\10_01_output.txt'
with open(path, 'a') as f:
    f.write('some stuff\n')
    f.write('some other stuff\n')
fileReader(path)    

