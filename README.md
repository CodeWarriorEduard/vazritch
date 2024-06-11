
# VAZRITCH

VAZRTICH es un lenguaje de programación creado con motivos académicos, a continuación se muestra una pequeña guía de usuario para poder usarlo.


### Arquitectura usada
Se usó una arquitectura limpia para separar por capas las distintas funcionalidades de la aplicación.

![Clean Coder Blog](https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

Esta arquitectura nos permite modularizar nuestro código y manejar un flujo de datos mucho más organizado.


### Tipos de datos

En VAZRITCH utilizamos datos dinamicos, los cuales serán inferidos.

#### Ejemplo:

```
- 5  Entero.
- 6.2 Float
- "Hola" String.
```

### Declaración de variables

En VAZRITCH la declaracion de variables es fácil, ya que se utilizan datos dinámicos, solo se le debe indicar al lenguaje que variable se usará.


#### Ejemplo:

```

var = value ###Estructura de declaración

radio = 5

pi = 3.141592

saludo = "Hola mundo!"


```

### Comentarios

Los comentarios nos permiten incluir en nuestro código explicaciones o notas acerca de cada línea de código presente en nuestro programa.
En QLEON los comentarios se realizan usando 3 almohadillas.

#### Ejemplo

```
### Este es un Ejemplo de comentario.

```


### Imprimir en pantalla


Para imprimir en pantalla en Qleon se utiliza la sentencia show.

#### Ejemplo

```

show("Hola mundo")

```


### Operaciones matemáticas básicas.

En Qleon se admiten operaciones matemáticas básicas como suma, resta, multiplicación y división.


#### Ejemplo

```

suma = 5 +4

resta = 5-2

división = 8/4

multiplicacion = 12*4

operacionesCompuestas = (12*4)/2


```


### Condicionales

Para controlar el flujo en ciertas instrucciones se incluyen los condicionales en VAZRITCH de la siguiente forma:


#### Ejemplo

```
condition(1 > 2){
    ### Código
}
```
Si se quiere contradecir la condición inicial se utiliza la palabra reservada "otherwise_if"

#### Ejemplo

```
condition(1 > 2){
    ### Código
}otherwise_if(2 > 1){
	### Código
}



### Operadores de comparación

Los operadores de comparación nos permitirán contrastar entre cantidades. 


```
> ### Mayor qué.

< ### Menor qué.

>= ### Mayor o igual qué.

<= ### Menor o igual qué.


```
```
```

### Esto es todo hasta ahora...

Qleon es un proyecto en desarrollo, con el tiempo se irán añadidendo características importantes.
