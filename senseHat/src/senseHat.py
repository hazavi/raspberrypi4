
from sense_hat import SenseHat
import joystick_events

def main():
    sense = SenseHat()
    
    # Handle joystick events
    joystick_events.handle_joystick_events(sense)

if __name__ == "__main__":
    main()