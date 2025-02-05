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
