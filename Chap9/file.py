f= open("file.txt") # open the file in read mode
data = f.read() # read the entire file
# Process the data as needed
print(data)
f.close() # close the file after reading
# Ensure the file is closed properly