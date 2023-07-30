# Python Notes  


## Try and Except

Try a block of code if it doesnt work execute another block.  
You can specific exceptions for different errors such as Value Error or Zero Division.  
You can also have a default except, this must always be at the end.  
```
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
```

#### ZeroDivisionError

This appears when you try to force Python to perform any operation which provokes division in which the divider is zero, or is indistinguishable from zero. Note that there is more than one Python operator which may cause this exception to raise. Can you guess them all?

Yes, they are: /, //, and %.

#### ValueError

Expect this exception when you're dealing with values which may be inappropriately used in some context. In general, this exception is raised when a function (like int() or float()) receives an argument of a proper type, but its value is unacceptable.

##### TypeError

This exception shows up when you try to apply a data whose type cannot be accepted in the current context.  

#### AttributeError

This exception arrives – among other occasions – when you try to activate a method which doesn't exist in an item you're dealing with.

***   

## Classes  

Python is an object-oriented programming language. 
When you assign a value to a variable you are creating an object. 
This object then belongs to its particular class. Eg an Integar, String, List, Dictionary etc.  
```
x = 12  
print(type(x))  
#<class 'int'>
```
The dir function will print all avaiable methods to that object.  
  
Python uses methods to represent the behavior of an object. Thus, methods are associated with an object and will perform some operations 
upon the data within an object. Another key distinguishing factor of a method is the self parameter that must always occur as the first 
parameter passed to the method.   
Methods are dependent on the class they are associated with. Thus, to call a method, an instance of the class must be created before 
the method can be accessed with the dot operator.  
Self is used to represent the instance of the class.

```
# Example of a method
class Human:
    # This is a method
    def walk(self):
        print("I am walking")

# Creating a new instance of a class and calling a method
# This will work
joe = Human()
joe.walk()

"""
I am walking
"""
```
A function, on the other hand, is different: we do not have to create an instance of a class. 

Python functions are steps executed as a block of code only when called. They are defined independently of any class object, 
meaning they can be called directly by their name. In essence, a function is simply a set of well-defined instructions the interpreter 
uses to perform a task. A function is simply a set of well-defined instructions the interpreter uses to perform a task. Functions also come 
in two different flavors: built-ins and user-defined. 

Some of those methods are:  
- **Initializer method** `__init__`, called in this way because it’s the method that initializes the attributes of the object.
  Moreover, it is automatically called once the object is created.
- **Magical methods** (also known as dunder functions) are special methods with double underscores on both sides. For example, `__add__` and `__mul__`
  Magic methods are a set of predefined methods in Python that provide special syntactic features.

**`__init__`**
```
class Employee:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
```
This code defines a class called "Employee" with three attributes: "name", "age", and "role".
The `__init__` method is a special method in Python classes that is called when an object of the class is created.

`__new__(cls, other)` - Used to create a new instance of a class

`__init__(self, other)` - Called after a new instance has been created; All attributes passed to the class constructor expression will be used as attributes. 

`__del__(self)` - Also known as the destructor; Called when an instance is to be destroyed. 

Notes taken from [Datacamp](https://www.datacamp.com/tutorial/introducing-python-magic-methods)

### Example Class  
### **Dog class:**  
**Properties:**  
- Age
- Breed  

**Methods:**  
- Eat()
- Sleep()
