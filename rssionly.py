import time
import pexpect
import subprocess
import sys

child = pexpect.spawn("bluetoothctl", echo = False)
child.send("scan on" + "\n")
for i in range(0, 10):
    print(i)
    time.sleep(1)
print child.before.split("\r\n")

