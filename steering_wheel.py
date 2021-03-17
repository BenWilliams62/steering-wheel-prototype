from functions import Control
import time
from pynput import keyboard
import datetime

def main():

    print("Controls:\n")
    print("u to upshift")
    print("d to downshift")
    print("n for neutral")
    print("n (hold) for reverse")
    print("t to start timer")
    print("c to reset the timer")
    print("esc to turn car off")

    print("\ncar started\n")

    # intiate the car
    car = Control()

    def on_press(key):
        
        # quick press only
        if key == keyboard.Key.esc:
            return False
        if key.char == "u":
            car.shift("up")
        elif key.char == "d":
            car.shift("down")
        elif key.char == "t":
            car.timer()
        elif key.char == "c":
            car.timer_reset()
        elif key.char == "n":
            car.shift("neutral")
        elif key.char == "r":
            car.shift("reverse")
        elif key.char == "f":
            return False

    def on_release(key):
        if key == keyboard.Key.esc:
            return False
        elif key.char == "f":
            # Stop listener
            return False

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    del car

    print("car stopped")
    return False
    


if __name__ == "__main__":
    main()