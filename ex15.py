# Reading Files
from sys import argv

print("What file do you want to open?")
filename = input(">  ")
txt = open(filename)

print(f"Here's your file {filename}:") 
print(txt.read())  

txt.close()

""" print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read()) """