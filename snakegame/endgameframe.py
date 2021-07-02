import tkinter as tk
from tkinter import ttk

class EndGameFrame(ttk.Frame):
    
    def __init__(self,container):
        super().__init__(container)
        self.__container = container
        self.rowconfigure((0,4,5),weight=1)
        self.rowconfigure((1,2,3),weight=0)                     
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
            font="Didot 18 bold",
            foreground='#00ff00')   
        self.__prevScrLabel = ttk.Label(
            self,
            font="Didot 15 bold",
            foreground='#CBC3E3')
        self.__hghScrLabel  = ttk.Label(
        self,
        font = "Didot 15 bold",
            foreground='#CBC3E3')
        self.__replayBtn = ttk.Button(
            self, padding=(20, 10),width=10,
            command=self.__container.update_snakeCanvas,
            text='RETRY',state=tk.DISABLED)
        self.__quitBtn = ttk.Button(
            self, padding=(20, 10),width=10,
            command=self.__container.destroy,
            text='QUIT', state=tk.DISABLED)

    def place_widgets(self):
        self.__label.grid(row=0,column=0)
        self.__scoreLabel.grid(row=1, column=0,sticky="N")
        self.__prevScrLabel.grid(row=2,column=0,pady=(40,5))
        self.__hghScrLabel.grid(row=3, column=0, pady=5)
        self.__replayBtn.grid(row=4, column=0 , padx=(0, 135))
        self.__quitBtn.grid(row=4, column=0,padx=(135,0))

    def change_label(self, score,pS,hS):
        self.__scoreLabel.config(text=f"Your Score is: {score}")        
        self.__prevScrLabel.config(text=f"Your Previous Score is: {pS}")
        self.__hghScrLabel.config(text=f"Your High Score is: {hS}")