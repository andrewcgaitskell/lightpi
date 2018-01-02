import time
import pexpect
import subprocess
import sys
pause = 0

child = pexpect.spawn("bluetoothctl", echo = False)
child.send("scan on" + "\n")
time.sleep(pause)
start_failed = child.expect(["bluetooth", pexpect.EOF])
if start_failed:
    raise BluetoothctlError("Bluetoothctl failed after running " + command)
out = child.before.split("\r\n")
for i in range(0, 10):
    print(i)
    time.sleep(1)
child.send("devices" + "\n")


