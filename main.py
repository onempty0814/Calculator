import tkinter as tk
from gui import AdvancedCalculator

def main():
    # Initialize the main Tkinter window
    root = tk.Tk()

    # Initialize the GUI and pass the logic to it
    AdvancedCalculator(root)
    
    # Start the app
    root.mainloop()

if __name__ == "__main__":
    main()
