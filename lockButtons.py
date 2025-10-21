# import nessesary modules
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)   # set mode to use pin numbering on breadboard to connect 
GPIO.setwarnings(False)

# setup button pins
BUTTON_RED_PIN = 6
GPIO.setup(BUTTON_RED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

BUTTON_YELLOW_PIN = 19
GPIO.setup(BUTTON_YELLOW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

BUTTON_BLUE_PIN = 4
GPIO.setup(BUTTON_BLUE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

BUTTON_WHITE_PIN = 17
GPIO.setup(BUTTON_WHITE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# setup pin for magnetic lock
RELAY_PIN = 12
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.HIGH)

# setup nessesary variables
buttons_pressed = []   # stores the currrent order of buttons a user has pressed
count = 0   # stores how many buttons the user has currently pressed
correct_puzzle = ["a", "b", "c", "d"]   # stores correct button order
last_button_time = 0   # stores the last time a button was pressed

# program will run until interrupted
try:
    while True:
        time.sleep(.25)
        # checks if the red button (Button 'a') was pressed
        if GPIO.input(BUTTON_RED_PIN) == GPIO.LOW:
            last_button_time = time.time()   # resets the time since a button was last pressed
            buttons_pressed.append("a")
            count += 1
            print("Button A pressed")
            time.sleep(.25)
            print(buttons_pressed)
        # checks if the yellow button (Button 'b') was pressed
        elif GPIO.input(BUTTON_YELLOW_PIN) == GPIO.LOW:
            last_button_time = time.time()   # resets the time since a button was last pressed
            buttons_pressed.append("b")
            count += 1
            print("Button B pressed")
            time.sleep(.25)
            print(buttons_pressed)
        # checks if the blue button (Button 'c') was pressed
        elif GPIO.input(BUTTON_BLUE_PIN) == GPIO.LOW:
            last_button_time = time.time()   # resets the time since a button was last pressed
            buttons_pressed.append("c")
            count += 1
            print("Button C pressed")
            time.sleep(.25)
            print(buttons_pressed)
        # checks if the white button (Button 'd') was pressed
        elif GPIO.input(BUTTON_WHITE_PIN) == GPIO.LOW:
            last_button_time = time.time()   # resets the time since a button was last pressed
            buttons_pressed.append("d")
            count += 1
            print("Button D pressed")
            time.sleep(.25)
            print(buttons_pressed)
        
        # checks if the four buttons have been presssed
        # and if the buttons pressed so far are in the correct order
        if count == 4 and buttons_pressed == correct_puzzle:
            GPIO.output(RELAY_PIN, GPIO.LOW)
            os.system("python3 /home/liams/pi_code_correct.py Correct")   # path should be changed
        # checks if the four buttons have been presssed
        # and if the buttons pressed so far are not in the correct order
        elif count == 4 and buttons_pressed != correct_puzzle:
            buttons_pressed = []   # resets the variable storing the buttons pressed so far the user
            count = 0    # resets the variable storing the number of buttons pressed so far
            os.system("python3 /home/liams/pi_code_incorrect.py Incorrect")   # path should be changed
        
        # checks if it's been 10 seconds since any buttons were last pressed
        if (last_button_time - time.time()) < -10:
            buttons_pressed = []   # resets the variable storing the buttons pressed so far the user
            count = 0    # resets the variable storing the number of buttons pressed so far
                
except KeyboardInterrupt:
    GPIO.cleanup()   # turn off all power to the GPIO pins
