# Sense HAT Project

This project is designed for the Raspberry Pi using the Sense HAT. It implements a variety of functionalities, including a binary clock, joystick event handling, and displays for temperature, humidity, and a Danish flag. Additionally, it features a simple snake game.

## Project Structure

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
└── README.md                # Project documentation
```

## Setup Instructions

1. **Install Raspberry Pi OS**: Ensure you have Raspberry Pi OS installed on your Raspberry Pi.

2. **Install the Sense HAT Library**: You can install the Sense HAT library using pip. Run the following command in your terminal:
   ```
   sudo apt-get update
   sudo apt-get install sense-hat
   ```

3. **Clone the Repository**: Clone this repository to your local machine:
   ```
   git clone <repository-url>
   cd senseHat
   ```

4. **Install Dependencies**: Navigate to the project directory and install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/senseHat.py
```

## Functionalities

- **Binary Clock**: Displays the current time in binary format on the Sense HAT LED matrix upon startup.
- **Joystick Events**: Listens for joystick pushes to switch between different displays:
  - Danish Flag
  - Temperature
  - Humidity
  - Snake Game
- **Danish Flag**: Draws the Danish flag on the LED matrix.
- **Temperature Display**: Retrieves and displays the current temperature from the Sense HAT's sensors.
- **Humidity Display**: Retrieves and displays the current humidity from the Sense HAT's sensors.
- **Snake Game**: A simple implementation of the classic snake game using the Sense HAT.

