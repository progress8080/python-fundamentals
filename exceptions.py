def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

print(divide(1, 0))

# python exception handling
try:
    print(divide(1, 0))
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("This will always execute")