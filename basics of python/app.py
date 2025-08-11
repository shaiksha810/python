# Data Types

# name = "Shaiksha"   # string
# age = 23            # integer
# height = 5.9        # float
# is_student = True   # boolean



# -------------- Arithematic operators -----------------------
# a = 10
# b = 3

# print(a + b)   # 13
# print(a - b)   # 7
# print(a * b)   # 30
# print(a / b)   # 3.333..
# print(a // b)  # 3
# print(a % b)   # 1
# print(a ** b)  # 1000


# ------------- comparison operartors -------------------------
# x = 5
# y = 7
# print(x == y)  # False
# print(x != y)  # True
# print(x > y)   # False
# print(x <= y)  # True



# -------------- Logical operators --------------------------
# a = 10
# b = 5
# print(a > 0 and b > 0)  # True
# print(a > 0 or b < 0)   # True
# print(not(a > b))       # False



# -------------- Assignment operators --------------------------
# x = 5
# x += 2
# print(x)  # 7
# x -= 3
# print(x)  # 4
# x *= 3
# print(x)  # 12
# x /= 3
# print(x)  # 4.0
# x //= 3
# print(x)  # 1.0
# x %= 3
# print(x)  # 1.0
# x **= 3
# print(x)  # 1.0


# -------------- Bitwise operators --------------------------
# a = 5  # 101 in binary
# b = 3  # 011 in binary
# print(a & b)  # 1  (001)
# print(a | b)  # 7  (111)
# print(a ^ b)  # 6  (110)
# print(~a)     # -6
# print(a << 1) # 10
# print(a >> 1) # 2



# -------------- Membership operators --------------------------
# fruits = ["apple", "banana", "cherry"]
# print("apple" in fruits)      # True
# print("grape" not in fruits)  # True




# -------------- Identity  operators --------------------------
# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]
# print(x is y)     # True  (same memory reference)
# print(x is z)     # False (different objects)
# print(x == z)     # True  (same content)



# -----------------conditional Statements-----------------------------

# 1. if Statement
# age = 20
# if age >= 18:
#     print("You are eligible to vote.")

# # 2. if...else Statement
# age = 16
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote yet.")



# # 3. if...elif...else Statement
# marks = 75

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("Grade: Fail")



# # 4.Nested if Statements
# age = 25
# citizen = True

# if age >= 18:
#     if citizen:
#         print("You can vote in national elections.")
#     else:
#         print("You must be a citizen to vote.")
# else:
#     print("You are not old enough to vote.")



# # 5. Short-hand if (One-liner)    
# x = 10
# if x > 5: print("x is greater than 5")


# # 7. Short-hand if...else (Ternary Operator)
# age = 18
# status = "Adult" if age >= 18 else "Minor"
# print(status)








# -------------------------------------Loops---------------------------------------

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Using range() with for
# range(start, stop, step) generates a sequence of numbers.
for i in range(1, 6):
    print(i)


# While Loop
count = 1
while count <= 5:
    print(count)
    count += 1


# Break
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# pass
for i in range(3):
    pass  # To be implemented later



# nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")


# loops with else
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")
        
















