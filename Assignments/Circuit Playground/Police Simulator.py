from adafruit_circuitplayground import cp
import time 

while True:
    cp.pixels.fill((0,0,1))
    cp.play_tone(500, .5)
    cp.pixels.fill((1,0,0))
    cp.play_tone(900, .5)