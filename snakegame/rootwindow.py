from tkinter import  ttk
import tkinter as tk
from .snakecanvas import Snake

class RootWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Snake Game')
        self.resizable(False, False)
        self.create()
        self.place()

    def create(self):
        self.__snakeCanvas = Snake(self)

    def place(self):
        self.__snakeCanvas.grid(row=0, column=0)