def draw_rectangle(x, y, width, height, color):
    for i in range(width):
        for j in range(height):
            set_pixel(x + i, y + j, color)

def set_pixel(x, y, color):
    from sense_hat import SenseHat
    sense = SenseHat()
    sense.set_pixel(x, y, color)

def clear_display():
    from sense_hat import SenseHat
    sense = SenseHat()
    sense.clear()

def display_message(message, color=(255, 255, 255)):
    from sense_hat import SenseHat
    sense = SenseHat()
    sense.show_message(message, text_colour=color)