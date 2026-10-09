# Brasic

**Brasic** es un lenguaje de programación en desarrollo, creado con Python, cuyo objetivo es facilitar el aprendizaje de la programación a personas que están empezando, especialmente a hablantes de español.

El proyecto busca ofrecer una forma más intuitiva de comprender cómo funciona un lenguaje de programación, utilizando palabras y conceptos familiares para reducir la barrera inicial de aprendizaje. Además de servir como herramienta educativa, Brasic es un proyecto para explorar cómo se construye un lenguaje de programación desde cero.

> Brasic no pretende sustituir a Python ni a otros lenguajes establecidos. Su propósito es servir como punto de partida para comprender sus fundamentos y facilitar la transición hacia lenguajes más complejos.

## ¿Por qué se ha creado?

Aprender a programar puede resultar complicado al principio. Además de comprender la lógica y resolver problemas, los principiantes deben familiarizarse con una sintaxis nueva, conceptos abstractos y palabras clave que no siempre les resultan intuitivas.

Brasic nace para reducir esa dificultad inicial mediante tres objetivos:

* **Facilitar el aprendizaje:** introducir los fundamentos de la programación de forma progresiva.
* **Acercar el código al español:** explorar el uso de palabras clave en español para que los principiantes puedan relacionar el código con conceptos que ya conocen.
* **Comprender antes de avanzar:** ayudar a construir una base sólida antes de pasar a lenguajes con ecosistemas, sintaxis y características más complejos.

El objetivo no es eliminar la necesidad de aprender conceptos técnicos, sino hacer que el primer contacto con ellos sea más accesible.

## Filosofía del proyecto

Brasic se desarrolla con un enfoque educativo y experimental. La idea es que el usuario no solo aprenda a escribir código, sino que también pueda comprender qué ocurre detrás de él.

Por eso, el proyecto se construye a partir de componentes propios, como el analizador léxico (*lexer*), el analizador sintáctico (*parser*) y el árbol de sintaxis abstracta (*AST*).

Estos componentes permiten estudiar cómo una expresión escrita por el usuario se transforma en una estructura que el intérprete puede procesar.

El proyecto está en desarrollo, por lo que su sintaxis, sus funcionalidades y su arquitectura pueden cambiar con el tiempo.

## Estructura y funcionamiento interno

Brasic está escrito en Python. Su arquitectura se organiza en componentes que procesan el código en distintas etapas.

| Componente | Función                                                                                                                 |
| ---------- | ----------------------------------------------------------------------------------------------------------------------- |
| Lexer      | Lee el texto de entrada y lo transforma en tokens, como números y operadores.                                           |
| Parser     | Analiza la secuencia de tokens y construye una estructura que representa la expresión.                                  |
| AST        | Representa las expresiones mediante nodos, como números y operaciones binarias.                                         |
| Intérprete | Será el encargado de ejecutar las estructuras generadas y producir resultados, según las funcionalidades implementadas. |

Actualmente, el proyecto incluye las bases del análisis léxico y sintáctico. Las capacidades de ejecución dependen del estado de desarrollo del intérprete.

## Modificar y ampliar Brasic

Brasic está diseñado como un proyecto que se puede estudiar, modificar y ampliar. Si conoces Python, puedes experimentar con su implementación y añadir nuevas funcionalidades.

### 1. Comprender el código existente

Antes de introducir cambios, conviene familiarizarse con el flujo de ejecución:

1. `shell.py` recibe el texto que escribe el usuario.
2. `brasic.py` procesa ese texto mediante el lexer.
3. El parser organiza los tokens en una estructura sintáctica.
4. Los componentes posteriores podrán interpretar esa estructura y ejecutar las operaciones correspondientes.

Los nombres y la organización exacta de los archivos pueden cambiar a medida que evolucione el proyecto.

### 2. Añadir una función integrada (*built-in*)

Una función integrada es una función que forma parte del propio lenguaje y que el usuario puede ejecutar directamente desde el código de Brasic.

Para añadir una función integrada personalizada, hay que modificar la clase `BuiltInFunction` y registrar la función en la tabla de símbolos global. El proceso se divide en tres pasos.

#### Paso 1. Crear la función dentro de `BuiltInFunction`

Dentro de la clase `BuiltInFunction`, crea un método cuyo nombre siga este formato:

```python
def execute_nombre(self, ...):
```

Sustituye `nombre` por el nombre interno que quieras dar a la función. Los parámetros del método dependerán de la estructura que utilice tu clase.

**Importante:** la mayor parte del código de una función integrada suele estar dedicada a comprobar errores. Estas comprobaciones permiten verificar que los argumentos sean válidos, que tengan los tipos correctos y que se cumplan las condiciones necesarias antes de ejecutar la operación.

El código que realiza la función propiamente dicha suele encontrarse al final del método, una vez superadas las comprobaciones.


Justo debajo de la definición de la función, añade:

```python
execute_nombre.arg_names = [argumentos]
```

Sustituye `nombre` por el nombre utilizado en `execute_nombre` y `argumentos` por los nombres de los argumentos que deberá recibir la función.

Por ejemplo, si la función recibe dos argumentos llamados `texto` y `veces`:

```python
execute_repetir.arg_names = ["texto", "veces"]
```

Esta lista permite al sistema conocer los nombres de los argumentos que acepta la función.

#### Paso 2. Registrar la función en `BuiltInFunction`

Justo debajo de la clase `BuiltInFunction`, añade:

```python
BuiltInFunction.nombre = BuiltInFunction(nombre)
```

Sustituye `nombre` por el nombre que quieras asignar a la función.

**Importante:** en este caso, el nombre no debe llevar el prefijo `execute_`. Debe ser únicamente la parte del nombre que identifica la función.

Por ejemplo, si has creado `execute_repetir`, debes registrar la función así:

```python
BuiltInFunction.repetir = BuiltInFunction("repetir")
```

De esta manera, `BuiltInFunction.repetir` representa la función integrada que acabas de crear.

#### Paso 3. Añadir la función a la tabla de símbolos global

Por último, justo encima de la función `run`, añade:

```python
global_symbol_table.set("NOMBRE", BuiltInFunction.nombre)
```

Sustituye `nombre` por el nombre utilizado al registrar la función en `BuiltInFunction.nombre` y `NOMBRE` por el identificador que se utilizará para invocarla desde el código de Brasic.

Por ejemplo, si en el paso anterior has registrado `BuiltInFunction.repetir`, puedes añadir:

```python
global_symbol_table.set("REPETIR", BuiltInFunction.repetir)
```

En este ejemplo, `REPETIR` será el nombre que reconocerá el entorno global de Brasic.

**Recuerda la diferencia entre los nombres:**

* `execute_repetir`: nombre del método que implementa el comportamiento de la función.
* `BuiltInFunction.repetir`: nombre con el que se registra la función dentro de la clase.
* `"REPETIR"`: identificador con el que se expone la función al código de Brasic.

Una vez completados los tres pasos, la función estará registrada para que el intérprete pueda acceder a ella, siempre que el sistema de ejecución y el parser admitan correctamente las llamadas a funciones.


### 3. Funcionalidades

## Manual de uso

El funcionamiento del lenguaje, los ejemplos de código y las instrucciones para utilizar las funcionalidades disponibles se explican en el manual de uso del proyecto.

Consulta ese documento para aprender a utilizar Brasic. Este README se centra en presentar el proyecto y orientar a quienes quieran estudiar o modificar su implementación.

[Consultar el manual de uso](./MANUAL.md)

## Estado del proyecto

Brasic se encuentra en desarrollo. Su objetivo es evolucionar de manera progresiva, incorporando funcionalidades mientras se mantiene el enfoque educativo y la posibilidad de estudiar cómo funciona internamente un lenguaje de programación.

Las características disponibles deben entenderse según la implementación actual, no como una lista de funcionalidades futuras garantizadas.

## Contribuciones

Las propuestas, mejoras y experimentos son bienvenidos. Si quieres ampliar Brasic, procura que los cambios mantengan el objetivo principal del proyecto: facilitar el aprendizaje de la programación y hacer comprensible el funcionamiento interno del lenguaje.
