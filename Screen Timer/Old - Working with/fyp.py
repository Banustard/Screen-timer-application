from __future__ import print_function
from time import sleep
from random import random
from threading import Timer

print("Started program")
print("You are allicated "  " hours today") 
print("you have "  " hours remaining")

def hour():
    print("One Hour left!")

t = Timer(5.0, hour)
t.start()              # After 5 seconds, "One hour left!" will be printed

#sleep(5.0)
#if random() < 0.5:     # But half of the time
#     t.cancel()        # We might just cancel the timer
#     print('Canceling')
