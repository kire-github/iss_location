import requests
from datetime import datetime
from threading import Timer

def fetch_location():
    location = requests.get("http://api.open-notify.org/iss-now.json").json()

    time = get_time(location["timestamp"])
    latitude = location["iss_position"]["latitude"]
    longitude = location["iss_position"]["longitude"]

    return time, longitude, latitude

def get_time(timestamp):
    time = datetime.fromtimestamp(timestamp)
    return time.strftime("%H:%M,%m/%d")

def save_location():
    try:
        with open("location.txt", "a") as f:
            time, lon, lat = fetch_location()
            f.write(f"{time} {lon} {lat}\n")

            print(f"Wrote to file: {time} {lon} {lat}")
    except:
        print(f'Failed to fetch location at or write to file: {datetime.now().strftime('%m-%d %H:%M')}')

    finally:
        create_timer()

def create_timer():
    t = Timer(10 * 60.0, save_location)
    t.start()

if __name__ == "__main__":
    save_location()