# SnakeGame
_classic snake game gui, built with python with increasing speed._<br><br>
Use arrow keys to move Up, Down, Left & Right. If the snake touches itself or the boundary the game is over.
For the best experience please turn on your device audio as an audio clip plays when the snake successfully eats it food or when the snake dies.
There are two buttons on the scoring page for playing again and quitting the game.<br><br>

## Built With
- _Python version 3.8.0_<br><br>

## How to run ?

#### Clone the repo
```bash
$ git clone https://github.com/shahan007/SnakeGame
```

#### Set up the environment
```bash
$ python -m venv venv
$ source venv/Scripts/activate
(venv) $ pip install -r requirements.txt
```

#### Setting up database _(optional as it has been already created)_
```bash
(venv) $ python create_table.py
```

#### Start the game
```bash
(venv) $ python run.py
```
