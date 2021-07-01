import tkinter as tk
from tkinter import ttk

class EndGameFrame(ttk.Frame):
    
    def __init__(self,container):
        super().__init__(container)
        self.__container = container
        self.rowconfigure((3),weight=2)
        self.rowconfigure((0,1,2),weight=1)
        self.columnconfigure(0,weight=1)        
        self.create_widgets()
        self.place_widgets()
    
    @property
    def replayBtn(self):
        return self.__replayBtn
    
    @property
    def quitBtn(self):
        return self.__quitBtn
    
    def create_widgets(self):        
        self.__label = ttk.Label(
            self,
            text='GAME OVER!',
            font = "Arial 26 bold",
            foreground='red')
        self.__scoreLabel =  ttk.Label(
            self,
            font="Didot 15 bold",
            foreground='#00ff00')        
        self.__replayBtn = ttk.Button(
            self, padding=(20, 10),width=10,
            command=self.__container.update_snakeCanvas,
            text='RETRY',state=tk.DISABLED)
        self.__quitBtn = ttk.Button(
            self, padding=(20, 10),width=10,
            command=self.__container.destroy,
            text='QUIT', state=tk.DISABLED)

    def place_widgets(self):
        self.__label.grid(row=1,column=0)
        self.__scoreLabel.grid(row=2, column=0,sticky="N")
        self.__replayBtn.grid(row=2, column=0, sticky='S', padx=(0, 135))
        self.__quitBtn.grid(row=2, column=0, sticky='S',padx=(135,0))

    def change_label(self, score):
        self.__scoreLabel.config(text=f"Your Score is: {score}")        