
# 
import os
import time

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

while True:
        print(measure_temp())
        f = open("TempRecorder.txt","w")
        f.write(measure_temp() + "\n")
        f.close()
        time.sleep(2)
