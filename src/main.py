from tkinter import *
from UserInterface import UserInterface
        
if __name__=="__main__":
    root = Tk()
    calculator = UserInterface(root)
    root.title("Compounding Interest Calculator")
    root.mainloop()