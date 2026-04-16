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

---

## Punto 2: Implementación con Bison y Flex

Se implementó la gramática utilizando herramientas de análisis léxico y sintáctico:

* Flex: para reconocer tokens (palabras clave, identificadores, números, etc.)
* Bison: para validar la estructura del lenguaje

### Pasos de ejecución:

```
bison -d parser.y
flex lexer.l
gcc lex.yy.c parser.tab.c -lfl -o parser
./parser
```

El programa permite ingresar instrucciones como:

```
CREATE usuarios {nombre:"Juan",edad:20};
READ usuarios WHERE edad=20;
```

Y valida si son correctas según la gramática.

---

## Punto 3: Ambigüedad en if-then-else

La gramática original presenta ambigüedad debido al problema del "dangling else".

Ejemplo ambiguo:

```
if E1 then if E2 then S1 else S2
```

No es claro a qué `if` pertenece el `else`.

### Solución (gramática no ambigua):

```
prop -> prop_emparejada | prop_no_emparejada

prop_emparejada -> if expr then prop_emparejada else prop_emparejada
                | otras

prop_no_emparejada -> if expr then prop
                    | if expr then prop_emparejada else prop_no_emparejada
```

Esta solución asegura que el `else` se asocie al `if` más cercano.

---

## Punto 4: Parser CYK

Se implementó el algoritmo CYK, el cual permite verificar si una cadena pertenece a un lenguaje definido por una gramática en Forma Normal de Chomsky.

El algoritmo utiliza programación dinámica y tiene complejidad O(n³).

Ejemplo de prueba:

* Cadena: "ab"
* Resultado: válida

El algoritmo construye una tabla donde se almacenan los posibles símbolos generadores de cada subcadena.

---

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

---

## Conclusión

En este trabajo se diseñaron gramáticas formales, se implementaron analizadores sintácticos con diferentes técnicas (Bison, CYK y descendente recursivo), y se resolvió una ambigüedad clásica en lenguajes de programación. Esto permitió comprender mejor cómo funcionan los compiladores y los parsers.
