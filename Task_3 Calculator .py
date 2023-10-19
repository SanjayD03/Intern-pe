import tkinter as tk
import math

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)
    entry.config(bg='white', fg='black')  

def backspace():
    current = entry.get()[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, current)

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        result = str(eval(entry.get()) ** 2)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        result = str(math.sqrt(eval(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.configure(bg='#E0E0E0')


entry_font = ("DS-Digital", 24)
button_font = ("DS-Digital", 18)

entry = tk.Entry(root, width=20, borderwidth=5, font=entry_font, bg='#E0E0E0', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    'C', 'DEL', 'x²', '√',  
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+'
    ]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        equal_button = tk.Button(root, text=button, width=5, height=2, font=button_font, bd=0, relief='ridge')
        equal_button.grid(row=row_val, column=col_val, padx=5, pady=5)
        equal_button.config(command=calculate)
    elif button == 'C':
        clear_button = tk.Button(root, text=button, width=5, height=2, font=button_font, bd=0, relief='ridge')
        clear_button.grid(row=row_val, column=col_val, padx=5, pady=5)
        clear_button.config(command=lambda: entry.delete(0, tk.END))
    elif button == 'DEL':
        del_button = tk.Button(root, text=button, width=5, height=2, font=button_font, bd=0, relief='ridge')
        del_button.grid(row=row_val, column=col_val, padx=5, pady=5)
        del_button.config(command=backspace)
    elif button == 'x²':
        square_button = tk.Button(root, text=button, width=5, height=2, font=button_font, bd=0, relief='ridge')
        square_button.grid(row=row_val, column=col_val, padx=5, pady=5)
        square_button.config(command=square)
    elif button == '√':  # Square root button
        sqrt_button = tk.Button(root, text=button, width=5, height=2, font=button_font, bd=0, relief='ridge')
        sqrt_button.grid(row=row_val, column=col_val, padx=5, pady=5)
        sqrt_button.config(command=square_root)
    else:
        num_button = tk.Button(root, text=button, width=5, height=2, font=button_font, bd=0, relief='ridge')
        num_button.grid(row=row_val, column=col_val, padx=5, pady=5)
        num_button.config(command=lambda symbol=button: button_click(symbol))
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
root.mainloop()
