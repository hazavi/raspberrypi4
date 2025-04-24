import time
import random
from sense_hat import SenseHat

class SnakeGame:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()
        self.snake = [(3, 3), (3, 4), (3, 5)]
        self.direction = (0, -1)  # Moving left initially
        self.food = self.place_food()
        self.score = 0
        self.game_over = False

    def place_food(self):
        while True:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            if (x, y) not in self.snake:
                return (x, y)

    def update_snake(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        if (new_head in self.snake or
                new_head[0] < 0 or new_head[0] > 7 or
                new_head[1] < 0 or new_head[1] > 7):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()
        else:
            self.snake.pop()

    def draw(self):
        self.sense.clear()
        for segment in self.snake:
            self.sense.set_pixel(segment[0], segment[1], (0, 255, 0))  # Green for snake
        self.sense.set_pixel(self.food[0], self.food[1], (255, 0, 0))  # Red for food

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def run(self):
        while not self.game_over:
            self.update_snake()
            self.draw()
            time.sleep(0.5)

        self.sense.show_message("Game Over! Score: {}".format(self.score), text_colour=(255, 0, 0))

# Add this function to start the game
def start_snake_game(sense):
    game = SnakeGame()
    game.run()

def main():
    start_snake_game(SenseHat())
    
if __name__ == "__main__":
    main()