import time
import pexpect
import subprocess
import sys

child = pexpect.spawn("bluetoothctl", echo = False)
child.send("scan on" + "\n")
print child.before.split("\r\n")

