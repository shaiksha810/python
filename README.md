<!--  A. Basic Built-in Data Types -->

Data Type,	      Example,	                     Description
1. int     	      age = 25	                     Whole numbers
2. float   	      pi = 3.14	                     Decimal numbers
3. str     	      name = "Shaiksha"	             Text values
4. bool    	      is_active = True	             True/False


<!-- B. Collection Data Types -->
Data Type	     Example	                     Description
1. list	         [1, 2, 3]	                     Ordered, changeable collection
2. tuple	     (1, 2, 3)	                     Ordered, unchangeable collection
3. set	         {1, 2, 3}	                     Unordered, unique items
4. dict	         {"name": "Ali", "age": 25}	     Key-value pairs



<!-- C. Special Types -->
1. NoneType → None means no value assigned yet
   value = None



<!-- D. Checking the Data Type -->
You can use type() to check:
1. x = 10
print(type(x))  # <class 'int'>

2. y = 3.14
print(type(y))  # <class 'float'>

3. z = "Hello"
print(type(z))  # <class 'str'>




<!-- E. Changing (Casting) Data Types -->
1. x = int(3.14)      # 3
2. y = float(5)       # 5.0
3. z = str(100)       # "100"



<!-- Operators in Python -->

<!-- A. Arithmetic Operators -->
Used for math calculations:
x = 10
y = 3

1. print(x + y)  # 13  (Addition)
2. print(x - y)  # 7   (Subtraction)
3. print(x * y)  # 30  (Multiplication)
4. print(x / y)  # 3.333... (Division - float result)
5. print(x // y) # 3   (Floor Division - no decimal)
6. print(x % y)  # 1   (Modulus - remainder)
7. print(x ** y) # 1000 (Exponent - power)


<!-- B. Comparison Operators -->
Used to compare values (returns True or False):

1. print(x == y)  # False (Equal to)
2. print(x != y)  # True  (Not equal to)
3. print(x > y)   # True
4. print(x < y)   # False
5. print(x >= y)  # True
6. print(x <= y)  # False



<!-- C. Logical Operators -->
Used with boolean values:

a = True
b = False

1. print(a and b)  # False (Both must be True)
2. print(a or b)   # True  (At least one True)
3. print(not a)    # False (Reverses the result)




<!-- D. Assignment Operators -->
Used to assign values (with or without operations):

1. x = 5
2. x += 3  # x = x + 3 → 8
3. x -= 2  # x = x - 2 → 3
4. x *= 4  # x = x * 4 → 20
5. x /= 6  # x = x / 6 → 4.0




<!-- E. Membership Operators -->
Check if a value is in a sequence:

1. print(2 in list1)   # True
2. print(4 not in list1) # True



<!-- F. Identity Operators -->
Check if two variables refer to the same object:

a = [1, 2]
b = a
c = [1, 2]

1. print(a is b)     # True  (same memory location)
2. print(a is c)     # False (different memory location)
3. print(a == c)     # True  (values are same)



<!--  Input in Python -->
input() function lets users enter data.

By default, input is taken as a string:

1. name = input("Enter your name: ")
   print("Hello", name)
   To take numbers, you must convert them:

2. age = int(input("Enter your age: "))
   pi = float(input("Enter PI value: "))
   print("Next year, you will be", age + 1)



<!-- Output in Python -->
You can display values using print().

Basic Output:
1. print("Hello World")

Multiple Values:
name = "Shaiksha"
age = 23
2. print("My name is", name, "and I am", age, "years old")

Formatted Output (f-strings):
3. print(f"My name is {name} and I am {age} years old")



<!-- Conditional Statements -->

A. Syntax of Conditional Statements
Conditional statements let you make decisions in code based on conditions.

1. if Statement

    if condition:
        # code block


2. if-else Statement

    if condition:
        # code block if True
    else:
        # code block if False


3. if-elif-else Statement

    if condition1:
        # code block if condition1 is True
    elif condition2:
        # code block if condition2 is True
    else:
        # code block if all are False


4. Nested if

    if condition1:
        if condition2:
            # inner code block





<!-- Loops  -->

A. What is a Loop?
   --> loop lets you repeat a block of code multiple times until a condition is met.

B. Types of Loops in Python
    1. for Loop
    2. While Loop


1. for Loop
    Syntax:

    for variable in sequence:
        # code block

    usecase --> iterating over elements    


2. while Loop
    Syntax:

    while condition:
        # code block

    usecase --> Runs while the condition is True.    


3. break Statement
    Syntax:

    for variable in sequence:
        if condition:
            break

    usecase --> Stops the loop immediately.



4. continue Statement
    Syntax:

    for variable in sequence:
        if condition:
            continue

    usecase --> Skips the current iteration and moves to the next.  



5. else with Loops
    Syntax:

    for variable in sequence:
        # code block
    else:
        # executes if loop completes normally (no break)    

    usecase --> Confirm that all data items were processed successfully.




<!-- functions -->

A. What is a Function?
   A function is a block of reusable code that performs a specific task.
   It helps avoid repeating code and makes programs easier to maintain.    

1. Defining and Calling a Function

    Syntax:

    def function_name(parameters):
        # code block

    usecase -->
    When you have to greet multiple users in different parts of your program without rewriting the print statement.




2. Function with Parameters

    Syntax:

    def function_name(param1, param2):
        # code block

    usecase --> Pass user data to a function instead of hardcoding it. 



3. Function with Return Value
    Syntax:

    def function_name(param1, param2):
        return result       

    usecase --> When you need to use the function’s result in further calculations.


4. Default Parameters
    Syntax:
    def function_name(param1=value):
        # code block        
    

    usecase --> Useful when you want a parameter to be optional.


5. Keyword Arguments
    def display_info(name, age):
        print(f"Name: {name}, Age: {age}")

    display_info(age=25, name="Shaiksha")
    Use Case:
    Improves clarity, especially when passing many arguments.


6. Arbitrary Arguments (*args and **kwargs)

    *args → multiple positional arguments (tuple)
    **kwargs → multiple keyword arguments (dictionary)

    
    Example:

    1. def sum_all(*numbers):
        return sum(numbers)
    print(sum_all(1, 2, 3, 4, 5))


    2. def print_details(**details):
        for key, value in details.items():
            print(f"{key}: {value}")
    print_details(name="Shaiksha", age=23, city="Pamidi")

    Use Case --> When you don’t know how many arguments will be passed.





7. Scope of Variables

Local Variable → defined inside a function (accessible only inside)
Global Variable → defined outside a function (accessible everywhere)

    Example:

    x = 10  # global

    def my_function():
        x = 5  # local
        print("Local x:", x)

    my_function()
    print("Global x:", x)



8. Anonymous Functions (Lambda Functions)
    A lambda function is a small, one-line function without a name.
    It is mainly used for short, throwaway functions.

    Syntax:
    lambda arguments: expression


    usecase --> Use Case:
    You need a small function for a short time
    You don’t want to formally define it using def



9. Recursive Functions
    A recursive function is a function that calls itself until a stopping condition is met.

    Syntax:
    def function_name(parameters):
        if stopping_condition:
            return result
        else:
            return function_name(modified_parameters)


    usecase -->
    Recursive functions are useful for:
    Mathematical problems (factorial, Fibonacci series)
    Breaking big problems into smaller ones (divide & conquer)
    Traversing nested data (like folders inside folders)        
