try:
    A = [0]*6
    B = [0]*5
    C = [0]*3

    print("Ingresar usuarios que ingresan desde la web: ")
    for i in range(6):
        A[i] = int(input())
    print("Ingresar usuarios que ingresan desde la API")
    for i in range(5):
        B[i] = int(input())
    print("Ingresar usuarios que generaron errores: ")
    for i in range(3):
        C[i] = int(input())
    print()
    print("CLASIFICACIÓN DE USUARIOS")
    #PRIMERAS REPETICIONES
    for i in range(6):
        diferentes_en_C = 0
        for j in range(3):
            if A[i] != C[j]:
                diferentes_en_C+=1            
        if diferentes_en_C==3:
            print(A[i], "= No critico")
        if diferentes_en_C<3:
            print(A[i], "= Critico")

    #SEGUNDAS REPETICIONES
    for i in range(5):
        diferentes_en_A=0
        for j in range(6):
            if B[i] != A[j]:
                diferentes_en_A+=1
        if diferentes_en_A==6:
            diferentes_en_C=0     
            for j in range(3):
                if B[i] != C[j]:
                    diferentes_en_C+=1
            if diferentes_en_C<3: 
                print(B[i], "= Critico")
            if diferentes_en_C==3:
                print(B[i], "= No critico")

    #TERCERAS REPETICIONES
    for i in range(3):
        diferentes_en_A=0
        diferentes_en_B=0
        for j in range(6):
            if C[i] != A[j]:
                diferentes_en_A+=1
        for j in range(5):
            if C[i] != B[j]:
                diferentes_en_B+=1
        if diferentes_en_A==6 and diferentes_en_B==5:
            print(C[i], "= No critico")
except ValueError:
    print("Error")
