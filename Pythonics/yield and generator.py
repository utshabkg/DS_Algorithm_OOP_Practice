# A Simple Python program to demonstrate working of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time


def yield_func():
    yield 1
    yield 2
    yield 3


# # Use loop
# for value in yield_func():
#     print(value)

# Use Generator
gen = yield_func()

print(next(gen))
print(next(gen))
print(next(gen))
