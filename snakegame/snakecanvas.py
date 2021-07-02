from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from random import randrange
from playsound import playsound
import threading
import sqlite3 as db
import os

class Snake(tk.Canvas):

    def __init__(self, container,root):
        super().__init__(container)
        self.__container = container
        self.__root      = root        
        self.__MoveIncrement = 20
        self.__GameSpeedVariance = 10
        self.__GameSpeed = 1000 // self.__GameSpeedVariance
        self.__score = 0
        self.__dataFile = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), 'data.sqlite')
        self.__connection = db.connect(self.__dataFile)
        self.read_data(self.__connection)        
        self.__snakePosition = [[60, 100], [80, 100], [100, 100]]
        self.__foodPosition = self.randomise_food_loc()
        self.__CurDirection = 'Right'
        self.__only_directions = ('Up', 'Down', 'Left', 'Right')
        self.__opposites = {'Up': 'Down',
                            'Left': 'Right',
                            'Right': 'Left',
                            'Down': 'Up'}

        self.bind_all('<Key>', self.key_press_execute)
        self.style_canvas()
        self.load_assets()
        self.insert_objects()
        self.execute_actions()

    def read_data(self,connection):
        with connection:
            query = connection.execute("SELECT * FROM user LIMIT 1;")
            self.__previousScore,self.__highScore = query.fetchone()

    def update_data(self,connection):
        self.__previousScore = self.__score
        with connection:
            connection.execute("""
                            UPDATE user
                            SET previousScore = ? ,
                            highScore = ?
                            """,
                            (self.__previousScore, self.__highScore))
        
    def style_canvas(self):
        self.config(
            width=600,
            height=620,
            background='black',
            highlightthickness=0)

    def load_assets(self):
        dirname = os.path.dirname(__file__)        
        with Image.open(os.path.join(dirname,"assets/snake.png")) as img:
            self.__snake = ImageTk.PhotoImage(image=img)

        with Image.open(os.path.join(dirname, "assets/food.png")) as img:
            self.__food = ImageTk.PhotoImage(image=img)

    def create_score(self):
        self.create_text(
            80, 15,
            text=f"Score: {self.__score} \t Speed is {self.__GameSpeedVariance} ms",
            tag='score',
            fill='#CBC3E3')

    def insert_objects(self):
        self.create_score()
        self.create_rectangle(10, 50, 590, 610, outline='#00FF00')
        for x, y in self.__snakePosition:
            self.create_image(
                x, y,
                image=self.__snake,
                tag='snake')

        self.create_image(
            self.__foodPosition[0],
            self.__foodPosition[1],
            image=self.__food,
            tag='food'
        )

    def move_snake(self):
        head_x, head_y = self.__snakePosition[-1]
        if self.__CurDirection == "Up":
            head_y = head_y - self.__MoveIncrement
        elif self.__CurDirection == 'Right':
            head_x = head_x + self.__MoveIncrement
        elif self.__CurDirection == 'Down':
            head_y = head_y + self.__MoveIncrement
        elif self.__CurDirection == 'Left':
            head_x = head_x - self.__MoveIncrement
        newHeadP = [head_x, head_y]
        self.__snakePosition = self.__snakePosition[1:] + [newHeadP]
        for segment, position in zip(self.find_withtag('snake'), self.__snakePosition):
            self.coords(segment, position)

    def check__collision(self, head):
        return (
            head[0] in (20, 580)
            or
            head[1] in (60, 600)
            or
            head in self.__snakePosition[:-1])

    def check_eat_food(self, head):
        if head == self.__foodPosition:      
            thread = threading.Thread(target=lambda: self.play_sound(
                os.path.join(os.path.dirname(__file__), 'assets/eat.wav'), status=False))
            thread.start()
            self.__score += 1
            self.__snakePosition.insert(0, self.__snakePosition[1])
            self.create_image(
                head[0],
                head[1],
                image=self.__snake,
                tag='snake'
            )
            self.__GameSpeedVariance += 1
            self.__GameSpeed = 1000 // self.__GameSpeedVariance
            self.__foodPosition = self.randomise_food_loc()
            self.coords(self.find_withtag('food'), *self.__foodPosition)
            score = self.find_withtag("score")
            self.itemconfigure(
                score,
                text=f"Score: {self.__score} \t Speed is {self.__GameSpeedVariance} ms")

    def randomise_food_loc(self):
        while True:
            x, y = randrange(40, 560, 20), randrange(80, 580, 20)
            new_pos = [x, y]
            if new_pos not in self.__snakePosition:
                return new_pos

    def execute_actions(self):
        head = self.__snakePosition[-1]
        if self.check__collision(head):
            self.end_game()   
            return         
        self.check_eat_food(head)
        self.move_snake()
        self.after(self.__GameSpeed, self.execute_actions)

    def key_press_execute(self, event):
        new_direction = event.keysym
        if new_direction in self.__only_directions and self.__opposites[self.__CurDirection] != new_direction:
            self.__CurDirection = new_direction

    def play_sound(self,path,status=False):
        playsound(path)
        if status:
            self.__root.EndGameFrame.replayBtn.config(state=tk.NORMAL)  
            self.__root.EndGameFrame.quitBtn.config(state=tk.NORMAL)
        
    def end_game(self):        
        thread = threading.Thread(target=lambda: self.play_sound(os.path.join(
            os.path.dirname(__file__), 'assets/gameover.wav'), status=True))
        thread.start()                
        if self.__score > self.__highScore:
            self.__highScore = self.__score
        self.__root.EndGameFrame.change_label(
            self.__score, self.__previousScore, self.__highScore)
        self.update_data(self.__connection)                                
        self.__root.EndGameFrame.tkraise()
        self.destroy()