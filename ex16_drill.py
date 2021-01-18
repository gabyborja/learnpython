from sys import argv

script, filename = argv

print(f"Opening {filename}")
target = open(filename)

print(target.read())