from geopy.geocoders import Nominatim

def get_coordinates():
    geolocator = Nominatim(user_agent="geo_locator")
    ip_address = get_public_ip()
    location = geolocator.geocode(ip_address)

    if location:
        # Extract latitude and longitude
        latitude, longitude = location.latitude, location.longitude
        print(f"Your GPS coordinates are: Latitude {latitude}, Longitude {longitude}")
    else:
        print("Unable to retrieve GPS coordinates.")

def get_public_ip():
    import requests
    response = requests.get('https://api64.ipify.org?format=json')
    ip_address = response.json()['ip']
    return ip_address

if __name__ == "__main__":
    get_coordinates()
