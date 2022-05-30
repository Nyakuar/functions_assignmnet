
# Write a function that accepts any number of integers as positional
# arguments and any number of a student's attributes as keyword arguments 
# and prints the result of multiplying all of the integers with a customized greeting based o
# n the keyword arguments. Name the function multiply_and_greet.

def multiply_and_greet(*args, **kwargs):
    item = 1
    for x in args:
        total *= x
        print(item)

    key = kwargs.keys()
    if "Country" in key:
        print(f"Hello {kwargs['name']} from {kwargs['country']}") 
    elif "age" in key:
        year = 2022 - kwargs['age']
        print(f"{kwargs['name']} and you're born in {year}") 
    elif "name" in key:
        print(f"{kwargs['name']}") 
    else:
       print(f"Are you a Anonymous?") 
       