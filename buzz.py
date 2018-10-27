import mraa
import time
from range_sensor import in_range

def buzz():
	BUZZER = mraa.Gpio(7)
	BUZZER.dir(mraa.DIR_OUT)

	BUZZER.write(1)
	time.sleep(3)
	BUZZER.write(0)
	time.sleep(3)


buzz()
