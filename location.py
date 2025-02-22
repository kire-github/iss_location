import requests
from datetime import datetime
from threading import Timer

FILE = "location.txt"
timer = 0
size = 0

def create_timer():
    t = Timer(10 * 60.0, save_location)
    t.start()

    global timer
    timer = t

def cancel_timer():
    global timer
    timer.cancel()


def get_time(timestamp):
    time = datetime.fromtimestamp(timestamp)
    return time.strftime("%H:%M,%m/%d")

def fetch_location():
    location = requests.get("http://api.open-notify.org/iss-now.json").json()

    time = get_time(location["timestamp"])
    latitude = location["iss_position"]["latitude"]
    longitude = location["iss_position"]["longitude"]

    return time, longitude, latitude

def save_location():
    try:
        with open(FILE, "a") as f:
            time, lon, lat = fetch_location()
            f.write(f"{time} {lon} {lat}\n")

            global size
            size += 1

            print(f"Wrote to file: {time} {lon} {lat}")
    except:
        print(f'Failed to fetch location or write to file at: {datetime.now().strftime('%m/%d,%H:%M')}')

    finally:
        create_timer()


def insert_breakpoint():
    try:
        options = input("Tracking <name color>: ").split(" ")
        name, color = options[0], options[1]
        global size

        with open(FILE, "a") as f:
            f.write(f"x {size} {color} {name}\n")
        print(f"Created new breakpoint at: {datetime.now().strftime('%m/%d,%H:%M')}")
    except:
        print(f'Could not insert breakpoint at: {datetime.now().strftime('%m/%d,%H:%M')}')