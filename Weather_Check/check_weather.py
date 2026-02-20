import requests
from bs4 import BeautifulSoup

def get_weather_by_address(address):
    # Use Google to find the weather for the address
    search_url = f"https://www.google.com/search?q=weather+{address.replace(' ', '+')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scrape the relevant weather data
        location_elem = soup.find("div", attrs={"id": "wob_loc"})
        time_elem = soup.find("div", attrs={"id": "wob_dts"})
        weather_elem = soup.find("span", attrs={"id": "wob_dc"})
        temp_elem = soup.find("span", attrs={"id": "wob_tm"})
        
        if not (location_elem and time_elem and weather_elem and temp_elem):
            return "Sorry, I couldn't extract the weather information. Google might have changed its layout."

        location = location_elem.text
        # time = time_elem.text # Unused in the output string
        weather = weather_elem.text
        temp = temp_elem.text
        
        weather_report = (f"Weather in {location}: {weather}\n"
                          f"Temperature: {temp}°C")
        
        return weather_report
    else:
        return "Error retrieving weather data."

