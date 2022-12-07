import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("250x400+200+200")
root.resizable(0, 0)
root.title("Calculator")

val = ""
A = 0
operator = ""


def button1_is_clicked():
    global val
    val = val + "1"
    data.set(val)


def button2_is_clicked():
    global val
    val = val + "2"
    data.set(val)


def button3_is_clicked():
    global val
    val = val + "3"
    data.set(val)


def button4_is_clicked():
    global val
    val = val + "4"
    data.set(val)


def button5_is_clicked():
    global val
    val = val + "5"
    data.set(val)


def button6_is_clicked():
    global val
    val = val + "6"
    data.set(val)


def button7_is_clicked():
    global val
    val = val + "7"
    data.set(val)


def button8_is_clicked():
    global val
    val = val + "8"
    data.set(val)


def button9_is_clicked():
    global val
    val = val + "9"
    data.set(val)


def button0_is_clicked():
    global val
    val = val + "0"
    data.set(val)


def button_plus_is_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def button_minus_is_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def button_multiply_is_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def button_divide_is_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def buttonC_is_clicked():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)


def button_equal_is_clicked():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division by 0 not allowed")
            A = ""
            val = ""
            data.set(val)
        else:
            c = int(A / x)
            data.set(c)
            val = str(c)


data = StringVar()
lbl = Label(root, anchor=SE, font=("verdana", 20), textvariable=data, bg="white", fg="black")
lbl.pack(expand=True, fill="both")

buttonrow1 = Frame(root)
buttonrow1.pack(expand=True, fill="both")

buttonrow2 = Frame(root)
buttonrow2.pack(expand=True, fill="both")

buttonrow3 = Frame(root)
buttonrow3.pack(expand=True, fill="both")

buttonrow4 = Frame(root)
buttonrow4.pack(expand=True, fill="both")

btn1 = Button(buttonrow1, text="1", font=("verdana", 22), relief=GROOVE, border=0, command=button1_is_clicked)
btn1.pack(side="left", expand=True, fill="both")

btn2 = Button(buttonrow1, text="2", font=("verdana", 22), relief=GROOVE, border=0, command=button2_is_clicked)
btn2.pack(side="left", expand=True, fill="both")

btn3 = Button(buttonrow1, text="3", font=("verdana", 22), relief=GROOVE, border=0, command=button3_is_clicked)
btn3.pack(side="left", expand=True, fill="both")

btnplus = Button(buttonrow1, text="+", font=("verdana", 22), relief=GROOVE, border=0, command=button_plus_is_clicked)
btnplus.pack(side="left", expand=True, fill="both")

btn4 = Button(buttonrow2, text="4", font=("verdana", 22), relief=GROOVE, border=0, command=button4_is_clicked)
btn4.pack(side="left", expand=True, fill="both")

btn5 = Button(buttonrow2, text="5", font=("verdana", 22), relief=GROOVE, border=0, command=button5_is_clicked)
btn5.pack(side="left", expand=True, fill="both")

btn6 = Button(buttonrow2, text="6", font=("verdana", 22), relief=GROOVE, border=0, command=button6_is_clicked)
btn6.pack(side="left", expand=True, fill="both")

btnminus = Button(buttonrow2, text="-", font=("verdana", 22), relief=GROOVE, border=0, command=button_minus_is_clicked)
btnminus.pack(side="left", expand=True, fill="both")

btn7 = Button(buttonrow3, text="7", font=("verdana", 22), relief=GROOVE, border=0, command=button7_is_clicked)
btn7.pack(side="left", expand=True, fill="both")

btn8 = Button(buttonrow3, text="8", font=("verdana", 22), relief=GROOVE, border=0, command=button8_is_clicked)
btn8.pack(side="left", expand=True, fill="both")

btn9 = Button(buttonrow3, text="9", font=("verdana", 22), relief=GROOVE, border=0, command=button9_is_clicked)
btn9.pack(side="left", expand=True, fill="both")

btnmultiply = Button(buttonrow3, text="*", font=("verdana", 22), relief=GROOVE, border=0,
                     command=button_multiply_is_clicked)
btnmultiply.pack(side="left", expand=True, fill="both")

btnC = Button(buttonrow4, text="C", font=("verdana", 22), relief=GROOVE, border=0, command=buttonC_is_clicked)
btnC.pack(side="left", expand=True, fill="both")

btn0 = Button(buttonrow4, text="0", font=("verdana", 22), relief=GROOVE, border=0, command=button0_is_clicked)
btn0.pack(side="left", expand=True, fill="both")

btnequal = Button(buttonrow4, text="=", font=("verdana", 22), relief=GROOVE, border=0, command=button_equal_is_clicked)
btnequal.pack(side="left", expand=True, fill="both")

btndivide = Button(buttonrow4, text="/", font=("verdana", 22), relief=GROOVE, border=0,
                   command=button_divide_is_clicked)
btndivide.pack(side="left", expand=True, fill="both")

root.mainloop()