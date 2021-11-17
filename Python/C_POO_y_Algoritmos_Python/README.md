

 :link: :octocat: <a href="!#" target="_blank">Documentación</a>

# Curso de POO y Algoritmos con Python
## Programación Orientada a Objetos

2. Programación Orientada a Objetos
Uno de los elementos más importantes de los lenguajes de programación es la utilización de clases para organizar programas en módulos y abstracciones de datos.

Las clases se pueden utilizar de diversas maneras. Pero en este artículo hablaremos de cómo utilizarlas en el contexto de la programación orientada a objetos. La clave para entender la programación orientada a objetos es pensar en objetos como agrupaciones de datos y los métodos que operan en dichos datos.

Por ejemplo, podemos representar a una persona con propiedades como nombre, edad, género, etc. y los comportamientos de dicha persona como caminar, cantar, comer, etc. De la misma manera podemos representar unos audífonos con propiedades como su marca, tamaño, color, etc. y sus comportamientos como reproducir música, pausar y avanzar a la siguiente canción.

Puesto de otra manera, la programación orientada a objetos nos permite modelar cosas reales y concretas del mundo y sus relaciones con otros objetos.

Las ideas detrás de la programación orientada a objetos tienen más de 50 años y han sido ampliamente aceptadas y practicadas en los últimos treinta. A mediados de la década de los setenta se comenzaron a escribir artículos académicos explicando los beneficios de esta aproximación a la programación. También durante esos años se comenzaron a escribir los primeros lenguajes de programación que incorporaban estas ideas (como Smalltalk y CLU). Pero no fue hasta la llegada de Java y C++ que la idea consiguió un número importante de seguidores.

Hasta ahora, en el curso previo de esta serie hemos utilizado programación orientada a objetos de manera implícita. Cuando decimos “Los objetos son las principales cosas que un programa de Python manipula. Cada objeto tiene un tipo que define qué cosas puede realizar un programa con dicho objeto,” nos estamos refiriendo a las ideas principales de la programación orientada a objetos. Hemos utilizado los tipos lista y
diccionario, entre muchos otros, así como los métodos asociados a dichos tipos.

Así como los creadores de un lenguaje de programación solo pueden diseñar una fracción muy pequeña de todas las funciones útiles (como abs, float, type, etc.), también pueden escribir una fracción muy pequeña de los tipos útiles (int, str, dict, list, etc.). Ya sabemos los mecanismos que nos permiten crear funciones, ahora veremos los mecanismos que nos permiten crear nuevos tipos (o clases).

#### Clases en Python
---
Las estructuras primitivas con las que hemos trabajado hasta ahora nos permiten definir cosas sencillas, como el costo de algo, el nombre de un usuario, las veces que debe correr un bucle, etc. Sin embargo, existen ocasiones cuando necesitamos definir estructuras más complejas, por ejemplo un hotel. Podríamos utilizar dos listas: una para definir los cuartos y una segunda para definir si el cuarto se encuentra ocupado o no.

```py
cuartos_de_hotel = [101, 102, 103, 201, 202, 203]
cuarto_ocupado = [True, False, False, True, True, False]
```

Sin embargo, este tipo de organización rápidamente se sale de control. ¿Qué tal que quisiéramos añadir más propiedades, cómo si el cuarto ya fue aseado o no? ¿Si el cuarto tiene cama doble o sencilla? Esto nos lleva a una falta fuerte de organización y es justamente el punto que justifica la existencia de clases.

Las clases nos permiten crear nuevos tipos que contiene información arbitraria sobre un objeto. En el caso del hotel, podríamos crear dos clases Hotel() y Cuarto() que nos permitiera dar seguimiento a las propiedades como número de cuartos, ocupación, aseo, tipo de habitación, etc.

Es importante resaltar que las clases solo proveen estructura. Son un molde con el cual podemos construir objetos específicos. La clase señala las propiedades que los hoteles que modelemos tendrán, pero no es ningún hotel específico. Para eso necesitamos las instancias.

#### Instancias
---
Mientras que las clases proveen la estructura, las instancias son los objetos reales que creamos en nuestro programa: un hotel llamado PlatziHotel o Hilton. Otra forma de pensarlo es que las clases son como un formulario y una vez que se llena cada copia del formulario tenemos las instancias que pertenecen a dicha clase. Cada copia puede tener datos distintos, al igual que cada instancia es distinta de las demás (aunque todas pertenecen a una misma clase).

Para definir una clase, simplemente utilizamos el keyword class. Por ejemplo:
```py
class Hotel:
    pass
```
Una vez que tenemos una clase llamada Hotel podemos generar una instancia llamando al constructor de la clase.

```py
hotel = Hotel()
```
#### Atributos de la instancia
Todas las clases crean objetos y todos los objetos tienen atributos. Utilizamos el método especial __init__ para definir el estado inicial de nuestra instancia. Recibe como primer parámetro obligatorio self (que es simplemente una referencia a la instancia).

```py
class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0


hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
print(hotel.lugares_de_estacionamiento) # 20
```
#### Métodos de instancia
Mientras que los atributos de la instancia describen lo que representa el objeto, los métodos de instancia nos indican qué podemos hacer con las instancias de dicha clase y normalmente operan en los mencionados atributos. Los métodos son equivalentes a funciones dentro de la definición de la clase, pero todos reciben self como primer argumento.

```py
class Hotel:

    ...

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes


hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() # 2
```

![Python POO](../img/python_poo_01.png)


3. Tipos de datos abstractos y clases, Instancias

Pag. 5 - 11

```py
# definicion de la clase
class <nombre_de_la_clase>(super_de_la_clase):
    def __init__(self, <params>):
        <expresion>
    
    def <nombre_del_metodo>(self, <params>):
        <expresion>
```
Ejemplo
```py
# definicion
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self, otra_persona):
        return f"Hola, {otra_persona.nombre}, me llamo {self.nombre}"
    
#Uso
david = Persona('David', 30)
erika = Persona('Erika', 32)

david.saluda(erika)
# 'Hola, Erika, me llamo David'
```
ejemplo
```py
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordendada):
        x_diff = (self.x - otra_coordendada.x)**2
        y_diff = (self.y - otra_coordendada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    # 22.02271554554524
    print(isinstance(coord_2, Coordenada))
    # True
```


4. Decomposición

Pag. 12 - 13

```py
class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def informacion(self, temperatura_motor):#Esta funcion es temporal, solo para revisar que todo esta funcionanndo :v xd 
        print("\n")
        print(f"nivelGasolina = {self.nivelGasolina} y temperatura = {self.estadoTemperatura}")
        print("\n")
    
    def inyecta_gasolina(self, cantidad):
        pass

if __name__ = "__main__":
    car1 = Automovil("ABC", "Nissan", "Plata")

```


5. Abstracción

Pag. 14 - 15

```py
class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura="caliente"):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f"Llenando el tanque con agua {temperatura}")

    def _anadir_jabon(self):
        print("Anadiendo jabon")

    def _lavar(self):
        print("Lavando la ropa")

    def _centrifugar(self):
        print("Centrifugando la ropa")


if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()
```

6. Funciones: base de los decoradores

El concepto de decorador en Python es algo que podríamos ubicar en un nivel “intermedio” en el manejo del lenguaje, por lo que es buena idea que tengas una base sólida, sobre todo en cuanto a funciones al momento de profundizar e implementarlas.

Los decoradores son una forma sencilla de llamar funciones de orden mayor, es decir, funciones que toman otra función como parámetro y/o retornan otra función como resultado. De esta forma un decorador añade capacidades a una función sin modificarla.

Un ejemplo de esto son las llantas de un automóvil. Si les colocas cadenas para la nieve, el automóvil aún puede andar y además extiende su funcionalidad para conducirse en otros terrenos.

Recordando sobre funciones   
Antes de abordar el tema de decoradores haremos un pequeño repaso por las funciones, las cuales retornan un valor ante la entrada de un argumento.

Analicemos este sencillo ejemplo donde una función que multiplica un número se eleva a la tercera potencia:
```py
def elevar_cubo(numero):
	return numero * numero * numero
```
Si damos como argumento el número 3, entonces tendremos como salida el número 27 al ejecutar la función:

```py
>>> elevar_cubo(3)
27
```
Funciones como objetos de primera-clase   
Otro concepto importante a tener en cuenta es que en Python las funciones son objetos de primera-clase, es decir, que pueden ser pasados y utilizados como argumentos al igual que cualquier otro objeto (strings, enteros, flotantes, listas, etc.).

Veamos un ejemplo donde definimos 3 diferentes funciones que utilizaremos de manera conjunta:

```py
def presentarse(nombre):
	return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
	return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
	return funcion_entrante("David")
```
Las primeras dos funciones son obvias en su resultado, donde nos mostrarán un mensaje con el valor de la variable nombre. La tercera función puede ser más compleja de predecir, ya que toma otra función como entrada. Veamos que pasa cuando colocamos una función como atributo:
```py
>>> consume_funciones(presentarse)
'Me llamo David'

>>> consume_funciones(estudiemos_juntos)
'¡Hey David, aprendamos Python!'
```

Pongamos atención en cómo la función consume_funciones() se escribe con paréntesis para ser ejecutada, mientras que la función presentarse y estudiemos_juntos solo hace referencia a estas.

Funciones anidadas   
Al igual que los condicionales y bucles también puedes colocar funciones dentro de otra función.

Tómate un minuto para analizar el siguiente código e inferir cuál será el resultado de salida:

```py
def funcion_mayor():
	print("Esta es una función mayor y su mensaje de salida.")

	def librerias():
		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

	def frameworks():
		print("Algunos frameworks de Python son: Django, Dash y Flask.")

	frameworks()
	librerias()
```
Si llamamos a la función funcion_mayor tendremos la siguiente salida:
```py
>>> funcion_mayor()
Esta es una función mayor y su mensaje de salida.
Algunos frameworks de Python son: Django, Dash y Flask.
Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.
```
Debemos considerar que las funciones anidadas dentro de funcion_mayor no se ejecutan hasta que se llama a esta primera, siendo muestra del scope o alcance de las funciones. Si las llamamos obtendremos un error

7. Setters, getters y decorador property

Entendiendo el concepto de decorador   
Antes de comenzar me gustaría que analices el siguiente código:
```py
def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

def zumbido():
	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido)
```
out
```py
>>> zumbido()
Este es el último mensaje...
Buzzzzzz
Este es el primer mensaje ;)
```
Todo lo que sucede se conoce en programación como metaprogramación (metaprogramming), ya que una parte del programa trata de modificar a otra durante el tiempo de compilación. En tanto un decorador básicamente toma una función, le añade alguna funcionalidad y la retorna.

Mejorando la sintaxis   
Definitivamente la forma en que decoramos la función es complejo, pero afortunadamente Python lo tiene en cuenta y podemos utilizar decoradores con el símbolo @. Volviendo al mismo ejemplo de funcion_decoradora(), podemos simplificarlo así:
```py
@funcion_decoradora
def zumbido():
	print("Buzzzzzz")
```
En solo tres líneas de código tenemos el mismo resultado que escribir zumbido = funcion_decoradora(zumbido).

¿Qué son getters y setters?

A diferencia de otros lenguajes de programación, en Python los getters y setters tienen el objetivo de asegurar el encapsulamiento de datos. Cómo habrás visto, si declaramos una variable privada en Python al colocar un guión bajo al inicio de esta (_) y normalmente son utilizados para: añadir lógica de validación al momento de obtener y definir un valor y, para evitar el acceso directo al campo de una clase.

La realidad es que en Python no existen variables netamente privadas, pues aunque se declaren con un guión bajo podemos seguir accediendo a estas. En Programación Orientada a Objetos esto es peligroso, pues podemos alterar el método de alguna clase y tener efectos colaterales que afecten la lógica de nuestra aplicación.

Clases sin getters y setters

Veamos un ejemplo con una clase que almacena un dato de distancia recorrida en millas (mi) y lo convierte a kilómetros (km):
```py
class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)
```
Ahora creemos un objeto que haga referencia a un viaje:
```py
# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos el atributo distancia
>>> print(avion.distancia)
200

# Obtenemos el método convertir_a_kilometros
>>> print(avion.convertir_a_kilometros())
321.8688
```
Utilizando getters y setters

Incluyamos un par de métodos para obtener la distancia y otro para que no acepte valores inferiores a cero, pues no tendría sentido que un vehículo recorra una distancia negativa. Estos son métodos getters y setters:
```py
class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)

	# Método getter
	def obtener_distancia(self):
		return self._distancia

	# Método setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor
```
El método getter obtendrá el valor de la distancia que y el método setter se encargará de añadir una restricción. También debemos notar cómo distancia fue reemplazado por `_distancia`, denotando que es una variable privada.

Si probamos nuestro código funcionará, la desventaja es que cualquier aplicación que hayamos creado con una base similar deberá ser actualizado. Esto no es nada escalable si tenemos cientos o miles de líneas de código.

Función _property()_

Esta función está incluida en Python, en particular crea y retorna la propiedad de un objeto. La propiedad de un objeto posee los métodos `getter()`, `setter()` y `del()`.

En tanto la función tiene cuatro atributos: `property(fget, fset, fdel, fdoc)` :

+ `fget` : trae el valor de un atributo.
+ `fset` : define el valor de un atributo.
+ `fdel` : elimina el valor de un atributo.
+ `fdoc` : crea un docstring por atributo.

Veamos un ejemplo del mismo caso implementando la función `property()` :
```py
class Millas:
    def __init__(self):
        self._distancia = 0

    # Función para obtener el valor de _distancia
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia

    # Función para definir el valor de _distancia
    def definir_distancia(self, recorrido):
        print("Llamada al método setter")
        self._distancia = recorrido

    # Función para eliminar el atributo _distancia
    def eliminar_distancia(self):
        del self._distancia

    distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)


if __name__ == "__main__":

    # Creamos un nuevo objeto
    avion = Millas()

    # Indicamos la distancia
    avion.distancia = 200

    # Obtenemos su atributo distancia
    print(avion.distancia)
    # Llamada al método getter
    # Llamada al método setter
    # 200
```
Aunque en este ejemplo hay una sola llamada a `print`, tenemos tres líneas como salida pues esta llama a los primeros dos métodos. Por lo que la propiedad distancia es una propiedad de objeto que ayuda a mantener el acceso de forma privada.

Decorador @property

Este decorador es uno de varios con los que ya cuenta Python, el cual nos permite utilizar getters y setters para hacer más fácil la implementación de la programación orientada a objetos en Python cambiando los métodos o atributos de las clases de forma que no modifiquemos el código.

Pero mejor veamos un ejemplo en acción:

```py
class Millas:
    def __init__(self):
        self._distancia = 0

    # Función para obtener el valor de _distancia
    # Usando el decorador property
    @property
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia

    # Función para definir el valor de _distancia
    @obtener_distancia.setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        print("Llamada al método setter")
        self._distancia = valor

# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
>>> print(avion.definir_distancia)
Llamada al método getter
Llamada al método setter
200
```


8. Encapsulación, getters and setters

[Role of Underscore(_) in Python](https://www.datacamp.com/community/tutorials/role-underscore-python)

La encapsulación nos permite agrupar datos y controlar su comportamiento en nuestra clase. También nos permite controlar el acceso a nuestros datos y prevenir modificaciones no autorizadas.
```py
class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        print(region)
        if region in self._pais:
            self._region = region
            raise ValueError(f"La region {region} no es valida o ya se encuentra en {self._pais}")


# casilla = CasillaDeVotacion(123, ["CDMX", "Morelos"])
#  print(casilla.region)
# None
#
#
# casilla.region = "CDMX"
# ValueError: La region CDMX no es valida o ya se encuentra en ['CDMX', 'Morelos']
#
# casilla.region = "CDMX."
# print(casilla.region)
# "CDMX."
```


9. Herencia

Pag 19 - 

La herencia nos permite generar una jerarquía de clases en las que podemos compartir funcionamientos comunes y en el que existirá una clase _padre_ también conocida como **superclase** y una o varias _clases hijas_ conocidas como **subclases**.

Para extender de una clase _padre_ en Python solo tendremos que pasar como parámetro el nombre de la clase _padre_ **a la hija en su definición** y ya podremos usar las funcionalidades de la clase padre.

```py
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == "__main__":
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())
```



10. Polimorfismo

```py
```

```py
```
## Complejidad algorítmica

11. Introducción a la complejidad algorítmica

12. Conteo abstracto de operación

13. Notación asintótica

14. Clases de complejidad algorítmica

Algoritmos de búsqueda y ordenación

15. Búsqueda lineal

16. Búsqueda binaria

17. Ordenamiento de burbuja

18. Ordenamiento por inserción

19. Ordenamiento por mezcla

## Ambientes virtuales

20. Ambientes virtuales

### Graficado

21. ¿Por qué graficar?

22. Graficado simple

## Algoritmos de optimización

23. Introducción a la optimización

24. El problema del morral

