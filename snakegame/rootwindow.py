from tkinter import  ttk
import tkinter as tk
from .snakecanvas import Snake
from .endgameframe import EndGameFrame
from ttkbootstrap import Style

class RootWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Snake Game')                
        self.style = Style()
        self.style.theme_use('solar')
        self.style.configure('TButton', borderwidth=0)
        self.style.map(
            "TButton",
            foreground=[('hover', '!disabled', self.style.lookup('TButton', 'background')),
                        ('disabled','white')],
            background =[('hover','!disabled',self.style.lookup('TButton','foreground')),
                         ('disabled','grey')])
        self.resizable(False, False)        
        self.create()
        self.place()
        self.__MainGameFrame.tkraise()

    @property
    def EndGameFrame(self):
        return self.__EndGameFrame
        
    def update_snakeCanvas(self):        
        self.__snakeCanvas = Snake(self.__MainGameFrame, self)
        self.__EndGameFrame.replayBtn.config(state=tk.DISABLED)
        self.__EndGameFrame.quitBtn.config(state=tk.DISABLED)
        self.__snakeCanvas.grid(row=0, column=0)
        self.__MainGameFrame.tkraise()
            
    def create(self):
        self.__MainGameFrame   = ttk.Frame(self)
        self.__snakeCanvas = Snake(self.__MainGameFrame,self)                
        self.__EndGameFrame= EndGameFrame(self)
    
    def place(self):
        self.__MainGameFrame.grid(row=0, column=0)
        self.__snakeCanvas.grid(row=0, column=0)        
        self.__EndGameFrame.grid(row=0, column=0, sticky='NEWS')        