# Pluggie Victim Information Tool

This tool allows you to capture a screenshot, gather system information, and send it to a Microsoft Teams channel using a webhook. It consists of two parts: an Arduino Ducky Script and a PowerShell script.

## Prerequisites

- An Arduino device compatible with Ducky Script (e.g., Rubber Ducky).
- An internet-connected computer running Windows with PowerShell.
- Access to a Microsoft Teams channel with a configured incoming webhook.
- A web server where you can host the PowerShell script.

## Setup

### Arduino Ducky Script

1. Upload the provided Arduino Ducky Script to your Arduino device.

### PowerShell Script

1. Host the PowerShell script (`run.ps1`) on a web server that is accessible from your computer.

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
- Adjust any other parameters in the PowerShell script as needed.

## Troubleshooting

- If you encounter issues, ensure that your Arduino device is properly configured and connected.
- Check the PowerShell script for any errors and make sure it is hosted on a reachable server.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.