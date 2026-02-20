# pip install psutil
# CTRL + J Terminal 

import psutil
import time
import time
from Brain.personality import jarvis_speak
import threading
from Alert import Alert

battery = psutil.sensors_battery()

def battery_Alert():
    while True:
        time.sleep(3)
        percentage = int(battery.percent)
        if percentage == 100:
            t1 = threading.Thread(target=Alert,args=("100%charge",))
            t2 = threading.Thread(target=jarvis_speak,args=("Battery fully charged. Please unplug the charger.", "success"))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 20:
            t1 = threading.Thread(target=Alert,args=("Battery Low",))
            t2 = threading.Thread(target=jarvis_speak,args=("Battery level is low.", "warning"))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <=10:
            t1 = threading.Thread(target=Alert,args=("Battery is too Low",))
            t2 = threading.Thread(target=jarvis_speak,args=("Battery level is critical.", "warning"))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 5:
            t1 = threading.Thread(target=Alert,args=("Battery is going to died",))
            t2 = threading.Thread(target=jarvis_speak,args=("System will shut down soon. Connect power immediately.", "error"))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        time.sleep(10)




def check_plug():
    print("_____started___")
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged
    while True:
        battery = psutil.sensors_battery()
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                t1 = threading.Thread(target=Alert,args=("Charging **STARTED**",))
                t2 = threading.Thread(target=jarvis_speak,args=("Charging started.", "success"))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
            else:
                t1 = threading.Thread(target=Alert,args=("Charging **STOP**",))
                t2 = threading.Thread(target=jarvis_speak,args=("Charging stopped.", "warning"))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
      
            previous_state = battery.power_plugged



def check_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    t1 = threading.Thread(target=Alert,args=(f"The device is running on {percent}% power",))
    t2 = threading.Thread(target=jarvis_speak,args=(f"Power level is at {percent}%.",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    

