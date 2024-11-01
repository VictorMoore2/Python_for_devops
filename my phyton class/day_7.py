#File Handling and E rror handling

#file = open("example.txt","r")

""" with open("example>txt","r") as 
file:
    content = file.read()
    print(content) """
""" 
  #writing to files
with open("output.txt", "w") as file:
    file.write("Hello, world!")
    file.write("Second message") """

#working with large files
""" with open("large_file.txt", "r") as file:
    for line in file:
        print(line.strip()) """

#working with file paths using the os Module
#Getting the current working directory

import os #operating system
###print(os.getcwd()) 
#cwd =currentworkingdirectory

#creating, renaming and deleting files or directories

#creating directory
##os.mkdir("new_folder")

#rename a file or directory
#os.rename("example.txt","victormoore.txt")

#remove a file or directory
#os.remove("victormoore.txt")

#checking id a file exist:
""" if os.path.exists("output.txt"):
    print("file exists") """

#joining and splitting path
""" file_path=os.path.join("folder","subfolder","file.txt")
print(file_path) """


#Exception Handling
#Basic Exception Handling
""" try:
    file = open("Out_date.txt","r")
except FileNotFoundError:
    print("File Not Found!")
 """

#Multiple Exception Types
""" try:
    result =10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}") """

#The Finally Block
""" try:
    file = open("example.txt","r")
finally:
    file.close() #this runs even if an error occurs """

#Word Count Program
""" def word_count(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)
            print(f"Lines: {len(lines)}")
            print(f"Words: {word_count}")
            print(f"Characters: {char_count}")
    except FileNotFoundError:
        print("File not found!")

word_count("output.txt") """

#Practical exercises: #
# File processing and log analysis

def analyze_log(file_path):
    try:
        with open(file_path,"r") as file:
            for line in file:
                if "ERROR" in line:
                    print(line.strip())
    except FileNotFoundError:
        print("log file not found!")
analyze_log("output.txt")