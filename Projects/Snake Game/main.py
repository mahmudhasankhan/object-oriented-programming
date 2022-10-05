from tkinter import *
import random
import settings


class Snake:
    def __init__(self):
        self.body_parts = settings.BODY_PARTS
        self.coordinates = []
        self.square_graphics = []

        for i in range(0, settings.BODY_PARTS):
            self.coordinates.append([0, 0])

        for x_square, y_square in self.coordinates:
            square_graphic = canvas.create_rectangle(x_square,
                                                     y_square,
                                                     x_square + settings.SPACE_SIZE,
                                                     y_square + settings.SPACE_SIZE,
                                                     fill=settings.SNAKE_COLOR,
                                                     tag='snake')
            self.square_graphics.append(square_graphic)


class Food:
    def __init__(self):
        food_x = random.randint(0, int((settings.GAME_WIDTH/settings.SPACE_SIZE)) - 1) * settings.SPACE_SIZE
        food_y = random.randint(0, int((settings.GAME_HEIGHT/settings.SPACE_SIZE)) - 1) * settings.SPACE_SIZE

        self.coordinates = [food_x, food_y]
        canvas.create_oval(food_x,
                           food_y,
                           food_x + settings.SPACE_SIZE,
                           food_y + settings.SPACE_SIZE,
                           fill=settings.FOOD_COLOR, tag='food')


def next_turn(snake, food):
    snake_x, snake_y = snake.coordinates[0]

    if initial_direction == 'up':
        snake_y -= settings.SPACE_SIZE
    elif initial_direction == 'down':
        snake_y += settings.SPACE_SIZE
    elif initial_direction == 'left':
        snake_x -= settings.SPACE_SIZE
    elif initial_direction == 'right':
        snake_x += settings.SPACE_SIZE

    snake.coordinates.insert(0, (snake_x, snake_y))

    square_graphic = canvas.create_rectangle(snake_x,
                                             snake_y,
                                             snake_x + settings.SPACE_SIZE,
                                             snake_y + settings.SPACE_SIZE,
                                             fill=settings.SNAKE_COLOR)
    snake.square_graphics.insert(0, square_graphic)

    if snake_x == food.coordinates[0] and snake_y == food.coordinates[1]:
        global score
        score += 1

        label.config(text='Score:{}'.format(score))

        canvas.delete('food')

        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.square_graphics[-1])
        del snake.square_graphics[-1]
    if check_collision(snake):
        game_over()
    else:
        window.after(settings.SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global initial_direction

    if new_direction == 'left':
        if initial_direction != 'right':
            initial_direction = new_direction
    elif new_direction == 'right':
        if initial_direction != 'left':
            initial_direction = new_direction
    elif new_direction == 'up':
        if initial_direction != 'down':
            initial_direction = new_direction
    elif new_direction == 'down':
        if initial_direction != 'up':
            initial_direction = new_direction


def check_collision(snake):
    snake_x, snake_y = snake.coordinates[0]

    if snake_x < 0 or snake_x >= settings.GAME_WIDTH:
        print('Game Over')
        return True
    elif snake_y < 0 or snake_y >= settings.GAME_HEIGHT:
        print('Game Over')
        return True

    for body_part in snake.coordinates[1:]:
        if snake_x == body_part[0] and snake_y == body_part[1]:
            return True

    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font=('consolas', 70),
                       text='GAME OVER',
                       fill='red',
                       tag='game_over')


window = Tk()
window.title('Snake Game')
window.resizable(False, False)

score = 0
initial_direction = 'down'

label = Label(window, text='Score:{}'.format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window,
                bg=settings.BACKGROUND_COLOR,
                height=settings.GAME_HEIGHT,
                width=settings.GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Binding Keys
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
snake = Snake()

food = Food()

next_turn(snake, food)


window.mainloop()
