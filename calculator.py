# https://github.com/NMrocks/Calculator
import tkinter as tk
from math import *
expression = ""

def calculate():
	def summation(num):
		summ = list(range(int(num) + 1))
		summ = sum(summ)
		return summ
	global expression, expression_field
	try:
		if len(str(eval(expression.replace("abs", "fabs").replace("^", "**")))) > 10:
			length = len(str(eval(expression.replace("abs", "fabs").replace("^", "**")))) - 1
			equation.set(str(eval(str(eval(expression.replace("abs", "fabs").replace("^", "**")))[:4])/1000) + f"*10^{length}")
			expression = str(eval(expression))
		else:
			expression = str(eval(expression.replace("abs", "fabs").replace("^", "**")))
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

	#finally:
	#	equation.set(" Error: Syntax Error")
	#	expression = ""

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
	
	if arg == None:
		expression = expression + str(num)
		if num != 0:
			expression = expression.lstrip("0.0") 
		equation.set(expression)


def clear(arg = None):
	global expression
	if arg == None:
		expression = ""
		equation.set(expression)

	if arg:
		if len(expression) > 2:
			expression = expression[:-1]
			equation.set(expression)
		elif len(expression) == 2:
			expression = expression[0]
			equation.set(expression)
		else:
			clear()


#def display():
#	global display_expression, expression
#	display_expression.config(text=expression)


root = tk.Tk()
root.title("Calculator")
equation = tk.StringVar() 
expression_field = tk.Entry(textvariable=equation, font=("Verdana", 16)) 
expression_field.grid(row=2, column=1, columnspan=9, sticky="NSEW")
equation.set("0")
tk.Button(text="7", command=lambda: press(7), font=("Verdana", 16), width=3).grid(row=3, column=1, sticky="NSEW")
tk.Button(text="8", command=lambda: press(8), font=("Verdana", 16), width=3).grid(row=3, column=2, sticky="NSEW")
tk.Button(text="9", command=lambda: press(9), font=("Verdana", 16), width=3).grid(row=3, column=3, sticky="NSEW")
tk.Button(text="4", command=lambda: press(4), font=("Verdana", 16), width=3).grid(row=4, column=1, sticky="NSEW")
tk.Button(text="5", command=lambda: press(5), font=("Verdana", 16), width=3).grid(row=4, column=2, sticky="NSEW")
tk.Button(text="6", command=lambda: press(6), font=("Verdana", 16), width=3).grid(row=4, column=3, sticky="NSEW")
tk.Button(text="1", command=lambda: press(1), font=("Verdana", 16), width=3).grid(row=5, column=1, sticky="NSEW")
tk.Button(text="2", command=lambda: press(2), font=("Verdana", 16), width=3).grid(row=5, column=2, sticky="NSEW")
tk.Button(text="3", command=lambda: press(3), font=("Verdana", 16), width=3).grid(row=5, column=3, sticky="NSEW")
tk.Button(text="0", command=lambda: press(0), font=("Verdana", 16), width=3).grid(row=6, column=1, columnspan=3, sticky="NSEW")
tk.Button(text="+", command=lambda: press("+"), font=("Verdana", 16), width=3).grid(row=3, column=4, sticky="NSEW")
tk.Button(text="-", command=lambda: press("-"), font=("Verdana", 16), width=3).grid(row=3, column=5, sticky="NSEW")
tk.Button(text="×", command=lambda: press("*"), font=("Verdana", 16), width=3).grid(row=4, column=4, sticky="NSEW")
tk.Button(text="÷", command=lambda: press("/"), font=("Verdana", 16), width=3).grid(row=4, column=5, sticky="NSEW")
tk.Button(text="=", command=calculate, font=("Verdana", 16)).grid(row=5, column=4, columnspan=2, sticky="NSEW")
tk.Button(text="C", command=clear, font=("Verdana", 16), width=3).grid(row=6, column=4, sticky="NSEW")
tk.Button(text="B", command=lambda: clear(True), font=("Verdana", 16), width=3).grid(row=6, column=5, sticky="NSEW")
tk.Button(text="±", command=lambda: press(arg="switch_symbol"), font=("Verdana", 16), width=3).grid(row=3, column=6, sticky="NSEW")
tk.Button(text="√", command=lambda: press("sqrt("), font=("Verdana", 16), width=3).grid(row=4, column=6, sticky="NSEW")
tk.Button(text="(", command=lambda: press("("), font=("Verdana", 16), width=3).grid(row=5, column=6, sticky="NSEW")
tk.Button(text=")", command=lambda: press(")"), font=("Verdana", 16), width=3).grid(row=6, column=6, sticky="NSEW")
tk.Button(text="sin", command=lambda: press("sin(radians("), font=("Verdana", 16)).grid(row=3, column=7, sticky="NSEW")
tk.Button(text="cos", command=lambda: press("cos(radians("), font=("Verdana", 16)).grid(row=4, column=7, sticky="NSEW")
tk.Button(text="tan", command=lambda: press("tan(radians("), font=("Verdana", 16)).grid(row=5, column=7, sticky="NSEW")
tk.Button(text="rad", command=lambda: press("radians("), font=("Verdana", 16)).grid(row=6, column=7, sticky="NSEW")
tk.Button(text="asin", command=lambda: press("asin(radians("), font=("Verdana", 16)).grid(row=3, column=8, sticky="NSEW")
tk.Button(text="acos", command=lambda: press("acos(radians("), font=("Verdana", 16)).grid(row=4, column=8, sticky="NSEW")
tk.Button(text="atan", command=lambda: press("atan(radians("), font=("Verdana", 16)).grid(row=5, column=8, sticky="NSEW")
tk.Button(text="deg", command=lambda: press("degrees("), font=("Verdana", 16)).grid(row=6, column=8, sticky="NSEW")
tk.Button(text="yˣ", command=lambda: press("^"), font=("Verdana", 16)).grid(row=3, column=9, sticky="NSEW")
tk.Button(text="•", command=lambda: press("."), font=("Verdana", 16)).grid(row=4, column=9, sticky="NSEW")
tk.Button(text="!", command=lambda: press("factorial("), font=("Verdana", 16)).grid(row=5, column=9, sticky="NSEW")
tk.Button(text="sum", command=lambda: press("summation("), font=("Verdana", 16)).grid(row=6, column=9, sticky="NSEW")


root.mainloop()
