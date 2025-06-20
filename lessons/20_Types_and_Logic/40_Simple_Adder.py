"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
window.withdraw()

# Hide the window, hint: use the withdraw method

# Ask the user for the first number 

num1 = simpledialog.askinteger("First number", "Pick a number")  

# Ask the user for the second number

num2 = simpledialog.askinteger("Second number", "Pick another number")

# Display the sum of the two numbers 

messagebox.showinfo("Sum", ("Sum of two number is " + str(num1 + num2)))

# Keep the window open

