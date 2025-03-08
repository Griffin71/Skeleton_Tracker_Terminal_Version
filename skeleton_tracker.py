import os
import time
import requests
import ipinfo
from geopy.geocoders import Nominatim
import re
import requests

# ASCII Art Skeleton Logo
ASCII_ART = """
        .-"      "-.
       /            \\
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \\o_)( |
      |/     /\\     \\|
      (_     ^^     _)
       \\__|IIIIII|__/
        | \\IIIIII/ |
        \\          /
         `--------`
   ~ Griffin71 ~
"""
    
# Country codes dictionary for phone number tracking
country_codes = {
    "South Africa": "ZA",
    "United States": "US",
    "United Kingdom": "GB",
    "India": "IN",
    "Australia": "AU",
    "Canada": "CA",
    "Germany": "DE",
    "France": "FR",
    "Brazil": "BR",
    "Japan": "JP",
    "Russia": "RU",
    "China": "CN",
    "Italy": "IT",
    "Spain": "ES",
    "Mexico": "MX",
    "Indonesia": "ID",
    "Nigeria": "NG",
    "Argentina": "AR",
    "Pakistan": "PK",
    "Bangladesh": "BD",
    "Netherlands": "NL",
    "Vietnam": "VN",
    "Turkey": "TR",
    "Iran": "IR",
    "Philippines": "PH",
    "Thailand": "TH",
    "Egypt": "EG",
    "Colombia": "CO",
    "Poland": "PL",
    "Saudi Arabia": "SA",
    "Malaysia": "MY",
    "Ukraine": "UA",
    "Peru": "PE",
    "Venezuela": "VE",
    "Australia": "AU",
    "Chile": "CL",
    "Romania": "RO",
    "Czech Republic": "CZ",
    "Portugal": "PT",
    "Sweden": "SE",
    "Hungary": "HU",
    "Belgium": "BE",
    "Greece": "GR",
    "Norway": "NO",
    "Austria": "AT",
    "Switzerland": "CH",
    "Hong Kong": "HK",
    "Denmark": "DK",
    "Finland" : "FK",
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_intro():
    print(ASCII_ART)
    print("I'm Griffin, you can check me out at github.com/Griffin71 and star my projects and follow me at instagram.com/okaygriffy.")
    print("While we are at it, it's important to note that skeleton_tracker is a free software and only distributed via terminal unless otherwise(THERE'S A WEBSITE IN DEVELOPMENT RN!!! XD).")
    print("Using this software, you are agreeing to the terms and conditions.")
    print("THIS IS FOR EDUCATIONAL PURPOSES so anything that comes after meaning law, unethical conduct/ misuse of the product, you're accountable for it, not me.")
    print("Read more in the terms and conditions.\n")

def print_menu():
    print("1. Track IP Address")
    print("2. Track Device (Geolocation)")
    print("3. Track Location by Phone Number")
    print("4. Terms and Conditions")
    print("5. Help")
    print("6. Display Your IP Location")  # New option
    print("7. Exit")


# Function to get the user's IP location
def get_user_ip_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        
        print("\nFetching your IP location...")
        time.sleep(3)  # Give the user a moment to see the information
        print(f"IP: {data['ip']}")
        print(f"Location: {data['city']}, {data['region']}, {data['country']}")
        print(f"Coordinates: {data['loc']}")
        
        # Keep the information displayed until the user chooses to go back to the menu
        while True:
            user_input = input("\nDo you want to return to the menu? (y/n): ")
            if user_input.lower() == 'y':
                return
            elif user_input.lower() == 'n':
                print("\nStill showing your IP location... You can press Ctrl+C to exit.")
                continue
            else:
                print("Invalid input, please type 'y' or 'n'.")
    except Exception as e:
        print(f"Error fetching IP location: {e}")


def is_valid_ip(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)
    if match:
        return all(0 <= int(group) <= 255 for group in match.groups())  # Ensures each part is 0-255
    return False
# Function to track the IP
def track_ip():
    attempts = 3
    while attempts > 0:
        ip = input("Enter a valid IP Address (e.g., 192.168.154.133): ")
        if not is_valid_ip(ip):
            attempts -= 1
            print(f"Invalid IP Address. Please enter a full valid IPv4 address. {attempts} attempt(s) left.")
            if attempts == 0:
                print("Skeleton is redirecting you to the main menu...\n")
                time.sleep(2)
                return  # Return to main menu
            continue
        
        access_token = "a8bf925d933553"  # Replace with your API key
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip)
        
        if not details.city:
            print("\nThe IP Address does not exist or cannot be tracked.")
            print("Skeleton is redirecting you to the main menu...\n")
            time.sleep(5)
            return  # Return to main menu
        
        print("\nTracking IP...")
        time.sleep(6)  # Simulate loading time
        print(f"IP: {details.ip}")
        print(f"City: {details.city}")
        print(f"Region: {details.region}")
        print(f"Country: {details.country}")
        print(f"Coordinates: {details.loc}")
        print(f"ISP: {details.org}")
        
        # After displaying the IP details, ask if the user wants to go back to the menu or continue
        user_input = input("\nDo you want to return to the main menu? (y/n): ")
        if user_input.lower() == 'y':
            return  # Return to the main menu
        elif user_input.lower() == 'n':
            print("You can continue viewing the IP details. Press Ctrl+C to exit at any time.")
            time.sleep(5)  # Allow some time before prompting again
        else:
            print("Invalid input. Please type 'y' to return to the main menu or 'n' to stay here.")

def track_device():
    geolocator = Nominatim(user_agent="geo_tracker")

    try:
        # Fetch approximate location via IP
        print("\nFetching device location...")
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        coordinates = data.get("loc", None)  # Example: "37.7749,-122.4194"
        
        if coordinates:
            location = geolocator.reverse(coordinates)
            print(f"IP-Based Location: {location.address}")
            print(f"Coordinates: {coordinates}")
        
        # HTML5 Geolocation API (More Accurate)
        print("\nTrying to get a more accurate location via GPS...")
        import geocoder
        gps_location = geocoder.ip('me')  # Fetch location using GPS if available

        if gps_location.latlng:
            print(f"GPS-Based Location: {gps_location.address}")
            print(f"Coordinates: {gps_location.latlng}")
        
    except Exception as e:
        print("Error fetching location:", e)

# Run function
track_device()


def track_location_by_phone():
    print("Select your country:")
    # Display country options
    for i, country in enumerate(country_codes.keys(), 1):
        print(f"{i}. {country}")
    
    try:
        choice = int(input("Enter the number of your country: "))
        
        if choice < 1 or choice > len(country_codes):
            print("Invalid selection. Please select a valid country number.")
            return
        
        # Get the selected country code
        country_name = list(country_codes.keys())[choice - 1]
        country_code = country_codes[country_name]
        
        phone_number = input(f"Enter your phone number (without country code, e.g., 0700000000 for {country_name}): ")
        
        # Remove spaces and handle formatting
        phone_number = phone_number.strip()
        
        # Check if phone number starts with 0 (common for some countries like SA)
        if phone_number.startswith("0"):
            phone_number = phone_number[1:]  # Remove the leading zero
        
        # Format the phone number with the country code
        formatted_number = f"+{country_code}{phone_number}"
        
        # API key for NumVerify
        api_key = "ee46261de4feab186a706e874e0af2fa"
        
        # Prepare the API URL with the correct parameters
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={formatted_number}&country_code={country_code}&format=1"
        
        # Send the request to the API
        response = requests.get(url)
        
        # Debugging: Print the raw response to check for issues
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        
        # Parse the response from the API
        data = response.json()
        
        if response.status_code == 200 and data.get('valid'):
            # Extract location data from the response
            country = data.get('country_name')
            location = data.get('location', "No location data available")
            print(f"Phone number {formatted_number} is valid.")
            print(f"Location: {country}, {location}")
        else:
            print("Invalid phone number or unable to fetch location.")
    except ValueError:
        print("Invalid input. Please enter a valid number for your country selection.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while contacting the API: {e}")

def show_terms_and_conditions():
    print("\nTerms and Conditions:\n")
    print("1. This software is free for educational purposes.")
    print("2. Misuse or unethical conduct using this software is your responsibility.")
    print("3. By using this software, you agree to the terms and conditions outlined.")
    print("4. We do not track or store sensitive data unless explicitly stated.")
    print("5. Any legal issues arising from misuse of the software are not the responsibility of the developers.\n")

def show_help():
    print("\nHelp Menu:\n")
    print("1 - Track an IP Address and get location info.")
    print("2 - Track your device's location (if allowed).")
    print("3 - Track location based on phone number.")
    print("4 - Show the Terms and Conditions.")
    print("5 - Show this Help menu.\n")

def main():
    clear_screen()
    print_intro()
    
    while True:
        print_menu()
        
        choice = input("Select an option (1-7): ")
        
        if choice == "1":
            track_ip()
        elif choice == "2":
            track_device()
        elif choice == "3":
            track_location_by_phone()
        elif choice == "4":
            show_terms_and_conditions()
        elif choice == "5":
            show_help()
        elif choice == "6":
            get_user_ip_location()
        elif choice == "7":
            print("Exiting program... Thank you for using Skeleton Tracker!")
            break
        else:
            print("Invalid choice, please try again.")
        

if __name__ == "__main__":
    main()
