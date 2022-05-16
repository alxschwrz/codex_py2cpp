def add_something(x, y):
    print("casually adding some stuff together")
    z = x + y
    return z


def print_something_fancy(n):
    [print(it * "#") for it in range(1, n)]


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print('Okay, lets go...')
    x = add_something(5, 4)
    print("taking the result and printing something fancy with it...")
    print_something_fancy(x)
    print("doing the fibonacci of {}...".format(35))
    print(fibonacci(35))
