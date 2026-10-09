# Brasic V1.0

Brasic es un lenguaje de programación interpretado con palabras clave en
español. Los programas se guardan en archivos `.bras` y se
pueden ejecutar desde la consola de Brasic mediante
`EJECUTAR("archivo.bras")`.

> Esta guía se basa en las funciones y la sintaxis presentes en el
> código actual de Brasic. Algunas características pueden variar si el
> intérprete cambia.

## Índice

-   [Ejecutar Brasic](#ejecutar-brasic)
-   [Sintaxis básica](#sintaxis-básica)
-   [Variables y tipos](#variables-y-tipos)
-   [Operadores](#operadores)
-   [Condicionales](#condicionales)
-   [Bucles](#bucles)
-   [Funciones propias](#funciones-propias)
-   [Funciones integradas](#funciones-integradas)
-   [Añadir una función integrada](#añadir-una-función-integrada)
-   [Errores comunes](#errores-comunes)

## Ejecutar Brasic

Desde la carpeta del proyecto, inicia la consola:

``` bash
python shell.py
```

Aparecerá el indicador:

``` text
brasic_console >
```

Puedes escribir instrucciones directamente o ejecutar un archivo:

``` bras
IMPRIMIR("Hola Mundo!")
```

Guarda tus programas en archivos con extensión `.bras`. Si una
instrucción ocupa una línea nueva, el intérprete la reconoce como una
nueva sentencia. También admite `;` como separador de sentencias. 
Los comentarios empiezan con `#`.

## Sintaxis básica

### Mostrar texto y calcular

``` bras
IMPRIMIR("Hola, mundo!")
IMPRIMIR(2 + 3 * 4)
IMPRIMIR(2 ^ 3)
```

### Variables

Las variables se declaran con `VAR`:

``` bras
VAR nombre = "Paco"
VAR edad = 18
VAR precio = 3.5

IMPRIMIR(nombre)
IMPRIMIR(edad)
```

### Tipos y valores

Los valores que reconoce el intérprete incluyen:

-   Números enteros y decimales, por ejemplo `10` y `3.14`.
-   Texto entre comillas dobles, por ejemplo `"Hola"`.
-   Listas entre corchetes, por ejemplo `[1, 2, 3]`.
-   `VERDADERO` y `FALSO`, que representan valores booleanos.
-   `NULL`, el valor nulo.

Las cadenas admiten secuencias como `\n` para salto de línea y `\t` para
tabulación.

### Listas

``` bras
VAR numeros = [10, 20, 30]
IMPRIMIR(numeros)
IMPRIMIR(LARGO(numeros))
AÑADIR(numeros, 40)
IMPRIMIR(numeros)
```

## Operadores

  Categoría     Operadores
  ------------- ----------------------------------
  Aritmética    `+`, `-`, `*`, `/`, `^`
  Comparación   `==`, `!=`, `<`, `>`, `<=`, `>=`
  Lógica        `Y`, `O`, `NO`

Ejemplo:

``` bras
VAR puntos = 12
IMPRIMIR(puntos >= 10 Y puntos < 20)
```

## Condicionales

Las palabras clave para condiciones son `SI`, `ENTONCES`, `SINOS`,
`SINO` y `FIN`.

Ejemplo de una condición en una sola línea:

``` bras
SI edad >= 18 ENTONCES IMPRIMIR("Mayor de edad") SINO IMPRIMIR("Menor de edad")
```

Ejemplo en varias líneas:

``` bras
SI edad >= 18 ENTONCES
    IMPRIMIR("Mayor de edad")
SINO
    IMPRIMIR("Menor de edad")
FIN
```

También puedes encadenar condiciones con `SINOS`:

``` bras
SI nota >= 9 ENTONCES
    IMPRIMIR("Excelente")
SINOS nota >= 5 ENTONCES
    IMPRIMIR("Aprobado")
SINO
    IMPRIMIR("Suspendido")
FIN
```

## Bucles

### `MIENTRAS`

Repite el bloque mientras la condición sea verdadera:

``` bras
VAR i = 1
MIENTRAS i <= 5 ENTONCES
    IMPRIMIR(i)
    VAR i = i + 1
FIN
```

### `PARA`

El bucle `PARA` usa `HASTA` y, opcionalmente, `PASO`:

``` bras
PARA i = 0 HASTA 5 ENTONCES
    IMPRIMIR(i)
FIN
```

Con un paso explícito:

``` bras
PARA i = 0 HASTA 10 PASO 2 ENTONCES
    IMPRIMIR(i)
FIN
```

Dentro de los bucles, `ROMPER` sale del bucle y `CONTINUAR` pasa a la
siguiente iteración.

## Funciones propias

Se declaran con `FUNCION`. Para devolver un valor explícitamente,
utiliza `DEVOLVER`.

Función de una línea:

``` bras
FUNCION doble(x) -> x * 2
IMPRIMIR(doble(5))
```

Función con cuerpo de varias líneas:

``` bras
FUNCION sumar(a, b)
    DEVOLVER a + b
FIN

IMPRIMIR(sumar(3, 4))
```

Los argumentos se separan con comas y las funciones se llaman con
paréntesis.

## Funciones integradas

Los nombres siguientes están registrados en la tabla global del
intérprete.

  ---------------------------------------------------------------------------------------
  Función o valor               Uso                               Descripción
  ----------------------------- --------------------------------- -----------------------
  `IMPRIMIR(valor)`             `IMPRIMIR("Hola")`                Muestra un valor en la
                                                                  salida y devuelve el
                                                                  valor nulo.

  `IMPRIMIR_RET(valor)`         `VAR texto = IMPRIMIR_RET(123)`   Devuelve el valor
                                                                  convertido a texto, sin
                                                                  imprimirlo por sí
                                                                  misma.

  `ENTRADA()`                   `VAR nombre = ENTRADA()`          Lee una línea de texto
                                                                  introducida por el
                                                                  usuario.

  `ENTRADA_INT()`               `VAR edad = ENTRADA_INT()`        Lee una entrada hasta
                                                                  obtener un entero
                                                                  válido.

  `ALEATORIO(minimo, maximo)`   `ALEATORIO(1, 6)`                 Devuelve un entero
                                                                  aleatorio entre ambos
                                                                  límites, incluidos.

  `EJECUTAR(archivo)`           `EJECUTAR("otro.bras")`           Lee y ejecuta el
                                                                  archivo indicado.

  `LIMPIAR()`                   `LIMPIAR()`                       Limpia la terminal.

  `CLS()`                       `CLS()`                           Alias de `LIMPIAR()`.

  `ES_NUMERO(valor)`            `ES_NUMERO(42)`                   Devuelve `VERDADERO` si
                                                                  el valor es un número.

  `ES_TEXTO(valor)`             `ES_TEXTO("hola")`                Devuelve `VERDADERO` si
                                                                  el valor es texto.

  `ES_LISTA(valor)`             `ES_LISTA([1, 2])`                Devuelve `VERDADERO` si
                                                                  el valor es una lista.

  `ES_FUN(valor)`               `ES_FUN(mi_funcion)`              Devuelve `VERDADERO` si
                                                                  el valor es una
                                                                  función.

  `AÑADIR(lista, valor)`        `AÑADIR(datos, 4)`                Añade un elemento al
                                                                  final de una lista.

  `SACAR(lista, indice)`        `SACAR(datos, 0)`                 Elimina y devuelve el
                                                                  elemento situado en el
                                                                  índice indicado.

  `EXTENDER(listaA, listaB)`    `EXTENDER(a, b)`                  Añade a la primera
                                                                  lista los elementos de
                                                                  la segunda.

  `LARGO(lista)`                `LARGO([1, 2, 3])`                Devuelve el número de
                                                                  elementos de una lista.
  ---------------------------------------------------------------------------------------

Valores globales:

  Nombre        Descripción
  ------------- ----------------------------
  `NULL`        Valor nulo del intérprete.
  `VERDADERO`   Valor booleano verdadero.
  `FALSO`       Valor booleano falso.
  `MATH_PI`     Constante matemática π.

### Notas sobre las funciones integradas

-   `ALEATORIO` requiere dos números y el límite mínimo no puede superar
    al máximo.
-   `AÑADIR`, `SACAR`, `EXTENDER` y `LARGO` esperan listas en los
    argumentos indicados.
-   `EJECUTAR` recibe una ruta como texto. La ruta se interpreta
    respecto al directorio de trabajo desde el que se ejecuta Python.
-   Las funciones que realizan una acción, como `IMPRIMIR` o `AÑADIR`,
    normalmente devuelven `NULL` (que la consola actual puede mostrar
    como `0`).

## Añadir una función integrada

Las funciones integradas se implementan en Python dentro de la clase
`BuiltInFunction` y después se registran en `global_symbol_table`.

Este es el procedimiento general.

### 1. Crear el método de ejecución

Por ejemplo, vamos a añadir `CUADRADO(numero)`, que devuelve el cuadrado
de un número.

Dentro de `class BuiltInFunction`, añade:

``` python
def execute_square(self, exec_ctx):
    numero = exec_ctx.symbol_table.get("numero")

    if not isinstance(numero, Number):
        return RTResult().failure(RTError(
            self.pos_start,
            self.pos_end,
            "El argumento debe ser un número.",
            exec_ctx
        ))

    return RTResult().success(Number(numero.value ** 2))

execute_square.arg_names = ["numero"]
```

Puntos importantes:

-   `exec_ctx.symbol_table.get("numero")` obtiene el argumento por
    nombre.
-   `arg_names` define los nombres y el número de argumentos que
    recibirá la función.
-   Comprueba los tipos de los argumentos antes de operar con ellos.
-   Devuelve el resultado mediante `RTResult().success(...)`.
-   Si ocurre un error, devuelve `RTResult().failure(RTError(...))`.

### 2. Crear la instancia de la función integrada

En la sección donde se crean las instancias de `BuiltInFunction`, añade:

``` python
BuiltInFunction.square = BuiltInFunction("square")
```

El nombre `"square"` debe coincidir con el sufijo del método
`execute_square`.

### 3. Registrar el nombre que verá el usuario de Brasic

En la sección de `global_symbol_table`, añade:

``` python
global_symbol_table.set("CUADRADO", BuiltInFunction.square)
```

Este paso es imprescindible: si lo omites, Brasic no reconocerá
`CUADRADO` y mostrará un error indicando que no está definida.

### 4. Probar la función

Reinicia la consola de Brasic y ejecuta:

``` bras
IMPRIMIR(CUADRADO(5))
```

Resultado esperado:

``` text
25
```

### Añadir una función con dos argumentos

El patrón es el mismo que el de `ALEATORIO`:

``` python
def execute_sumar_numeros(self, exec_ctx):
    a = exec_ctx.symbol_table.get("a")
    b = exec_ctx.symbol_table.get("b")

    if not isinstance(a, Number) or not isinstance(b, Number):
        return RTResult().failure(RTError(
            self.pos_start,
            self.pos_end,
            "Los argumentos deben ser números.",
            exec_ctx
        ))

    return RTResult().success(Number(a.value + b.value))

execute_sumar_numeros.arg_names = ["a", "b"]
```

Después crea y registra la función:

``` python
BuiltInFunction.sumar_numeros = BuiltInFunction("sumar_numeros")
global_symbol_table.set("SUMAR_NUMEROS", BuiltInFunction.sumar_numeros)
```

Y úsala en Brasic:

``` bras
IMPRIMIR(SUMAR_NUMEROS(7, 8))
```

Resultado esperado:

``` text
15
```

## Errores comunes

-   **`'NOMBRE' no se ha definido`:** revisa que la función esté
    registrada en `global_symbol_table` y que el nombre coincida
    exactamente.
-   **Número incorrecto de argumentos:** revisa la lista `arg_names`.
-   **Tipo de argumento incorrecto:** valida el tipo con `isinstance`,
    como hacen `ALEATORIO` y las funciones de listas.
-   **El archivo no se encuentra:** comprueba el directorio de trabajo y
    la ruta que pasas a `EJECUTAR`.
-   **Aparece `0` después de una función que imprime:** puede ser el
    valor nulo que devuelve esa función y que la consola representa como
    `0`.

## Contribuir

Al añadir una función integrada:

1.  Implementa `execute_nombre` en `BuiltInFunction`.
2.  Define `execute_nombre.arg_names`.
3.  Crea la instancia
    `BuiltInFunction.nombre = BuiltInFunction("nombre")`.
4.  Registra el nombre público en `global_symbol_table`.
5.  Prueba casos válidos, tipos incorrectos y límites.
6.  Documenta la función en la tabla de funciones integradas.

------------------------------------------------------------------------

**Brasic** --- un lenguaje interpretado en desarrollo.
