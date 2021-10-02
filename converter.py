raw_data = open("file_name.txt", "r")  #reads data from file to a handle

raw_string = raw_data.read() #reads data from handle to a string

newline = raw_string.replace(',', '\n') #replaces commas in the data with a newline character

final = newline.replace(' ', '') #removes whitespace from data

print(final)
