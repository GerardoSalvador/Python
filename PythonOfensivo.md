# Python Ofensivo

## Introduccion al curso de python ofensivo

Nos detalla la ruta correcta para llegar a ser pentester, llevando primero el curso de linux, luego el de personalizacion de linux, luego este de python y por ultimo el de introduccion a la ciberseguridad.

## Historia y filosofía de Python

* Python fue creado por Guido Van Rossum, programador Holandes en 1989.
* El propósito principal del desarrollo de python, era la productividad del programador y la legibilidad del código.
* La filosofia de python se resume en el Zen Of Python, la cual es una colección de 19 aforismos que sirven como guia para escribir programas en Python.
* Python es un lenguaje de programación de **alto nivel e interpretado**.

## Características y ventajas de Python

### Características

* **Sintaxis simple y fácil de aprender:** Python es famoso por su legibilidad, lo que facilita el aprendizaje para los principiantes y permite a los desarrolladores expresar conceptos complejos en menos líneas de código que serían necesarias en otros lenguajes.
* **Interpretado:** Python es procesado en tiempo de ejecución por el intérprete. Puedes ejecutar el programa tan pronto como termines de escribir los comandos, sin necesidad de compilar.
* **Tipado dinámico:** Python sigue las variables en tiempo de ejecución, lo que significa que puedes cambiar el tipo de datos de una variable en tus programas.
* **Multiplataforma:** Python se puede ejecutar en una variedad de sistemas operativos como Windows, Linux y MacOs.
* **Bibliotecas extensas:** Python cuenta con una gran biblioteca estándar que está disponible sin cargo alguno para todos los usuarios.
* **Soporte multiparadigma:** Python soporta varios estilos de programación, incluyendo programación orientada a objetos, imperativa y funcional.

### Ventajas de usar Python

* **Productividad mejorada:** La simplicidad de Python aumenta la productividad de los desarrolladores ya que les permite enfocarse en resolver el problema en lugar de la complejidad del lenguaje.
* **Amplia comunidad:** Una comunidad grande y activa significa que es fácil encontrar ayuda, colaboración y contribuciones de terceros.
* **Aplicabilidad en múltiples dominios:** Python se utiliza en una variedad de aplicaciones, desde desarrollo web hasta inteligencia artificial, ciencia de datos y automatización.
* **Compatibilidad y colaboración:** Python se integra fácilmente con otros lenguajes y herramientas, y es una excelente opción para equipos de desarrollo colaborativos.

## Diferencias entre Python2, Python3, PIP2 y PIP3

Python 2 y 3 son dos versiones del lenguaje de programacion Python, cada una con sus propias características y diferencias clave. PIP2 y PIP3 son las herramientas de gestión de paquetes correspondientes a cada versión, utilizadas para instalar y administrar bibliotecas y dependencias.

Python2 vs Python3:

* **Sintaxis de print:** En python 2, 'print' es una declaración, mientras que en Python3, 'print()' es una función, lo que requiere el uso de paréntesis.
* **División de enteros:** Python 2 realiza una división entera por defecto, mientras que Python 3 realiza una división real (flotante) por defecto.
* **Unicode:** Python 3 usa Unicode (texto) como tipo de datos por defecto para representar cadenas, mientras que Python 2 utiliza ASCII.
* **Librerías:** Muchas librerías populares de Python 2 han sido actualizadas o reescritas para Python 3, con mejoras y nuevas funcionalidades.
* **Soporte:** Python 2 llegó al final de su vida útil en 2020, lo que significa que ya no recibe actualizaciones, ni siquiera para correciones de seguridad.

PIP2 vs PIP3:

* **Gestión de paquetes:** PIP2 y PIP3 son herramientas que permiten instalar paquetes para Python 2 y Python 3, respectivamente. Es importante usar la versión correcta para garantizar la compatibilidad con la versión de Python que estés utilizando.
* **Comandos de instalación:** El uso de PIP o PIP3 antes de un comando determina si el paquete se instalará en Python2 o Python3. Algunos sistemas operativos pueden requerir especificar PIP 2 o PIP3 explícitamente para evitar ambigüedades.
* **Ambientes virtuales:** Es una buena práctica usar ambientes virtuales para mantener separadas las dependencias de proyectos específicos y evitar conflictos entre versiones de paquetes para Python2 y Python3.

## El interprete de Python

El intérprete de Python es el motor que ejecuta el código. Cuando nos referimos al intérprete de Python nos referimos al programa que lee y ejecuta el código en tiempo real.

Funciones clave del intérprete de Python:

* **Ejecución de código:** El intérprete ejecuta el código línea por línea, lo que facilita la depuración y permite a los desarrolladores probar fragmentos de códigos de forma interactiva.
* **Modo interactivo:** El intérprete puede usarse en un modo interactivo que permite a los usuarios ejecutar comando de Python uno a uno y ver los resultados de inmediate.
* **Modo script:** Además puede ejecutar programas completos o scripts que se escriben en archivos con la extensión *'.py'*
* **Compilación a Bytecode:** Internamente, el intérprete compila el código a bytecode antes de ejecutarlo, lo que mejora el rendimiento.
* **Máquina Virtual de Python:** El bytecode compilado se ejecuta en la Máquina Virtual de Python (Python Virtual Machine - PVM), que es una abstracción que hace que el código sea portable y se pueda ejecutar en cualquier S.O. donde el intérprete esté disponible.

Ventajas del intérprete:

* **Facilidad de uso:** La capacidad de ejecutar código inmediatamente y de manera interactiva hace de Python una herramienta excelente para principiantes y para el desarrollo rápido de aplicaciones.
* **Portabilidad:** Está disponible en múltiples plataformas.
* **Extensibilidad:** Permite la extensión con módulos escritos en otros lenguajes como C o C++, lo que puede ser utilizado para optimizar el rendimiento.

## Shebang y convenios de Python

* **Shebang:** Sirve para decir con que debe ser interpretado el script

Si deseamos correr el script como un ejecutable podemos dejar la shebang, agregar permisos de ejecución al script python y ejecutarlo como ejecutable como:

```Python
#!/usr/bin/python3
#!/usr/bin/env python3
print("Hola")
```

> #/home/gersal > **chmod +x test.py** \
> #/home/gersal > **./test.py** \
> hola

* **Uso de  main:** Python define todos sus scripts como modulos principales, el uso de main me permite validar al importarla a otro script que el módulo es el principal o secundario, segun cual este ejecutando.

Código de test.py

```Python
#!/usr/bin/python3
if __name__ == '__main__':
    print("Soy el módulo principal")
else:
    print("No soy el módulo principal")
```

> #/home/gersal > **./test.py** \
> Soy el módulo principal

Código de prueba.py

```Python
#!/usr/bin/python3
import test
```

> #/home/gersal > **./prueba.py** \
> No soy el módulo principal

### Convenios de Python

```Python
#!/usr/bin/python3
def comprobacionEstadoApi(): # Convenio loweCamelCase, usado para crear nombres de funciones, el primer caracter de la primera palabra que conforma el nombre de la funcion debe ir en minúscula, y el primer caracter de las palabras siguientes debe estar en mayúsculas.

class TwitterApi: # Convenio UpperCamelCase, usado para crear nombres de clases y excepciones, el primer caracter de todas las palabras que conforman el nombre de la clase inician con mayúscula

    VERSION_API = 1 # Convenio SCREAMING_SNAKE_CASE, usado para crear nombres de constantes en python
    URL_API = "https://gerardosalvador.com.mx"

# La guía de estilo para la programación en Python (PEP 8), nos dice que los nombres de funciones en Python deberían seguir el convenio snake_case
def comprobar_estado_api(): # Convenio snake_case usado para establecer el nombre de las funciones o variables en python
```

## Variables y tipos de datos

```Python
#!/usr/bin/python3

ip_address = "192.168.1.1" # variable de tipo cadena
port = 80 # variable de tipo entero
number = 4.5 # variable de tipo float
print(type(ip_address)))
print(type(port)))
print(type(number)))
```

> #/home/gersal > **./variables.py** \
> <class 'str' > \
> <class 'int' > \
> <class 'float' >

### Type casting

El type casting sirve para convertir de un tipo de dato a otro.

```Python
#!/usr/bin/python3

number = 4
print(number)
print(type(number))

number = float(4)
print(number)
print(type(number))

number = str(4)
print(number)
print(type(number))
```

> #/home/gersal > **./variables.py** \
> 4 \
> <class 'int' > \
> 4.0 \
> <class 'float' > \
> 4 \
> <class 'str' >

### Listas

```python
#!/usr/bin/env python3

my_ports = [22, 10, 34] # Estructura de creación de una lista
my_ports.append (80) # Con append solo podemos pasarle un argumento
my_ports.extend([84, 85]) # Extend si nos permite agregar mas de un argumento a una lista en python
my_ports += [86, 87]

for port in my_ports:
    print(f"Puerto: {port}")
print(f"\n[+] La lsita tiene un total de {len(my_ports)} elementos")

my_ports = sorted(my_ports) # Para ordenar una lista de menor a mayor
del my_ports[0] # El 0 indica la posicion que se desea eliminar de una lista

for port in my_ports:
    print(f"Puerto: {port}")
print(f"\n[+] La lsita tiene un total de {len(my_ports)} elementos")
```

> #/home/gersal > **./listas.py** \
> Puerto: 22 \
> Puerto: 10 \
> Puerto: 34 \
> Puerto: 80 \
> Puerto: 84 \
> Puerto: 85 \
> Puerto: 86 \
> Puerto: 87 \
> [+] La lista tiene un total de 10 elementos \
> #/home/gersal > **./listas.py** \
> Puerto: 10 \
> Puerto: 22 \
> Puerto: 34 \
> Puerto: 80 \
> Puerto: 84 \
> Puerto: 85 \
> Puerto: 86 \
> Puerto: 87 \
> [+] La lista tiene un total de 10 elementos

### Uso de listas

```python
#!/usr/bin/env python3
my_list[5, 6, 7, 8, 9, 10]
print(my_list[:2]) # Imprime los primeros 2 elementos de la lista my_list
print(my_list[:3]) # Imprime los primeros 3 elementos de la lista my_list
print(my_list[:4]) # Imprime los primeros 4 elementos de la lista my_list
print(my_list[4]) # Imprime el elemento de la posicion 4, pos 0, pos 1, pos 2, etc
print(my_list[0]) # Imprime el elemento de la posicion 0, pos 0, pos 1, pos 2, etc
print(my_list[0:3]) # Imprime un rango de una lista definiendo el rango con pos:pos, el último no lo contempla [5, 6, 7]
print(my_list[2:]) # Omite los 2 primeros elementos de la lista
print(my_list[3:]) # Omite los 3 primeros elementos de la lista
print(my_list[-1]) # Imprime en reversa, siendo -1 el último elemento de la lista
```

> [5, 6] \
> [5, 6, 7] \
> [5, 6, 7, 8] \
> 9 \
> 5 \
> [5, 6, 7] \
> [7, 8, 9, 10] \
> [8, 9, 10] \
> [10]

```python
#!/usr/bin/env python3
my_list = [1, 2, 3, 4]
my_list.insert(2, 9) # Insertamos en la posicion 2 el valor 9
print(my_list)
my_list.insert(2, 5)
print(my_list)
my_list.pop() # Elimina el ultimo elemento de una lista
my_list.index(4) # Para saber el indice del valor 4

print(max(my_list)) # Nos devuelve el valor mas alto
print(min(my_list)) # Nos devuelve el valor mas bajo
print(sum(my_list)) # suma los valores de la lista
print(len(my_list)) # nos dice el tamaño de la lista
print(sum(my_list) / len(my_list)) # nos da el promedio de los numeros dentro de la lista
print(round(sum(my_list) / len(my_list), 2)) # redondea a 2 decimales
```

> [1, 2, 9, 3, 4] \
> [1, 2, 5, 9, 3, 4] \
> [1, 2, 5, 9, 3] \
> 5 \
> 9 \
> 1 \
> 14

## Operadores básicos en Python

```python
#!/usr/bin/env python3
first_number = 12
second_number = 7
result = first_number ** second_number # Elevar a una potencia.
print("{:,}".format(result)) # Nos da el formato de separacion por comas en miles
print("{:,}".format(result).replace(",", ".")) # Las comas las cambia por puntos
```

> 35,831,808 \
> 35.831.808

## String Formatting

Python proporciona varias maneras de formatear cadenas, permitiendo insertar variables en ellas, así como controlar el espaciado, alineación y precisión de los datos mostrados

### Operador % (Porcentaje)

También conocido como 'interpolación de cadenas', este método clásico utiliza marcadores de posición como '%s' para enteros, o '%f' para números de puntos flotante.

```python
#!/usr/bin/env python3
name = "gerardo"
rol = "pentester"
edad = 26

print(name)
print("Hola mi nombre es " + name)
print("Hola, mi nombre es %s" % name)
print("Hola, mi nombre es %s y soy un %s" % (name, rol))
print("Hola, mi nombre es %s,  soy un %s y tengo %d años" % (name, rol, edad)) #la %d infiere a decimal
```

> gerardo \
> Hola mi nombre es gerardo \
> Hola, mi nombre es gerardo \
> Hola, mi nombre es gerardo y soy un pentester \
> Hola, mi nombre es gerardo, soy un pentester y tengo 26 años

### Método format()

Introducción en Python 2.6, permite una mayor flexibiliad y claridad. Utiliza llaves '{}' como marcadores de posición dentro de la cadena y puede incluir detalles sobre el formato de la salida.

```python
#!/usr/bin/env python3
name = "gerardo"
rol = "pentester"
edad = 26

print("Hola, soy {}!".format(name))
print("Hola, soy {}! y tengo {} años".format(name, edad))
print("Hola, soy {0}! y tengo {1} años. No es broma, mi nombre real es {0}".format(name, edad))# Jugando con los indices
```

> Hola, soy gerardo! \
> Hola, soy gerardo! y tengo 26 años \
> Hola, soy gerardo! y tengo 26 años. No es broma, mi nombre real es gerardo

### F-Strings (Literal String Interpolation)

Disponible desde Python 3.6, los F-Strings ofrecen una forma concisa y legible de incrustar expresiones dentro de literales de cadena usando la letra 'f' antes de las comillas de apertura y llaves para indicar dónde se insertarán las variables o expresiones.

```python
#!/usr/bin/env python3
name = "gerardo"
rol = "pentester"
edad = 26

print(f"Hola, soy {name}!")
print(f"Hola, soy {name}! y tengo {edad}")
print(f"Hola, soy {name}! y tengo {edad}. No es broma, mi nombre real es {name}")
```

> Hola, soy gerardo! \
> Hola, soy gerardo! y tengo 26 años \
> Hola, soy gerardo! y tengo 26 años. No es broma, mi nombre real es gerardo

## Control de flujos (Condicionales y Bucles)

### Condicionales

Los condicionales son estructuras de control que permiten ejecutar diferentes bloques de código dependiendo de si una o más condiciones son verdaderas o falsas. En Python, las declaraciones condicionales más comunes son 'if', 'elif' y 'else'

* if: Evalúa si una condición es verdadera y, de ser así, ejecuta un bloque de código.

```python
#!/usr/bin/env python3
edad = 20
mensaje  = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad" # Operadores ternarios
```

* * and: Condición lógica que me ayuda a determinar que se cumpla una accion y otra
* * or: Condición lógica que me ayuda a determinar que se cumpla una accion u otra

* elif: Abreviatura de "else if", se utiliza para verificar múltiples expresiones sólo si las anteriores no son verdaderas.
* else: Captura cuaquier caso que no haya sido capturado por las declaraciones 'if' y 'elif' anteriores.

### Bucles

Los bucles permiten ejecutar un bloque de código repetidamente mientras una condición sea verdadera o para cada elemento en una secuencia. Los dos tipos principales de bucles que utilizamos en Python son 'for' y 'while'.

* **for:** Se usa para iterar sobre una secuencia (como una lista, un diccionario, una tupla o un conjunto) y ejecutar un bloque de código para cada elemento de la secuencia.

```python
#!/usr/bin/env python3
for i in range(5):
    print(i)

names = ["Gerardo", "Marcelo", "Lobotec", "Hackermate", "TheGoodHacker"]
for name in names:
    print(name)
```

> 0 \
> 1 \
> 2 \
> 3 \
> 4 \
> Gerardo \
> Marcelo \
> Lobotec \
> Hackermate \
> TheGoodHacker

Tanto bucles for como while pueden usar la sentencia else:

```python
#!/usr/bin/env python3
for i in range(6):
    if i == 10:
        break
else:
    print("Bucle concluido exitosamente")
print("Continuamos con la ejecución del bucle")
```

> Bucle concluido exitosamente \
> Continuamos con la ejecución del bucle

* **while:** Ejecuta un bloque de código repetidamente mientras una condición específica se mantiene verdadera.

```python
#!/usr/bin/env python3
i = 0

while i < 5:
    print(i)
    i += 1
```

> 0 \
> 1 \
> 2 \
> 3 \
> 4 \

* **enumerate:** Siempre devuelve el indice y el elemento

```python
#!/usr/bin/env python3
nombres = ["Gerardo", "Marcelo", "TheGoodHacker", "Lobotec"]
for i, nombre in enumerate(nombres):
    print(f"Nombre [{i+1}]: {nombre}")


odd_list = [1, 3, 5, 7, 9]
cuadrado = [i ** 2 for i in odd_list]
print(cuadrado)
```

> Nombre [1]: Gerardo \
> Nombre [2]: Marcelo \
> Nombre [3]: TheGoodHacker \
> Nombre [4]: Lobotec \
> [1, 9, 24, 49, 81]

### Control de flujo en bucles

Existen declaraciones de control de flujo que pueden modificar el comportamiento de los bucles, como 'break', 'continue' y 'pass'.

* break: Termina el bucle y pasa el control a la siguiente declaración fuera del bucle.

```python
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    print(i)
    if i == 5:
        break
```

> 0 \
> 1 \
> 2 \
> 3 \
> 4 \
> 0 \
> 1 \
> 2 \
> 3 \
> 4 \
> 5

* continue: Omite el resto del código dentro del bucle y continúa con la siguiente iteración.

```python
#!/usr/bin/env python3
for i in range(10):
    if i == 5:
        continue
    print(i)
```

En la salida vemos como se omite el valor 5
> 0 \
> 1 \
> 2 \
> 3 \
> 4 \
> 6 \
> 7 \
> 8 \
> 9

* pass: No hace nada, se utiliza como una declaración de relleno donde el código eventualmente irá, pero no ha sido escrito todavía.

## Funciones  y ámbitos de las variables

### Funciones

Las funciones son bloques de código reutilizables diseñados para realizar una tarea específica. Se definen usando la palabra reservada 'def' seguido de un nombre descriptivo, paréntesis que pueden contener parámetros y dos puntos. Los parámetros son 'variables de entrada' que pueden cambiar cada vez que se llama a la función. Esto permite a las funciones operar con diferentes datos y producir resultados correspondientes.

Las funciones pueden devolver valores al programa principal o a otras funciones mediante la palabra clave "return". Esto las hace increíblemente versátiles, ya que pueden procesar datos y luego pasar esos datos modificados a otras partes del programa.

```python
#!/usr/bin/env python3
def saludo():
    print("\nHola mundo")

saludo()
```

> Hola mundo

Pasando un argumento a la función para imprimir el nombre pasado quedaría:

```python
#!/usr/bin/env python3
def saludo(nombre):
    print(f"\nHola {nombre}")

saludo("Gerardo")
```

> Hola Gerardo

Realizando una suma con una función pasando dos argumentos para ser sumados:

```python
#!/usr/bin/env python3
def suma(numero_uno, numero_dos):
    print("[+] La suma es igual a: ",numero_uno + numero_dos)

suma(2,3)
```

> [+] La suma es igual a: 5

```python
#!/usr/bin/env python3
def suma(number_one, number_two):
    return x + y
resultado = suma(2, 8) #Es conveniente guardar el resultado de una función en una variable

print(f"\n[+] El resultado es {suma(1,5)}")
```

> [+] El resultado es 6

### Ámbito de las variables (Scope)

El ámbito de las variables se refiere a la región de un porgrama donde esa variable es accesible, hay dos tipos de principales ámbitos:

* Local: Las variables definidas dentro de una función tienen un ámbito local, lo que significa que solo pueden ser accesadas y modificadas dentro de la función donde fueron creadas.

```python
#!/usr/bin/env python3
def mi_funcion():
    variable_local = "Soy local"
    print(variable_local)

mi_funcion()
print(variable_local) # Nos da error porque es una variable local de la funcion por lo cual no esta accesible desde fuera de la funcion
```

> Soy local \
> Error, Error, Error

* Global: Las variables definidas fuera de todas las funciones tiene un ámbito global, lo que significa que pueden ser accesadas desde cualquier parte del programa. Sin embargo, para modificar una variable global dentro de una función, se debe declarar como global.

```python
#!/usr/bin/env python3
variable = "Soy global"

def mi_funcion():
    variable = "Soy local"
    print(variable)

mi_funcion()
print(variable)
```

> Soy local \
> Soy global

```python
#!/usr/bin/env python3
variable = "Soy global"
def my_function():
    global variable
    variable = "Soy global y he sido modificado"
    print(variable)

my_function()
print(variable)
```

> Soy global y he sido modificado \
> Soy global y he sido modificado

## Funciones lambda anónimas

Esta clase se centra en una característica poderosa y expresiva de Python que permite la creación de funciones en una sola línea: las funciones Lambda.

### Funciones Lambda

Las funciones lambda son también conocidas como funciones anónimas debido a que no se les asigna un nombre explícito al definirlas. Se utilizan para crear pequeñas funciones en el lugar donde se necesitan, generalmente para una operación específica y breve. En python, una función lambda se define con la palabra clave 'lambda', seguida de una lista de argumentos, dos puntos y la expresión que desea evaluar y devolver.

Una de las ventajas de las funciones lambda es su simplicidad sintáctica, lo que las hace ideal para su uso en operaciones que requieren una función por un breve momento y para casos donde la definición de una función tradicional completa sería excesivamente verbosa.

```python
#!/usr/bin/env python3
my_function = lambda: "Hola mundo"
print(my_function)
```

> Hola mundo

Pasando un argumento a funcion anónima

```python
#!/usr/bin/env python3
cuadrado = lambda x: x**2 #recibe el parametro "x"
print(cuadrado(6))
```

> 36

pasando dos argumentos a función anónima

```python
#!/usr/bin/env python3
suma = lambda x, y: x + y
print(suma(2,10))
```

> 12

### Usos comunes de las funciones lambda

* Con funciones de órden superior: Como aquellas que requieren otra función como argumento, por ejemplo, 'map()', 'filter()' y 'sorted()'.

* * map()

```python
#!/usr/bin/env python3
#map recibe una funcion y un iterable
numeros = [1,2,3,4,5]
cuadrados = map(lambda x: x**2, numeros) #funcion e iterable

for numero in cuadrados:
    print(numero)
```

> 1 \
> 4 \
> 9 \
> 16 \
> 25

Simplificando la operacion anterior:

```python
#!/usr/bin/env python3
numeros = [1,2,3,4,5]
cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados)
```

> [1, 4, 9, 16, 25]

* * filter()

Ocupamos este caso para filtrar por numeros pares

```python
#!/usr/bin/env python3
#filter en base a la condicion si devuelve un true o un false te devuelve un numero
numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
pares = list(filter(lambda x: x % 2 == 0, numeros))#lo metemos dentro de una lista para poder printearlo 

print(pares)
```

> [ 2, 4, 6, 8, 10, 12]

Para este caso filtramos por numeros impares

```python
#!/usr/bin/env python3
numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)
```

> [1, 3, 5, 7, 9, 11]

* Operaciones simples: Para realizar cálculos o acciones rápidas donde una función completa sería inncesariamente larga.
* Funcionalidad en línea: Cuando se necesita una funcionalidad simple sin la necesidad de reutilizarla en otro lugar del código.

## Manejo de errores y excepciones

Los errores pueden ocurrir por muchas razones: errores de código, datos de entraa incorrectos, problemas de conectividad, entre otros. En lugar de permitir que un programa falle con un error, Python nos proporciona herramientas para 'atrapar' estos errores y manejarlos de manera controlada, evitando así que el programa se detenga inesperadamente y permitiendo reaccionar de manera adecuada.

### Excepciones

Una excepción en Python es un evento que ocurre durante la ejecución de un programa que interrumple el flujo normal de las instrucciones del programa. Cuando el intérprete se encuentra con una situación que no puede manejar, 'levanta' o 'arroja' una excepción.

### Bloques try y except

Para manejar las excepciones, utilizamos los bloques 'try' y 'except'. Un bloque 'try' contiene el código que puede producir una excepción, mientras que un bloque 'except'captura la excepción y contiene el código que se ejecuta cuando se produce una.

Division da error por división entre cero

```python
#!/usr/bin/env python3
try:
    num = 5/0
except ZeroDivisionError: # Se define el tipo de error para ser específico
    print("No se puede dividir un número entre cero")
```

> No se puede dividir un número entre cero

Division con otro tipo de dato para este ejemplo una cadena contra un entero

```python
#!/usr/bin/env python3
try:
    num = "Hola" / 4
except ZeroDivisionError: # Se define el tipo de error para ser específico
    print("No se puede dividir un número entre cero")
except TypeError: # Se define otro tipo de error
    print("No se puede dividir entre diferentes tipos de datos")
except:
    ("Esta excepcion la estoy agregando para añadir el except sin un tipo de error")
```

> No se puede dividir entre diferentes tipos de datos

### Otras palabras clave de manejo de excepciones

* else: Se puede usar después de los bloques 'except' para ejecutar código si el bloque 'try' no generó una excepción.
* finally: Se utiliza para ejecutar código que debe correr independientemente de si se produjo una excepción o no, como cerrar un archivo o una conexión de red.

```python
#!/usr/bin/env python3
try:
    num = "hola" / 1
except ZeroDivisionError:
    print("No se puede dividir un número entre cero")
except TypeError:
    print("Las operatorias matemáticas sólo deben realizarse con números")
else:
    print(f"La división de ambos números da como resultado {num}")
finally:
    print("Esto siempre se va a ejecutar")
```

> Las operatorias matemáticas sólo deben realizarse con números \
> Esto siempre se va a ejecutar

### Levantar excepciones

También es posible 'levantar' excepciones intecionalmente con la palabra clave 'raise', lo que permite forzar que se produzca una excepción bajo condiciones específicas.

```python
#!/usr/bin/env python3
x = -5
if x<0:
    raise Exception("No se pueden utilizar números negativos")
```

> Traceback (most recent call last): \
> raise Exception("No se pueden utilizar números negativos") \
> Exception: No se pueden utilizar números negativos

## Listas en Python

La listas son estructuras de datos que nos permiten almacenar secuencias ordenadas de elementos. Son mutables, lo que significa que podemos modificarlas después de su creación, y son dinámicas, permitiéndonos añadir o quitar elementos de ellas.

### Características de las Listas

* Almacenar datos herogéneos, es decir, pueden contener elementos de diferentes tipos (enteros, cadenas, flotantes y más) dentro de una misma lista.
* Ser indexadas y cortadas, lo que permite acceder a elementos específicos de la lista directamente a través de su índice.
* Ser anidadas, es decir, una lista puede contener otras lsitas como elementos, lo que permite crear estructuras de datos complejas como matrices.

### Operaciones con listas

* Añadir elementos con métodos como 'append()' y 'extend()'.
* Eliminar elementos con métodos como 'remove()' y 'pop()'.
* Ordenar las listas con el método 'sort()' o la función incorporada 'sorted'.
* Invertir los elementos de una lista con el método 'reverse()' o la sintaxis de corte '[::-1]'.
* Comprender las compresiones de listas, una forma "pythonica" de crear y manipular listas de manera concisa y eficiente.

```python
#!/usr/bin/env python3
tcp_ports = [21,22,25,80,443,8880,445,69]
print(tcp_ports)
print(len(tcp_ports)) # Imprime el tamaño de la lista

tcp_ports.append(1337) # Añade un nuevo valor a la lista
print(tcp_ports)

tcp_ports.remove(22) # Remueve el valor 22 de la lista
print(tcp_ports)

tcp_ports.sort() # Ordena los valores de menor a mayor
print(tcp_ports)

tcp_ports.reverse() # Ordena los valores de manera inversa
print(tcp_ports)

other_ports = tcp_ports[2:4] # Nos muestra un rango de valores dentro de la lista por indice
print(other_ports)

attacks = ["Phising", "DDoS", "SQL Injection", "Man In The Middle", "Cross-Site Scripting"]
for i, attack in enumerate(attacks):
    print(f"\nAtaque #{i}: {attack}\n")

attacks = ["Phising", "DDoS", "SQL Injection", "Man In The Middle", "Cross-Site Scripting"]

attacks_uppercase = [attack.upper() for attack in attacks] # Convertimos los nombres a Mayúsculas
print(attacks_uppercase)

names = ["Gerardo", "Marcelo", "HackerMate", "Lobotec", "Hackavis", "Savitar"]
edades = [26, 27, 45, 13, 20, 27]

for name, edad in zip(names,edades): # Zip nos sirve para recorrer dos listas del mismo tamaño a la par
    print(f"{name} tiene {edad} años")

print(names)
deleted_user = names.pop(3) # Eliminamos un nombre de la lista por su indice a la vez que lo agregamos a una variable
print(f"El usuario eliminado ha sido {deleted_user}")
print(names)

names.insert(2, "Ivon") # Inserta un elemento en la posicion 2 y recorre la lista
print(names)
```

> [21, 22, 25, 80, 443, 8880, 445, 69] \
> 8 \
> [21, 22, 25, 80, 443, 8880, 445, 69, 1337] \
> [21, 25, 80, 443, 8880, 445, 69, 1337] \
> [21, 25, 69, 80, 443, 445, 1337, 8880] \
> [8880, 1337, 445, 443, 80, 69, 25, 21] \
> [445, 443] \
> Ataque #0: Phising \
> Ataque #1: DDoS \
> Ataque #2: SQL Injection \
> Ataque #3: Man In The Middle \
> Ataque #4: Cross-Site Scripting \
> ['PHISING', 'DDOS', 'SQL INJECTION', 'MAN IN THE MIDDLE', 'CROSS-SITE SCRIPTING'] \
> Gerardo tiene 26 años \
> Marcelo tiene 27 años \
> Hackermate tiene 45 años \
> Lobotec tiene 13 años \
> Hackavis tiene 20 años \
> ['Gerardo', 'Marcelo', 'HackerMate', 'Lobotec', 'Hackavis', 'Savitar'] \
> El usuario eliminado ha sido Lobotec \
> ['Gerardo', 'Marcelo', 'HackerMate', 'Hackavis', 'Savitar'] \
> ['Gerardo', 'Marcelo', 'Ivon', 'HackerMate', 'Hackavis', 'Savitar']

## Tuplas en Python

Las tuplas son colecciones ordenadas de elementos que no pueden modificarse una vez creadas (inmutables). Esta característica las hace ideales para asegurar que ciertos datos permanezcan constantes a lo largo del ciclo de vida de un programa.

```python
#!/usr/bin/env python3
numeros = (1,2,3,4,5) # Las tuplas se definen con paréntesis
my_first_tuple = (2,4,6,8)
my_second_tuple = (1,3,5,7)

my_third_tuple = my_first_tuple + my_second_tuple
print(my_third_tuple)

my_third_tuple = my_first_tuple * 3
print(my_third_tuple)

numeros_pares = tuple(i for i in numeros if i % 2 == 0)
print(numeros_pares)
```

> (1, 2, 3, 4, 5, 6, 7, 8) \
> (2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8) \
> (2, 4) \

### Características de las tuplas

* Inmutabilidad: Una vez que se crea la tupla, no puedes cambiar, añadir o eliminar elementos. Esta inmutabilidad garantiza la integridad de los datos que desea mantener constantes.
* Indexación y Slicing: Al igual que las listas, puedes acceder a los elementos de la tupla mediante índices y también puedes realizar operaciones de slicing para obtener subsecuencias de la tupla.
* Heterogeneidad: Las tuplas pueden contener elementos de diferentes tipos, incluyendo otras tuplas, lo que las hace muy versátiles.

### Operaciones con tuplas

Aunque no puedes modificar una tupla, hay varias funciones que puedes realizar:

* Empaquetado y desempaquetado de tuplas: Las tuplas permiten asignar y desasignar sus elementos a múltiples variables de forma simultánea.
* Concatenación y repetición: Similar a las listas, puedes combinar tuplas usando el operardo '+' y repetir los elementos de una tupla un número determinado de veces con el operador '*'.
* Métodos de búsqueda: Puedes usar métodos como 'index()' para encontrar la posición de un elemento y 'count()' para contar cuántas veces aparece un elemento en la tupla

### Uso de tupla en python

* Funciones y asignaciones múltiples: Las tuplas son muy útiles cuando una función necesita devolver múltiples valores o cuando se realizan asignaciones múltiples en una sola línea.
* Estructuras de datos fijas: Se usan para crear estructuras de datos que no deben cambiar, como los días de la semana o las coordenadas de un punto en el espacio.

## Conjuntos en Python

Los conjuntos son una colección de elementos sin órden y sin elementos repetidos, inspirados en la teoría de conjutnos de las matemáticas. Son ideales para la gestión de coleeciones de elementos únicos y operaciones que requieren eliminar duplicados o realizar comparaciones de conjuntos.

### Características de los conjuntos

* Unicidad: Los conjuntos automáticamente descartan elementos duplicados, lo que los hace perfectos para recolectar elementos únicos.
* Desordenados: A diferencia de las listas y las tuplas, los conjuntos no mantiene los elementos en ningún órden específico.
* Mutabilidad: Los elementos de un conjunto pueden ser agregados o eliminados, pero los elementos mismos deben ser inmutables (por ejemplo, no puedes tener un conjunto de listas, ya que las listas se pueden modificar).

### Operaciones con conjuntos

Exploraremos las operaciones básicas de conjutnos que Python facilita, como:

* Adición y eliminación: Añadir elemento con 'add()' y eliminar elementos con 'remove()' o 'discard()'.
* Operaciones de conjuntos: Realizar uniones, intersecciones, diferencias y diferencias simétricas utilizando métodos o operadores respectivos.
* Pruebas de pertenencia: Comprobar rápidamente si un elemento es miembro de un conjunto.
* Inmutabilidad opcional: Usar el tipo 'frozenset' para crear conjutnos que no se pueden modificar despues de su creación.

### Uso de conjuntos en Python

* Eliminacion de duplicados: Son útiles cuando necesitas asegurarte de que una colección no tenga elementos repetidos.
* Relaciones entre colecciones: Facilitan la comprensión y el manejo de relaciones matemáticas entre colecciones, como subconjuntos y superconjuntos.
* Rendimiento de búsqueda: Proporcionan una búsqueda de elementos más rápida que las listas o las tuplas, lo que es útil para grandes volúmenes de datos.

```python
#!/usr/bin/env python3

mi_conjunto = {1,2,3}

mi_conjunto.add(98)
print(mi_conjunto)

mi_conjunto.update({23,32,11})
print(mi_conjunto)

mi_conjunto.remove(3)
print(mi_conjunto)

#mi_conjunto.remove(1222) # Al no encontrar el elemento nos dará error, usar discard()cuando no estemos seguros que ese elemento esta dentro del set.
mi_conjunto.discard(1222) # Usamos discard para evitar errores al no encontrarlo
print(mi_conjunto)

# INTERSECCIONES
first_set = {1,2,3,4,5}
second_set = {1,2,3,4,5,6,7,8}

intersection_set = first_set.intersection(second_set)
print(f"Nos muestra los elementos en comun del primer set {first_set} y el segundo set {second_set}: {intersection_set}")

# UNIONES
union_set = first_set.union(second_set)
print(f"Nos muestra ambos set unidos sin repeticiones, primer set {first_set} y el segundo set {second_set}: {union_set}")

# SUBCONJUNTOS
print(first_set.issubset(second_set))

# BUSQUEDA
mi_set = set(range(1000))
print(34 in mi_set)
```

> {1, 2, 3, 98} \
> {32, 1, 2, 3, 98, 23, 11} \
> {32, 1, 2, 98, 23, 11} \
> {32, 1, 2, 98, 23, 11} \
> Nos muestra los elementos en comun del primer set {1, 2, 3, 4, 5} y el segundo set {1, 2, 3, 4, 5, 6, 7, 8}: {1, 2, 3, 4, 5} \
> Nos muestra ambos set unidos sin repeticiones, primer set {1, 2, 3, 4, 5} y el segundo set {1, 2, 3, 4, 5, 6, 7, 8}: {1, 2, 3, 4, 5, 6, 7, 8} \
> True \
> True

## Diccionarios en Python

Los diccionarios en Python son colecciones desordenadas de pares clave-valor. A diferencia de las secuencias, que se indexan mediante un rango numérico, los diccionarios se indexan con claves únicas, que pueden ser cualquier tipo inmutable, como cadenas o números.

### Característias de los diccionarios

* Desordenados: Los elementos en un diccionario no están ordenados y no se accede a ellos mediante un índice numérico, sino a través de claves únicas.
* Dinámicos: Se pueden agregar, modificar y eliminar pares clave-valor.
* Claves únicas: Cada clave en un diccionario es única, lo que previene de duplicaciones y sobreescrituras accidentales.
* Valores accesibles: Los valores no necesitan ser únicos y pueden ser de cualquier tipo de dato.

### Operaciones con diccionarios

* Agregar y modificar: Cómo agregar nuevos pares clave-valor y modificar valores existentes.
* Eliminar: Cómo eliminar pares clave-valor usando del o el metodo 'pop()'
* Métodos de diccionarios: Utilizar métodos como 'keys()', 'values()' y 'items()' para acceder a las claves, valores o ambos en forma de pares.
* Comprensión de diccionarios: Una forma elegante y concisa de construir diccionarios basados en secuencias o rangos.

### Uso de diccionarios en Python

* Almacenamiento de datos estructurados: Idelaes para almacenar y organizar datos que están relacionados de manera lógica, como una base de datos de memoria.
* Búsqueda eficiente: Los diccionarios son altamente optimizados para recuperar valores cuando se conoce la clave, proporcionando tiempos de búsqueda muy rápidos.
* Flexibilidad: Pueden ser anidad, lo que significa que los valores dentro de un diccionario pueden ser otros diccionarios, listas o cualquer otro tipo de dato.

```python
#!/usr/bin/env python3
mi_diccionario = {"nombre":"Gerardo", "edad":26, "estado":"Tabasco"} # Establecemos claves:valor para nuestro diccionario
print(mi_diccionario["nombre"]) # Vemos el valor para la clave nombre

mi_diccionario["nombre"] = "Salvador" # Actualizamos el valor para la clave nombre
print(mi_diccionario["nombre"])

mi_diccionario["Profesion"] = "Consultor cybersec" # Agregamos una nueva clave:valor al dict
print(mi_diccionario)

del mi_diccionario["estado"]
print(mi_diccionario)

for key, value in mi_diccionario.items():
    print(f"\nPara la clave\033[1;31m {key}\033[0;m tenemos el valor \033[1;31m {value}\033[0;m")

cuadrados = {x: x**2 for x in range(6)}
print(cuadrados)

print(cuadrados.keys())
print(cuadrados.values())

mi_diccionario2 = {"carrera":"sistemas", "mascotas":"perro"}
mi_diccionario.update(mi_diccionario2)
print(mi_diccionario)

my_dict = {
    "nombre": "Gerardo",
    "hobbies": {"Primero":"Música", "Segundo":"Futbol"},
    "edad": 26
}

print(my_dict["hobbies"]["Segundo"])

for key, value in my_dict.items():
    print(f"[{key}]: [{value}]")
```

> Gerardo \
> Salvador \
> {'nombre': 'Salvador', 'edad': 26, 'estado': 'Tabasco', 'Profesion': 'Consultor cybersec'} \
> {'nombre': 'Salvador', 'edad': 26, 'Profesion': 'Consultor cybersec'} \
> Para la clave nombre tenemos el valor  Salvador \
> Para la clave edad tenemos el valor  26 \
> Para la clave Profesion tenemos el valor  Consultor cybersec \
> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25} \
> dict_keys([0, 1, 2, 3, 4, 5]) \
> dict_values([0, 1, 4, 9, 16, 25]) \
> {'nombre': 'Salvador', 'edad': 26, 'Profesion': 'Consultor cybersec', 'carrera': 'sistemas', 'mascotas': 'perro'} \
> Futbol \
> [nombre]: [Gerardo] \
> [hobbies]: [{'Primero': 'Música', 'Segundo': 'Futbol'}] \
> [edad]: [26]

## Proyecto de videojuegos

Este proyecto integrador nos servirá para consolidar nuestras habilidades de programación, ya que abordaremos la administración de ventas, la gestión de stock y la actualización de datos en un sistema de control central.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

tope = 700

juegos = ["Super Mario Bros", "Zelda", "CyberPunk", "Final Fantasy"]

# Géneros
generos = {
    "Super Mario Bros": "Aventura",
    "Zelda": "Aventura",
    "CyberPunk": "Rol",
    "Final Fantasy": "Rol"
}
# Ventas y Stock
ventas_y_stock = {
    "Super Mario Bros":(400, 200),
    "Zelda":(600, 20),
    "CyberPunk":(60, 120),
    "Final Fantasy":(924, 3),

}

# Clientes
clientes = {
    "Super Mario Bros": {"Marcelo", "Hackermate", "Hackavis", "Securiters", "Lobotec"},
    "Zelda": {"Marcelo", "Hackermate", "Hackavis"},
    "CyberPunk": {"Ivon", "Gerardo", "Mauricio"},
    "Final Fantasy": {"Indira", "Rogelio", "Gonzalo"}
}

mi_juego = "Zelda"

# Sumario
def sumario(juego):
    print(f"[i] Resumen del juego {juego}\n")
    print(f"\t[+] Género del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Total de stock para este juego: {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Clientes que han adquirido el juego: {', '.join(clientes[juego])}\n")

for juego in juegos:
    if ventas_y_stock[juego][0] > tope:
        sumario(juego)

ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope)
print(f"El total de ventas es {ventas_totales()}")
```

## PROGRAMACIÓN ORIENTA A OBJETOS EN PYTHON (POO) - 8

## Clases y objetos (1/2)

La programación orienta a objetos, es un paradigma de programación que utiliza objetos y clases en su enfoque central. Es una manera de estructurar y organizar el código que refleja cómo los desarrolladores piensan sobre el mundo real y las entidades dentro de él.

### Clases

Las clases son los fundamentos de la POO. **Actúan como plantillas para la creación de objetos y definen atributos y comportamientos que los objetos creados a partir ella tendrán**. En Python, una clase se define con la palabra clave 'class' y proporcionan la estructura inicial para todo objeto que se derive de ella

### Instancias de clases

**Un objeto es una instancia de una clase**. Cada vez que se crea un objeto, se está creando una isntancia que tiene su propio espacio de memoria y conjunto de valores para los atributos definidos por su clase. Los objetos encapsulan datos y funciones juntos en una entidad discreta.

### Métodos de clase (1/2)

Los métodos de clase **son funciones que se definen dentro de una clase y solo pueden ser llamados por las instancias de esa clase**. Estos métodos son el mecanismo principal para interactuar con los objetos, permitiéndoles realizar operaciones o acciones, modificar su estado o incluso interactuar con otros objetos.

---
Codigo: **Ejemplo 1**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Persona:

    def __init__(self, nombre, edad, profesion): # Definimos el constructor con los parámetros que vamos a recibir
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludo(self): # Persona.saludo(marcelo)
        return f"Hola soy {self.nombre} y tengo {self.edad} años"


gerardo = Persona("Salvador", 26, "Consultor") # Estamos creando una instancia de la clase Persona, nombrando al objeto gerardo
print(gerardo.saludo())

juan = Persona("Gerardo", 21, "Pentester")
print(juan.saludo())
```

> Hola soy Salvador y tengo 26 años \
> Hola soy Gerardo y tengo 21 años
---
Codigo: **Ejemplo 2**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Animal:
    
    def __init__(self, nombre, animal): # Animal.__init__(gato, nombre, animal)
        self.nombre = nombre
        self.animal = animal

    def descripcion(self): # Animal.descripcion(obj)
        return f"{self.nombre} es un {self.animal}"
    
gato = Animal("QWERTY", "Gato")
print(gato.descripcion())

perro = Animal("Canela", "Perro")
print(perro.descripcion())
```

> QWERTY es un Gato \
> Canela es un Perro

---
Codigo: **Ejemplo 3**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class CuentaBancaria:

    # En el constructor inicializamos el atributo dinero = 0, si no ponemos un valor el dinero estará en 0 pero si ponemos un valor si inicializará ese valor pasado por el objeto
    def __init__(self, cuenta, nombre, dinero = 0):
        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero

    def depositar_dinero(self, deposito): # CuentaBancaria.depositar_dinero(Gerardo)
        self.dinero += deposito # self.dinero = dinero del objeto, deposito = dinero agregado al dinero del objeto
        return f"[+] Se han depositado ${deposito} pesos mexicanos, el balance de la cuenta es de ${self.dinero} pesos mexicanos"
    
    def retirar_dinero(self, retiro): #CuentaBancaria.retirar_dinero(Gerardo, retiro)
        
        if retiro > self.dinero:
            return f"\n\033[1;31m[!] Operación denegada: Fondos insuficientes\033[0;m\n\t[!] Retiro solicitado: ${retiro}\n\t[!] Saldo actual: ${self.dinero}"
        
        if retiro <= self.dinero:
            self.dinero -= retiro
            return f"\n\033[1;36m[+] Operación exitosa: Retiro aprobado\033[0;m\n\t[+] Retiro solicitado: ${retiro}\n\t[+] Saldo actual: ${self.dinero}"


Gerardo = CuentaBancaria("4452 8133", "Jose Gerardo Salvador", 1000) # Instancia de objeto

# Se usa la funcion depositar dinero para agregar dinero al objeto
print(Gerardo.depositar_dinero(500))
print(Gerardo.depositar_dinero(700))
print(Gerardo.depositar_dinero(300))

# Se usa la funcion retirar dinero para quitar dinero al objeto
print(Gerardo.retirar_dinero(5000))
print(Gerardo.retirar_dinero(500))
```

> [+] Se han depositado $500 pesos mexicanos, el balance de la cuenta es de $1500 pesos mexicanos \
> [+] Se han depositado $700 pesos mexicanos, el balance de la cuenta es de $2200 pesos mexicanos \
> [+] Se han depositado $300 pesos mexicanos, el balance de la cuenta es de $2500 pesos mexicanos \
> \
> [!] Operación denegada: Fondos insuficientes \
> &nbsp;&nbsp;[!] Retiro solicitado: $5000 \
> &nbsp;&nbsp;[!] Saldo actual: $2500 \
> \
> [+] Operación exitosa: Retiro aprobado \
> &nbsp;&nbsp;[+] Retiro solicitado: $500 \
> &nbsp;&nbsp;[+] Saldo actual: $2000

---

## Clases y objetos (2/2)

Dentro del paradigma de la Programación Orientada a Objetos en Python, existen conceptos avanzados como los decoradores, métodos de clase y  métodos estáticos que enriquecen y expanden las posibilidades de cómo interactuamos con las clases y sus instancias.

### Decoradores

Los decoradores son una herramienta poderosa en Python que permite modificar el comportamiento de una función o método. Funcionan como 'envoltorios', que agregan funcionalidad antes y después del método o función decorada, sin cambiar su código fuente. En POO, los decoradores son frecuentemente utilizados para agregar funcionalidades de manera dinámica a los métodos, como la sincronización de hilos, la memorización de resultados o la verificación de permisos.

### Métodos de clase (2/2)

Un método de clase es un método que está ligado a la clase y no a una instancia de la clase. Esto significa que el método puede ser llamado sobre la clase misma, en lugar de sobre un objeto de la clase. Se definen utilizando el decorador '@classmethod' y su primer argumento es siempre una referencia a la clase, convencionalmente llamada 'cls'. Los métodos de clase son utilizados a menudo para definir métodos "factory" que pueden crear instancias de la clase de diferentes maneras.

### Métodos estáticos 1/2

Los métodos estáticos, definidos con el decorador '@staticmethod', no reciben una referencia implícita ni a la instancia (self) ni a la clase (cls). Son básicamente como funciones regulares, pero pertenecen al espacio de nombre de la clase. Son útiles cuando queremos realizar alguna funcionalidad que está relacionada con la clase, pero que no requiere acceder a la instancia o a los atributos de la clase.

Estos elementos de la POO en Python nos permiten crear abstracciones más claras y mantener el código organizado, modular y flexible, facilitando el mantenimiento y la extensibilidad del software.

---

Codigo: **Ejemplo 1**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    # Sin emplear decorador
    def area(self): # Rectangulo.area(rect1)
        return self.alto * self.ancho
    
    @property # Al definir esta decorador, la funcion podemos llamarla como si fuera un atributo omitiendo el uso de parentisis al llamarla
    def areados(self):
        return self.alto * self.ancho
    

    def __str__(self): # Método especial, este método especial sustituye la salida por default que nos devolveria al imprimir el objeto sin parentesis, reportandonos que es un objeto
        return f"\n[+] Propiedades del rectangulo\n\tAncho:{self.ancho}\n\tAlto:{self.alto}\n[!] Sustituyendo la salida por defecto:\n\t<__main__.Rectangulo object at 0x0000024A9E726A50>"
    
    def __eq__(self, otro):# Método especial que debe ser declarado para poder usarlo
        
        return self.ancho == otro.ancho and self.alto == otro.alto

rect1 = Rectangulo(20, 80)
print(f"\n[+] El área es {rect1.area()}") # Uso de parentesis al llamar al método

rect2 = Rectangulo(20,800)
print(f"\n[+] El área es {rect2.areados}") # Omito el uso de parentesis al llamar al método @property

print(rect1) # Omitimos el uso de rect1() porque la salida convencional ha sido modificado con el metodo especial str

print(f"\n[+] ¿Son iguales? -> {rect1 == rect2}") # Definido con metodo especial eq
```

> [+] El área es 1600 \
> \
> [+] Propiedades del rectangulo \
> &nbsp;Ancho:20 \
> &nbsp;Alto:80 \
> [!] Sustituyendo la salida por defecto:\
> &nbsp;<\_\_main__.Rectangulo object at 0x0000024A9E726A50>\
> \
> [+] ¿Son iguales? -> False

---

Codigo: **Ejemplo 2**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 
class Libro:

    IVA = 0.20

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
    
    @staticmethod # Decorador, no necesitan acceder a las propiedades del objeto
    def es_best_seller(total_ventas): # Libro.es_best_seller(total_ventas) #omitimos el uso del objeto para este tipo de metodos porque hacemos referencia a la clase y ya no a un método
        return total_ventas > 5000
    
    @classmethod
    def precio_con_iva(cls, precio):
        return precio + precio * cls.IVA
    
class LibroDigital(Libro): # Creamos otra clase que hereda los atributos y métodos de la clase libro
    IVA = 0.10 # El iva es la unica constante que va a cambiar con respecto a la clase libro

        
mi_libro = Libro("¿Cómo ser un lammer?", "Gerardo", 20) # Instancia de clase Libro
mi_libro_digital = LibroDigital("Iniciacion a lammer", "Gerardo Salvador", 20) # Instancia de clase Libro Digital

#print(mi_libro.es_best_seller(7000)) # este nos manda error porque ya no necesitamos pasar un objeto sino la clase
print(Libro.es_best_seller(7000))

print(f"\n[+] El precio del libro con IVA es de {Libro.precio_con_iva(mi_libro.precio)}")
print(f"\n[+] El precio del libro con IVA es de {LibroDigital.precio_con_iva(mi_libro_digital.precio)}")
```

> True \
> \
> [+] El precio del libro con IVA es de 24.0 \
> \
> [+] El precio del libro con IVA es de 22.

## Métodos estáticos y métodos de clase

Los métodos estáticos y los métodos de clase son dos herramientas poderosas en la programación orientada a objetos en Python, que ofrecen flexibilidad en cómo se puede acceder y utilizar la funcionalidad asociada con una clase.

### Métodos de clase

Se definen con el decorador '@classmethod', lo que les permite tomar la clase como primer argumento, generalmente nombrada 'cls'. Este acceso a la clase permite que los métodos de clase interactúen con la estructura de la clase en sí, como modificar atributos de clase que afectarán a todas las instancias. Se utilizan para tareas que requieren conocimiento del estado global de la clase, como la construcción de instancias de maneras específicas, también conocidos como métodos factory.

### Métodos estáticos 2/2

Se definen con el decorador '@staticmethod' y no reciben un argumento implícito de referencia a la clase o instancia. Son similares a las funciones regulares definidas dentro del cuerpo de una clase.
Se utilizan para funciones que, aunque conceptualmente pertenecen a la clase debido a la relevancia temática, no necesitan acceder a ningún dato específico de la clase o instancia.
Proporcionan una manera de encapsular la funcionalidad dentro de una clase, manteniendo la cohesión y la organización del código.

Ambos métodos contribuyen a un diseño de software más limpio y modular, permitiendo una clara separación entre la funcionalidad que opera con respecto a la clase en su totalidad y la funcionalidad que es independiente de las instancias de clase y de la clase misma.
La elección entre utilizar un método de clase o un método estático a menudo depende del requisito específico de acceso o no a la clase o a sus instancias.

---

Codigo: **Ejemplo 1**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

# MÉTODOS ESTÁTICOS
class Calculadora:

    @staticmethod
    def suma(num1, num2): # no se usa self porque no jugamos con objetos
        return num1 + num2
    
    @staticmethod
    def resta(num1, num2): # no se usa self porque no jugamos con objetos
        return num1 - num2
    
    @staticmethod
    def division(num1, num2):
        return num1 / num2 if num2 != 0 else "\n[!] Error no se puede dividir un numero entre 0"

print(Calculadora.suma(2,5))
print(Calculadora.resta(8,4))
print(Calculadora.division(8,0))

# MÉTODOS DE CLASE
class Automovil:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @classmethod
    def deportivos(cls, marca):
        return cls(marca, "Deportivo")
    
    @classmethod
    def sean(cls, marca):
        return cls(marca, "Sean")

    def __str__(self):
        return f"La marca {self.marca} es un modelo {self.modelo}"

deportivo = print(Automovil.deportivos("Ferrari"))
sean = print(Automovil.sean("Toyota"))
```

> 7 \
> 4 \
> [!] Error no se puede dividir un numero entre 0 \
> La marca Ferrari es un modelo Deportivo \
> La marca Toyota es un modelo Sean

---

Codigo: **Ejemplo 2**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Estudiantes:

    estudiantes = []

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        Estudiantes.estudiantes.append(self)

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18

    @classmethod
    def crear_estudiantes(cls, nombre, edad):
        if cls.es_mayor_de_edad(edad):
            return cls(nombre, edad)
        else:
            print(f"[!] Error: El estudiante {nombre} es menor de edad")

    @staticmethod
    def mostrar_estudiantes():
        for i, x in enumerate(Estudiantes.estudiantes):
            print(f"[+] Estudiante número [{i + 1}]: {x.nombre}")

Estudiantes.crear_estudiantes("HackerMate", 43)
Estudiantes.crear_estudiantes("Savitar", 28)
Estudiantes.crear_estudiantes("Xerosec", 12)
Estudiantes.crear_estudiantes("Hackavis", 8)

Estudiantes.mostrar_estudiantes()

```

> [!] Error: El estudiante Xerosec es menor de edad \
> [!] Error: El estudiante Hackavis es menor de edad \
> [+] Estudiante número [1]: HackerMate \
> [+] Estudiante número [2]: Savitar

---

Codigo: **Ejemplo 3 Externo**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Perro:
    especie = "Canino"  # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie  # Modifica el atributo de clase

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Modificación del atributo de clase
Perro.cambiar_especie("Lobo")

# Instancias
perro1 = Perro("Rex")
perro2 = Perro("Firulais")

print(perro1.especie)  # Imprime "Lobo"
print(perro2.especie)  # Imprime "Lobo"
perro1.ladrar()        # Imprime "Rex dice: ¡Guau!"
```

> Lobo \
> Lobo \
> Rex dice: ¡Guau!

Se lee de manera más detallada en esta página web [Métodos de clase](https://oregoom.com/python/metodos-clase/)

## Comprendiendo mejor el uso de self

El uso de self es uno de los aspectos más fundamentales y a la vez confusos para quienes se adentran en la Programación Orientada a Objetos (POO) en Python. Este identificador es crucial para entender cómo Python maneja los métodos y atributos dentro de sus clases y objetos.

### Definición de 'self'

A nivel conceptual, 'self' es una referencia al objeto actual dentro de la clase. Es el primer parámetro que se pasa a cualquier método de una clase en Python. A través de self, un método puede acceder y manipular los atributos del objeto y llamar a otros métodos dentro del mismo objeto.

### Uso de 'self'

Cuando se crea una nueva instancia de una clase, Python pasa automáticamente la instancia recién creada como el primer argumento al método '\_\_init__' y a otros métodos definidos en las clases que tienen self como su primer parámetro. Esto es lo que permite que un método opere con datos específicos del objeto y no con datos de la clase en general o de otras instancias de la clase.

### Importancia de 'self'

El concepto de self es importante en la POO ya que asegura que los métodos y atributos se apliquen al objeto correcto. Sin self, no podríamos diferenciar entre las operaciones y datos de diferentes instancias de una clase.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Persona:

    def __init__(self, nombre, edad): # Persona.__init__(gerardo, nombre, edad)
        self.nombre = nombre # gerardo.nombre = nombre
        self.edad = edad # gerardo.edad = edad

    def presentacion(self): # Persona.presentacion(gerardo)
        return f"Hola soy {self.nombre} y tengo {self.edad} años" # gerardo.nombre gerardo.edad

gerardo = Persona("Gerardo", 26)
print(gerardo.presentacion())



class Calculador:

    def __init__(self, numero): # Calculador.__init__(calc, numero)
        self.numero = numero # calc.numero = 5

    def suma(self, otro_numero): # Calculador.suma(calc, otro_numero)
        return self.numero + otro_numero # calc.numero + 8 -> 5 + 8
    
    def doble_suma(self, num1, num2): # Calculador.doble_suma(calc, 2, 9)
        return self.suma(num1) + self.suma(num2) # calc.suma(2) + calc.suma(9) -> Calculador.suma(calc,2) + Calculador.suma(calc, 9)

calc = Calculador(5)
print(calc.suma(8))

print(calc.doble_suma(2,9))

```

> Hola soy Gerardo y tengo 26 años \
> 13 \
> 21

## Herencia y polimorfismo
