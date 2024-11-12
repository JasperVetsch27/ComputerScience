from adafruit_circuitplayground import cp

while True:
    if cp.switch:
        for i in range(0,5):
            cp.pixels[i] = (0,1,0)
        for i in range(5,10):
            cp.pixels[i] = (0,0,0)
    else:
        for i in range(5,10):
            cp.pixels[i] = (0,1,0)
        for i in range(0,5):
            cp.pixels[i] = (0,0,0)