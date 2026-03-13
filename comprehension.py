numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

names = ["John", "Jane", "Jim", "Jill"]
ages = [20, 21, 22, 23]

age_dict = {name: age for name, age in zip(names, ages)}
print(age_dict)

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)


# python hint

def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(1, 2))

# python logging
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# python logging to file
logging.basicConfig(filename="example.log", level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")