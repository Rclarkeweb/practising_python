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

```
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2)) # prints Everything went fine
# It's time to say goodbye
# 0.5
print(reciprocal(0)) # Division failed
# It's time to say goodbye
# None
```
The else: branch of the try statement is executed when there has been no exception during the execution of the try: block.

The `finally` block is always executed (it finalizes the try-except block execution, hence its name), no matter what happened earlier, even when raising an exception, no matter whether this has been handled or not.

Exceptions are classes. when an exception is raised, an object of the class is instantiated, and goes through all levels of program execution, looking for the except branch that is prepared to deal with it.

#### Extending the except block
```
try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())
```
the except statement is extended, and contains an additional phrase starting with the as keyword, followed by an identifier. The identifier is designed to catch the exception object so you can analyze its nature and draw some useful conclusions.
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


The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.  
  
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

***Example Class***  
**Dog class:**  
**Properties:**  
- Age
- Breed  

**Methods:**  
- Eat()
- Sleep()  

#### Instance Variables

```
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.set_second(6)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# {'first': 1}  
# {'first': 2, 'second': 3}  
# {'first': 4, 'second': 6, 'third': 5}
```

Python objects, when created, are gifted with a small set of predefined properties and methods. Each object has got them, whether you want them or not. One of them is a variable named `__dict__` (it's a dictionary).

The variable contains the names and values of all the properties (variables) the object is currently carrying. Let's make use of it to safely present an object's contents.  

The class named `ExampleClass` has a constructor, which unconditionally creates an instance variable named `first`. The `set_variable` method creates another instance variable called `second`. Modifying an instance variable of any object has no impact on all the remaining objects. Instance variables are perfectly isolated from each other.  

An instance variable is a property whose existence depends on the creation of an object. Every object can have a different set of instance variables.  

Moreover, they can be freely added to and removed from objects during their lifetime. All object instance variables are stored inside a dedicated dictionary named __dict__, contained in every object separately.  

#### Private Instance Variables  

```
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5


print(example_object_1.__dict__)
# {'_ExampleClass__first': 1}

print(example_object_2.__dict__)
# {'_ExampleClass__first': 2, '_ExampleClass__second': 3}

print(example_object_3.__dict__)
# {'_ExampleClass__first': 4, '__third': 5}

print(example_object_1._ExampleClass__first)
# 1
```

The instance variables have become private (they now have `__` in front of them.  
When Python sees that you want to add an instance variable to an object and you're going to do it inside any of the object's methods, it mangles the operation in the following way:  
- it puts a class name before your name;  
- it puts an additional underscore at the beginning.

This is why the `__first` becomes `_ExampleClass__first`.
The name is now fully accessible from outside the class.    
  
An instance variable can be private when its name starts with __, but don't forget that such a property is still accessible from outside the class using a mangled name constructed as _ClassName__PrivatePropertyName.  

#### Class Variables 
A class variable is a property which exists in just one copy and is stored outside any object.

```
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


# 5 objects are created so the class counter variable is equal to 5
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
example_object_4 = ExampleClass()
example_object_5 = ExampleClass()

# __first is a private intance variable (hence the self and __)
# counter is a class variable

print(example_object_1.__dict__, example_object_1.counter)
# {'_ExampleClass__first': 1} 5

print(example_object_2.__dict__, example_object_2.counter)
# {'_ExampleClass__first': 2} 5

print(example_object_3.__dict__, example_object_3.counter)
# {'_ExampleClass__first': 4} 5

print(example_object_4.counter)
# 5
```

Class variables aren't shown in an object's `__dict__`.  
A class variable always presents the same value in all class instances (objects).  
Even if you mangle the class variable `counter` (set it to private) `__counter`. And change it in the class to `ExampleClass.__counter += 1`. When you print it out `example_object_1._ExampleClass__counter`, you will still get the number of `ExampleClass` objects that have been created (5), like before.

A class variable is a property which exists in exactly one copy, and doesn't need any created object to be accessible. Such variables are not shown as `__dict__` content.  

#### hasattr function  
A function named hasattr() can be used to determine if any object/class contains a specified property.  
Python provides a function which is able to safely check if any object/class contains a specified property. The function is named `hasattr`, and expects two arguments to be passed:
- the class or the object being checked;
- the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)
The function returns True or False
```
class ExampleClass:
    attr = 1

print(hasattr(ExampleClass, 'attr')) # True
print(hasattr(ExampleClass, 'prop')) # False
```

#### Instance, Private and Class Variable Summary
```
class Sample:
    gamma = 0 # Class variable.
    def __init__(self):
 
        self.alpha = 1 # Instance variable.
        self.__delta = 3 # Private instance variable.
 
# create an object called obj
obj = Sample()

obj.beta = 2 # Another instance variable (existing only inside the "obj" instance.)

print(obj.__dict__)
# {'alpha': 1, '_Sample__delta': 3, 'beta': 2}

print(obj.gamma) # prints class variable
# 0

print(hasattr(Sample, 'attr'))
# False (no attribute 'attr' in Sample Class)
```

### OOP Methods
A method is a function embedded inside a class.  
There is one fundamental requirement – a method is obliged to have at least one parameter (there are no such things as parameterless methods – a method may be invoked without an argument, but not declared without parameters).  
The first (or only) parameter is usually named self.  
The name self suggests the parameter's purpose – it identifies the object for which the method is invoked.  
If you name a method like this: `__init__`, it won't be a regular method – it will be a constructor.  
If a class has a constructor, it is invoked automatically and implicitly when the object of the class is instantiated.  
The constructor:
- is obliged to have the self parameter (it's set automatically, as usual)
- may (but doesn't need to) have more parameters than just self; if this happens, the way in which the class name is used to create the object must reflect the __init__ definition;
- can be used to set up the object, i.e., properly initialize its internal state, create instance variables, instantiate any other objects if their existence is needed, etc.
```
class Classy:
    def __init__(self, value = None):
        self.var = value

obj_1 = Classy("object")
obj_2 = Classy()

print(obj_1.var)
# object
print(obj_2.var)
# none
```
**Property name mangling** applies to method names, too – a method whose name starts with `__` is (partially) hidden.
```
class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")

# Create object
obj = Classy()
obj.visible() # prints visible

try:
    obj.__hidden()
except:
    print("failed")

# accessing private method
obj._Classy__hidden()

# will print:
# visible
# failed
# hidden
```

Each Python class and each Python object is pre-equipped with a set of useful attributes which can be used to examine its capabilities.  
```
class Classy:
    varia = 1 # class variable
    def __init__(self):
        self.var = 2 # instance variable

    def method(self):
        pass
    
    def __hidden(self): # hidden method
        pass


obj = Classy()

print(obj.__dict__) # prints {'var': 2}
print(Classy.__dict__)
```

`__name__` - The property contains the name of the class.
`print(ClassName.__name__)`

If you want to find the class of a particular object, you can use a function named type(), which is able (among other things) to find a class which has been used to instantiate any object.
`obj = ClassName()`
`print(type(obj).__name__)`

All classes (but not objects) contain a property named __name__, which stores the name of the class. Additionally, a property named __module__ stores the name of the module in which the class has been declared, while the property named __bases__ is a tuple containing a class's superclasses.

#### introspection
which is the ability of a program to examine the type or properties of an object at runtime;  

#### reflection
which goes a step further, and is the ability of a program to manipulate the values, properties and/or functions of an object at runtime.

### Class Inheritance
Inheritance is a common practice (in object programming) of passing attributes and methods from the superclass (defined and existing) to a newly created class, called the subclass.
In other words, inheritance is a way of building a new class, not from scratch, but by using an already defined repertoire of traits. The new class inherits (and this is the key) all the already existing equipment, but is able to add some new ones if needed.
#### `issubclass()`
```
# superclass
class Vehicle:
    pass

# subclass of vehicle and superclass of TrackedVehicle
class LandVehicle(Vehicle):
    pass

# subclass of both vehicle and LandVehicle
class TrackedVehicle(LandVehicle):
    pass
```
Python offers a function which is able to identify a relationship between two classes, and although its diagnosis isn't complex, it can check if a particular class is a subclass of any other class.
`issubclass(ClassOne, ClassTwo)`
It returns True or False

#### `isinstance()`
An object is an incarnation of a class.
`isinstance(objectName, ClassName)`
The function returns True if the object is an instance of the class, or False otherwise.

#### is operator
`object_one is object_two`
The is operator checks whether two variables (object_one and object_two here) refer to the same object.
Variables don't store the objects themselves, but only the handles pointing to the internal Python memory.

#### Inhertiting Methods
```
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

obj = Sub("Andy")

print(obj)
# My name is Andy.
```
As there is no __str__() method within the Sub class, the printed string is to be produced within the Super class. This means that the __str__() method has been inherited by the Sub class.

You can also use the `super()` function. 
In the last example, we explicitly named the superclass. You can also use the super() function, which accesses the superclass without needing to know its name:
`super().__init__(name)`
The super() function creates a context in which you don't have to (moreover, you mustn't) pass the self argument to the method being invoked – this is why it's possible to activate the superclass constructor using only one argument.
```
# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()

print(obj.subVar) # 12 
print(obj.supVar) # 11
```
The Sub class constructor creates an instance variable named subVar, while the Super constructor does the same with a variable named supVar. Both variables are accessible from within the object of class Sub.

#### polymorphism and hierarchy
inheritance extends a class's capabilities
composition projects a class as a container
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.


> single inheritance class is always simpler, safer, and easier to understand and maintain;
> 
> multiple inheritance is always risky, as you have many more opportunities to make a mistake in identifying these parts of the superclasses which will effectively influence the new class;
>
> multiple inheritance may make overriding extremely tricky; moreover, using the super() function becomes ambiguous;
>
> multiple inheritance violates the single responsibility principle (more details here: https://en.wikipedia.org/wiki/Single_responsibility_principle) as it makes a new class of two (or more) classes that know nothing about each other;
>
> we strongly suggest multiple inheritance as the last of all possible solutions

```
class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
bob = SheepDog("Sausage")

print(rocky) # Collie says: Woof! Don't run away, Little Lamb!
print(luna) # Dobermann says: Woof! Stay where you are, Mister Intruder!
print(Dog.kennel) # 3
print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog)) # True, False
print(luna is luna, rocky is luna) # True, False
```

## Generators
A Python generator is a piece of specialized code able to produce a series of values, and to control the iteration process. This is why generators are very often called iterators.
The `range()` function is, in fact, a generator, which is (in fact, again) an iterator.
A function returns one, well-defined value – it may be the result of a more or less complex evaluation of, something like a polynomial, and is invoked once – only once.
A generator returns a series of values, and in general, is (implicitly) invoked more than once.

The iterator protocol is a way in which an object should behave to conform to the rules imposed by the context of the for and in statements.
An object conforming to the iterator protocol is called an iterator.
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
When you create a list, you can read its items one by one. Reading its items one by one is called iteration. The list is an iterable.
Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods `__iter__()` and `__next__()`.
An iterator must provide two methods:
- `__iter__()` which should return the object itself and which is invoked once (it's needed for Python to successfully start the iteration)
- `__next__()` which is intended to return the next value (first, second, and so on) of the desired series – it will be invoked by the for/in statements in order to pass through the next iteration; if there are no more values to provide, the method should raise the `StopIteration` exception.

To create an object/class as an iterator you have to implement the methods `__iter__()` and `__next__()` to your object.

All classes have a function called `__init__()`, which allows you to do some initializing when the object is being created.

The `__iter__()` method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The `__next__()` method also allows you to do operations, and must return the next item in the sequence.

Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
```
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter)) # prints 1
print(next(myiter)) # prints 2
```
##### StopIteration
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
To prevent the iteration from going on forever, we can use the `StopIteration` statement.
In the `__next__()` method, we can add a terminating condition to raise an error if the iteration is done a specified number of times.
```
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x) # prints 1 2 3 4 5
```

##### Yield
The yield statement suspends a function’s execution and sends a value back to the caller, but retains enough state to enable the function to resume where it left off. When the function resumes, it continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory. Yield is used in Python generators. A generator function is defined just like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function. 

The yield statement can be used only inside functions. The yield statement suspends function execution and causes the function to return the yield's argument as a result. Such a function cannot be invoked in a regular way – its only purpose is to be used as a generator (i.e. in a context that requires a series of values, like a for loop).

```
def fun(n):
    for i in range(n):
        yield i
 
for v in fun(5):
    print(v) # prints 0 1 2 3 4
```
The main difference between return and yield is, the return statement terminates the execution of the function. Whereas, the yield statement only pauses the execution of the function.
```
def fun_generator():
    yield "Hello world!!"
    yield "Boo"
 
obj = fun_generator()
 
print(next(obj)) # prints Hello world!!
print(next(obj)) # prints Boo
```
Generators can used in List Comprehensions (creating lists)
```
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
t = [x for x in powers_of_2(5)]
print(t) # prints [1, 2, 4, 8, 16]
```
List comprehension:
```
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list) # prints [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# starts at 0 which is even
```
**List comprehension vs Generators**
```
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
# different brackets. len(the_list) = 10 len(the_generator) = error, generators have no length.
```

A list comprehension becomes a generator when used inside parentheses (used inside () brackets, it produces a regular list). For example:

## Lambda function
A lambda function is a function without a name (you can also call it an anonymous function).
`lambda parameters: expression`
```
sqr = lambda x: x * x    # one-parameter anonymous function that returns the value of its squared argument.
pwr = lambda x, y: x ** y   # takes two parameters and returns the value of the first one raised to the power of the second one.
```
The power of lambda is better shown when you use them as an anonymous function inside another function.
```
def myfunc(n):
  return lambda a : a * n
```
#### Map
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
`map(function, iterables)`
```
def myfunc(a):
  return len(a)
​
x = map(myfunc, ('apple', 'banana', 'cherry'))
​
print(x)
​
#convert the map into a list, for readability:
print(list(x))
```
```
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2) # [1, 2, 4, 8, 16]
```


#### Filter
The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
`filter(function, iterable)`
```
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x) # 18 24 32
```
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

#### Closures
Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.
closure is a nested function that helps us access the outer function's variables even after the outer function is closed. For example;
```
def greet():
    # variable defined outside the inner function
    name = "John"
    
    # return a nested anonymous function
    return lambda: "Hi " + name

# call the outer function
message = greet()

# call the inner function
print(message())

# Output: Hi John
```
