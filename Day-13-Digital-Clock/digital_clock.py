import time 
from datetime import datetime

def display_clock():
    print("=================================")
    print("         DIGITAL CLOCK")
    print("==================================")
    try:
        while True:
            current_time = datetime.now()
            time_value = current_time.strftime("%H:%M:%S")
            date_value = current_time.strftime("%d-%m-%Y")
            day_value = current_time.strftime("%A")
            print(f"\rTime:{time_value} | Date:{date_value}|Date:{day_value}",
                  end ="",
                  flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
            print("\n\nClock stopped. Goodbye!") 
display_clock()               
