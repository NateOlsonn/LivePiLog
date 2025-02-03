from flask import Flask, render_template, jsonify
import serial
import csv
import time

app = Flask(__name__)

# Serial port settings - update the port if needed (e.g., '/dev/ttyUSB0' on Linux or 'COM3' on Windows)
SERIAL_PORT = '/dev/ttyACM0'  # Update this to your actual serial port
BAUD_RATE = 9600

# Set up serial connection
def get_serial_data():
    # Initialize the serial connection (make sure the Arduino is connected)
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)  # Timeout for reading
        time.sleep(2)  # Wait for the connection to establish
        ser.flushInput()  # Clear input buffer
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None
    
    try:
        # Read the data from Arduino over serial (assuming CSV format)
        data = ser.readline().decode('utf-8').strip()  # Read a line of data
        if data:
            # Parse the CSV data into a dictionary
            reader = csv.DictReader([data], fieldnames=["rpm", "maf", "afr"])  # Assuming CSV headers
            for row in reader:
                # Convert values to appropriate types
                rpm = int(row["rpm"])
                maf = float(row["maf"])
                afr = float(row["afr"])
                return {'rpm': rpm, 'maf': maf, 'afr': afr}
    except Exception as e:
        print(f"Error reading serial data: {e}")
        return None
    finally:
        ser.close()  # Close the serial connection

# Define a route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to get live data (from Arduino through serial)
@app.route('/live-data')
def live_data():
    data = get_serial_data()
    if data:
        return jsonify(data)  # Send parsed data to the frontend
    else:
        return jsonify({'rpm': 0, 'maf': 0, 'afr': 0})  # Return default values if error occurs

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
