try:
    M=[[0]*3 for i in range(3)]  
    print("Ingrese los números de la matriz (ingresando los elemenos por fila de izquierda a derecha): ")
    for i in range(3):  
        for j in range(3):  
            M[i][j]=int(input())  
    for i in range(3):  
        suma=0  
        for j in range(3):  
            suma+=M[i][j]  
        prom=suma / 3  
        print("Promedio función", i+1, "=", prom)  
    for j in range(3):  
        suma=0 
        for i in range(3):  
            suma+=M[i][j]  
        prom=suma / 3  
        print("Promedio servidor", j+1, "=", prom)

    print()
    MT = [[0]*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            MT[i][j] = M[j][i]
    print("MATRIZ TRANSPUESTA: ")
    for i in range(3):
        for j in range(3):
            print(MT[i][j], end=" ")
        print()
except ValueError:
    print("Error")