#2nd attempt door sensor server script
#Reversed server-client roles of web server and door server.
#This pi checks for door events and pushes updates to the web server

#Example request sent by this script:
# {
#   "isDoorOpen": true,
#   "time": 1629538651.9597645,
#   "humantime": "Sat Aug 21 11:37:31 2021"
# }

import requests
import time
import RPi.GPIO as GPIO

SERVER_ADDR = "https://hookb.in/W1NkmpggqKCYplzzpBay"
SWITCH_PIN = "GPIO2"

#Debug, replace with gpio read
def getDoorState():
    #GpIO.input might return 0, False or GPIO.LOW if the pin is low, convert to bool
    return True if GPIO.input(SWITCH_PIN) else False

def sendState(doorState):
    epochtime = time.time()
    timestamp = time.ctime()
    payload = {
        "isDoorOpen": doorState,
        "time": epochtime,
        "humantime": timestamp
    }

    response = requests.post(SERVER_ADDR, json=payload)
    print(response.text)


def main():
    GPIO.setmode(GPIO.BCM) #Set numbering scheme for other GPIO functions
    GPIO.setup(SWITCH_PIN, GPIO.IN) #Set our pin to input/read-mode

    #Wait for pin change, POST to server, repeat
    while True:
        GPIO.wait_for_edge(SWITCH_PIN, GPIO.BOTH) #Blocking wait, halts the program until the value changes

        doorState = getDoorState()
        sendState(doorState)


    


#Call main if file is directly invoked
if __name__ == '__main__':
    main()
