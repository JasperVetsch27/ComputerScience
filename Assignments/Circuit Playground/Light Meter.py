from adafruit_circuitplayground import cp
import time 

while True:
    if cp.light > 30:
        light = 1
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 27:
        light = 2
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 24:
        light = 3
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 21:
        light = 4
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 18:
        light = 5
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 15:
        light = 6
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 12:
        light = 7
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 9:
        light = 8
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 6:
        light = 9 
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 3:
        light = 10
        for i in range(light):
            cp.pixels[i] = (1,1,1)
        for i in range(light,10):
            cp.pixels[i] = (0,0,0)