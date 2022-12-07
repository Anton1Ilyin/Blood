import bloodFunctions as b
import time

start = time.time()

finish = start + 20

b.initSpiAdc()

array = []

while(time.time() < finish):
    array.append(b.getAdc())
    time.sleep(0.01)
 
b.save(array, start, finish)

b.deinitSpiAdc()