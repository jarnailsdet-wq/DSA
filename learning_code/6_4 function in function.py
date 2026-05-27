#function in function
def my__decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
@my__decorator
def say_hello():
    print("Hello, World!")

say_hello()