# Juego del contador
import functools
n = 0
def decoratosBoton(func):

    @functools.wraps(func)
    def wrapper_Boton(*args, **kwargs):
        global n
        n += func(*args, **kwargs)
        print(func(*args, **kwargs))
        return n

    return wrapper_Boton


@decoratosBoton
def Boton(n):
    return n


print("Ingresa una de las siguiente Alternativas")
print("Donde \'n\' pertenece al conjunto de los Z")
print("-1 | 1 | n | R")
while(n < 10):
    var = input("> ")
    if (var == 'R'):
        n = 0
        print("Contador de n = 0")
    else:
        print(Boton(int(var)))


print("Termino el juego ")

