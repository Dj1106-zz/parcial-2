# Parser descendente recursivo simple

tokens = []
pos = 0

def match(t):
    global pos
    if pos < len(tokens) and tokens[pos] == t:
        pos += 1
    else:
        raise Exception("Error sintactico")

# S -> id = E
def S():
    match('id')
    match('=')
    E()

# E -> T + E | T
def E():
    T()
    if pos < len(tokens) and tokens[pos] == '+':
        match('+')
        E()

# T -> id | num
def T():
    if pos < len(tokens) and tokens[pos] == 'id':
        match('id')
    elif pos < len(tokens) and tokens[pos] == 'num':
        match('num')
    else:
        raise Exception("Error en T")

# ------------------------
# PRUEBA
# ------------------------

tokens = ['id', '=', 'id', '+', 'num']

try:
    S()
    if pos == len(tokens):
        print("Cadena valida")
    else:
        print("Error: tokens restantes")
except:
    print("Cadena no valida")