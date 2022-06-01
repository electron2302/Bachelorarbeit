#
# Pulls a GPIO Pin High every minute and measurs time until it Recives a UDP Package
# Extra message if no or to many Package(s) arrive(s) within a minute 
#

import threading
from time import perf_counter_ns as timer
from time import sleep as sleep
import signal
import sys
import RPi.GPIO as GPIO
import socket

PIN_OUT_PULSE = 7
UDP_SOCK_IP = "10.10.10.21" # localhost IP
UDP_PORT = 6666
MESSAGE = b"Hi"

def handler_stop_signals(sig, frame):
    clean_up()

def clean_up():
    print("Exit")
    GPIO.cleanup()
    sock.close()
    print("\n")
    sys.exit(0)

def setup_udp():
    # Datagram (udp) socket
    try :
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print ("Socket created")
    except socket.error as msg :
        print ('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        clean_up()

    # Bind socket to local host and port
    try:
        sock.bind((UDP_SOCK_IP, UDP_PORT))
        print ('Socket bind complete')
    except socket.error as msg:
        print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        clean_up()

    udpThread = threading.Thread(target=wait_for_udp, args=(sock,), daemon=True)
    udpThread.start()

def wait_for_udp(sock): #TODO: check content;
    while True:
        data, addr = sock.recvfrom(8) # buffer size is 1024 bytes
        global recived
        if data == MESSAGE and not recived:
            end = timer()
            recived = True
            line = "{time}".format(time = end - start)
            print(line)
            append_line(line)
        elif not recived:
            line = "wrong message"
            print(line)
            append_line(line)
        else: 
            line = "already recived a message"
            print(line)
            append_line(line)
                     
def seput_GPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_OUT_PULSE, GPIO.OUT)
    GPIO.output(PIN_OUT_PULSE, GPIO.LOW)
    

def append_line(line):
    if not line.endswith("\n"):
        line += "\n"

    file = open("output.txt", "a")  # append mode
    file.write(line)
    file.close()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler_stop_signals)
    signal.signal(signal.SIGTERM, handler_stop_signals)

    seput_GPIO()
    setup_udp()

    append_line("new run")

    global start
    global end
    global recived
    recived = True

    while True:
        if not recived:
            line = "not recived"
            print(line)
            append_line(line)
        recived = False
        start = timer()
        GPIO.output(PIN_OUT_PULSE, GPIO.HIGH)
        sleep(0.25)
        GPIO.output(PIN_OUT_PULSE, GPIO.LOW)
        sleep(60)