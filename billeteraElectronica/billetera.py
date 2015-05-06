'''
Andrea Centeno
Andrea Cutillas
Roberto Romero 10-10642
Equipo: PyTech
Billetera electronica proyecto SAGE'''
 
#clase transaccion
class transaccion(object):
    
    def __init__(self,monto, fecha, idem):
        self.monto = monto
        self.fecha = fecha
        self.id = idem
                
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
        suma_debitos = 0
        suma_creditos = 0
        
        #se suman todos las recargas realizadas
        for i in range(len(self.debitos)):
            suma_debitos += self.debitos[i].monto
            
        #se suman todos los consumos realizados
        for j in range(len(self.creditos)):
            suma_creditos += self.creditos[j].monto
            
        #se restan las recargas menos los consumos para obtener el saldo    
        total = suma_creditos - suma_debitos      
        
        return total
    
#funcion para recargar el saldo de la billetera      
    def recargar(self,monto,fecha,iden):
        if monto < 0:
            raise Exception("No se admiten recargas negativas.")
        else:
            new_credito = transaccion(monto,fecha,iden)
            self.creditos.append(new_credito)