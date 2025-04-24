import time
from sense_hat import SenseHat
from binary_clock import display_binary_clock
from danish_flag import draw_danish_flag
from temperature_display import display_temperature
from humidity_display import display_humidity
from snake_game import start_snake_game

sense = SenseHat()

def joystick_event_handler(event):
    """Handle individual joystick events."""
    if event.action == 'pressed':
        if event.direction == 'up':
            display_temperature(sense)
        elif event.direction == 'down':
            display_humidity(sense)
        elif event.direction == 'left':
            draw_danish_flag(sense)
        elif event.direction == 'right':
            start_snake_game(sense)

def handle_joystick_events(sense):
    """Continuously update the binary clock and handle joystick events."""
    while True:
        # Update the binary clock for a short duration
        display_binary_clock(sense, duration=0.1)

        # Check for joystick events
        for event in sense.stick.get_events():
            joystick_event_handler(event)

def main():
    handle_joystick_events(sense)

if __name__ == "__main__":
    main()