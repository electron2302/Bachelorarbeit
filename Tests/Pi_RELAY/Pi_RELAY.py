#
# Pulls a GPIO Pin High every minute and measurs time until a GPIO pin gets pulled up. 
# Extra message if pin doesnt get pulled up once or gets pulled up more than once within a minute 
#

from time import perf_counter_ns as timer
from time import sleep as sleep
import signal
import sys
import RPi.GPIO as GPIO

PIN_OUT_PULSE = 7
PIN_INPUT = 12

def handler_stop_signals(sig, frame):
    clean_up()

def clean_up():
    print("Exit")
    GPIO.cleanup()
    print("\n")
    sys.exit(0)
                     
def seput_GPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_OUT_PULSE, GPIO.OUT)
    GPIO.output(PIN_OUT_PULSE, GPIO.LOW)
    
    GPIO.setup(PIN_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(PIN_INPUT, GPIO.RISING, callback=pin_input_callback, bouncetime=500)

def pin_input_callback(channel):
    end = timer()
    global recived
    if not recived:
        recived = True
        line = "{time}".format(time = end - start)
        print(line)
        append_line(line)
    else:
        line = "Already got input_pulse"
        print(line)
        append_line(line)

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