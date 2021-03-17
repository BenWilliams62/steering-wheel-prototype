# steering wheel prototype

## description
This project is a logic test for an upcoming f1 steering wheel project.

For this CLI prototype, there is a key press listener, listening for presses that are mapped to functions such as change gear up or down, start or reset a timer. The functions.py file contains an object Controls. This object has all the controls available for the car: changing gear, timers, and has room for further functions. 

## how to use

- clone this repository
- install dependencies
> pip install datetime
> pip install time
> pip instal pynput
- run steering_wheel.py
> python steering_wheel.py

## License
Free and open to use if you're building a similar project

## Controls

u - shift up
d - shift down
t - start timer
c - clear timer
n - neutral
r - reverse (must be in neutral for this to work)
8 forward gears, 1 reverse gear
