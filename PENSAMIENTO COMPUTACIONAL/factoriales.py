def factorial(n):
    """
    Calcula el factorial de n

    n int > 0

    return n!
    """
    if n==1:
        return 1
    
    return n * factorial(n-1)

n = int(input('escribe un numero entero : '))

print(factorial(n))