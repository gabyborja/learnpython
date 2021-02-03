class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

print("dad.implicit()")
dad.implicit()
print("son.implicit()")
son.implicit() # Even though son.implicit() does not exist, it will pull the implicit function from Parent()