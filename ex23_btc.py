import sys
script, encoding, error = sys.argv


""" def main(language_file, encoding, errors)
    line = language_file.readline()

    if line: 
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip() """


languages = open("languages.txt", 'rb')
line = languages.readline()
print(f">>> {line}")
strip_line = line.strip()
print(f">> {strip_line}")