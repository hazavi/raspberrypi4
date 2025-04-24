from sense_hat import SenseHat
import time
import datetime

def display_binary_clock(sense, duration=1):
    """Display a binary clock on the Sense HAT for a specified duration."""
    sense.clear()
    start_time = time.time()

    while time.time() - start_time < duration:
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

        # Display each time component in binary
        def display_binary(value, row, color):
            binary_str = "{0:08b}".format(int(value))
            for x in range(0, 8):
                if binary_str[x] == '1':
                    sense.set_pixel(x, row, color)
                else:
                    sense.set_pixel(x, row, off)

        display_binary(t.year % 100, 0, year_color)  # Last two digits of the year
        display_binary(t.month, 1, month_color)
        display_binary(t.day, 2, day_color)
        display_binary(t.hour, 3, hour_color)
        display_binary(t.minute, 4, minute_color)
        display_binary(t.second, 5, second_color)
        display_binary(t.microsecond / 10000, 6, hundredths_color)

        # Update the display frequently
        time.sleep(0.1)


def main():
    display_binary_clock(SenseHat(), duration=1)  # Display for 1 second

if __name__ == "__main__":
    main()