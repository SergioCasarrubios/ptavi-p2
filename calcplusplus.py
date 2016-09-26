#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

fichero = csv.reader(open(sys.argv[1]))
calculadora = calcoohija.CalculadoraHija()
funciones = {'suma': calculadora.suma, 'resta': calculadora.resta,
             'multiplica': calculadora.mult, 'divide': calculadora.divide}

for row in fichero:
    operacion = row[0]
    row = row[1:]
    result = int(row[0])
    row = row[1:]

    for dato in row:
        try:
            result = funciones[operacion](result, int(dato))
        except KeyError:
            sys.exit('Operación no definida.')
    print(result)
