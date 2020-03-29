def fibonacci(n):
    """
    Calcula el fibonacci de n

    n int > 0

    return int n!
    """
    if n==0 or n==1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input('escribe un numero entero : '))
print(fibonacci(n))