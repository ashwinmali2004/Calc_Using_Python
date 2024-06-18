import tkinter as tk

# Functions to perform the calculator operations:-
def update_display(value):
    current=display_var.get()
    display_var.set(current+value)

def clear_display():
    display_var.set("")

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

root=tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.iconbitmap("C:\\Users\\ASHWIN\\OneDrive\\Desktop\\python_programes\\Projects\\funProject\\calc.ico")

display_var=tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 21), bd=10)

display.grid(row=0,column=0,columnspan=5,pady=20)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2, calculate), ("+", 4, 3),
    ("Clear", 5, 0, clear_display),("Close", 5, 3, root.destroy)
]

for (text, row, col, *command) in buttons:
    if command:
        button = tk.Button(root, text=text, font=("Arial", 14, "bold"),bg="red",fg="white", padx=20, pady=10, command=command[0])
    else:
        button = tk.Button(root, text=text, font=("Arial", 14,"bold"), bg="blue",fg="white",padx=20, pady=10, command=lambda t=text: update_display(t))
    button.grid(row=row, column=col,padx=5,pady=5)
root.mainloop()
