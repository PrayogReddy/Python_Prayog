import requests
try:
    response = requests.get("https://google.com/", timeout=10)    
    if response.status_code == 200:
        print("Success! Google is online and reachable.")
    else:
        print(f"Google returned a status code: {response.status_code}")
except Exception as e:
    print(f"Could not connect: {e}")