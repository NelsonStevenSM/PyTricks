from debug import debug
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


make_greeting("Benjamin")
make_greeting("Richard", age=112)
make_greeting(name="Nelson", age=116)
