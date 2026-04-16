# Algoritmo CYK simple

def cyk(cadena, G, start):
    n = len(cadena)
    tabla = [[set() for _ in range(n)] for _ in range(n)]

    # Inicialización
    for i in range(n):
        for A in G:
            for regla in G[A]:
                if regla == cadena[i]:
                    tabla[i][i].add(A)

    # Llenado de la tabla
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for A in G:
                    for regla in G[A]:
                        if isinstance(regla, tuple) and len(regla) == 2:
                            B, C = regla
                            if B in tabla[i][k] and C in tabla[k + 1][j]:
                                tabla[i][j].add(A)

    return start in tabla[0][n - 1]


# ------------------------
# PRUEBA
# ------------------------

# Gramática en Forma Normal de Chomsky
G = {
    'S': [('A', 'B')],
    'A': ['a'],
    'B': ['b']
}

cadena = "ab"

if cyk(cadena, G, 'S'):
    print("Cadena válida")
else:
    print("Cadena no válida")