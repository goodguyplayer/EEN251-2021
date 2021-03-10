import RPi.GPIO as gpio
from time import sleep

# Configurar como modo BCM
gpio.setmode(gpio.BCM)

# Configura led como saida
gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.OUT)

# Aciona as saídas
print("Pin 17 - Low -- Turn led on")
gpio.output(17, gpio.LOW)
sleep(2)
print("Pin 27 - Low -- Turn led on")
gpio.output(27, gpio.LOW)
sleep(2)

print("Pin 17 - High -- Turn led off")
gpio.output(17, gpio.HIGH)
sleep(2)
print("Pin 27 - High -- Turn led off")
gpio.output(27, gpio.HIGH)
sleep(2)

# Desfaz modificações no GPIO
gpio.cleanup()

