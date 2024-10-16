import tkinter as tk

# Function to update the expression in the text entry widget
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + key)

# Function to evaluate the expression and display the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the text entry widget
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for displaying the expression and result
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=calculate)
    elif button == 'C':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=clear)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18),
                        command=lambda b=button: press(b))
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add a clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear)
clear_button.grid(row=row_val, column=0, columnspan=4)

# Start the Tkinter event loop
root.mainloop()
