from gpiozero import OutputDevice as OutPut
from enum import Enum
import asyncio

class GpioControler:
    def __init__(self, pin_direccion:int, pin_step: int):
        self.sleep_time = 0.0001
        self.out_direction:OutPut = OutPut(pin_direccion)
        self.out_step:OutPut      = OutPut(pin_step)

    async def move(self):
        self.out_step.on()
        await asyncio.sleep(self.sleep_time)
        self.out_step.off()
        await asyncio.sleep(self.sleep_time)

    async def move_positive(self):
        self.out_direction.on()
        await self.move()

    async def move_negative(self):
        self.out_direction.off()
        await self.move()


class Direction(Enum):
    NEGATIVE = 1    
    POSITIVE = 2
    

class StepMotor():
    def __init__(self, name:str, gpio_controler: GpioControler):
        self.mm_by_step = 1
        self.name = name
        self.gpio_controler = gpio_controler
    
    async def move(self, direction: Direction, distance:float):
        if distance == 0:
            return

        #TODO: calcular los pasos del motor para lacanzar una presicion adecuada, esto debe ser un entero, pero no ser calculado asi
        number_of_steps = int(distance/self.mm_by_step)

        print("nombre motor -> ", self.name)
        print("numero pasos -> ", number_of_steps)
        print("distance -> ", distance)

        if direction is Direction.NEGATIVE:
            for i in range(0,number_of_steps):
                await self.gpio_controler.move_negative()
        else:
            for i in range(0,number_of_steps):
                await self.gpio_controler.move_positive()


class StepMotorsController:
    def __init__(self, step_motor_x: StepMotor, step_motor_y: StepMotor ):
        self.step_motor_x = step_motor_x
        self.step_motor_y = step_motor_y

    async def f(self, x_direction:Direction, x_distance:float, y_direction:Direction, y_distance:float):
        await asyncio.gather(
                self.step_motor_x.move(x_direction, x_distance),
                self.step_motor_y.move(y_direction, y_distance)
            )

    def execute_movement(self, x_direction:Direction, x_distance:float, y_direction:Direction, y_distance:float):
        asyncio.run( self.f(x_direction, x_distance, y_direction, y_distance) )