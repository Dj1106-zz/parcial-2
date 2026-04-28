# Parcial 2 - Lenguajes de Programación

## Punto 1: Diseño de gramática (CRUD)

Se diseñó una gramática sencilla para un lenguaje que permite realizar operaciones CRUD (Create, Read, Update, Delete) sobre una base de datos NoSQL.

```
Programa -> Instruccion
          | Instruccion ; Programa

Instruccion -> Create
             | Read
             | Update
             | Delete

Create -> CREATE ID { ListaCampos }

Read -> READ ID
      | READ ID WHERE Condicion

Update -> UPDATE ID SET ListaCampos
        | UPDATE ID SET ListaCampos WHERE Condicion

Delete -> DELETE ID
        | DELETE ID WHERE Condicion

ListaCampos -> Campo
             | Campo , ListaCampos

Campo -> ID : Valor

Condicion -> ID = Valor

Valor -> STRING
       | NUMBER
```

Esta gramática permite trabajar con datos tipo clave-valor y usar condiciones mediante la cláusula WHERE.



## Punto 2: Implementación con Bison y Flex

Se implementó la gramática utilizando herramientas de análisis léxico y sintáctico:

* Flex: para reconocer tokens (palabras clave, identificadores, números, etc.)
* Bison: para validar la estructura del lenguaje

### Pasos de ejecución:


bison -d parser.y
flex lexer.l
gcc lex.yy.c parser.tab.c -lfl -o parser
./parser


El programa permite ingresar instrucciones como:

```
CREATE usuarios {nombre:"Juan",edad:20};
READ usuarios WHERE edad=20;
```

Y valida si son correctas según la gramática.

<img width="466" height="410" alt="image" src="https://github.com/user-attachments/assets/6f28a1c3-79f3-4ecf-84c0-8bf7157b3099" />


## Punto 3: Ambigüedad en if-then-else

En este punto se analiza un problema clásico de las gramáticas en lenguajes de programación, conocido como el “dangling else”, que ocurre cuando no es claro a qué if pertenece un else.

La gramática original es:

prop -> if expr then prop
     | prop_emparejada

prop_emparejada -> if expr then prop_emparejada else prop
                | otras
 Problema de ambigüedad

El problema aparece cuando se tienen if anidados. Por ejemplo:

if Messi then if Goku then atacar else defender

Esta expresión puede interpretarse de dos formas diferentes:

 Interpretación 1 (else con el if más cercano)
if Messi then (if Goku then atacar else defender)

Paso a paso:

Se evalúa si Messi es verdadero
Si lo es, se entra al segundo if
Si Goku es verdadero → atacar
Si no → defender
 Interpretación 2 (else con el primer if)
(if Messi then (if Goku then atacar)) else defender

Paso a paso:

Se evalúa si Messi es verdadero
Si lo es, se evalúa el segundo if:
Si Goku es verdadero → atacar
Si Messi es falso → defender
 Conclusión

La misma expresión tiene dos interpretaciones distintas, lo que demuestra que la gramática es ambigua.

Solución (gramática no ambigua)

Para eliminar la ambigüedad, se separan las producciones en emparejadas y no emparejadas:

prop -> prop_emparejada | prop_no_emparejada

prop_emparejada -> if expr then prop_emparejada else prop_emparejada
                | otras

prop_no_emparejada -> if expr then prop
                    | if expr then prop_emparejada else prop_no_emparejada
 Ejemplo ya sin ambigüedad

Tomando nuevamente:

if Messi then if Goku then atacar else defender

Ahora solo se puede interpretar así:

if Messi then (if Goku then atacar else defender)

Paso a paso:

El else se asocia automáticamente con el if más cercano (Goku)
El if de Messi queda sin else
Solo existe una interpretación válida
 Explicación final

El problema del dangling else se resuelve asegurando que cada else se asocie con el if más cercano, eliminando cualquier ambigüedad en la gramática.
Árbol 1 (else con Goku → el más cercano)
        if
       / | \
   Messi then   if
               / | \
           Goku then else
           /     \     \
       atacar   defender
 Interpretación paso a paso:
Se evalúa Messi
Si es verdadero → se evalúa Goku
Si Goku es verdadero → atacar
Si no → defender
 Árbol 2 (else con Messi)
           if
         /  |   \
     Messi then  else
           |       \
           if     defender
         /  |  \
     Goku then atacar
 Interpretación paso a paso:
Se evalúa Messi
Si es verdadero → evalúa Goku → atacar si es true
Si Messi es falso → defender
 Problema

La misma expresión genera dos árboles distintos, por lo tanto la gramática es ambigua.

 Solución (gramática no ambigua)
prop -> prop_emparejada | prop_no_emparejada

prop_emparejada -> if expr then prop_emparejada else prop_emparejada
                | otras

prop_no_emparejada -> if expr then prop
                    | if expr then prop_emparejada else prop_no_emparejada
 Árbol único (ya sin ambigüedad)
        if
       / | \
   Messi then   if
               / | \
           Goku then else
           /     \     \
       atacar   defender

## Punto 4: Parser CYK

Se implementó el algoritmo CYK, el cual permite verificar si una cadena pertenece a un lenguaje definido por una gramática en Forma Normal de Chomsky.

El algoritmo utiliza programación dinámica y tiene complejidad O(n³).

Ejemplo de prueba:

* Cadena: "ab"
* Resultado: válida

El algoritmo construye una tabla donde se almacenan los posibles símbolos generadores de cada subcadena.

<img width="1291" height="243" alt="image" src="https://github.com/user-attachments/assets/94d15c99-4ea7-46a0-9d15-c7cc0ab4396c" />


## Punto 5: Parser descendente recursivo

Se implementó un parser descendente recursivo basado en la siguiente gramática:

```
S -> id = E
E -> T + E | T
T -> id | num
```

Cada no terminal se implementa como una función:

* S(): inicio del análisis
* E(): maneja expresiones
* T(): reconoce valores

El parser analiza la cadena de izquierda a derecha usando una función `match` para validar tokens.

Ejemplo:

```
id = id + num
```

Resultado:

```
Cadena válida
```

<img width="1462" height="379" alt="image" src="https://github.com/user-attachments/assets/153b78d7-6aa6-46d1-b338-1b4d9c261fb7" />


## Conclusión

En este trabajo se diseñaron gramáticas formales, se implementaron analizadores sintácticos con diferentes técnicas (Bison, CYK y descendente recursivo), y se resolvió una ambigüedad clásica en lenguajes de programación. Esto permitió comprender mejor cómo funcionan los compiladores y los parsers.
