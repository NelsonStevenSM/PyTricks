from decorators import do_twice
@do_twice
def say_whee():
    print("Whee!!!")

@do_twice
def greet(name):
    print(f"Hello {name}")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

say_whee()
greet("World")
hi_adam = return_greeting("Adam")
print(hi_adam)
print(say_whee)
print(say_whee.__name__)


