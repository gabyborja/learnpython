print("I will now count my chickens:")
# The next line will first calculate 30 / 6 then add to 25 = 30
print("Hens", 25 + 30 / 6)
# Percent sign is the modulo operator. First compute 25 * 3, then take the modulo 4 to give 3. Subtract from 100
print("Roosters", 100 - 25 * 3 % 4)
# print the next line
print("Now I will count the eggs:")
# 1 / 4 is 0 because of precision. 4 % 2 is 0 because it's even (remainder is 0). The rest evaluates to 7
print(3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6)
# print next line
print("Is it true that  3 + 2 < 5 - 7")
# This prints false 
print(3 + 2 < 5 - 7)
# Evaluate the terms after printing the line
print("What is 3 + 2?", 3 + 2)
# Evaluate the term after printing the line
print("What is 5 - 7?", 5 - 7)
# print next line
print("Oh, that's why it's False.")
# print next line
print("How about some more.")
# this evaluates to true
print("Is it greater?", 5 > -2)
# this evaluates to true
print("Is it greater or equal?", 5 >= -2)
# this evalutes to false
print("Is it less or equal?", 5 <= -2)