
<meta name="google-site-verification" content="JXgz7W3BffQ4QY7erEV45-2MzLVBMTmIwsgtvPdGGN4" />


# LivePiLog
This project requires set up past the provided set up instructions customization to this project lies in a few places, the arduino code and the html file in templates. 
The most challenging part once your Pi is running stable is converting the analog voltage to units, I recommend this be done on the arduino, however it is possible to rely on the python code in (app.py) to convert values.

### Use Case & Value
The value I find out of this project is being able to read and log rpm & load data at the same time as my AFR data. Instead of being forced to glance at 3 different guages when road/self tuning.
Additionally you can look at this as a cost effective way to access guages and logging equipment for a fraction of general costs.
Currently the code reads 3 values, AFR, Load and RPM, the arduino prints to serial in .csv form which is then read and parsed by app.py. My plan is to use this with a screen 

There are tons of different ways to go about this project but it is purposed with getting you to a starting point on your custom guages and/or logging.

### Current Access Method
Currently I'm using a desktopless environment, and accessing the page with 192.168.x.x:5000 from a seperate device on the same network, if you need to change the port it is specified at the bottom of app.py. 
I plan on utilizing a screen connected to the Pi, which will autoboot to a browser(localhost:5000) using Chromium.

### AP MODE
If you interested in driving around with a broadcasting wifi network then you should find interest in the other option that will be released soon.
The other option will be to configure the Pi in AP mode so that you can connect to its network on any wifi supported device (phone, laptop, another pi).

### Web Page View
![image](https://github.com/user-attachments/assets/dd807cdb-63be-4c6b-b8f6-f34f1ad9e9fa)

### flask_app.service properly running 
![image](https://github.com/user-attachments/assets/e7e8715b-c836-4ab1-bd51-e1b5d964ad9d)



## Pi Configuration

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
   https://github.com/NateOlsonn/LivePiLog/blob/main/arduino/read.cpp

3. **Copy the code**:  
   Copy all of the code from the `read.cpp` file.

4. **Create a new sketch in the Arduino IDE**:  
   Open the Arduino IDE and create a new, empty file.

5. **Paste the copied code**:  
   Paste the copied code from the `read.cpp` file into the new sketch.

6. **Upload the code to the Arduino**:  
   Click the **Upload** button in the Arduino IDE to upload the code to your Arduino board.

7. **Connect the Arduino to the Raspberry Pi**:  
   To connect the Arduino to the Raspberry Pi, you will need a **Micro USB OTG Host to Standard B Type cable**.  
   You can purchase it from [Amazon here](https://www.amazon.com/dp/B06XXL8T45?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1).

Once the Arduino is uploaded with the code and connected to the Raspberry Pi, it will start sending data from each input.
Which should be visible on the webpage. 

