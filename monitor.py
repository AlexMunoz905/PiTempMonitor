print("Raspberry Pi Temperature Monitor")
print("Version 0.1: By Alexander Munoz")

import subprocess
import os

cmd = '/opt/vc/bin/vcgencmd measure_temp'
os.system( cmd )
