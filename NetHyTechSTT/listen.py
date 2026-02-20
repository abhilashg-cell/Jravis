from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd

Recog_File = f"{getcwd()}\\input.txt"
def listen():
    print("Support in Youtube @NetHyTech")
    # Setting up Chrome options with specific arguments
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    # chrome_options.add_argument("--headless=old")  # Commented out to run in visible mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-renderer-backgrounding")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")

    # Use webdriver_manager to automatically manage ChromeDriver
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print(f"Failed to initialize Chrome WebDriver: {e}")
        print("Attempting to use local chromedriver.exe")
        try:
            service = Service(executable_path="chromedriver.exe")
            driver = webdriver.Chrome(service=service, options=chrome_options)
        except Exception as e2:
            print(f"Local chromedriver also failed: {e2}")
            print("Trying to disable headless mode and retry.")
            chrome_options.add_argument("--headless=new")  # Try new headless mode
            try:
                driver = webdriver.Chrome(service=Service(), options=chrome_options)
            except Exception as e3:
                print(f"All attempts failed: {e3}")
                raise e

    try:
        # Creating the URL for the website
        website = "https://allorizenproject1.netlify.app/"
        # Opening the website in the Chrome browser
        driver.get(website)

        start_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'startButton')))
        start_button.click()
        print("Listening...")
        output_text = ""
        is_second_click = False
        while True:
            output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'output')))
            current_text = output_element.text.strip()
            if "Start Listening" in start_button.text and is_second_click:
                if output_text:
                    is_second_click = False
            elif "Listening..." in start_button.text:
                is_second_click = True
            if current_text != output_text:
                output_text = current_text
                with open(Recog_File, "w") as file:
                    file.write(output_text.lower())
                    print("User:", output_text)
    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()
