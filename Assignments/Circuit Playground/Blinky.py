from adafruit_circuitplayground import cp

import time

while True:
    for i in range(0,10):
        cp.pixels[i] = (0,1,0)
    time.sleep(0.367)
    
    for i in range(0,10):
        cp.pixels[i] = (0,0,0)
    time.sleep(.367)
