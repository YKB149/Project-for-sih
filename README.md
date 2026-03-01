# AI Traffic Management System

An intelligent traffic signal control system designed to optimize traffic flow using real-time sensor data and automated timing calculations. The system integrates a Python Flask backend with Arduino sensors to dynamically adjust green light durations based on vehicle density across multiple lanes.

## 🚀 Features

- **Real-time Monitoring**: Collects data from Arduino-connected sensors across four lanes.
- **Dynamic Timing**: Calculates optimal green light duration per lane using a density-based algorithm.
- **Web Dashboard**: A Flask-powered interface to visualize current traffic timings and sensor status.
- **Hardware Integration**: Serial communication support for direct hardware-to-software data transfer.

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Data Processing**: NumPy
- **Hardware Communication**: PySerial
- **Frontend**: HTML5, CSS3
- **Hardware**: Arduino (for sensor data collection)

## 📂 Project Structure

```text
.
├── traffic/
│   ├── app.py              # Main Flask application & logic
│   ├── templates/          # HTML dashboard
│   └── static/             # CSS and JS assets
├── Source code.txt         # Additional source code references
├── nebula.pdf              # Project documentation/research
└── NewPPT_Traffic_light.pptx # Project presentation
```

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.x
- Arduino IDE (for sensor setup)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/ykbind/Ai-traffic-management.git
   cd Ai-traffic-management
   ```

2. **Install dependencies**:
   ```bash
   pip install flask numpy pyserial
   ```

3. **Configure Hardware**:
   - Connect your sensors to the Arduino.
   - In `traffic/app.py`, update the serial port to match your system (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux):
     ```python
     arduino = serial.Serial(port='YOUR_PORT_HERE', baudrate=9600, timeout=1)
     ```

4. **Run the application**:
   ```bash
   python traffic/app.py
   ```
   Navigate to `http://127.0.0.1:5000` in your web browser.

## 🚦 How It Works

1. **Sensing**: Sensors at each lane send vehicle counts to the Arduino.
2. **Transmission**: The Arduino transmits this data via Serial to the Flask app.
3. **Calculation**: The system calculates the proportion of vehicles in each lane relative to the total and assigns a proportional "Green Light" time based on a 30-second base cycle.
4. **Display**: The web interface fetches these timings via the `/get_timings` endpoint and displays them in real-time.

## 📄 Documentation
For detailed information regarding the logic and research behind this project, please refer to:
- [System Presentation (PPTX)](./NewPPT_Traffic_light.pptx)
- [Project Documentation (PDF)](./nebula.pdf)
