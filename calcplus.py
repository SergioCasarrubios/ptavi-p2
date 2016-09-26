#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fichero = open(sys.argv[1], 'r')
calculadora = calcoohija.CalculadoraHija()
lineas = fichero.readlines()
funciones = {'suma': calculadora.suma, 'resta': calculadora.resta,
             'multiplica': calculadora.mult, 'divide': calculadora.divide}

for linea in lineas:
    datos = linea.split(',')
    operacion = datos[0]
    datos = datos[1:]
    datos[-1] = datos[-1][:-1]
    result = int(datos[0])
    datos = datos[1:]

    for dato in datos:
        try:
            result = funciones[operacion](result, int(dato))
        except KeyError:
            sys.exit('Operación no definida.')
    print(result)
