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
     
    #Letras en la cedula   
    def testLetrasEnCi(self):
        self.assertRaises(Exception,BilleteraElectronica,'123ABC','Andrea Victoria','Centeno Lopez','111y1111')
        
    #Acentos
    def testNombreAcento(self):
        billetera = BilleteraElectronica('123ABC', 'Andrea Victoria','Centeno López',20755110)
        self.fail("No acepta acentos")
    
     