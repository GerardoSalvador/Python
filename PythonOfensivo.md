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
> 35.831.808 \
> 