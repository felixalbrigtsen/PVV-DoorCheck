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
SWITCH_PIN = 26 #GPIO2 when using BCM numbering
WAIT_TIMEOUT = 60000 #Miliseconds

#Debug, replace with gpio read
def getDoorState():
    doorState = bool(GPIO.input(SWITCH_PIN))
    return doorState


def sendState(doorState):
    epochtime = time.time()
    timestamp = time.ctime()
    payload = {
        "isDoorOpen": doorState,
        "time": epochtime,
        "humantime": timestamp
    }

    print("Sending doorState: " + str(payload) + "\n")

    response = requests.post(SERVER_ADDR, json=payload)
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


#Call main if file is directly invoked
if __name__ == '__main__':
    main()

###TODO
# -Hook into website
# -Autostart on boot
# -Check security
