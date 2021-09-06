#Client for PVV door sensor. Made for raspberry pi.
#Example POST-request sent by this script:
# {
#   "isDoorOpen": true,
#   "time": 1629538651
# }

import requests
import time
import math
import RPi.GPIO as GPIO

SERVER_ADDR = "https://www.pvv.ntnu.no/door/"
SWITCH_PIN = 26 #GPIO26 when using BCM numbering
WAIT_TIMEOUT = 10 * 60 * 1000 #Miliseconds
SECRET = "BEARER TOKEN SECRET GOES HERE"

headers = {'Authorization': f'Bearer {SECRET}'}

#Debug, replace with gpio read
def getDoorState():
    doorState = bool(GPIO.input(SWITCH_PIN))
    return doorState


def sendState(doorState):
    epochtime = math.floor(time.time())
    payload = {
        "isDoorOpen": doorState,
        "time": epochtime,
    }

    print("Sending doorState: " + str(payload) + "\n")

    response = requests.post(SERVER_ADDR, json=payload, headers=headers)
    print(response.text)


def main():
    GPIO.setmode(GPIO.BCM) #Set numbering scheme for other GPIO functions
    GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Set our pin to input/read-mode

    #Send on startup
    sendState(getDoorState())

    #Wait for pin change, POST to server, repeat
    while True:
        #NOTICE: the following statement will block everything, including keyboard interrupts from the shell
        GPIO.wait_for_edge(SWITCH_PIN, GPIO.BOTH, timeout=WAIT_TIMEOUT) #Blocking wait, halts the program until the value changes, or timeout is reached

        doorState = getDoorState()
        sendState(doorState)


#Call main if file is directly invoked, not imported
if __name__ == '__main__':
    main()
