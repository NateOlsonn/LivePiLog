#!/bin/bash

# Set up the project directory (ensure you're in your project directory)
PROJECT_DIR="/LivePiLog"  # Update this to your actual project path

# Change to your project directory
cd "$PROJECT_DIR" || exit 1

# Step 1: Set up Python Virtual Environment
echo "Creating virtual environment..."
sudo python3 -m venv venv

# Step 2: Activate Virtual Environment
echo "Activating virtual environment..."
source venv/bin/activate

# Step 3: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt  # Assumes you have a 'requirements.txt' file

# Step 4: Deactivate the virtual environment
deactivate

# Step 5: Set up systemd to run the Flask app on boot
echo "Setting up systemd service..."

# Create a systemd service file
cat <<EOF | sudo tee /etc/systemd/system/flask_app.service
[Unit]
Description=Flask App
After=network.target

[Service]
User=nathan
WorkingDirectory=$PROJECT_DIR
ExecStart=$PROJECT_DIR/venv/bin/python $PROJECT_DIR/app.py
Restart=always
Environment=PATH=$PROJECT_DIR/venv/bin:$PATH
Environment=VIRTUAL_ENV=$PROJECT_DIR/venv
ExecStartPre=/bin/sleep 10

[Install]
WantedBy=multi-user.target
EOF


# Step 6: Enable the service to start on boot
sudo systemctl enable flask_app.service

# Step 7: Start the Flask app service immediately
sudo systemctl start flask_app.service

echo "Setup complete. Flask app will now run on boot."
