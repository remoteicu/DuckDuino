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

### Python and Required Packages

1. Install Python and pip:

```bash
         sudo apt update
         sudo apt install python3
         sudo apt install python3-pip
```

2. Clone or download this project to your computer.

3. Open a terminal or command prompt and navigate to the project directory.

4. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```
Activate the virtual environment:

On macOS and Linux:
```bash
source venv/bin/activate
```
On Windows (PowerShell):
```powershell
.\venv\Scripts\Activate
```
Install the required Python packages:

```bash
pip install -r requirements.txt
```

Usage
1. Set up your Arduino with the converted Ducky Script.
2. Run the Python script app.py:
```bash
python app.py
```
The script will capture system information, take a screenshot, and send it to the specified Microsoft Teams channel via a webhook.

Note: Make sure to update the $UploadUrl variable in the PowerShell script to point to your server's upload endpoint.

Directory Structure
bash
Copy code
- app.py                 # Python script to capture and send data
- uploads/               # Directory for uploaded files
- README.md              # Project documentation
- LICENSE.md             # License information
- requirements.txt       # Python package dependencies
License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Setup

### Arduino Ducky Script

1. Upload the provided Arduino Ducky Script to your Arduino device using Arduino IDE.

> **_NOTE:_**  Make sure to select `Arduino Leonardo` under tools > board > boards manager, as well as select the correct COM Port.

## Usage

1. Insert the Arduino device into the target computer.
2. Wait for the script to execute.
3. The script will:
   - Capture a screenshot of the target computer.
   - Gather system information (computer name, username, IP address).
   - Upload the screenshot and information to the web server.
   - Send a message with the screenshot link to the specified Microsoft Teams channel using the webhook.
4. Check the Teams channel for the message with the screenshot and information.

## Configuration

### Arduino Ducky Script

- Modify the delays and keypresses in the Ducky Script as needed for your setup.

### PowerShell Script

- Update the `$teamsWebhookUrl` variable with your Microsoft Teams webhook URL.
- Update the `$UploadUrl` variable with the URL of the web server where the script is hosted.
- Adjust any other parameters in the PowerShell script as needed.

## Troubleshooting

- If you encounter issues, ensure that your Arduino device is properly configured and connected.
- Check the PowerShell script for any errors and make sure it is hosted on a reachable server.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
