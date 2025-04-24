from sense_hat import SenseHat
import time

def draw_danish_flag(sense):
    """Draw the Danish flag on the Sense HAT display."""
    # Danish flag colors
    red = (255, 0, 0)
    white = (255, 255, 255)
    
    # Define the Danish flag pattern
    # Red background with white cross
    flag = [
        red, red, red, white, white, red, red, red,
        red, red, red, white, white, red, red, red,
        red, red, red, white, white, red, red, red,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        red, red, red, white, white, red, red, red,
        red, red, red, white, white, red, red, red,
        red, red, red, white, white, red, red, red
    ]
    
    # Display the flag
    sense.set_pixels(flag)
    
    # Keep it displayed for a while
    print("Displaying Danish flag")
    time.sleep(3)
    
    # Clear the display after showing the flag
    sense.clear()

if __name__ == "__main__":
    sense = SenseHat()
    draw_danish_flag(sense)