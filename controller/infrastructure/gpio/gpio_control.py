
from enum import Enum

class GpioControler:
    def __init__(self, pin_direccion:int, pin_step: int):
        pass

    def move_positive(self):
        pass

    def move_negative(self):
        pass


class Direction(Enum):
    NEGATIVE = 1    
    POSITIVE = 2
    

class StepMotor():
    def __init__(self, name:str, gpio_controler: GpioControler):
        self.name = str
    
    def move(self, direction: Direction, distance:int):
        pass


class StepMotorsController:
    def __init__(self, step_motor_x: StepMotor, step_motor_y: StepMotor ):
        self.step_motor_x = step_motor_x
        self.step_motor_y = step_motor_y

    def execute_movement(self, x_direction:Direction, x_distance:float, y_direction:Direction, y_distance:float):
        pass