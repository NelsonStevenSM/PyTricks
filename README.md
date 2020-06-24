## Decoradores

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
