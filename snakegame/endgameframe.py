import tkinter as tk
from tkinter import ttk

class EndGameFrame(ttk.Frame):
    
    def __init__(self,container):
        super().__init__(container)
        self.__container = container
        self.create_widgets()
        self.place_widgets()
    
    def create_widgets(self):        
        self.__label = ttk.Label(self, text='Play Again ? ')
        self.__replayBtn = ttk.Button(
            self,
            command=self.__container.update_snakeCanvas,
            text='retry')

    def place_widgets(self):
        self.__label.pack()
        self.__replayBtn.pack()

    def change_label(self, text):
        self.__label.config(text=text)