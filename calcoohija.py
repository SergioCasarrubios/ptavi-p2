#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):
    def mult(self, op1, op2):
        return op1 * op2
    
    def divide(self, op1, op2):
        try:
            return op1 / op2 
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")        

if __name__ == "__main__":
    
    calculadora = CalculadoraHija()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    
    if sys.argv[2] == 'suma':
        result = calculadora.suma(operando1, operando2)
    elif sys.argv[2] == 'resta':
        result = calculadora.resta(operando1, operando2)
    elif sys.argv[2] == 'multiplica':
        result = calculadora.mult(operando1, operando2)
    elif sys.argv[2] == 'divide':
        result = calculadora.divide(operando1, operando2)
    else:
        sys.exit('Operación no definida.')
        
    print(result)
