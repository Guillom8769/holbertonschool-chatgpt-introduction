#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Diminuer n pour éviter une boucle infinie
    return result

# Récupérer l'argument de ligne de commande
f = factorial(int(sys.argv[1]))
print(f)
