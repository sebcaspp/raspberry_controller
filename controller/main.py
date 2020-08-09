from controller.infrastructure.gpio.gpio_control import *



gpio_controler_x = GpioControler(14,15)
motor_x = StepMotor("X", gpio_controler_x)

gpio_controler_y = GpioControler(16,17)
motor_y = StepMotor("Y", gpio_controler_y)