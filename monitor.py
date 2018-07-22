# Stating my name and the version number at the begining of the program.
print("Raspberry Pi Temperature Monitor")
print("Version 0.1: By Alexander Munoz")

import os
import time

time.sleep(3)

t_end = time.time() + 10
while time.time() < t_end:
	cmd = '/opt/vc/bin/vcgencmd measure_temp'
	os.system( cmd )
