# Skeleton Tracker (Terminal Version)

## Overview
Skeleton Tracker is a terminal-based tool designed for educational purposes. It allows users to track IP addresses, geolocate devices, and retrieve location data based on phone numbers. The tool is currently distributed exclusively through the terminal, with a website version in development.

## Features
- Track IP addresses and retrieve location details.
- Obtain device geolocation using IP-based tracking.
- Track location based on phone numbers using country codes.
- Display the user's own IP location.
- Educational and informational use only.

## Installation
To use Skeleton Tracker, ensure you have Python installed along with the required dependencies:

### Prerequisites
- Python 3.x
- Required Python libraries:
  - `requests`
  - `ipinfo`
  - `geopy`
  - `geocoder`

### Installation Steps
1. Clone or download the repository:
   ```sh
   git clone https://github.com/Griffin71/Skeleton_Tracker_Terminal_Version.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Skeleton_Tracker_Terminal_Version
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the script:
   ```sh
   python skeleton_tracker.py
   ```

## Usage
Upon launching the program, the ASCII skeleton logo appears along with an introduction and disclaimer. Users can select from the following menu options:

1. **Track IP Address**: Enter an IP address to retrieve details such as city, country, and ISP.
2. **Track Device (Geolocation)**: Get an approximate location based on the device's IP address.
3. **Track Location by Phone Number**: Input a phone number to retrieve location details using country codes.
4. **Terms and Conditions**: View the disclaimer and terms of use.
5. **Help**: Access general usage information.
6. **Display Your IP Location**: Retrieve and display the user's own IP location.
7. **Exit**: Close the program.

## Important Notes
- This tool is **strictly for educational purposes**.
- Users are responsible for any misuse of the software.
- Data accuracy depends on the external APIs used.
- Some features require an internet connection.

## API Keys
Skeleton Tracker uses third-party services for geolocation. Ensure you replace placeholder API keys in the script with your own:
- **ipinfo.io API Key**: Used for IP address tracking.
- **NumVerify API Key**: Used for phone number validation and tracking.

## Future Developments
- **Website version** is under development.
- **Enhanced security** to prevent misuse.
- **Improved accuracy** for geolocation services.

## Contact & Contributions
- GitHub: [github.com/Griffin71](https://github.com/Griffin71)
- Instagram: [instagram.com/okaygriffy](https://instagram.com/okaygriffy)

Feel free to star the repository and contribute to future updates!

