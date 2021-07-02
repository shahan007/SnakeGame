import os
import sqlite3 as db

baseDir  = os.path.abspath(os.path.dirname(__file__))
datapath = os.path.join(baseDir, 'data.sqlite')
connection = db.connect(datapath)

def drop_tables():
    with connection:
        connection.execute("DROP TABLE IF EXISTS user")

def create_tables():
    with connection:
        connection.execute("""
                           CREATE TABLE user(
                               previousScore INT NOT NULL,
                               highScore INT NOT NULL,
                               CONSTRAINT invalidHigh CHECK(highScore >= previousScore)                               
                           );
                           """)

def insert_into():
    with connection:
        connection.execute("""
                        INSERT INTO user
                        VALUES
                        (?,?);
                        """,
                        (0,0))
    
drop_tables()
create_tables()
insert_into()