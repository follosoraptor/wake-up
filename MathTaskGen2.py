# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:28:50 2024

Math Generation Pt 2

@author: Sasha Folloso
"""

# Libraries
import numpy as np
import time
import threading

# Classes
class MathProblem:
    def __init__(self):
        self.currentTask = False
        self.op = rng.integers(1,3)
        if self.op == 1: # addition problem
            self.num1 = rng.integers(1,56)
            self.num2 = rng.integers(1,56)
            self.sol = self.num1 + self.num2
            print("Task: ", self.num1, "+", self.num2, "=", self.sol)
        elif self.op == 2: # multiplication problem
            self.num1 = rng.integers(1,13)
            self.num2 = rng.integers(1,13)
            self.sol = self.num1 * self.num2
            print("Task: ", self.num1, "*", self.num2, "=", self.sol)
    
    def generateProblem(self):
        """Generates a new math problem for the task."""
        self.op = rng.integers(1,3)
        if self.op == 1: # addition problem
            self.num1 = rng.integers(1,56)
            self.num2 = rng.integers(1,56)
            self.sol = self.num1 + self.num2
            print("Task: ", self.num1, "+", self.num2, "=", self.sol)
        elif self.op == 2: # multiplication problem
            self.num1 = rng.integers(1,13)
            self.num2 = rng.integers(1,13)
            self.sol = self.num1 * self.num2
            print("Task: ", self.num1, "*", self.num2, "=", self.sol)
            
# Functions


# Main Program
if __name__ == "__main__":
    # random number generation setup
    rng = np.random.default_rng()
    
    # generate math problems
    Task1 = MathProblem()
    Task2 = MathProblem()
    Task3 = MathProblem()
    
    alarm = True
    Task1.currentTask = True
    
    while alarm == True:
        # prompt task 1
        while Task1.currentTask == True:
            if Task1.op == 1:
                ans = input(f"Task 1: What is {Task1.num1} + {Task1.num2}? \n>> ")
            elif Task1.op == 2:
                ans = input(f"Task 1: What is {Task1.num1} * {Task1.num2}? \n>> ")
            if int(ans) == Task1.sol:
                print("That is correct!")
                Task1.currentTask = False
                Task2.currentTask = True
                break
            else:
                print("That isn't correct! Try again.")
                continue
        # prompt task 2
        while Task2.currentTask == True:
            if Task2.op == 1:
                ans = input(f"Task 2: What is {Task2.num1} + {Task2.num2}? \n>> ")
            elif Task2.op == 2:
                ans = input(f"Task 2: What is {Task2.num1} * {Task2.num2}? \n>> ")
            if int(ans) == Task2.sol:
                print("That is correct!")
                Task2.currentTask = False
                Task3.currentTask = True
                break
            else:
                print("That isn't correct! Try again.")
                continue
        # prompt task 3
        while Task3.currentTask == True:
            if Task3.op == 1:
                ans = input(f"Task 3: What is {Task3.num1} + {Task3.num2}? \n>> ")
            elif Task3.op == 2:
                ans = input(f"Task 3: What is {Task3.num1} * {Task3.num2}? \n>> ")
            if int(ans) == Task3.sol:
                print("That is correct!")
                Task3.currentTask = False
                break
            else:
                print("That isn't correct! Try again.")
                continue
        alarm = False
        print("The alarm has been shut off!")
        break
            
        
    
    
    


