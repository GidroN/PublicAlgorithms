from tkinter import *

root = Tk()

root.title("Caculator")
root.resizable(False, False)

start = True
lastcommand = ''
result = 0


buttons = (("%", "C", "x**2", "SQRT"),
           ("7", "8", "9", "*"),
           ("4", "5", "6", "-"),
           ("1", "2", "3", "+"),
           ("+/-", "0", ".", "="))

display = Label(root, text="0", font="Tahoma 20", bd="10", fg="#FFF", bg="#000")
display.grid(row=0, column=0, columnspan=4)

root["bg"] = "#000"

for row in range(5):
    for column in range(4):
        button = Button(root, text=buttons[row][column], font="Tahoma 20",bg="#000",fg="#FFF" ,command=lambda text=buttons[row][column]: click(text))
        button.grid(row=row + 1, column=column, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")



def click(text):
    global start
    global lastcommand
    global display
    if text.isdigit() or text == ".":
        if start:
            display.config(text="")
            start = False

        if text != "." or display.cget("text").find(".") == -1:
            display.config(text=(display.cget('text') + text))
    else:
        if start:
            lastcommand = text
        else:
            pass
            calculate(float(display.cget("text")))
            lastcommand = text
            start = True

def calculate(x):
    global lastcommand
    global result
    global display
    if lastcommand == "+":
        result += x
    elif lastcommand == "-":
        result -= x
    elif lastcommand == "%":
        result %= x
    elif lastcommand == "*":
        result *= x
    elif lastcommand == "x**2":
        result **= x
    elif lastcommand == "+/-":
        result = x * (-1)
        display.config(text=result)
    elif lastcommand == "C":
        display.config(text="0")
    elif lastcommand == "SQRT":
        result = x ** 0.5
        display.config(text=result)
    elif lastcommand == "/":
        try:
            result /= x
        except ZeroDivisionError:
            pass
    elif lastcommand == "=":
        result = x
    display.config(text=result)


w = root.winfo_reqwidth()
h = root.winfo_reqheight()

ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()

x = int(ws / 2 - w / 2)
y = int(wh / 2 - h / 2)

root.geometry(f"+{x}+{y}")

root.mainloop()