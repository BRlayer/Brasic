# Brasic 1.0 --- Manual de uso

> **Estado del documento:** manual inicial de Brasic 1.0, preparado a
> partir del código fuente compartido. Algunas construcciones del parser
> y del lexer tienen inconsistencias; se señalan en la sección
> [Limitaciones conocidas](#limitaciones-conocidas).

## Índice

1.  [¿Qué es Brasic?](#qué-es-brasic)
2.  [Cómo ejecutar Brasic](#cómo-ejecutar-brasic)
3.  [Sintaxis básica](#sintaxis-básica)
4.  [Variables y tipos de datos](#variables-y-tipos-de-datos)
5.  [Operadores](#operadores)
6.  [Condicionales](#condicionales)
7.  [Bucles](#bucles)
8.  [Funciones definidas por el
    usuario](#funciones-definidas-por-el-usuario)
9.  [Funciones integradas](#funciones-integradas)
10. [Constantes integradas](#constantes-integradas)
11. [Listas](#listas)
12. [Comentarios y cadenas de texto](#comentarios-y-cadenas-de-texto)
13. [Errores](#errores)
14. [Programa de ejemplo](#programa-de-ejemplo)
15. [Limitaciones conocidas](#limitaciones-conocidas)

------------------------------------------------------------------------

## ¿Qué es Brasic?

Brasic es un lenguaje interpretado. El intérprete procesa el código
fuente, analiza su sintaxis y ejecuta las instrucciones sin generar
previamente un ejecutable independiente.

La implementación actual incluye números, cadenas de texto, listas,
variables, operaciones aritméticas y de comparación, condicionales,
bucles, funciones y funciones integradas para entrada/salida y
manipulación de listas.

## Cómo ejecutar Brasic

### Abrir la consola interactiva

Desde la terminal, ejecuta el archivo de la consola:

``` bash
python shell.py
```

La consola muestra un prompt parecido a:

``` text
brasic_console >
```

Escribe una instrucción y pulsa Enter. Por ejemplo:

``` text
brasic_console > IMPRIMIR("Hola, mundo")
Hola, mundo
```

### Ejecutar un archivo

La función integrada `EJECUTAR` permite cargar y ejecutar un archivo:

``` text
EJECUTAR("programa.bras")
```

En la implementación compartida, `EJECUTAR` abre la ruta indicada y pasa
el contenido al intérprete. La comprobación de que la extensión sea
`.bras` debe estar incorporada en la versión de `execute_run()` para que
se rechacen otras extensiones.

Las rutas relativas se resuelven respecto al directorio de trabajo desde
el que se ha iniciado Brasic. Si el archivo no se encuentra o no se
puede leer, se devuelve un error de ejecución.

## Sintaxis básica

### Separar instrucciones

Se puede escribir una instrucción por línea. El lexer también reconoce
`;` como separador de instrucciones.

``` bras
IMPRIMIR("Primera línea")
IMPRIMIR("Segunda línea")
```

También se puede separar con punto y coma:

``` bras
IMPRIMIR("Primera instrucción"); IMPRIMIR("Segunda instrucción")
```

### Distinguir entre mayúsculas y minúsculas

Los nombres de variables y las palabras clave se comparan distinguiendo
mayúsculas y minúsculas. Por convención, las palabras clave y las
funciones integradas se escriben en mayúsculas.

### Identificadores

Los identificadores se utilizan para nombrar variables y funciones. La
implementación actual admite letras ASCII, números y guion bajo, y no
permite que un identificador empiece por un número.

Ejemplos:

``` bras
VAR nombre = "Nombre"
VAR puntuacion_1 = 10
```

**Nota:** aunque algunos nombres integrados contienen `Ñ` (por ejemplo,
`AÑADIR`), el lexer compartido utiliza el conjunto de letras ASCII. Por
ello, ese nombre puede no reconocerse correctamente hasta ampliar el
reconocimiento de identificadores.

## Variables y tipos de datos

### Crear una variable

Se utiliza `VAR` para declarar o asignar una variable:

``` bras
VAR edad = 14
VAR nombre = "Alex"
VAR nota = 8.5
```

La asignación devuelve el valor asignado. Para leer una variable,
escribe su nombre:

``` bras
VAR resultado = 12 * 2
IMPRIMIR(resultado)
```

### Tipos de datos

  -----------------------------------------------------------------------
  Tipo                    Ejemplo                 Descripción
  ----------------------- ----------------------- -----------------------
  Entero                  `12`                    Número entero.

  Decimal                 `3.14`                  Número con parte
                                                  decimal.

  Texto                   `"Hola"`                Cadena delimitada por
                                                  comillas dobles.

  Lista                   `[1, 2, 3]`             Colección ordenada de
                                                  valores.

  Valor lógico            `VERDADERO`, `FALSO`    Se representa
                                                  internamente mediante
                                                  números: `1` y `0`.

  Nulo                    `NULL`                  Se representa
                                                  internamente mediante
                                                  `0` en esta
                                                  implementación.
  -----------------------------------------------------------------------

### Cadenas de texto

Las cadenas se escriben entre comillas dobles:

``` bras
VAR mensaje = "Hola, Brasic"
IMPRIMIR(mensaje)
```

El lexer contempla estas secuencias de escape:

-   `\n`: salto de línea.
-   `\t`: tabulación.
-   `\"`: comilla doble dentro del texto.
-   `\\`: barra invertida.

El comportamiento de escape depende de la implementación del lexer y
conviene probarlo si se usa en código importante.

## Operadores

### Aritméticos

  -----------------------------------------------------------------------
  Operador                Operación               Ejemplo
  ----------------------- ----------------------- -----------------------
  `+`                     Suma de números o       `2 + 3`,
                          concatenación de textos `"Hola " + "mundo"`

  `-`                     Resta                   `8 - 3`

  `*`                     Multiplicación; también `4 * 2`, `"ja" * 3`
                          repite un texto si se   
                          multiplica por un       
                          número                  

  `/`                     División; también       `8 / 2`, `[10, 20] / 0`
                          permite obtener un      
                          elemento de una lista   
                          mediante su índice      

  `^`                     Potencia                `2 ^ 3`

  `-` unario              Cambia el signo de un   `-5`
                          número                  
  -----------------------------------------------------------------------

### Comparación

  Operador   Significado
  ---------- ---------------
  `==`       Igual
  `!=`       Distinto
  `<`        Menor que
  `>`        Mayor que
  `<=`       Menor o igual
  `>=`       Mayor o igual


### Operadores lógicos

El lenguaje declara las palabras clave `Y`, `O` y `NO` con la intención
de representar AND, OR y NOT:

``` bras
NO FALSO O VERDADERO
```


## Condicionales

### `SI`

Ejecuta una instrucción si la condición es verdadera:

``` bras
VAR edad = 18

SI edad >= 18 ENTONCES IMPRIMIR("Mayor de edad")
```

### Bloques de varias líneas

Para ejecutar varias instrucciones, se escribe el bloque en líneas
separadas y se cierra con `FIN`:

``` bras
SI edad >= 18 ENTONCES
    IMPRIMIR("Mayor de edad")
    IMPRIMIR("Puede continuar")
FIN
```

### `SINOS` y `SINO`

`SINOS` permite añadir otra condición; `SINO` define el caso
alternativo:

``` bras
SI nota >= 5 ENTONCES
    IMPRIMIR("Aprobado")
SINOS nota >= 0 ENTONCES
    IMPRIMIR("Suspenso")
SINO
    IMPRIMIR("Nota no válida")
FIN
```

La forma exacta de combinar `SINOS` y `SINO` debe probarse con la
versión concreta del parser, ya que el tratamiento de bloques anidados y
`FIN` depende de su implementación actual.

## Bucles

### `MIENTRAS`

Repite el bloque mientras la condición sea verdadera:

``` bras
VAR contador = 0

MIENTRAS contador < 3 ENTONCES
    IMPRIMIR(contador)
    VAR contador = contador + 1
FIN
```

### `PARA`, `HASTA` y `PASO`

Recorre valores desde el inicio hasta antes del límite final. El paso es
opcional y, si se omite, vale `1`:

``` bras
PARA i = 0 HASTA 5 ENTONCES
    IMPRIMIR(i)
FIN
```

```text
0
1
2
3
4
5
```

Con un paso explícito:

``` bras
PARA i = 0 HASTA 10 PASO 2 ENTONCES
    IMPRIMIR(i)
FIN
```

El límite final no se incluye. Con paso positivo, el bucle continúa
mientras `i` sea menor que el límite; con paso negativo, mientras sea
mayor.

### `SALIR` y `CONTINUAR`

-   `SALIR`: solicita salir del bucle actual.
-   `CONTINUAR`: solicita saltar al siguiente ciclo del bucle.

Estas instrucciones están implementadas en el intérprete para los bucles
`PARA` y `MIENTRAS`.

## Funciones definidas por el usuario

### Función de una sola expresión

Se puede definir una función con `FUN`, parámetros entre paréntesis y
`->` seguido de una expresión:

``` bras
FUN doble(n) -> n * 2

IMPRIMIR(doble(5))
```

La expresión después de `->` se devuelve automáticamente.

### Funciones con varios parámetros

``` bras
FUN sumar(a, b) -> a + b

IMPRIMIR(sumar(3, 4))
```

### `DEVOLVER`

Dentro de una función, `DEVOLVER` permite devolver un valor
explícitamente:

``` bras
FUN cuadrado(n) ->
    DEVOLVER n * n
FIN
```

### Funciones anónimas

El parser admite definiciones sin nombre, por ejemplo:

``` bras
FUN(x) -> x * 2
```

El uso de funciones anónimas como valores depende de cómo se asignen y
se pasen en el programa.

## Funciones integradas

Los nombres siguientes están registrados en la tabla global de símbolos
del código compartido. Los argumentos se pasan entre paréntesis y se
separan con comas.

  --------------------------------------------------------------------------------------------------
  Función                      Argumentos        Qué hace          Ejemplo
  ---------------------------- ----------------- ----------------- ---------------------------------
  `IMPRIMIR(valor)`            1                 Muestra el valor  `IMPRIMIR("Hola")`
                                                 en la consola. No 
                                                 devuelve un valor 
                                                 útil; devuelve    
                                                 `NULL`.           

  `IMPRIMIR_RET(valor)`        1                 Convierte el      `VAR texto = IMPRIMIR_RET(123)`
                                                 valor a texto y   
                                                 lo devuelve como  
                                                 cadena, sin       
                                                 imprimirlo.       

  `ENTRADA()`                  0                 Lee una línea de  `VAR nombre = ENTRADA()`
                                                 texto introducida 
                                                 por el usuario y  
                                                 la devuelve.      

  `ENTRADA_INT()`              0                 Lee una entrada   `VAR edad = ENTRADA_INT()`
                                                 hasta que pueda   
                                                 convertirse a     
                                                 entero.           

  `LIMPIAR()`                  0                 Intenta limpiar   `LIMPIAR()`
                                                 la consola.       

  `CLS()`                      0                 Alias de          `CLS()`
                                                 `LIMPIAR()`.      

  `ES_NUMERO(valor)`           1                 Devuelve `1` si   `ES_NUMERO(42)`
                                                 el valor es       
                                                 numérico y `0` en 
                                                 caso contrario.   

  `ES_TEXTO(valor)`            1                 Devuelve `1` si   `ES_TEXTO("hola")`
                                                 el valor es una   
                                                 cadena y `0` en   
                                                 caso contrario.   

  `ES_LISTA(valor)`            1                 Devuelve `1` si   `ES_LISTA([1, 2])`
                                                 el valor es una   
                                                 lista y `0` en    
                                                 caso contrario.   

  `ES_FUN(valor)`              1                 Devuelve `1` si   `ES_FUN(IMPRIMIR)`
                                                 el valor es una   
                                                 función definida  
                                                 por el usuario o  
                                                 integrada y `0`   
                                                 en caso           
                                                 contrario.        

  `AÑADIR(lista, valor)`       2                 Añade un elemento `AÑADIR(datos, 7)`
                                                 al final de la    
                                                 lista existente.  

  `SACAR(lista, indice)`       2                 Elimina y         `SACAR(datos, 0)`
                                                 devuelve el       
                                                 elemento en el    
                                                 índice indicado.  

  `EXTENDER(listaA, listaB)`   2                 Añade a `listaA`  `EXTENDER(a, b)`
                                                 todos los         
                                                 elementos de      
                                                 `listaB`.         
                                                 Modifica          
                                                 `listaA`.         

  `LARGO(lista)`               1                 Devuelve el       `LARGO([2, 4, 6])`
                                                 número de         
                                                 elementos de una  
                                                 lista.            

  `EJECUTAR(fn)`               1                 Lee y ejecuta el  `EJECUTAR("programa.bras")`
                                                 código de un      
                                                 archivo.          
  --------------------------------------------------------------------------------------------------

### Detalles importantes de las funciones integradas

#### `ENTRADA()`

Devuelve una cadena de texto. Si el usuario escribe `25`, el resultado
es `"25"`, no el número `25`.

#### `ENTRADA_INT()`

Devuelve un número entero. Si la entrada no es un entero válido, vuelve
a pedirla.

#### `AÑADIR(lista, valor)`

Modifica la lista original y devuelve `NULL`:

``` bras
VAR numeros = [1, 2]
AÑADIR(numeros, 3)
IMPRIMIR(numeros)
```

Resultado esperado:

``` text
[1, 2, 3]
```

#### `SACAR(lista, indice)`

Elimina el elemento de la lista original y devuelve el elemento
eliminado. Los índices empiezan en `0`. Si el índice no existe, se
genera un error de ejecución.

``` bras
VAR numeros = [10, 20, 30]
VAR eliminado = SACAR(numeros, 1)
IMPRIMIR(eliminado)
IMPRIMIR(numeros)
```

#### `EXTENDER(listaA, listaB)`

Añade todos los elementos de `listaB` al final de `listaA`. Modifica la
primera lista; no crea una lista independiente.

#### `LARGO(lista)`

En el código actual solo acepta listas. No se debe asumir que funciona
con cadenas de texto.

#### `EJECUTAR(fn)`

Recibe una ruta en forma de texto. Intenta leer el archivo y ejecutar su
contenido. Si la lectura o la ejecución falla, propaga un error. Es 
necesario que el archivo tenga la extension `.bras`

## Constantes integradas

  Constante     Valor o significado
  ------------- -----------------------------------------------------------
  `NULL`        Valor nulo de Brasic; internamente se representa con `0`.
  `FALSO`       Valor lógico falso; internamente `0`.
  `VERDADERO`   Valor lógico verdadero; internamente `1`.
  `MATH_PI`     Aproximación de π proporcionada por Python.

Ejemplo:

``` bras
IMPRIMIR(MATH_PI)
IMPRIMIR(VERDADERO)
```

## Listas

Las listas se crean con corchetes y elementos separados por comas:

``` bras
VAR numeros = [10, 20, 30]
VAR vacia = []
```

Se pueden concatenar dos listas con `*`:

``` bras
VAR a = [1, 2]
VAR b = [3, 4]
IMPRIMIR(a * b)
```

También se puede añadir un elemento a una lista mediante `+`, lo que
crea una lista nueva:

``` bras
VAR original = [1, 2]
VAR nueva = original + 3
IMPRIMIR(nueva)
```

En la implementación actual, la división de una lista por un número
devuelve el elemento de ese índice:

``` bras
VAR colores = ["rojo", "verde", "azul"]
IMPRIMIR(colores / 1)
```

Resultado esperado: `"verde"`.

**Precaución:** el método `copy()` de la lista compartida reutiliza la
lista interna de elementos en lugar de copiarla profundamente. Algunas
operaciones que parecen crear una lista nueva pueden compartir la
estructura interna; revisa este comportamiento antes de depender de
copias independientes.

## Comentarios y cadenas de texto

### Comentarios

El lexer utiliza `#` para iniciar un comentario:

``` bras
# Este es un comentario
IMPRIMIR("Esto sí se ejecuta")
```

En la implementación compartida, el bucle que omite comentarios no
comprueba correctamente el final del archivo. Evita dejar un comentario
sin salto de línea al final hasta corregirlo.

### Secuencias de escape

Ejemplo de uso previsto:

``` bras
IMPRIMIR("Primera línea\nSegunda línea")
IMPRIMIR("Columna 1\tColumna 2")
```

Prueba estos casos en la versión instalada, ya que el comportamiento
depende del código exacto del lexer.

## Errores

El intérprete distingue varias categorías de error:

-   **Carácter ilegal:** aparece cuando el lexer encuentra un carácter
    que no reconoce.
-   **Carácter esperado:** aparece cuando falta un carácter requerido,
    por ejemplo `=` después de `!`.
-   **Sintaxis inválida:** aparece cuando la secuencia de tokens no
    cumple la gramática.
-   **Error de ejecución:** aparece durante la ejecución, por ejemplo al
    dividir entre cero, utilizar una variable no definida, pasar un tipo
    incorrecto a una función integrada o acceder a un índice
    inexistente.

Los mensajes pueden incluir el archivo, la línea y una indicación visual
de la posición del error.

## Programa de ejemplo

El siguiente ejemplo combina variables, listas, un bucle y una función
integrada:

``` bras
VAR numeros = [2, 4, 6]
VAR total = 0

PARA i = 0 HASTA LARGO(numeros) ENTONCES
    VAR total = total + numeros / i
FIN

IMPRIMIR("Total:")
IMPRIMIR(total)
```

El ejemplo ilustra el acceso a elementos mediante `lista / indice` y el
uso de `LARGO`. En la versión actual, conviene probarlo después de
corregir los operadores de comparación que utiliza el bucle.

## Limitaciones conocidas

Este apartado recoge inconsistencias visibles en el código fuente
compartido. No son características deseables del lenguaje; son puntos
que conviene corregir antes de declarar la versión 1.0 estable.

1.  **Funciones multilínea:** el parser comprueba `END`, mientras que el
    resto de la sintaxis y los mensajes indican `FIN`.
2.  **Comentarios al final del archivo:** `skip_comment()` puede seguir
    avanzando después de llegar al final del texto si no hay un salto de
    línea.
3.  **Identificadores con `Ñ`:** el lexer usa letras ASCII; nombres como
    `AÑADIR` pueden no tokenizarse correctamente.
4.  **Limpieza de consola:** `LIMPIAR()` ejecuta `cls` tanto en Windows
    como en otros sistemas; en Linux normalmente debería ejecutarse
    `clear`.
