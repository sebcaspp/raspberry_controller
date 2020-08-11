from controller.infrastructure.gpio.gpio_control import *
from controller.handler.command_handler  import *
from controller.transformers.gcode_transformers import transform_string_to_gcode as string_to_gcode

def main():

    gpio_controler_x = GpioControler(14,15)
    motor_x = StepMotor("X", gpio_controler_x)

    gpio_controler_y = GpioControler(23,24)
    motor_y = StepMotor("Y", gpio_controler_y)

    step_controller = StepMotorsController(motor_x, motor_y)

    current_values = CurrentValues()

    commandHandler = CommandHandler(step_controller)

    gcomands = [
        "G1 X90.6 Y13.8",
        "G1 X9.6 Y1.8",
        "G1 X90.6 Y13.8",
        "G1 X9.6 Y1.8",
        "G1 X90.6 Y13.8",    
        ]
    while True:
        for string_command in gcomands:
            command = string_to_gcode(string_command)
            if command is not None:
                print("command -> ", command.gcode_to_string())
                current_values = commandHandler.handle_command(command, current_values)
                print("current values -> ", current_values)


