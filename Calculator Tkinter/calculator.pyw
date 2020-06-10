from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.iconbitmap("calculator.ico")
e = Entry(root, width=40, borderwidth=4)
e.grid(row=0, column=0, columnspan=3, padx=18, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))


def clear():
    current = e.get()
    if current == "":
        return
    e.delete(0, END)
    num = int(current)//10
    if num == 0:
        e.delete(0, END)
    else:
        e.insert(0, int(current)//10)


def allclear():
    e.delete(0, END)


def operation(o):
    global first
    global op
    op = o
    first = e.get()
    e.delete(0, END)


def equal():
    second = e.get()
    e.delete(0, END)
    if second == "":
        return
    if op == "+":
        e.insert(0, int(first)+int(second))
    elif op == "-":
        e.insert(0, int(first)-int(second))
    elif op == "/":
        e.insert(0, float(first)/float(second))
    elif op == "*":
        e.insert(0, int(first)*int(second))


button7 = Button(root, text="7", padx=40, pady=20,
                 command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20,
                 command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20,
                 command=lambda: button_click(9))

button4 = Button(root, text="4", padx=40, pady=20,
                 command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20,
                 command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20,
                 command=lambda: button_click(6))

button1 = Button(root, text="1", padx=40, pady=20,
                 command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20,
                 command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20,
                 command=lambda: button_click(3))


button0 = Button(root, text="0", padx=40, pady=20,
                 command=lambda: button_click(0))
button_clear = Button(root, text="C", padx=39, pady=20, command=clear)
button_allclear = Button(root, text="AC", padx=35, pady=20, command=allclear)

button_sub = Button(root, text="-", padx=40.5, pady=20,
                    command=lambda: operation("-"))
button_mul = Button(root, text="*", padx=40, pady=20,
                    command=lambda: operation("*"))
button_div = Button(root, text="/", padx=41, pady=20,
                    command=lambda: operation("/"))

buttonadd = Button(root, text="+", padx=39, pady=20,
                   command=lambda: operation("+"))
button_equal = Button(root, text="=", padx=87, pady=20, command=equal)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button_sub.grid(row=5, column=0)
button_mul.grid(row=5, column=1)
button_div.grid(row=5, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_allclear.grid(row=4, column=2)

button_equal.grid(row=6, column=1, columnspan=2)
buttonadd.grid(row=6, column=0)

root.mainloop()
