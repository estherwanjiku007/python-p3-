#!/usr/bin/env python3
def greet_programmer():
   print("Hello, programmer!")
greet_programmer()
def greet(name):
    print(f"Hello, {name}!")
greet("Esther")
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
def add(num1, num2):
    my_sum=num1+num2
    print(my_sum)
    return my_sum
add(8,10)
def halve(number):
    my_div=number/2
    print(my_div)
    return my_div
halve(24)
def my_print(args):
    total=0
    for my_nums in args:
         total+=my_nums
    return total
print(my_print([1,2,3,4,5]))
square=lambda x:x*x
print(square(4))
sqrt=lambda y:y/y
print(sqrt(81))
