# Rasberry Pi 4

#### **Project Overview**
This project includes a Bash script (`linux_info.sh`) and Python scripts for interacting with the Raspberry Pi's Sense HAT.

---

### **1. `linux_info.sh`**

#### **Description**
The `linux_info.sh` script performs the following tasks:
1. Creates a new user named `testuser`.
2. Creates a `Projects` directory in `/home/testuser/`.
3. Displays system and kernel information.
4. Prints Linux distribution details.

#### **Usage**
```bash
chmod +x linux_info.sh
./linux_info.sh
```

---

### **2. Sense HAT Scripts**

#### **Features**
- Display temperature, pressure, and humidity.
- Handle joystick events to trigger actions like displaying flags or starting snake game.
- Show a binary clock on the LED matrix.

#### **Key Scripts**
- `humidity_display.py`: Displays humidity or fallback data.
- `joystick_events.py`: Handles joystick interactions.
- `danish_flag.py`: Displays the Danish flag.
- `snake_game.py`: Starts snake game.
- `binary_clock.py`: Shows a binary clock.
- 
### Project Structure

```
senseHat
├── src
│   ├── senseHat.py          # Main entry point of the application
│   ├── binary_clock.py      # Displays the current time in binary format
│   ├── joystick_events.py    # Manages joystick events
│   ├── danish_flag.py       # Draws the Danish flag
│   ├── temperature_display.py # Displays current temperature
│   ├── humidity_display.py   # Displays current humidity
│   ├── snake_game.py        # Implements the snake game
│   └── utils
│       └── helpers.py       # Utility functions
├── requirements.txt         # Project dependencies
```

#### **Run a Script**
```bash
python3 <script_name>.py
```


---

### **3. Requirements**

 **Install Raspberry Pi OS**: Ensure you have Raspberry Pi OS installed on your Raspberry Pi.
 
#### **Hardware**
- Raspberry Pi with Sense HAT

#### **Software**
- Python 3
- Sense HAT library
```
sudo apt-get update
sudo apt-get install sense-hat
 ```

#### **Install Dependencies**
```bash
sudo apt-get update
sudo apt-get install sense-hat python3-sense-hat
```

## Usage

To run the application, execute the following command:
```
python3 src/senseHat.py
```

