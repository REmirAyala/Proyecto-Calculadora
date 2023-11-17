from tkinter import *

window = Tk()
window.title("Calculadora")

index = 0

##Input text>
i_text = Entry(window, font="Roboto 20")
i_text.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


##Fuctions

def click_button(value):
    global index
    i_text.insert(index, value)
    index += 1


def clear():
    global index
    i_text.delete(0, END)
    index = 0


def calculate():
    global index
    equation = i_text.get()
    result = eval(equation)
    i_text.delete(0, END)
    i_text.insert(0, result)


##Buttons>
button1 = Button(window, text="1", width=5, height=2, command=lambda: click_button(1))
button2 = Button(window, text="2", width=5, height=2, command=lambda: click_button(2))
button3 = Button(window, text="3", width=5, height=2, command=lambda: click_button(3))
button4 = Button(window, text="4", width=5, height=2, command=lambda: click_button(4))
button5 = Button(window, text="5", width=5, height=2, command=lambda: click_button(5))
button6 = Button(window, text="6", width=5, height=2, command=lambda: click_button(6))
button7 = Button(window, text="7", width=5, height=2, command=lambda: click_button(7))
button8 = Button(window, text="8", width=5, height=2, command=lambda: click_button(8))
button9 = Button(window, text="9", width=5, height=2, command=lambda: click_button(9))
button0 = Button(window, text="0", width=13, height=2, command=lambda: click_button(0))

button_clear = Button(window, text="AC", width=5, height=2, command=lambda: clear())
button_parenthesis1 = Button(window, text="(", width=5, height=2, command=lambda: click_button(("(")))
button_parenthesis2 = Button(window, text=")", width=5, height=2, command=lambda: click_button(")"))
button_dot = Button(window, text=".", width=5, height=2, command=lambda: click_button("."))

button_div = Button(window, text="/", width=5, height=2, command=lambda: click_button("/"))
button_mult = Button(window, text="*", width=5, height=2, command=lambda: click_button("*"))
button_sum = Button(window, text="+", width=5, height=2, command=lambda: click_button("+"))
button_min = Button(window, text="-", width=5, height=2, command=lambda: click_button("-"))
button_equal = Button(window, text="=", width=5, height=2, command=lambda: calculate())

##Buttons in windows

button_clear.grid(row=1, column=0, padx=5, pady=5)
button_parenthesis1.grid(row=1, column=1, padx=5)
button_parenthesis2.grid(row=1, column=2, padx=5)
button_div.grid(row=1, column=3, padx=5, pady=5)

button7.grid(row=2, column=0, padx=5, pady=5)
button8.grid(row=2, column=1, padx=5, pady=5)
button9.grid(row=2, column=2, padx=5, pady=5)
button_mult.grid(row=2, column=3, padx=5, pady=5)

button4.grid(row=3, column=0, padx=5, pady=5)
button5.grid(row=3, column=1, padx=5, pady=5)
button6.grid(row=3, column=2, padx=5, pady=5)
button_sum.grid(row=3, column=3, padx=5, pady=5)

button1.grid(row=4, column=0, padx=5, pady=5)
button2.grid(row=4, column=1, padx=5, pady=5)
button3.grid(row=4, column=2, padx=5, pady=5)
button_min.grid(row=4, column=3, padx=5, pady=5)

button0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
button_dot.grid(row=5, column=2, padx=5, pady=5)
button_equal.grid(row=5, column=3, padx=5, pady=5)

window.mainloop()
