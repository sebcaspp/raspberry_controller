from enum import Enum


class CurrentValues:
    def __init__(self, x:float, y:float, z:float, e:float, f:float ):
        self.x = x
        self.y = y
        self.z = z
        self.e = e 
        self.f = f
class G0Command:
    def __init__(self,x:float, y:float, z:float, e:float, f:float):
        self.x = x
        self.y = y
        self.z = z
        self.e = e    
        self.f = f
    
    def gcode_to_string(self):
        stringGcode="G0Command(x:"+str(self.x)+" "+"y:"+str(self.y)+" "+"z:"+str(self.z)+" "+"e:"+str(self.e)+" "+"f:"+str(self.f)+")"
        print(stringGcode)
        return stringGcode


class Direction(Enum):
    NEGATIVE = 1    
    POSITIVE = 2
    
class G1CommandHandler:    
   def execute(self, g1_command:G0Command, current_values: CurrentValues)-> CurrentValues:
        cordenadaNuevaX:float=0.0
        cordenadaNuevaY:float=0.0
        cordenadaNuevaZ:float=0.0
        cordenadaNuevaE:float=0.0
        cordenadaNuevaF:float=0.0        
        
        movimientoX:float=0.0
        movimientoY:float=0.0
        movimientoZ:float=0.0
        movimientoE:float=0.0
        movimientoF:float=0.0
 
        if g1_command.x != None:
            movimientoX=g1_command.x-current_values.x
            if movimientoX<0:
                dirX=Direction.NEGATIVE
                movimientoX=movimientoX*-1
            elif movimientoX>0:
                dirX=Direction.POSITIVE
            cordenadaNuevaX=g1_command.x
        else :
            cordenadaNuevaX = current_values.x

        if g1_command.y != None:
            movimientoY=g1_command.y-current_values.y
            if movimientoY<0:
                dirY=Direction.NEGATIVE
                movimientoY=movimientoY*-1
            elif movimientoY>0:
                dirY=Direction.POSITIVE
            cordenadaNuevaY=g1_command.y
        else:
            cordenadaNuevaY = current_values.y
        print(movimientoY)
        print(movimientoX)
        return CurrentValues(cordenadaNuevaX,cordenadaNuevaY,cordenadaNuevaZ,cordenadaNuevaE,cordenadaNuevaF)

cordenadaPasada=CurrentValues(12.0,12.0,13.0,14.0,15.0)
primerMovimiento=G0Command(12.0,13.0,14.0,15.0,16.0)

ddd=G1CommandHandler()
dd2=ddd.execute(primerMovimiento,cordenadaPasada)
print(dd2.y)