types_of_people = 10 
x = f"there are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}" #1 #2

print(x)
print(y)

print(f"I said: {x}") #3
print(f"I also said: '{y}'") #4

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))    

w = "This is the left side of..."
e = "a string with a ride side."

print(w + e)