def my_decorator(func):
    def wrapper():
        print("Algo esta ocurriendo antes de la función")
        func()
        print("Algo esta ocurriendo despúes de la función")
    return wrapper

def say_Nelson():
    print("Nelson!")

print("Antes de llamar modificar a la función say_Nelson")
say_Nelson()
print("##########################")
say_Nelson = my_decorator(say_Nelson)

say_Nelson()



