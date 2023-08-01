import time
import requests
import pyautogui
import os
from datetime import datetime
import socket

server_url = 'http://localhost:5000/upload'
screenshot_interval = 30  # seconds

def take_screenshot():
    # Create an "screenshots" folder if it doesn't exist
    screenshots_folder = os.path.join(os.getcwd(), 'screenshots')
    os.makedirs(screenshots_folder, exist_ok=True)

    # Capture the screenshot and save it in the "screenshots" folder
    screenshot = pyautogui.screenshot()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_path = os.path.join(screenshots_folder, f'screenshot_{timestamp}.png')
    screenshot.save(screenshot_path)
    return screenshot_path

def send_screenshot_to_server(screenshot_path):
    # Open the screenshot file in binary mode
    with open(screenshot_path, 'rb') as f:
        # Send the screenshot file to the server using a POST request
        response = requests.post(server_url, files={'file': (os.path.basename(screenshot_path), f)}, data={'computer_name': socket.gethostname()})
        # Note: You may want to handle the response from the server here, e.g., check for success or errors.

while True:
    # Take a screenshot and get the path where it was saved
    screenshot_path = take_screenshot()
    
    # Send the screenshot to the server
    send_screenshot_to_server(screenshot_path)
    
    # Wait for the specified interval before taking the next screenshot
    time.sleep(screenshot_interval)
