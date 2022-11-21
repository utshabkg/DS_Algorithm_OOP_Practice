def division(a, b):
    print(a / b)


def add_logic(function):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return function(a, b)

    return inner


div = add_logic(division)
div(2, 4)  # changed logic and worked like division(4,2)
division(2, 4)

# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function
#
#
# def display():
#     print("display function ran")
#
#
# decorated_display = decorator_function(display)
#
# decorated_display()
