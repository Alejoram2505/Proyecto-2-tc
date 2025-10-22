import time
from pprint import pprint

# ---------------------------------------------------
# LECTURA DE LA GRAMÁTICA EN CNF DESDE ARCHIVO
# ---------------------------------------------------
def leer_gramatica(nombre_archivo):
    """
    Lee una gramática en formato CNF desde un archivo .txt
    """
    gramatica = {}
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea or "->" not in linea:
                continue
            izquierda, derecha = linea.split("->")
            izquierda = izquierda.strip()
            producciones = [p.strip().split() for p in derecha.split("|")]
            gramatica.setdefault(izquierda, []).extend(producciones)
    return gramatica


# ---------------------------------------------------
# ALGORITMO CYK CON ESTRUCTURA DE ÁRBOL
# ---------------------------------------------------
def cyk_con_parse_tree(gramatica, cadena):
    """
    Implementa el algoritmo CYK y guarda información de estructura
    para poder reconstruir el árbol sintáctico.
    """
    palabras = cadena.strip().split()
    n = len(palabras)
    variables = list(gramatica.keys())

    # Tabla P[i][j]: diccionario {NoTerminal: [(B, C, k), ...] o palabra terminal}
    P = [[{} for _ in range(n)] for _ in range(n)]

    # Inicializar primera fila (palabras terminales)
    for i in range(n):
        for A in variables:
            for prod in gramatica[A]:
                if len(prod) == 1 and prod[0] == palabras[i]:
                    P[i][i].setdefault(A, []).append(palabras[i])

    # Rellenar resto de la tabla
    for l in range(2, n + 1):  # longitud del substring
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for A in variables:
                    for prod in gramatica[A]:
                        if len(prod) == 2:
                            B, C = prod
                            if B in P[i][k] and C in P[k + 1][j]:
                                P[i][j].setdefault(A, []).append((B, C, k))

    pertenece = "S" in P[0][n - 1]
    return pertenece, P, n


# ---------------------------------------------------
# RECONSTRUCCIÓN DEL ÁRBOL SINTÁCTICO
# ---------------------------------------------------
def construir_arbol(P, i, j, simbolo):
    """
    Reconstruye recursivamente el árbol sintáctico desde la tabla CYK.
    """
    if i == j:
        return (simbolo, list(P[i][j][simbolo])[0])  # terminal

    for produccion in P[i][j][simbolo]:
        B, C, k = produccion
        izquierda = construir_arbol(P, i, k, B)
        derecha = construir_arbol(P, k + 1, j, C)
        return (simbolo, izquierda, derecha)

    return (simbolo,)  # fallback


# ---------------------------------------------------
# IMPRESIÓN DEL ÁRBOL EN FORMA LEGIBLE
# ---------------------------------------------------
def imprimir_arbol(arbol, nivel=0):
    """
    Imprime el árbol sintáctico con indentación.
    """
    if len(arbol) == 2 and isinstance(arbol[1], str):
        print("  " * nivel + f"{arbol[0]} -> {arbol[1]}")
    else:
        print("  " * nivel + f"{arbol[0]}")
        for hijo in arbol[1:]:
            imprimir_arbol(hijo, nivel + 1)


# ---------------------------------------------------
# MAIN PRINCIPAL
# ---------------------------------------------------
if __name__ == "__main__":
    gramatica = leer_gramatica("cnf.txt")

    frase = input("Ingrese una frase (en minúsculas): ").strip()

    inicio = time.time()
    pertenece, P, n = cyk_con_parse_tree(gramatica, frase)
    fin = time.time()

    print("\nResultado:")
    if pertenece:
        print("La frase pertenece al lenguaje.")
        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

        print("\nÁrbol sintáctico:")
        arbol = construir_arbol(P, 0, n - 1, "S")
        imprimir_arbol(arbol)
    else:
        print(" La frase NO pertenece al lenguaje.")
        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
