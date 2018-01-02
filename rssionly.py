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
    
print out

child.send("devices" + "\n")
time.sleep(pause)
start_failed = child.expect(["bluetooth", pexpect.EOF])
if start_failed:
    raise BluetoothctlError("Bluetoothctl failed after running " + command)

#out = child.before.split("\r\n")
out = child.before

for i in range(0, 10):
    print(i)
    time.sleep(1)

print type(out)

print out
device_count = out.count("Device")

out_working = out

dl = []

for dc in range(0,device_count):
    di = out_working.index("Device")
    dr = out_working.index("\r\n")
    dd = out_working[di:dr]
    dl.extend([dd])
    
print(dl)

dsplit = out.split("\r\n")
print(dsplit)

dsplit = out.split("Device")
print(dsplit)

rssilist = []

for ds in dsplit:
    try:
        rsi = ds.index("RSSI")
       
        dsa = ds.lstrip()
        dsas = dsa.split("\r\n")
        dsal = dsas[0].split(" ")
        dsala = [dsal[0],dsal[2]]
        rssilist.append(dsala)
    except:
        pass
    

print rssilist
    
