from adafruit_circuitplayground import cp
import time
import random
a = 0
while True:
    if cp.button_a: 
        a += 1
        cp.pixels.fill((0,0,0))
        for i in range(a):
            cp.pixels[i] = (1,1,1)
        time.sleep(.5)

    if cp.button_b:
        a -= 1
        cp.pixels.fill((0,0,0))
        for i in range(a):
            cp.pixels[i] = (1,1,1)
        time.sleep(.5)