'''
Andrea Centeno
Andrea Cutillas
Roberto Romero 10-10642
Equipo: PyTech
Suite de casos de prueba para Billetera electronica proyecto SAGE'''

import unittest
from billetera import *

class Test (unittest.TestCase):

    #Instancia de la clase billetera
    def testClaseBilletera(self):
        billetera = BilleteraElectronica('123ABC', 'Andrea Victoria','Centeno Lopez',20755110)