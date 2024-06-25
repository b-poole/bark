#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:48:01 2024

@author: barrettpoole14
"""
import time

while True:
    try:
        countdown = int(input("Please enter countdown timer, in seconds: "))
        break
    except ValueError:
        print("Invalid input, please enter a number.")
    finally:
        time.sleep(0.1)

for i in range(0, countdown):
    print(str(countdown) + " seconds left!")
    time.sleep(1)
    countdown -= 1

print("Countdown over!")
