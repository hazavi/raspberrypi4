
# Raspberry Pi 4 Sense HAT Projects

This project includes Bash and Python scripts made for the Raspberry Pi and Sense HAT. It shows how to automate basic system tasks and use the Sense HAT’s sensors and LED display to interact with real-world data like temperature, humidity, and more.

---

## 📌 Project Overview

### 1. `linux_info.sh`
A Bash script for quick system setup and information gathering.

#### ✅ Features
- Creates a new user `testuser`
- Sets up a `Projects` folder in `/home/testuser/`
- Displays system/kernel and distribution information

#### ▶️ Usage
```bash
chmod +x linux_info.sh
./linux_info.sh
```

---

### 2. Sense HAT Applications

This part of the project uses the Raspberry Pi Sense HAT to create interactive and visual Python applications. These scripts use the LED matrix, sensors (temperature, humidity, pressure), and joystick to display data or play simple games.

#### 📁 Project Structure
```
senseHat/
├── src/
│   ├── senseHat.py           # Main entry point
│   ├── binary_clock.py       # Binary clock display
│   ├── joystick_events.py    # Joystick controls
│   ├── danish_flag.py        # Danish flag visual
│   ├── temperature_display.py# Temperature data
│   ├── humidity_display.py   # Humidity data
│   ├── snake_game.py         # Classic snake game
│   └── utils/helpers.py      # Shared utility functions
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

#### ⚙️ Setup
1. **Install Raspberry Pi OS**  
2. **Install the Sense HAT library**:
   ```bash
   sudo apt-get update
   sudo apt-get install sense-hat
   ```
3. **Clone the repo**:
   ```bash
   git clone <repository-url>
   cd senseHat
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### 🚀 Run the Application
```bash
python3 src/senseHat.py
```

#### 🎮 Functionalities
- **Binary Clock** – Shows time in binary on the LED matrix.
- **Joystick Navigation** – Switch between:
  - Danish Flag - Left
  - Temperature Display - Up
  - Humidity Display - Down
  - Snake Game - Right
- **Sensor Displays** – Real-time data from built-in sensors.
- **Games** – Simple interactive experiences like Snake.

---

### 3. Binary Clock as a Standalone Project

A focused application displaying the current time in binary on the LED matrix with support for display rotation and service automation.

#### 🌟 Features
- LED matrix time display in binary format
- Optional rotation angle (`-r 0|90|180|270`)
- Graceful signal termination (`SIGTERM`)
- Runs as a Linux service
- Includes a `Makefile` and a manual page

#### 🔧 Requirements
- Raspberry Pi with Sense HAT
- Python 3 + `sense-hat` library
- `pandoc` for man page generation

#### ⚙️ Setup
```bash
chmod +x binary_clock.py
```

#### ▶️ Usage

**Run manually:**
```bash
./binary_clock.py -r 90
```

---

### 🔄 Managing the Linux Service

| Action              | Command                                  |
|---------------------|------------------------------------------|
| Start service       | `sudo systemctl start binaryClock.service` |
| Check status        | `sudo systemctl status binaryClock.service` |
| Stop service        | `sudo systemctl stop binaryClock.service` |
| Enable on boot      | `sudo systemctl enable binaryClock.service` |
| Disable service     | `sudo systemctl disable binaryClock.service` |

---

### 🛠 Makefile Automation

| Task                  | Command               |
|-----------------------|------------------------|
| Run all tasks         | `make all`             |
| Delete temp folder    | `make delete_folder`   |
| Delete service        | `make delete_service`  |
| Restore service       | `make restore_service` |

---

### 📄 View the Man Page

```bash
man binary_clock
```

---

## 📜 License

This project is intended for educational purposes only.

