def factorial(n):
    """Calcula el factorial de n.

    Args:
        n (int): Número a conseguir su factorial
    """

    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(int(input('Escribe un entero: '))))
