'''
Andrea Centeno
Andrea Cutillas
Roberto Romero 10-10642
Equipo: PyTech
Billetera electronica proyecto SAGE'''
         
#clase billetera
class BilleteraElectronica(object):
    
    def __init__(self, iden, pin, nombres, apellidos, ci):
        self.iden = iden
        self.pin = pin
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.debitos = []
        self.creditos = []
        
        if not isinstance(ci, int):
            raise Exception("Solo se admiten numero en el campo cedula.")
        
#funcion que devuelve el saldo de la billetera      
    def saldo(self):