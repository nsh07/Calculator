# https://github.com/NMrocks/Calculator
import tkinter as tk
from math import *

expression = ""


def summation(num):
    return sum(range(1, int(num) + 1))


def calculate():
    global expression, expression_field

    try:
        calculation = str(eval(expression.replace("abs", "fabs").replace("^", "**")))

        if len(calculation) > 10:
            length = len(calculation) - 1
            equation.set(str(eval(calculation[:4]) / 1000) + f"*10^{length}")
            expression = str(eval(expression))

        else:
            expression = str(calculation)
            equation.set(expression)

    except ZeroDivisionError:
        expression = ""
        equation.set(" Error: Can't divide by zero")

    except SyntaxError:
        try:
            expression = str(eval(expression_field.get()))
            equation.set(expression)

        except SyntaxError:
            equation.set(" Error")
            expression = ""

    except ValueError:
        equation.set(" Error")
        expression = ""


def press(num=None, arg=None):
    global expression

    if arg == "switch_symbol":
        if len(expression) >= 1:
            if expression[:2] == "-(" and expression[-1] == ")":
                expression = expression.lstrip("-(").rstrip(")")
                equation.set(expression)
            else:
                expression = f"-({expression})"
                equation.set(expression)
        else:
            expression = "-(" + expression
            equation.set(expression)

    if arg is None:
        expression = expression + str(num)

        if num != 0:
            expression = expression.lstrip("0.0")

        equation.set(expression)


def clear(arg=None):
    global expression

    if arg is None:  # If 'C' button is pressed
        expression = '0'

    else:  # If 'B' button is pressed
        if expression and expression != '0':
            expression = expression[:-1]

            if not expression:  # If entry field is empty then inserting '0'
                expression = '0'

    equation.set(expression)


font = ('Verdana', 16)

root = tk.Tk()
root.title("Calculator")
equation = tk.StringVar()
expression_field = tk.Entry(textvariable=equation, font=font)
expression_field.grid(row=2, column=1, columnspan=9, sticky="NSEW")
equation.set("0")

tk.Button(text="7", command=lambda: press(7), font=font, width=3).grid(row=3, column=1, sticky="NSEW")
tk.Button(text="8", command=lambda: press(8), font=font, width=3).grid(row=3, column=2, sticky="NSEW")
tk.Button(text="9", command=lambda: press(9), font=font, width=3).grid(row=3, column=3, sticky="NSEW")
tk.Button(text="+", command=lambda: press("+"), font=font, width=3).grid(row=3, column=4, sticky="NSEW")
tk.Button(text="-", command=lambda: press("-"), font=font, width=3).grid(row=3, column=5, sticky="NSEW")
tk.Button(text="±", command=lambda: press(arg="switch_symbol"), font=font, width=3).grid(row=3, column=6, sticky="NSEW")
tk.Button(text="sin", command=lambda: press("sin(radians("), font=font).grid(row=3, column=7, sticky="NSEW")
tk.Button(text="asin", command=lambda: press("asin(radians("), font=font).grid(row=3, column=8, sticky="NSEW")
tk.Button(text="yˣ", command=lambda: press("^"), font=font).grid(row=3, column=9, sticky="NSEW")

tk.Button(text="4", command=lambda: press(4), font=font, width=3).grid(row=4, column=1, sticky="NSEW")
tk.Button(text="5", command=lambda: press(5), font=font, width=3).grid(row=4, column=2, sticky="NSEW")
tk.Button(text="6", command=lambda: press(6), font=font, width=3).grid(row=4, column=3, sticky="NSEW")
tk.Button(text="×", command=lambda: press("*"), font=font, width=3).grid(row=4, column=4, sticky="NSEW")
tk.Button(text="÷", command=lambda: press("/"), font=font, width=3).grid(row=4, column=5, sticky="NSEW")
tk.Button(text="√", command=lambda: press("sqrt("), font=font, width=3).grid(row=4, column=6, sticky="NSEW")
tk.Button(text="cos", command=lambda: press("cos(radians("), font=font).grid(row=4, column=7, sticky="NSEW")
tk.Button(text="acos", command=lambda: press("acos(radians("), font=font).grid(row=4, column=8, sticky="NSEW")
tk.Button(text="•", command=lambda: press("."), font=font).grid(row=4, column=9, sticky="NSEW")

tk.Button(text="1", command=lambda: press(1), font=font, width=3).grid(row=5, column=1, sticky="NSEW")
tk.Button(text="2", command=lambda: press(2), font=font, width=3).grid(row=5, column=2, sticky="NSEW")
tk.Button(text="3", command=lambda: press(3), font=font, width=3).grid(row=5, column=3, sticky="NSEW")
tk.Button(text="=", command=calculate, font=font).grid(row=5, column=4, columnspan=2, sticky="NSEW")
tk.Button(text="(", command=lambda: press("("), font=font, width=3).grid(row=5, column=6, sticky="NSEW")
tk.Button(text="tan", command=lambda: press("tan(radians("), font=font).grid(row=5, column=7, sticky="NSEW")
tk.Button(text="atan", command=lambda: press("atan(radians("), font=font).grid(row=5, column=8, sticky="NSEW")
tk.Button(text="!", command=lambda: press("factorial("), font=font).grid(row=5, column=9, sticky="NSEW")

tk.Button(text="0", command=lambda: press(0), font=font, width=3).grid(row=6, column=1, columnspan=3, sticky="NSEW")
tk.Button(text="C", command=clear, font=font, width=3).grid(row=6, column=4, sticky="NSEW")
tk.Button(text="B", command=lambda: clear(True), font=font, width=3).grid(row=6, column=5, sticky="NSEW")
tk.Button(text=")", command=lambda: press(")"), font=font, width=3).grid(row=6, column=6, sticky="NSEW")
tk.Button(text="rad", command=lambda: press("radians("), font=font).grid(row=6, column=7, sticky="NSEW")
tk.Button(text="deg", command=lambda: press("degrees("), font=font).grid(row=6, column=8, sticky="NSEW")
tk.Button(text="sum", command=lambda: press("summation("), font=font).grid(row=6, column=9, sticky="NSEW")


root.mainloop()
