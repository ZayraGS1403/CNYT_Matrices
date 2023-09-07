# CNYT_Espacio Vectorial
## Segunda entrega librerías 
### Por medio de un archivo en Pyhton se desarrollaron 8 librerías de opreaciones entre vectores y matrices.
### Trabajo realizado por Zayra Gutiérrez
Para ejecutar estos archivos es necesario tener la biblioteca numpy, ya que este proyecto la utiliza. El propósito de esta biblioteca es explorar conceptos relacionados con espacios vectoriales y sus operaciones, además de llevar a cabo su implementación en un lenguaje de programación. En total, la biblioteca consta de 15 funciones."
librerías realizadas:
1. Adición de vectores complejos.
2. Inverso de un vector complejos.
3. Multiplicación de un escalar por un vector complejo.
5. Adición de matrices complejas.
6. Inversa de una matriz compleja.
7. Multiplicación de un escalar por una matriz compleja.
8. Transpuesta de una matriz/vector
9. Conjugada de una matriz/vector
10. Adjunta (daga) de una matriz/vector
11. Producto de dos matrices (de tamaños compatibles)
12. Producto interno de dos vectores
13. Norma de un vector
14. Distancia entre dos vectores
15. Valores  y vectores propios de una matriz
Un ejemplo de las funciones sería:
3.
def multliescalar(k,v1):
    vector = []
    for i in range(len(v1)):
        vector.append(k * v1[i])
    return vector
La cual realiza la operacion de un escalar con un vector.

14.
def distancia(v1, v2):
    h = sumavec(v1, inverso(v2))
    dis = vectornormal(h)
    return dis
Calcula la distancia entre dos vectores.

Además de este archivo, abrá otro archivo de test que verificará si las funciones de la librería funcionan adecuadamente.
