import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator For My Internship")
        self.root.resizable(0, 0)
        self.root.configure(bg='black')  
        self.entry = tk.Entry(root, width=35, bg='black', fg='white', borderwidth=5, justify='right', font='Calibri 15')
        self.entry.grid(row=0, column=0, columnspan=3, padx=12, pady=12)
        self.num1 = None
        self.math = None
        self.create_buttons()
        
    def button_click(self, num):
        temp = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, temp + num)

    def button_clear(self):
        self.entry.delete(0, tk.END)

    def button_get(self, oper):
        self.num1 = self.entry.get()
        self.math = oper
        self.entry.insert(tk.END, self.math)
        try:
            self.num1 = float(self.num1)
        except ValueError:
            print("Invalid input. Please enter a number.")

    def button_equal(self):
        inp = self.entry.get()
        num2 = float(inp[inp.index(self.math) + 1:])
        self.entry.delete(0, tk.END)
        if self.math == '+':
            self.entry.insert(0, str(self.num1 + num2))
        elif self.math == '-':
            self.entry.insert(0, str(self.num1 - num2))
        elif self.math == 'x':
            self.entry.insert(0, str(self.num1 * num2))
        elif self.math == '/':
            try:
                self.entry.insert(0, str(self.num1 / num2))
            except ZeroDivisionError:
                self.entry.insert(0, 'Undefined')

    def create_buttons(self):
        button_config = [
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('-', 4, 3),
            ('AC', 0, 3)
        ]

        for (text, row, col) in button_config:
            if text == 'AC':
                btn = tk.Button(self.root, text=text, padx=20, pady=10, command=self.button_clear, font='Calibri 12', bg='black', fg='white')
            elif text == '=':
                btn = tk.Button(self.root, text=text, padx=39, pady=10, command=self.button_equal, font='Calibri 12', bg='black', fg='white')
            elif text in '+-x/':
                btn = tk.Button(self.root, text=text, padx=30, pady=10, command=lambda t=text: self.button_get(t), font='Calibri 12', bg='black', fg='white')
            else:
                btn = tk.Button(self.root, text=text, padx=40, pady=10, command=lambda t=text: self.button_click(t), font='Calibri 12', bg='black', fg='white')
            btn.grid(row=row, column=col)

root = tk.Tk()
Mycalculator = Calculator(root)
root.mainloop()
