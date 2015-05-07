#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Andrea Centeno
Andrea Cutillas
Roberto Romero 10-10642
Equipo: PyTech
Suite de casos de prueba para Billetera electronica proyecto SAGE'''

import unittest
from billetera import *

class Test (unittest.TestCase):

    """TDD"""
    #Instancia de la clase billetera
    def testClaseBilletera(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno Lopez',20755110)
     
    #Letras en la cedula   
    def testLetrasEnCi(self):
        self.assertRaises(Exception,BilleteraElectronica,23,'123ABC','Andrea Victoria','Centeno Lopez','111y1111')
        
    #Acentos
    def testNombreAcento(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno López',20755110)
        
    #enies
    def testNombreEnies(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Jose','Patiño',20755110)
        
    #DIeresis
    def testNombreDieresis(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Jose','Pingüino',20755110)
    
    #FUNCION SALDO
    def testFuncionSaldo(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno Lopez',20755110)
        saldo = billetera.saldo()
        
    #FUNCION RECARGAR
    def testFuncionRecargar(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno Lopez',20755110)
        billetera.recargar(20,28/04/2015,1293)
        
    #credito negativo
    def testCreditoNegativo(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno Lopez',20755110)
        self.assertRaises(Exception,billetera.recargar,-2000,28/04/2015,1293)
        
    #FUNCION CONSUMIR
    def testFuncionConsumir(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno Lopez',20755110)
        self.assertRaises(Exception,billetera.consumir,20,28/04/2015,1293,'123ABC')
    
    #debito negativo   
    def testDebitoNegativo(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno Lopez',20755110)
        self.assertRaises(Exception,billetera.consumir,-2000,28/04/2015,1293,'123ABC')
        
    #verificar pin
    def testPinIgual(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno Lopez',20755110)
        self.assertRaises(Exception,billetera.consumir,2000,28/04/2015,1293,'123')
        
    #Consumo mayor al saldo que hay
    def testConsumoMayorASaldo(self):
        billetera = BilleteraElectronica(23,'123ABC','Andrea Victoria','Centeno Lopez',20755110)
        billetera.recargar(2000,28/04/2015,1293)
        self.assertRaises(Exception,billetera.consumir,2001,28/04/2015,1293,'123ABC')
                
    """CASOS BORDES"""
    #saldo = 0
    def testSaldoCero(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno Lopez',20755110)
        self.assertEqual(billetera.saldo(), 0, 'Saldo = 0')
        
    #monto a debitar igual al saldo 
    def testMontoIgualSaldo(self):
        billetera = BilleteraElectronica(23,'123ABC', 'Andrea Victoria','Centeno Lopez',20755110)
        try:
            billetera.recargar(2000,28/04/2015,1293)
            billetera.consumir(2000,28/04/2015,1293,'123ABC')  
        except: 
            self.fail("Resultado inesperado")
            
    #Campo de nombre vacio
    def testNombreVacio(self):
        self.assertRaises(Exception,BilleteraElectronica,23,'123ABC', '','Centeno Lopez',20755110)
        
    #Campo de apellido vacio
    def testApellidoVacio(self):
        self.assertRaises(Exception,BilleteraElectronica,23,'123ABC', 'Andrea Victoria','',20755110)
    
    #Campo de Pin vacio
    def testIdenVacio(self):
        self.assertRaises(Exception,BilleteraElectronica,23,'', 'Andrea Victoria','Centeno Lopez',20755110)
        
    """CASOS ESQUINAS"""
    #Campos vacios
    def testCamposVacios(self):
        self.assertRaises(Exception,BilleteraElectronica,23,'','','',20755110)
            
    """MALICIOSOS"""
    #Cedula negativa
    def testCiNegativa(self):
        self.assertRaises(Exception,BilleteraElectronica,23,'123ABC','Andrea Victoria','Centeno Lopez',-20755110)
     