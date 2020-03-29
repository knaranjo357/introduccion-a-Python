#buscar la mejor solucion algoritmica para un problema
#conocer el tiempo que se demora un algoritmo
#espacio en memoria

import time

def factorial(n):
    respuesta=1

    while n>1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

if __name__=='__main__':
    n=200000

    comienzo = time.time()
    factorial(n)
    #print(factorial(n))
    final = time.time()
    print(final-comienzo)

    comienzo = time.time()
    factorial_r(n)

    #print(factorial_r(n))
    final = time.time()
    print(final-comienzo)
    

