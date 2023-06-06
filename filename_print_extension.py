# prompt user to input filename
filename = input("Input the Filename: ")

# find the position of the last period in the filename
last_dot_index = filename.rfind('.')

# extract the extension from the filename
if last_dot_index != -1:
    extension = filename[last_dot_index+1:]
else:
    extension = ""

# print the extension
print(f"The extension of the file is : '{extension}'")
