def add_something(x, y):
    print("casually adding some stuff together")
    z = x + y
    return z


def print_something_fancy(n):
    for it in range(n):
        string_to_print = it * "#"
        print(string_to_print)


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
    print(add_something(5, 2))
    print_something_fancy(20)
    print(fibonacci(35))
