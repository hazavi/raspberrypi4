from sense_hat import SenseHat
import time

def display_humidity(sense):
    """Display humidity data or fallback to other environmental data if humidity sensor fails."""
    try:
        # Try to get humidity reading
        try:
            humidity = sense.get_humidity()
            if humidity is not None and humidity > 0:
                print(f"Humidity: {humidity:.1f}%")
                sense.show_message(f"Humidity: {humidity:.1f}%", text_colour=[0, 0, 255])
                return
            else:
                raise ValueError("Invalid humidity value")
        except Exception as e:
            # Fallback to temperature and pressure
            print(f"Note: Humidity sensor not working ({e})")
            
            # Show temperature instead
            temperature = sense.get_temperature_from_pressure()
            temp_adjusted = temperature - 7.0  # Adjust for Pi's heat
            print(f"Temperature: {temp_adjusted:.1f}°C")
            sense.show_message(f"Temp: {temp_adjusted:.1f}C", text_colour=[255, 0, 0])
            
            # Show pressure
            pressure = sense.get_pressure()
            print(f"Pressure: {pressure:.1f} mb")
            sense.show_message(f"Press: {pressure:.0f}mb", text_colour=[0, 255, 0])
            
    except Exception as e:
        print(f"Error: {e}")
        sense.clear()
        sense.show_letter("E", text_colour=[255, 0, 0])
        time.sleep(1)
        sense.clear()

def main():
    sense = SenseHat()
    print("Starting humidity monitor...")
    
    try:
        display_humidity(sense)
    except KeyboardInterrupt:
        print("\nProgram terminated")
        sense.clear()
    except Exception as e:
        print(f"Error: {e}")
        sense.clear()

if __name__ == "__main__":
    main()