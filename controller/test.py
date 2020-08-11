
from controller.infrastructure.gpio.gpio_control import GpioControler
from gpiozero import Button
import asyncio

is_pressed_button1 = False
is_pressed_button2 = False

async def test_button():
    global is_pressed_button1
    global is_pressed_button2
    
    button1 = Button(18)
    button2 = Button(24)    

    while True:
        if button1.is_pressed :
            is_pressed_button1 = True    
        else:
            is_pressed_button1 = False
        if  button2.is_pressed :
            is_pressed_button2 = True
        else:
            is_pressed_button2 = False
        await asyncio.sleep(0.01)

async def move_motor():
    global is_pressed_button1
    global is_pressed_button2    
    
    step_count = 0
    gpio_controler = GpioControler(14,15)
    i = True

    while True:
        step_count = 0    
        if i:
            while is_pressed_button1 is False:
                await gpio_controler.move_positive()
                step_count += 1        
            i = False        
            print("numero de pasos positivo -> ", step_count)
        else:
            while is_pressed_button2 is False:
                await gpio_controler.move_negative()
                step_count += 1            
            i = True
            print("numero de pasos negativo -> ", step_count)

    

    

async def test():
    await asyncio.gather(
                test_button(),
                move_motor()
            )
        
    
    