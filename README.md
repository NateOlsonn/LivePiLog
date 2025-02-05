# LivePiLog
This repo supports a custom live logging software to display things like RPM, Load, AFR, and more. This project uses a Pi-0-W and an Arduino with analog input. Utilizing this repo on your own hardware requires understanding how to obtain data from your engines ECU, or specific sensors. You can piggyback off of your ecu pin-holes or do some splicing

## Setup Instructions

Assuming your Raspberry Pi is configured to boot and connect to WiFi with shell access, follow these steps to set up your project:

1. **Navigate to your desired directory** (or the default home directory you boot into).

2. **Clone the repository**:  
   `git clone https://github.com/NateOlsonn/LivePiLog`

3. **Change into the project directory**:  
   `cd LivePiLog`

4. **Make the setup script executable**:  
   `chmod +x setup.sh`

5. **Run the setup script**:  
   `./setup.sh`

6. **Check the status of the service**:  
   `sudo systemctl status flask_app.service`

7. **Reboot the Raspberry Pi**:  
   `sudo reboot`

Once the reboot is complete, your application should be up and running.


## Arduino Configuration

Follow these steps to configure your Arduino to connect with the Raspberry Pi:

1. **Access the Arduino code**:  
   Navigate to the following file in the repository:  
   [LivePiLog Arduino Code](https://github.com/NateOlsonn/LivePiLog/arduino/read.cpp)

2. **Copy the code**:  
   Copy all of the code from the `read.cpp` file.

3. **Create a new sketch in the Arduino IDE**:  
   Open the Arduino IDE and create a new, empty file.

4. **Paste the copied code**:  
   Paste the copied code from the `read.cpp` file into the new sketch.

5. **Upload the code to the Arduino**:  
   Click the **Upload** button in the Arduino IDE to upload the code to your Arduino board.

6. **Connect the Arduino to the Raspberry Pi**:  
   To connect the Arduino to the Raspberry Pi, you will need a **Micro USB OTG Host to Standard B Type cable**.  
   You can purchase it from [Amazon here](https://www.amazon.com/dp/B06XXL8T45?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1).

Once the Arduino is uploaded with the code and connected to the Raspberry Pi, it will be ready to communicate.

