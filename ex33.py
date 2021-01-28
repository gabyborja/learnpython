i = 0 
numbers = []

def call_loop(last_num, increment): 
    i = 0
    while i < last_num:
        print(f"At the top i is {i} ")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")\

print("Loop until what number?")
input_num = int(input("> "))
print("What is the step size?")
input_step = int(input("> "))

call_loop(input_num, input_step)

print("The numbers: ")

for num in numbers:
    print(num)

print("Printing with range")
x = range(0, input_num, input_step)
for n in x: 
    print(n)