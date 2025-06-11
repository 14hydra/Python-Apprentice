"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules

from tkinter import simpledialog, messagebox, Tk

# Create a window object

window = Tk()
window.withdraw()

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

num1 = simpledialog.askinteger("First number", "Pick a number")

# Ask the user for the second number

num2 = simpledialog.askinteger("Second number", "Pick another number")

# Ask the user for the math operation

operation = simpledialog.askstring("Operation", "Pick an operation")

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

result = 0

if (operation == "plus"):
   result = num1 + num2
elif (operation == "minus"):
   result = num1 - num2
elif (operation == "times"):
   result = num1 * num2
elif (operation == "divide"):
   result = num1 / num2
else:
   messagebox.showerror()


# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
messagebox.showinfo("Result", ("The result is " + str(result)))
# Keep the window open
