i = 0 
numbers = []

def call_loop(last_num): 
    i = 0
    while i < last_num:
        print(f"At the top i is {i} ")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")\

print("Loop until what number?")
input_num = int(input("> "))

call_loop(input_num)

print("The numbers: ")

for num in numbers:
    print(num)