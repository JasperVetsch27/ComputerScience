from adafruit_circuitplayground import cp
import time
import random
debounce_time = .5

while True:
    if cp.button_a:
        for i in range(random.randint(0,10)):
            cp.pixels[i] = (1,0,0)
        time.sleep(debounce_time)

    elif cp.button_b:
        cp.pixels.fill((0,0,0))