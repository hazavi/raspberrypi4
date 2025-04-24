#!/usr/bin/env python3
from sense_hat import SenseHat
import time
import datetime
import argparse
import signal
import sys

# Initialize Sense HAT
sense = SenseHat()

# Handle termination signals (e.g., SIGTERM)
def signal_handler(sig, frame):
    print("Signal received, shutting down gracefully...")
    sense.clear()  # Clear the LED matrix
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Binary Clock with rotation.")
parser.add_argument("-r", type=int, help="Rotate display by degrees (e.g., 0, 90, 180, 270).")
args = parser.parse_args()

# Validate rotation input
if args.r and args.r not in [0, 90, 180, 270]:
    print("Cannot mess with the given input")
    sys.exit(1)

rotation = args.r if args.r else 0
sense.set_rotation(rotation)
print(f"Rotation set to {rotation} degrees.")

# Function to display the binary clock
def display_binary_clock(sense):
    """Display a binary clock on the Sense HAT."""
    previous_pixels = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]  # Store the previous state of the matrix

    while True:
        # Get the current time
        t = datetime.datetime.now()

        # Define colors for each time component
        year_color = (0, 255, 0)
        month_color = (0, 0, 255)
        day_color = (255, 0, 0)
        hour_color = (0, 255, 0)
        minute_color = (0, 0, 255)
        second_color = (255, 0, 0)
        hundredths_color = (127, 127, 0)
        off = (0, 0, 0)

        # Create a new pixel matrix
        new_pixels = [[off for _ in range(8)] for _ in range(8)]

        # Helper function to update binary values in the matrix
        def update_binary(value, row, color):
            binary_str = "{0:08b}".format(int(value))
            for x in range(8):
                new_pixels[row][x] = color if binary_str[x] == '1' else off

        # Update the binary values for each time component
        update_binary(t.year % 100, 0, year_color)  # Last two digits of the year
        update_binary(t.month, 1, month_color)
        update_binary(t.day, 2, day_color)
        update_binary(t.hour, 3, hour_color)
        update_binary(t.minute, 4, minute_color)
        update_binary(t.second, 5, second_color)
        update_binary(t.microsecond // 10000, 6, hundredths_color)

        # Only update the pixels that have changed
        for y in range(8):
            for x in range(8):
                if new_pixels[y][x] != previous_pixels[y][x]:
                    sense.set_pixel(x, y, new_pixels[y][x])

        # Save the current state as the previous state
        previous_pixels = new_pixels

        # Update the display every 0.1 seconds
        time.sleep(0.1)

# Main function
def main():
    display_binary_clock(sense)

if __name__ == "__main__":
    main()