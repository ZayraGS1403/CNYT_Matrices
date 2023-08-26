def sumavec(v1, v2):
    c=[]
    if len(v1) == len(v2):
        for i in range(len(v1)):
           c.append(v1[i]+v2[i])
    else:
        c ="Vectores con tamaño diferente"
    return c

def inverso(v1):
    vector = []
    for k in range(len(v1)):
        vector.append(-1*v1[k])
    return vector

def multliescalar(k,v1):
    vector = []
    for i in range(len(v1)):
        vector.append(k * v1[i])
    return vector

def sumatriz(m1,m2):
    fil_a = len(m1)
    fil_b = len(m2)
    col_a = len(m1[0])
    col_b = len(m2[0])
    matriz = []
    if fil_a == fil_b and col_a == col_b:
        for i in range(fil_a):
            fila = []
            for j in range(col_a):
                fila.append(m1[i][j] + m2[i][j])
            matriz.append(fila)
    else:
        matriz = "Tamaños de matrices diferentes"
    return matriz

def inversamatriz(m1):
    fila = len(m1)
    colum = len(m1[0])
    for i in range(fila):
        for j in range(colum):
            m1[i][j] = (-1)*(m1[i][j])
    return m1

def multi_escalar_matriz(k,m1):
    fila = len(m1)
    colum = len(m1[0])
    for i in range(fila):
        for j in range(colum):
            m1[i][j] = k *m1[i][j]
    return m1

def transpuesta(m1):
    fila = len(m1)
    colum = len(m1[0])
    matriz = [[0 for i in range (fila)] for j in range (colum)]
    for i in range(fila):
        for j in range(colum):
            matriz[j][i] = m1[i][j]
    return matriz

def conjugada(m1):
    fila = len(m1)
    colum = len(m1[0])
    for i in range(fila):
        for j in range(colum):
            m1[i][j] = m1[i][j].conjugate()
    return m1
