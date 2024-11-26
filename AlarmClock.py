# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:22:46 2024

Task Oriented Alarm Clock!

@author: Sasha Folloso
"""

# Libraries
import numpy as np
import time
import threading
import datetime
import RPi.GPIO as GPIO
from time import sleep
from rpi_lcd import LCD
from signal import signal, SIGTERM, SIGHUP, pause
from pynput.keyboard import Key, Listener
# import pydub
# from pydub import AudioSegment
# from pydub.playback import play

global keyPress

# Classes
class MathProblem:
    def __init__(self):
        self.currentTask = False
        self.generateProblem()
            
    def generateProblem(self):
        """Generates a new math problem for the task."""
        self.op = rng.integers(1,3)
        if self.op == 1: # addition problem
            self.num1 = rng.integers(1,56)
            self.num2 = rng.integers(1,56)
            self.sol = self.num1 + self.num2
            self.str = "%d + %d?" % (self.num1, self.num2) # convert to string that can be printed on lcd
            print("Task: ", self.num1, "+", self.num2, "=", self.sol)
        elif self.op == 2: # multiplication problem
            self.num1 = rng.integers(1,13)
            self.num2 = rng.integers(1,13)
            self.sol = self.num1 * self.num2
            self.str = "%d * %d?" % (self.num1, self.num2) # convert to string that can be printed on lcd
            print("Task: ", self.num1, "*", self.num2, "=", self.sol)
            
            
class AlarmConfig:
    def setSound(songFile:str):
        """Allows user to change sound of the alarm with choice of .wav file"""
        pass
    def setTime():
        """Allows user to set the time in which the alarm should sound"""
        pass
            
# Functions
def safe_exit(signum, frame):
    exit(1)

def alarmWaitingMsg():
    """Displays text to LCD during time between alarm sounding and initial user input"""
    for x in range(6):
        lcd.text("    WEE WOO!",1)
        lcd.text("    WEE WOO!",2)
        sleep(.5)
        lcd.clear()
        sleep(.5)
    lcd.text("  It's time to", 1)
    lcd.text("    WAKE UP!",2)
    sleep(2)
    lcd.text("     GET UP!",2)
    sleep(2)
    lcd.text(" GET OUT THERE!",2)
    sleep(2)
    
def alarmOffMsg():
    lcd.clear()
    lcd.text("Alarm is now",1)
    lcd.text("shut off!",2)
    sleep(2)
    lcd.text("The day is",1)
    lcd.text("all yours",2)
    sleep(2)
    lcd.text("Have a great day!",1)
    lcd.text(":D",2)
    sleep(2)
    
def userInput(key):
    """Detects for spacebar input."""
    if key == Key.space:
        global keyPress
        keyPress = True
        return False
        
def stopUserInput(key): #works fine
    """Stops listening for user inputs when Esc is pressed."""
    if key == Key.esc:
        return False
    
def listenForInput(): #works fine
    """Enables input monitoring."""
    with Listener(on_press=userInput, on_release=stopUserInput) as listener:
        listener.join()

def initGPIO():
    """Initializes GPIO pins with keypad module."""
    global R1, R2, R3, R4, C1, C2, C3, C4
    R1 = 25 # ROW 1 = PIN 25
    R2 = 8  # ROW 2 = PIN 8
    R3 = 7  # ROW 3 = PIN 7
    R4 = 1  # ROW 4 = PIN 1

    C1 = 12 # COLUMN 1 = PIN 12
    C2 = 16 # COLUMN 2 = PIN 16
    C3 = 20 # COLUMN 3 = PIN 20
    C4 = 21 # COLUMN 4 = PIN 21
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)
    GPIO.setup(R3, GPIO.OUT)
    GPIO.setup(R4, GPIO.OUT)
    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def keypadInput(text:list):
    for row in [R1, R2, R3, R4]:
        
        if text == None:
            text = []
        GPIO.output(row, GPIO.HIGH)
        
        if(GPIO.input(C1) == 1):
            if row == R1:   # "1" KEY
                print(f"You pressed 1!")
                text.append("1")
                print(text)
            elif row == R2: # "4" KEY
                print(f"You pressed 4!")
                text.append("4")
                print(text)
            elif row == R3: # "7" KEY
                print(f"You pressed 7!")
                text.append("7")
                print(text)
            elif row == R4: # "*" KEY
                print(f"You pressed *! (Clear All)")
                text.clear()
                print(text)
        elif(GPIO.input(C2) == 1):
            if row == R1:   # "2" KEY
                print(f"You pressed 2!")
                text.append("2")
                print(text)
            elif row == R2: # "5" KEY
                print(f"You pressed 5!")
                text.append("5")
                print(text)                
            elif row == R3: # "8" KEY
                print(f"You pressed 8!")
                text.append("8")
                print(text)
            elif row == R4: # "0" KEY
                print(f"You pressed 0!")
                text.append("0")
                print(text)
        elif(GPIO.input(C3) == 1):
            if row == R1:   # "3" KEY
                print(f"You pressed 3!")
                text.append("3")
                print(text)
            elif row == R2: # "6" KEY
                print(f"You pressed 6!")
                text.append("6")
                print(text)
            elif row == R3: # "9" KEY
                print(f"You pressed 9!")
                text.append("9")
                print(text)
            elif row == R4: # "#" KEY
                print(f"You pressed #! (Enter)")
                text.append("#")
        elif(GPIO.input(C4) == 1):
            if row == R1:   # "A" KEY
                print(f"You pressed A! (Backspace)")
                if text:
                    text.pop()
                print(text)
            elif row == R2: # "B" KEY
                print(f"You pressed B! (Backspace)")
                if text:    
                    text.pop()
                print(text)
            elif row == R3: # "C" KEY
                print(f"You pressed C! (Backspace)")
                if text:    
                    text.pop()
                print(text)
            elif row == R4: # "D" KEY
                print(f"You pressed D! (Backspace)")
                if text:
                    text.pop()
                print(text)
        GPIO.output(row, GPIO.LOW)
    return text

def taskSolved(task, lcd): # False: Not solved // True: correctly solved
    """Handles verification of keypad input for math task."""
    text = [] # stores text from keypad input
    while task.currentTask == True:
        text = keypadInput(text)
        user_input = "".join(text).replace("#", "") # removes # from string output on lcd
        lcd.text(f"What is {task.str}",1)
        lcd.text(f"Answer: {user_input}",2)
        sleep(.3)
        
        if "#" in text: # detects if # (Enter) has been pressed)
            try:
                    if int(user_input) == task.sol:
                        task.currentTask = False
                        lcd.text("That is correct!",1)
                        lcd.text("",2)
                        sleep(1)
                        lcd.clear()
                        return True
                    else:
                        lcd.text("Incorrect!",1)
                        lcd.text("Please try again!",2)
                        sleep(1)
                        lcd.clear()
            except ValueError:
                    lcd.text("Invalid input!",1)
                    sleep(1)
                    lcd.clear()
            text.clear() # clears lcd after submission

# Main Program
if __name__ == '__main__':
    # Keypad Setup and Initialization
    initGPIO()   
    
    # RNG Initialization
    rng = np.random.default_rng()
    
    # LCD Display Initialization
    lcd = LCD()
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    
    # Math Problem Generation
    task1 = MathProblem()
    task2 = MathProblem()
    task3 = MathProblem()
    
    # alarm config
    # enter_c = input(f"Would you like to set the sound for your alarm? Type 'Y' or 'N'\n>>")
    
    global keyPress
    
    keyPress = False
    alarm:bool = True
    waitingOnUser:bool = True
    userHere:bool = False
    taskPrinted:bool = False # used so text isn't constantly being printed to lcd screen in while()
    taskComplete:bool = False
    
    while alarm == True:     
        while waitingOnUser == True: # waiting on user to verify they are physically there
            listener = Listener(on_press=userInput, on_release=stopUserInput)
            listener.start()
            if keyPress == True:
                waitingOnUser = False
                task1.currentTask = True
                listener.stop()  # Stop the listener once the condition is met
                break
            alarmWaitingMsg()
            sleep(.1)    
            
        while task1.currentTask == True: # STARTS FIRST TASK
            if not taskSolved(task1,lcd):
                break
            task2.currentTask = True
        
        while task2.currentTask == True: # STARTS SECOND TASK
            if not taskSolved(task2,lcd):
               break
            task3.currentTask = True
        
        while task3.currentTask == True: # STARTS THIRD TASK
            if not taskSolved(task3,lcd):
                break
            alarm = False
            
    print(f"Alarm has been turned off!")
    alarmOffMsg()                                                                  