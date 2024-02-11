# Calculator
#### *this project is a calculator and has three inputs.*
*first input is for the  number , second input for operation and third input for the number.*
*the operations that this calculator performans is : addition , subtarction , multiplication , division , power and logarithm.*

+ operations are as fllows :
```python
def calculate():
    operation = operation_entry.get()
    try:
        number1 = float(number_1_entry.get())
        number2 = float(number_2_entry.get())
    except:
        generate_label.config(text="Please entre the number!!")

    else:

        if operation == "+":
            a = number1 + number2
            generate_label.config(text=f"{a}")

        elif operation == "-":
            b = number1 - number2
            generate_label.config(text=f"{b}")

        elif operation == "*":
            c = number1 * number2
            generate_label.config(text=f"{c}")

        elif operation == "/":
            try:
                d = number1 / number2
            except:
                generate_label.config(text=f"Error")
            else:
                generate_label.config(text=f"{d}")

        elif operation == "**":
            e = math.pow(number1, number2)
            generate_label.config(text=f"{e}")

        elif operation == "log":
            try:
                f = math.log(number1, number2)
            except:
                generate_label.config(text=f"Error")
            else:
                generate_label.config(text=f"{f}")
```
