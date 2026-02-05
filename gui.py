"""
Docstring for GUI
Author: Andrew Berlett
Date: Feburary 3rd, 2026
"""
import tkinter as tk
from tkinter import ttk
from logic import CalculatorLogic

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Scientific Calc")
        self.root.geometry("400x600")
        self.logic = CalculatorLogic()
        # This variable stores the current text in the display
        self.display_var = tk.StringVar(value="0")
        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Modern Dark-ish Theme
        style.configure("TFrame", background="#2d2d2d")
        style.configure("TButton", font=("Segoe UI", 10), padding=5)
        style.configure("Op.TButton", foreground="#f39c12", font=("Segoe UI", 10, "bold"))
        style.configure("Display.TLabel", 
                        font=("Consolas", 28), 
                        background="#1e1e1e", 
                        foreground="#00ff00")

    def create_widgets(self):
        # Display
        container = ttk.Frame(self.root)
        container.pack(fill="both", expand=True)

        display_label = ttk.Label(container, textvariable=self.display_var, 
                                  anchor="e", style="Display.TLabel")
        display_label.pack(fill="x", padx=10, pady=20)

        # Button Grid Definition
        # Format: (Text, Row, Col, [Optional Style])
        buttons = [
            ('sin', 0, 0), ('cos', 0, 1), ('tan', 0, 2), ('log', 0, 3),
            ('asin', 1, 0), ('acos', 1, 1), ('atan', 1, 2), ('ln', 1, 3),
            ('x²', 2, 0), ('√', 2, 1), ('x!', 2, 2), ('%', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('/', 3, 3, "Op.TButton"),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3, "Op.TButton"),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3, "Op.TButton"),
            ('0', 6, 0), ('.', 6, 1), ('=', 6, 2, "Op.TButton"), ('+', 6, 3, "Op.TButton"),
            ('CLR', 7, 0, "Op.TButton"), ('(', 7, 1), (')', 7, 2), (',', 7, 3)
        ]

        grid_frame = ttk.Frame(container)
        grid_frame.pack(fill="both", expand=True, padx=5, pady=5)

        for btn in buttons:
            text, r, c = btn[0], btn[1], btn[2]
            btn_style = btn[3] if len(btn) > 3 else "TButton"
            
            action = lambda x=text: self.handle_click(x)
            ttk.Button(grid_frame, text=text, style=btn_style, command=action).grid(
                row=r, column=c, sticky="nsew", padx=2, pady=2
            )

        for i in range(4): grid_frame.columnconfigure(i, weight=1)
        for i in range(8): grid_frame.rowconfigure(i, weight=1)

    def handle_click(self, char):
        curr = self.display_var.get()
        
        if char == "CLR":
            self.display_var.set("0")
        elif char == "=":
            self.calculate_result()
        elif char == "x²":
            self.update_display("square(")
        elif char == "√":
            self.update_display("sqrt(")
        elif char == "x!":
            self.update_display("factorial(")
        elif char == "ln":
            self.update_display("natural_logarithm(")
        elif char == "log":
            self.update_display("logarithm(") # Note: needs comma for base
        else:
            if curr == "0" and char not in "+-*/.":
                self.display_var.set(char)
            else:
                self.display_var.set(curr + char)

    def update_display(self, text):
        curr = self.display_var.get()
        self.display_var.set(text if curr == "0" else curr + text)

    def calculate_result(self):
        """Mapping display strings to CalculatorLogic methods safely."""
        expr = self.display_var.get()
        try:
            allowed_names = {
                "sin": self.logic.sin_deg,
                "cos": self.logic.cos_deg,
                "tan": self.logic.tan_deg,
                "asin": self.logic.arcsin_deg,
                "acos": self.logic.arccos_deg,
                "atan": self.logic.arctan_deg,
                "square": self.logic.square,
                "sqrt": self.logic.sqrt,
                "factorial": self.logic.factorial,
                "logarithm": self.logic.logarithm,
                "natural_logarithm": self.logic.natural_logarithm,
                "percent": self.logic.percent
            }
            # Eval to test logic 
            result = eval(expr, {"__builtins__": None}, allowed_names)
            self.display_var.set(round(result, 8))
        except Exception as e:
            self.display_var.set(f"Error: {str(e)}")

if __name__ == "main":
    root = tk.Tk()
    AdvancedCalculator(root)
    root.mainloop()
"""
Docstring for GUI
Author: Andrew Berlett
Date: Feburary 3rd, 2026
"""
import tkinter as tk
from tkinter import ttk
from logic import CalculatorLogic

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Scientific Calc")
        self.root.geometry("400x600")
        self.logic = CalculatorLogic()
        # This variable stores the current text in the display
        self.display_var = tk.StringVar(value="0")
        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Modern Dark-ish Theme
        style.configure("TFrame", background="#2d2d2d")
        style.configure("TButton", font=("Segoe UI", 10), padding=5)
        style.configure("Op.TButton", foreground="#f39c12", font=("Segoe UI", 10, "bold"))
        style.configure("Display.TLabel", 
                        font=("Consolas", 28), 
                        background="#1e1e1e", 
                        foreground="#00ff00")

    def create_widgets(self):
        # Display
        container = ttk.Frame(self.root)
        container.pack(fill="both", expand=True)

        display_label = ttk.Label(container, textvariable=self.display_var, 
                                  anchor="e", style="Display.TLabel")
        display_label.pack(fill="x", padx=10, pady=20)

        # Button Grid Definition
        # Format: (Text, Row, Col, [Optional Style])
        buttons = [
            ('sin', 0, 0), ('cos', 0, 1), ('tan', 0, 2), ('log', 0, 3),
            ('asin', 1, 0), ('acos', 1, 1), ('atan', 1, 2), ('ln', 1, 3),
            ('x²', 2, 0), ('√', 2, 1), ('x!', 2, 2), ('%', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('/', 3, 3, "Op.TButton"),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3, "Op.TButton"),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3, "Op.TButton"),
            ('0', 6, 0), ('.', 6, 1), ('=', 6, 2, "Op.TButton"), ('+', 6, 3, "Op.TButton"),
            ('CLR', 7, 0, "Op.TButton"), ('(', 7, 1), (')', 7, 2), (',', 7, 3)
        ]

        grid_frame = ttk.Frame(container)
        grid_frame.pack(fill="both", expand=True, padx=5, pady=5)

        for btn in buttons:
            text, r, c = btn[0], btn[1], btn[2]
            btn_style = btn[3] if len(btn) > 3 else "TButton"
            
            action = lambda x=text: self.handle_click(x)
            ttk.Button(grid_frame, text=text, style=btn_style, command=action).grid(
                row=r, column=c, sticky="nsew", padx=2, pady=2
            )

        for i in range(4): grid_frame.columnconfigure(i, weight=1)
        for i in range(8): grid_frame.rowconfigure(i, weight=1)

    def handle_click(self, char):
        curr = self.display_var.get()
        
        if char == "CLR":
            self.display_var.set("0")
        elif char == "=":
            self.calculate_result()
        elif char == "x²":
            self.update_display("square(")
        elif char == "√":
            self.update_display("sqrt(")
        elif char == "x!":
            self.update_display("factorial(")
        elif char == "ln":
            self.update_display("natural_logarithm(")
        elif char == "log":
            self.update_display("logarithm(") # Note: needs comma for base
        else:
            if curr == "0" and char not in "+-*/.":
                self.display_var.set(char)
            else:
                self.display_var.set(curr + char)

    def update_display(self, text):
        curr = self.display_var.get()
        self.display_var.set(text if curr == "0" else curr + text)

    def calculate_result(self):
        """Mapping display strings to CalculatorLogic methods safely."""
        expr = self.display_var.get()
        try:
            allowed_names = {
                "sin": self.logic.sin_deg,
                "cos": self.logic.cos_deg,
                "tan": self.logic.tan_deg,
                "asin": self.logic.arcsin_deg,
                "acos": self.logic.arccos_deg,
                "atan": self.logic.arctan_deg,
                "square": self.logic.square,
                "sqrt": self.logic.sqrt,
                "factorial": self.logic.factorial,
                "logarithm": self.logic.logarithm,
                "natural_logarithm": self.logic.natural_logarithm,
                "percent": self.logic.percent
            }
            # Eval to test logic 
            result = eval(expr, {"__builtins__": None}, allowed_names)
            self.display_var.set(round(result, 8))
        except Exception as e:
            self.display_var.set(f"Error: {str(e)}")

if __name__ == "main":
    root = tk.Tk()
    AdvancedCalculator(root)
    root.mainloop()
