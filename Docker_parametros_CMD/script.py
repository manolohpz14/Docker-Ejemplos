# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:24:25 2024

@author: manolo
"""
import sys
import os

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    persona = os.getenv("PERSONA", "false")

    if persona != "false":
        print("Script ejecutado por" + persona)

    if len(sys.argv) != 2:
        print("Por favor, proporciona un número como argumento.")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print("El" +str(n) + "número de Fibonacci es"+  str(fibonacci(n)))
        
        
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
        sys.exit(1)