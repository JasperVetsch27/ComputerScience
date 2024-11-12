from adafruit_circuitplayground import cp
import time 

while True:
    if cp.light == 30:
        cp.pixels[0] = (1,1,1)
        time.sleep(1)
        cp.pixels[0] = (0,0,0)
    elif cp.light == 27:
        cp.pixels[0,1] = (1,1,1)
        time.sleep(1)
        cp.pixels[0,1] = (0,0,0)