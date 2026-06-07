# Advanced keyword arguments

# *args : Many positional arguments
def add (*args):
    print(args[0]) # accessing elements because args is a tuple

    sum = 0
    for n in args:
        sum += n
    return sum
print(add(5, 3, 8, 9, 10, 6))

# **kwargs : Many keyworded arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 3, multiply = 5)

# Example

def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x = 10, y = 64)