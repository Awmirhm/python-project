import math
import tkinter as tk

window = tk.Tk()
window.title("Calculator")

number_1_label = tk.Label(text="Number 1: ")
number_1_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

number_1_entry = tk.Entry(width=20)
number_1_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10))

oparation_label = tk.Label(text="Oparation: ")
oparation_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

oparation_entry = tk.Entry(width=20)
oparation_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 10))

number_2_label = tk.Label(text="Number 2: ")
number_2_label.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

number_2_entry = tk.Entry(width=20)
number_2_entry.grid(row=2, column=1, padx=(0, 10), pady=(10, 10))


def calculat():
    oparation = oparation_entry.get()
    try:
        number1 = float(number_1_entry.get())
        number2 = float(number_2_entry.get())
    except:
        generate_label.config(text="Please entre the number!!")

    else:

        if oparation == "+":
            a = number1 + number2
            generate_label.config(text=f"{a}")

        elif oparation == "-":
            b = number1 - number2
            generate_label.config(text=f"{b}")

        elif oparation == "*":
            c = number1 * number2
            generate_label.config(text=f"{c}")

        elif oparation == "/":
            d = number1 / number2
            generate_label.config(text=f"{d}")

        elif oparation == "**":
            e = math.pow(number1, number2)
            generate_label.config(text=f"{e}")

        elif oparation == "log":
            f = math.log(number1, number2)
            generate_label.config(text=f"{f}")


generate_label = tk.Label(text="Empty")
generate_label.grid(row=3, column=1, padx=(0, 20), pady=(10, 10))

generate_button = tk.Button(text="Generate", bg="yellow", command=calculat)
generate_button.grid(row=4, column=1, padx=(0, 20), pady=(10, 10))

window.mainloop()
