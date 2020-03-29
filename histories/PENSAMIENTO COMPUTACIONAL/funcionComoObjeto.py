def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
        resultado = f(numeros)
        return resultado

nums = 5

print(aplicar_operacion(multiplicar_por_dos, nums))
print(aplicar_operacion(sumar_dos, nums))