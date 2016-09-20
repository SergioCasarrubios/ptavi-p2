#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
    
    def suma(self, op1, op2):
        return op1 + op2 
    
    def resta(self, op1, op2):
        return op1 - op2

if __name__ == "__main__":
    
    calculadora = Calculadora()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    
    if sys.argv[2] == 'suma':
        result = calculadora.suma(operando1, operando2)
    elif sys.argv[2] == 'resta':
        result = calculadora.resta(operando1, operando2)
    else:
        sys.exit('La operación solo puede ser <suma> y <resta>')
    
    print(result)
