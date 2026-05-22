valores=[0]*9
print("COMPARACION DE PLANES")
print()
print("Ingrese los valores en X: ")
for i in range(9):
    valores[i]=int(input())

for i in range(9):
    x = valores[i]
    A = 40 * x + 200
    B = 70 * x + 50
    C = -2 * (x * x) + 80 * x + 100
    print("x =", x)
    print("Plan A =", A)
    print("Plan B =", B)
    print("Plan C =", C)

    if A == B and A < C:
        print("Planes mas economicos: A y B")
    elif A < B and A < C:
        print("Plan mas economico: A")
    elif B < A and B < C:
        print("Plan mas economico: B")
    elif C < 0:
        print("El Plan C tiene costo negativo")
        print("No tiene sentido en un caso real")
        if A < B:
            print("Plan mas economico: A")
        else:
            print("Plan mas economico: B")
    else:
        print("Plan mas economico: C")
    print()

matriz = [[" "] * 60 for i in range(20)]

for x in range(20):
    y = 19 - x
    if y >= 0:
        matriz[y][x * 2] = "A"

for x in range(20):
    y = 19 - x
    if y >= 0 and x + 15 < 60:
        matriz[y][x + 15] = "B"

for x in range(20):
    y = ((x - 10) * (x - 10)) // 10
    y = y + 11
    if y < 20 and x + 35 < 60:
        matriz[y][x + 35] = "C"
print()
print("GRAFICO EN CONSOLA")
print()
for fila in range(20):
    for columna in range(60):
        print(matriz[fila][columna], end="")
    print()
print()
print("A = Plan A")
print("B = Plan B")
print("C = Plan C")