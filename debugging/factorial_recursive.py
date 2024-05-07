#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le factoriel d'un nombre donné de manière récursive.

    Parameters:
    n (int): Le nombre entier dont on veut calculer le factoriel. Doit être positif ou zéro.

    Returns:
    int: Le résultat du calcul factoriel de n. Si n est 0, la fonction retourne 1 (par définition du factoriel).

    Example:
    >>> factorial(4)
    24
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Récupérer le premier argument en ligne de commande comme entier
f = factorial(int(sys.argv[1]))
print(f)
