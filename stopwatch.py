#!/usr/bin/env python
# Stopwatch.
# version 0.1

import time

# Display the programs instructions
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

# upon input, or simply pressing ENTER, start the program
input()
print('Started')
# initialize start time and last time.
startTime = time.time()
lastTime = startTime
lapNum = 1

running = 1
try:
    # loop until interrupted
    while True:        
        # wait for input, to start new lap.
        input()
        # this gets laptime, subracting last time with current time. rounded off to 2 decimals
        lapTime = round(time.time() - lastTime, 2)
        # gets total time. subtracting startTime with current time. also rounded off
        totalTime = round(time.time() - startTime, 2)
        # shows results of last lap.
        print(f'Total time: {totalTime}, Lap #{lapNum}: {lapTime}')
        # increment laptime
        lapNum += 1
        # update lasttime
        lastTime = time.time()
    
except KeyboardInterrupt:
    # program exits on interruption Ctrl-C
    print('Exiting...')

