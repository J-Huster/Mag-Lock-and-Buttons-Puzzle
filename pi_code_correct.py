import requests
import json
import sys
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# API endpoint
url = "http://10.1.10.88:5000"




# Data to be sent (in JSON format)
payload = {
    "message": "Hello world! "
}
if len(sys.argv) > 1:
    payload['message'] = str(sys.argv[1])
    print(f"New message: {sys.argv[1]}")

# Request headers
headers = {
    "Content-Type": "application/json",
}

try:
    # Send the POST request
    response = requests.post(url + "/data", headers=headers, data=json.dumps(payload))

    # Check for successful response
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

    # Process the response
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    
time.sleep(120)   # program waits 2 minutes

# maglock is locked again
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.HIGH)

# redirects back to initial puzzle program 
os.system("python3 /home/liams/lockButtons.py")   # path should be changed
