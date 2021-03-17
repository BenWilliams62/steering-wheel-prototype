import datetime
# controls

class Control:

    # initialise
    def __init__(self, initial_gear = "n"):
        if initial_gear != "n" and (initial_gear > 8 or initial_gear < 0):
            initial_gear = 0
            print("gear out of range, starting in neutral")
        self.gear = initial_gear
        self.best_time = 0      # best time recorded
        self.start_time = 0     # start time for timer
        self.hold_time = None
    
    # handle all gear functions
    def shift(self, direction):

        # handle neutral
        if self.gear == "n":
            self.gear = 0

        # handle reverse
        if self.gear == "r":
            self.gear = -1
        
        # handle change
        if direction == "up":
            if self.gear < 8:
                self.gear += 1
                print("up shift: ", self.gear)
        elif direction == "down":
            if self.gear > 0:
                self.gear -= 1
                print("down shift: ", self.gear)
        elif direction == "neutral":
            self.gear = "n"
            print("neutral selected")
        elif direction == "reverse":
            if self.gear == "n" or self.gear == 0:
                self.gear = "r"
                self.hold_time = None
                print("reverse selected")
        
        
        # handle neutral
        if self.gear == 0:
            self.gear = "n" # set GUI to N
        
        if self.gear == -1:
            self.gear = "r" # set GUI to R

    # handle timing
    def timer(self):
        # handle start
        if self.start_time == 0:
            self.start_time = datetime.datetime.now()
        
        else:
            temp = datetime.datetime.now()
            lap = temp - self.start_time
            if self.best_time == 0 or lap < self.best_time:
                self.best_time = lap
                print(lap)
            self.start_time = temp
    
    # handle timer clearing
    def timer_reset(self):
        self.best_time = 0
        self.start_time = 0
        print("reset")

    # handle button that can be pressed or held
    def hold_function(self):
        self.hold_time = datetime.datetime.now()
    
    # handle release of a button to check if it was held for 3 seconds
    def release_function(self, function_press, function_hold, press_arg = None, hold_arg = None):
        temp = datetime.datetime.now()
        if temp - self.hold_time > datetime.timedelta(seconds = 3):
            function_hold(hold_arg)
        else:
            function_press(press_arg)

    # handle other functions e.g. differential, brake balance etc.