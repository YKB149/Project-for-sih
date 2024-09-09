from flask import Flask, jsonify, render_template
import time
import numpy as np
import serial

# Initialize Flask app
app = Flask(__name__)

# Initialize serial communication with Arduino (replace 'COM3' with your correct port)
arduino = serial.Serial(port='8', baudrate=9600, timeout=1)

# Function to read sensor data from Arduino
def read_sensors():
    try:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            data = line.split(',')
            if len(data) == 4:
                return {
                    'lane1': int(data[0]),
                    'lane2': int(data[1]),
                    'lane3': int(data[2]),
                    'lane4': int(data[3])
                }
    except Exception as e:
        print(f"Error reading from Arduino: {e}")
    return {
        'lane1': 0,
        'lane2': 0,
        'lane3': 0,
        'lane4': 0
    }

# Function to calculate traffic signal timing based on sensor data
def calculate_timing(sensor_data):
    total_vehicles = sum(sensor_data.values())
    base_time = 30  # Base green light time in seconds

    # Calculate time per lane based on vehicle count
    timing = {}
    for lane, count in sensor_data.items():
        if total_vehicles > 0:
            timing[lane] = base_time * (count / total_vehicles)
        else:
            timing[lane] = base_time

    return timing

# Route for the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to provide current traffic signal timings as JSON
@app.route('/get_timings')
def get_timings():
    sensor_data = read_sensors()
    timing = calculate_timing(sensor_data)
    return jsonify(timing)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
