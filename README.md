# Proyecto 2 --- Algoritmo CYK (Cocke--Younger--Kasami)

------------------------------------------------------------------------

## Diseño de la aplicación

### Descripción general

El proyecto implementa el **algoritmo CYK (Cocke--Younger--Kasami)** en
Python.\
Su propósito es determinar si una frase dada pertenece al lenguaje
generado por una **gramática libre de contexto (CFG)** expresada en
**Forma Normal de Chomsky (CNF)**.\
Además, el programa genera el **árbol sintáctico (parse tree)**
correspondiente.

### Estructura del código

El script se compone de cinco módulos principales:

1.  **Lectura de la gramática (`leer_gramatica`)**
    -   Lee un archivo `.txt` llamado `cnf.txt` que contiene las
        producciones gramaticales en CNF.\
2.  **Algoritmo CYK (`cyk_con_parse_tree`)**
    -   Implementa el algoritmo CYK usando **programación dinámica**.\
    -   Construye una tabla triangular `P[i][j]` donde cada celda
        contiene los no terminales que generan un fragmento de la
        cadena.\
    -   También guarda las combinaciones `(B, C, k)` necesarias para
        reconstruir el árbol sintáctico.
3.  **Reconstrucción del árbol (`construir_arbol`)**
    -   Reconstruye el árbol sintáctico de forma recursiva a partir de
        la información almacenada en `P`.\
    -   Cada nodo muestra las producciones utilizadas para derivar la
        frase.
4.  **Impresión del árbol (`imprimir_arbol`)**
    -   Muestra el árbol con indentación jerárquica, facilitando la
        lectura del proceso de derivación.
5.  **Bloque principal (`__main__`)**
    -   Solicita al usuario una frase.\
    -   Ejecuta el algoritmo CYK.\
    -   Mide el tiempo de ejecución e imprime el resultado ("La frase
        pertenece / no pertenece al lenguaje") junto con el árbol
        sintáctico.

------------------------------------------------------------------------

## Discusión

### Obstáculos encontrados

-   **Representación de la gramática:**\
    Fue necesario garantizar que todas las producciones estuvieran en
    **Forma Normal de Chomsky (CNF)**, donde cada regla tiene una de las
    siguientes formas:

    -   `A → BC` (dos no terminales)\
    -   `A → a` (un terminal)

-   **Reconstrucción del árbol sintáctico:**\
    El algoritmo CYK tradicional solo determina pertenencia. Para
    obtener el árbol, se adaptó la tabla dinámica para almacenar no solo
    los símbolos sino también las combinaciones que los generaron.

-   **Control de índices:**\
    Se manejaron cuidadosamente los índices `i`, `j` y `k` para evitar
    errores de rango durante el llenado de la tabla.

### Recomendaciones

-   Usar siempre **terminales en minúscula** y **no terminales en
    mayúscula**.\
-   Asegurarse de que la frase ingresada contenga exactamente los
    terminales definidos en el archivo `cnf.txt`.\
-   Para gramáticas grandes, se recomienda evitar frases muy largas, ya
    que la complejidad de CYK es **O(n³)**.

------------------------------------------------------------------------

## Ejemplos y pruebas realizadas

### Gramática de prueba (`cnf.txt`)

    S -> NP VP
    NP -> Det N | Det N PP | N
    VP -> V NP | V NP PP | V | V PP
    PP -> P NP

    # Determinantes
    Det -> el | la | un | una

    # Sustantivos
    N -> niño | niña | perro | gato | manzana | agua | cuchara | parque

    # Verbos
    V -> come | bebe | corre | juega | ve

    # Preposiciones
    P -> con | en

### Ejemplo 1 --- Frase válida

**Entrada:**

    el niño come una manzana

**Salida:**

    Resultado:
    La frase pertenece al lenguaje.
    Tiempo de ejecución: 0.000102 segundos

    Árbol sintáctico:
    S
    NP
        Det -> el
        N -> niño
    VP
        V -> come
        NP
        Det -> una
        N -> manzana

### Ejemplo 2 --- Frase inválida

**Entrada:**

    la juega parque

**Salida:**

    Resultado:
    La frase NO pertenece al lenguaje.
    Tiempo de ejecución: 0.000112 segundos
    

### Ejemplo 3 --- Frase válida

**Entrada:**

    una niña juega con la cuchara

**Salida:**
    Resultado:
    La frase pertenece al lenguaje.
    Tiempo de ejecución: 0.000107 segundos

    Árbol sintáctico:
    S
    NP
        Det -> una
        N -> niña
    VP
        V -> juega
        PP
        P -> con
        NP
            Det -> la
            N -> cuchara
    
------------------------------------------------------------------------

## Conclusiones

-   El algoritmo CYK permite verificar de forma sistemática si una frase
    pertenece al lenguaje generado por una gramática CFG.\
-   La construcción del árbol sintáctico facilita la comprensión de la
    estructura jerárquica de la oración.\
-   El script es modular, legible y fácilmente adaptable a nuevas
    gramáticas o frases.
