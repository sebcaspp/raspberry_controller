
from controller.domain.gcode import GCode
from controller.domain.gxcode import G0Command, G1Command
from controller.infrastructure.gpio.gpio_control import *

class CurrentValues:
    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0, e:float=0.0, f:float=0.0 ):
        self.x = x
        self.y = y
        self.z = z
        self.e = e 
        self.f = f
class CommandHandler:
    def __init__(self, step_controller:StepMotorsController):
        self.step_controller = step_controller
        
        self.g1_command = G1CommandHandler(step_controller)
        self.g0_command = G0CommandHandler(step_controller)

    def handle_command(self, gcode:GCode, current_values: CurrentValues) -> CurrentValues:
        if isinstance(gcode, G1Command):
            return self.g1_command.execute(gcode, current_values)
        elif isinstance(gcode,G0Command):
            return self.g0_command.execute(gcode,current_values)
        else:
            pass     
            


class G1CommandHandler:    
    def __init__(self, step_controller:StepMotorsController):
        self.step_controller = step_controller        

    def execute(self, g1_command:G1Command, current_values: CurrentValues)-> CurrentValues:
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

        dirX = Direction.NEGATIVE
        if g1_command.x is not None:
            movimientoX = g1_command.x-current_values.x
            if movimientoX > 0:
                dirX = Direction.POSITIVE

            cordenadaNuevaX = g1_command.x
        else :
            cordenadaNuevaX = current_values.x

        dirY = Direction.NEGATIVE                        
        if g1_command.y is not None:
            movimientoY = g1_command.y - current_values.y
            if movimientoY > 0:
                dirY = Direction.POSITIVE

            cordenadaNuevaY = g1_command.y
        else:
            cordenadaNuevaY = current_values.y

        self.step_controller.execute_movement(dirX, abs(movimientoX), dirY, abs(movimientoY) )
        return CurrentValues(cordenadaNuevaX, cordenadaNuevaY, cordenadaNuevaZ, cordenadaNuevaE, cordenadaNuevaF)


class G0CommandHandler:    
    def __init__(self, step_controller:StepMotorsController):
        self.step_controller = step_controller        

    def execute(self, g0_command:G0Command, current_values: CurrentValues)-> CurrentValues:
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
        if g0_command.x != None:
            movimientoX=g0_command.x-current_values.x
            if movimientoX<0:
                dirX=Direction.NEGATIVE
                movimientoX=movimientoX*-1
            elif movimientoX>0:
                dirX=Direction.POSITIVE
            cordenadaNuevaX=g0_command.x
        else :
            cordenadaNuevaX = current_values.x

        if g0_command.y != None:
            movimientoY=g0_command.y-current_values.y
            if movimientoY<0:
                dirY=Direction.NEGATIVE
                movimientoY=movimientoY*-1
            elif movimientoY>0:
                dirY=Direction.POSITIVE
            cordenadaNuevaY=g0_command.y
        else:
            cordenadaNuevaY = current_values.y

        self.step_controller.execute_movement(dirX,movimientoX,dirY,movimientoY)
        return CurrentValues(cordenadaNuevaX,cordenadaNuevaY,cordenadaNuevaZ,cordenadaNuevaE,cordenadaNuevaF)

    