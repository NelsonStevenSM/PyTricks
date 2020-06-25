# Decoradores

Un decorador es una función que toma otra función (callback) y extiende el comportamiento de esta última sin modificarla explícitamente.

Recordar que, una función devuelve un valor basado en los argumentos dados.

```python
>>> def suma(a, b):
...		return a + b

>>> suma(2,5)
7
```

**Objetos de primera clase**

Las funciones son de primera clase. Esto significa que las *funciones se pueden pasar y utilizar como argumentos,* al igual que cualquier otro objeto(string, int, float, list, etc). Veamos con el ejemplo:

```python
def hello(name):
	return f"Hola {name}"

def special(name):
	return f"Soy {name}, nosotros somos amigos"

def greet(func):
	return func("Nelson")
```

Aquí, *hello()* y *special()* son funciones regulares que esperan un nombre dado como argumento. Sin embargo, la función *greet()* espera una función como argumento

```python
>>> greet(hello)
'Hello Nelson'

>>> greet(special)
'Soy Nelson, nosotros somos amigos'
```

Las funciones se nombran sin parénteis. Esto significa que solo se pasa una referencia a la función. La función no se ejecuta. 

**Funciones internas**

Es posible definir funciones dentro de otras funciones. Tales funciones se llaman *funciones internas.*

```python
def parent():
	print()"Imprimiendo a la función padre"

	def first_child():
		print("Imprimiendo al primer hijo")

	def second_child():
		print("Imprimiendo al segundo hijo")

	second_child()
	first_child()
```

**Funciones de retorno de funciones**

Python también le permite usar funciones como valores de retorno. 

```python
def parent(num)
	def first_child():
		return "Hola, Soy Marco"

	def second_child():
		return "Me llamo Nelson"

	if num == 1:
		return first_child
	else 
		return second_child
```

Recuede que esto significa que está **devolviendo una referencia a la función first_child.**

Ahora usar **first** y **second** como si fueran funciones regulares, aunque no se puede acceder directamente a las funciones a las que apuntan.

```python
>>> first()
'Hola, Soy Marco'

>>> second()
'Me llamo Nelson'
```

Sin embargo, en este último ejemplo, no agregamos paréntesis a las funciones internas (primer hijo) al retornar. De esta manera, no obtenemos una referencia para cada función que podamos llamar en el futuro.¿Tiene sentido?.

# Decorador Simple

Para entender un poco sobre la bestia mágica que es el Decorado de Python, empezamos con un ejemplo:

```python
def my_decorator(func):
    def wrapper():
        print("Algo esta ocurriendo antes de la función")
        func()
        print("Algo esta ocurriendo despúes de la función")
    return wrapper

def say_whee():
    print("Nelson!")

# Decorador
say_whee = my_decorator(say_whee)
```

En efecto, say_whee ahora apunta a la función interna **wrapper.** Recuerda que la funcipon my_decorator retorna como función **wrapper.**

Sin embargo, wrapper() tiene una referencia al original say_whee() como func, y llama a esa función entre las dos llamas a **print().**

En otras palabras, **los decoradores envuelven una función, modificando su comportamiento.**

# ¡Azúcar sintáctica!

La forma que hemos decorado arriba es un poco torpe. Porque terminamos escribiendo 3 veces el nombre say_whee. Además, la decoración se oculta un poco de la definición de la función.

En cambio, Python le permite **usar decoradores de una manera más simple con el símbolo @ ,** a veces llamado la sintáxis PIE.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

La sintáxis @ es llamar a my_decorator(say_whee) y asi mísmo modifica el comportamiento de la función say_whee.

# Reutilizando decoradores

Recuerde que un decorador es solo una función normal de Python. Todas las herramientas habituales para una fácil reutilización están disponibles.

Cree un archivo [decoratos.py](http://decoratos.py) 

```python
def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
```

Ahora podemos usar este nuevo decorador en otros archivos haciendo una importación regular:

```python
from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")
```

Cuando ejecutamos, debería ver que la función *say_whee* se ejecuta dos veces.

# Funciones de decoración con argumentos

Digamos que tiene una función que acepta algunos argumentos. ¿Todavía puedes decorarlo? Intentemos:

```python
from decorators import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")
```

Al ejecutar nos genera un error:

```python
>>> greet("World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given
```

El problema es que la función interna wrapper_do_twice() no toma ningún argumento, sino que **name** se le pasó.  La solución es usar ***args y **kwargs** en la función de envoltura interna. Entonces aceptará un número arbitrario de argumentos posicionales de palabras claves.

Reescribe el [decoratos.py](http://decoratos.py) de la siguiente manera:

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
```

# Valores devueltos de funciones decoradas

¿Qué sucede con el valor de retorno de las funciones decoradas?. Esto dependerá del decorador a decidir.

```python
from decorators import do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"
```

Nuevamente el decorador se comió el valor de retorno de la función.

Como wrapper_to_twice no devuelve un valor explícitmente, la llamada return_greeting("Adam") terminó devolviendo **None.**

Para solucionar esto, debe **asegurarse de que la función de contenedor devuelva el valor de retorno de la función decorada.**

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

# ¿Quien eres en realidad?

La instropección es la capacidad de un objeto para conocer sus propios atributos en tiempo de ejecución. Por ejemplo, una función conoce su propio nombre y documentación:

```python
>>> print
<built-in function print>

>>> print.__name__
'print'

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    <full help message>
```

La instropección también funciona para las funciones que usted define:

```python
>>> say_whee
<function do_twice.<locals>.wrapper_do_twice at 0x7f43700e52f0>

>>> say_whee.__name__
'wrapper_do_twice'

>>> help(say_whee)
Help on function wrapper_do_twice in module decorators:

wrapper_do_twice()
```

Sin embargo, después de ser decorado, se dice que say_whee ha confundido mucho sobre su identidad. Informa que la función interna **wrapper_do_twice**  esta dentro del decorador **do_twice.** Aunque técnicamente es cierto, esta información no es muy útil.

Para solucionar este problema de instropección, los decoradores deben usar el decorador @functools.wraps, **que preservará la información sobre la función original**. 

```python
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

# Código de depuración

El siguiente decorador **@debug** imprimirá los argumentos con los que se llama a una función, así como su valor de retorno cada vez que se llama a la función:

```python
import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug
```

La asignatura se crea uniendo las representaciones de cadena de todos los argumentos. Los números en la siguiente lista corresponden a los comentarios numerados en el código.

1. Crea una lista de los argumentos posicionales. Use **repr()** para obtener una buena cadena que repesente cada argumento.
2. Cree una lista de argumentos de palabras clave. El string-f formatea cada argumento como key=value donde el especificador **!r** significa que repr() se utiliza para representar el valor.
3. Las listas de argumentos posicionales y de palabras clave se unen en una cadena de firma con cada argumento separado por una coma.
4. El valor de retorno se imprime después de ejecutar la función.

Veamos cómo funciona el decorador en la práctica al aplicarlo a una función simple con una posición y un argumento de palabra clave:

```python
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
```

# Código de ralentización

Los decoradores no tienen que ajustar la función que están decorando. También pueden simplemente registrar que existe una función y devolverla sin abrir. Esto se puede usar, por ejemplo, para crear una arquitectura de complemento ligera:

```python
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
```

El principal beneficio de esta sencilla arquitectura de complementos es que no necesita mantener una lista de los complementos que existen. Esa lista se crea cuando los complementos se registran. Esto hace que sea trivial agregar un nuevo complemento: solo defina la función y decore con ella @register.

