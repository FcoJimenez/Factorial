print("\nFACTORIAL DE UN NUMERO")
print("\n Este programa calcula el factorial de un número")
print("\n -----------------------------------------------")
# ---------------------------
# Autor: Francisco Jiménez A.

# Definimos la variable
num = 4

# Definimos la función factorial(n), donde «n» es el número 
# al que se le calculará su factorial
def factorial(n):
    # Cuando 'n' sea equivalente a 0 (n == 0), entonces retornará 1. Si tomamos en cuenta 
    # que por convenio 0! es equivalente a 1, entonces se multiplicará por el resto.

    # Es decir: el factorial 4! = 4 x 3 x 2 x 1  = 24, pero si llega a 0, entonces seguirá
    # siendo 24.
    if n == 0:
        return 1

    # Si el usuario ha ingresado un valor negativo
    elif n < 0:
        return (n * factorial(-n - 1))

    # Mientras no sea cero (0) realizará una operación matemática de tipo recursiva.
    else:
        return n * factorial(n - 1)


x = factorial(num)
print(x); # 24
