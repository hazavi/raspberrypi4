import time
from sense_hat import SenseHat

sense = SenseHat()

def display_temperature(sense):
    try:
        # First attempt: Try direct temperature reading
        try:
            temperature = sense.get_temperature()
            print("Debug: Retrieved temperature value:", temperature)
            if temperature is None:
                raise OSError("Temperature sensor returned None")
        except OSError as e:
            print(f"Direct temperature reading failed: {e}")
            # Second attempt: Use temperature from pressure sensor
            print("Trying temperature from pressure sensor...")
            try:
                # Get temperature from pressure sensor
                temperature = sense.get_temperature_from_pressure()
                print(f"Using temperature from pressure sensor: {temperature:.1f}°C")
            except Exception as e:
                print(f"Alternative method failed: {e}")
                raise OSError("All temperature sensing methods failed")
        
        # Display the temperature value on the Sense HAT
        sense.show_message(f'Temp: {temperature:.1f}C', text_colour=(255, 0, 0))
        print(f'Temperature: {temperature:.1f}C')
    except OSError as e:
        # Handle sensor initialization failure gracefully
        print(f"Error: {e}")
        sense.clear()
        sense.show_letter("E", text_colour=(255, 0, 0))  # Display "E" for error
        time.sleep(1)  # Show the error briefly
        sense.clear()

def main():
    try:
        # Initialize the Sense HAT
        print("Debug: Sense HAT initialization")
        
        # Display temperature
        display_temperature(sense)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sense.clear()
        sense.show_letter("E", text_colour=(255, 0, 0))  # Display "E" for unexpected errors
        time.sleep(1)
        sense.clear()

if __name__ == "__main__":
    main()