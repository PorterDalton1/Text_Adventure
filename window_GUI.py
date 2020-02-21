"""
This file provides the GUI for the text adventure. 
"""
import tkinter

class WindowBase:
    def __init__(self, master):
        self.master = master
        self.master.configure(background = "black")
        self.master.minsize(600, 400)

def main():
    x = tkinter.Tk()
    WindowBase(x)
    x.mainloop()

if __name__ == '__main__':
    main()