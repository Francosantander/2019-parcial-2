class Telefono ():
    def __init__(self):
        self.credito = 0
    def agregar_credito(self,credito):
        self.credito += credito
    def dial(self,numero):
        if len(numero) == 3:
            if numero[0] == '8' or numero [0] == '9' : #llamada gratis
                return True
            else: 
                return False
        elif len(numero) == 7:
            if self.credito < 10:
                return False
            else:
                self.credito -= 10
                return True
        elif numero[0] == '0' and numero[1] == '0' :
            if self.credito < 100:
                return False
            else:
                self.credito -= 100
                return True
        return False
         


        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
