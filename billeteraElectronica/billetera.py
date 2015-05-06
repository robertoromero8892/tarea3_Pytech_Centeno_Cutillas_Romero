'''
Andrea Centeno
Andrea Cutillas
Roberto Romero 10-10642
Equipo: PyTech
Billetera electronica proyecto SAGE'''
 
         
#clase billetera
class BilleteraElectronica(object):
    
    def __init__(self, pin, nombres, apellidos, ci):
        self.pin = pin
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.debitos = []
        self.creditos = []
        