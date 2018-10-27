import mraa
import time


def in_range():
    TRIG = mraa.Gpio(8)
    ECHO = mraa.Gpio(9)


    TRIG.dir(mraa.DIR_OUT)
    ECHO.dir(mraa.DIR_IN)


    TRIG.write(0)
    time.sleep(2)

    TRIG.write(1)
    time.sleep(0.00001)
    TRIG.write(0)

    while ECHO.read() == 0:
        pulse_start = time.time()

    while ECHO.read() == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    GPIO.cleanup()

    if distance > 30:
        return False
    else:
        return True
