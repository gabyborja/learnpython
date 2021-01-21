import sys
script, encoding, error = sys.argv


""" def main(language_file, encoding, errors)
    line = language_file.readline()

    if line: 
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip() """


languages = open("languages.txt", 'rb') # open languages as bytes
line = languages.readline()
print(f">>> {line}")
strip_line = line.strip() #strips the trailing \n
print(f">> {strip_line}") 

line2 = languages.readline()
print(f'>>> {line2}')

""" whole = languages.read()
print(whole) """

raw_bytes = line2
print(f"raw bytes is \n {raw_bytes}")
# Decode bytes
cooked_string = raw_bytes.decode('utf-8', errors='strict')
print(f"cooked string is \n {cooked_string}")