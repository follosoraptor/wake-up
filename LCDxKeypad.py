# Trying to figure out how to use Keypad and LCD screen together

# Libraries
import numpy as np
import time
import keyboard
import RPi.GPIO as GPIO
from keyboard import send
from rpi_lcd import LCD
from signal import signal, SIGTERM, SIGHUP, pause


# Functions
def safeExit(signum, frame):
    exit(1)
    
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

def enterKeyHandler():
    """Simulates 'enter' key via a keystroke on the keypad module."""
    pass

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
                enterKeyHandler()
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
    
def main():
    signal(SIGTERM, safeExit)
    signal(SIGHUP, safeExit)
    initGPIO()
    lcd = LCD()
    lcd_text:list = []
    print(lcd_text)
    current_text:str = ""
    new_text:str = ""
    
    while True:
        lcd_text = keypadInput(lcd_text)
        new_text = "".join(lcd_text)
        if current_text != new_text:
            lcd.text(str(new_text), 1)
            current_text = new_text
            
        time.sleep(.4)
        

# Main Program
if __name__ == "__main__":
    main()
    