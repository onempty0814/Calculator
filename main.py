import tkinter as tk
from gui import AdvancedCalculator
from logic import CalculatorLogic

def main():
    # 1. Initialize the main Tkinter window
    root = tk.Tk()
    
    # 2. Instantiate the logic backend
    # This allows the GUI to access all your math methods
    logic_backend = CalculatorLogic()
    
    # 3. Initialize the GUI and pass the logic to it
    app = AdvancedCalculator(root)
    
    # 4. Start the application
    # This keeps the window open and listening for button clicks
    root.mainloop()

if __name__ == "__main__":
    main()
