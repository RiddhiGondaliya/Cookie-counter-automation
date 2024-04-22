# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import keyboard

# Function to get the current cookie count
def get_cookie_count(driver, cookies_id):
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    return int(cookies_count.replace(",", ""))

# Function to buy a product if the player has enough cookies
def buy_product(driver, cookies_count, product_price_prefix, product_prefix):
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break

# Path to the Google Chrome executable
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# WebDriver configuration
service = Service('C:/Users/Felipe/Desktop/Programação/Scripts python/GitHub/RiddhiGondaliya - Cookie-counter-automation/Cookie-counter-automation-main/Atualizado/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()
options.binary_location = chrome_path

# WebDriver initialization
driver = webdriver.Chrome(service=service, options=options)

# Open the "Cookie Clicker" game
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Try to load cookies from a previous game session
try:
    with open("cookies.pkl", "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
except FileNotFoundError:
    print("File 'cookies.pkl' not found. Continuing without loading cookies.")
except pickle.UnpicklingError:
    print("Error deserializing cookies. Continuing without loading cookies.")

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# Wait for the game to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# Click the language button to set the game language to English
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait for the big cookie to be present
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

# Find the big cookie
cookie = driver.find_element(By.ID, cookie_id)

pause = False

# Main game loop
while True:
    if keyboard.is_pressed('p'):  # If the 'p' key is pressed, pause the script
        pause = True
    if keyboard.is_pressed('r'):  # If the 'r' key is pressed, resume the script
        pause = False

    if not pause:
        # Click the big cookie
        cookie.click()
        # Get the current cookie count
        cookies_count = get_cookie_count(driver, cookies_id)
        # Try to buy a product
        buy_product(driver, cookies_count, product_price_prefix, product_prefix)