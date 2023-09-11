# A stack is an object designed to store data using the LIFO model. The stack usually performs at least two operations, named push() and pop().
# Implementing the stack in a procedural model (just using a list) raises several problems which can be solved by the techniques offered by 
# OOP (Object Oriented Programming).

# The part of the Python class responsible for creating new objects is called the constructor, and it's implemented as a method of the 
# name __init__.
# Each class method declaration must contain at least one parameter (always the first one) usually referred to as self, and is used by 
# the objects to identify themselves.
# To hide any of a class's components from the outside world, we should start its name with __. Such components are called private.

# define superclass called stack
class Stack:
    def __init__(self):
        self.__stack_list = []

    # push method to add items to the stack
    def push(self, val):
        self.__stack_list.append(val)

    # pop method to remove items from the top of the stack, the first item in the list
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


# create a subclass that adds all the items in the stack together
class AddingStack(Stack):
    def __init__(self):
        # invoke the superclasses constructor (stack class)
        Stack.__init__(self)
        # create private sum property
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


# create a stack object
stack_obj = AddingStack()

# a for loop that iterates through numbers 1-5
# push each iteration to stack list
for i in range(1, 6):
    stack_obj.push(i)
    
# print the sum of the stack
print(stack_obj.get_sum())
