import tkinter as tk
from gui import AdvancedCalculator
from logic import CalculatorLogic

def main():
    # Initialize the main Tkinter window
    root = tk.Tk()
    
    # Instantiate the logic backend
    # This allows the GUI to access all your math methods
    logic_backend = CalculatorLogic()
    
    # Initialize the GUI and pass the logic to it
    app = AdvancedCalculator(root)
    
    # Start the app
    root.mainloop()

if __name__ == "__main__":
    main()
