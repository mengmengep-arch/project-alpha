# เกมงู (Snake Game) ด้วย tkinter
import tkinter as tk
import random

GAME_WIDTH = 400
GAME_HEIGHT = 400
SPEED = 100  # ms
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])

class Food:
    def __init__(self, canvas, snake):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        while [x, y] in snake.coordinates:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.food = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction[0] == "up":
        y -= SPACE_SIZE
    elif direction[0] == "down":
        y += SPACE_SIZE
    elif direction[0] == "left":
        x -= SPACE_SIZE
    elif direction[0] == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        canvas.delete("food")
        new_food = Food(canvas, snake)
        food.coordinates = new_food.coordinates
        food.food = new_food.food
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        root.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if new_direction != opposites.get(direction[0]):
        direction[0] = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2, font=('Arial', 30), fill='white', text="Game Over")

root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

canvas = tk.Canvas(root, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

direction = ["right"]

snake = Snake()
for x, y in snake.coordinates:
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
    snake.squares.append(square)

food = Food(canvas, snake)

root.bind("<Up>", lambda event: change_direction("up"))
root.bind("<Down>", lambda event: change_direction("down"))
root.bind("<Left>", lambda event: change_direction("left"))
root.bind("<Right>", lambda event: change_direction("right"))

next_turn(snake, food)

root.mainloop()
