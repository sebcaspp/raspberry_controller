
from controller.domain.gcode import GCode
from controller.domain.gxcode import G0Command, G1Command
from controller.infrastructure.gpio.gpio_control import *

class CurrentValues:
    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0, e:float=0.0, f:float=0.0 ):
        self.x = x
        self.y = y

class CommandHandler:
    def __init__(self, step_controller:StepMotorsController):
        self.step_controller = step_controller
        
        self.g1_command = G1CommandHandler(step_controller)

    def handle_command(self, gcode:GCode, current_values: CurrentValues) -> CurrentValues:
        if isinstance(gcode, G1Command):
            return self.g1_command.execute(gcode, current_values)
        elif isinstance(gcode, G0Command):
            pass
        else:
            pass     
            


class G1CommandHandler:    
    def __init__(self, step_controller:StepMotorsController):
        self.step_controller = step_controller        

    def execute(self, g1_command:G1Command, current_values: CurrentValues)-> CurrentValues:
        pass

    