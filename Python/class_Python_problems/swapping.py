# Q => Given two numbers, write a program to swap both the numbers.
# A =>

def swap_using_third_var(a, b):
    print(f"Initial values are a = {a} and b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swapping inside function values are a = {a} and b = {b}")


a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

print(f"Initial values outisde function are a = {a} and b = {b}")

swap_using_third_var(a, b)

print(f"Final values outside function are a = {a} and b = {b}")
