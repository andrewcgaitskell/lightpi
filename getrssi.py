import subprocess, time, os, sys

MAC_ADDR = "XX:XX:XX:XX:XX:XX"

thecommand = "sudo ./btmon"
thecommand2 = "sudo hcitool lescan"
last_seen = 0
last_rssi = 0
lastn = 0

cmd = thecommand.split(" ")
cmd2 = thecommand2.split(" ")

p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

p2 = subprocess.Popen(cmd2,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

n = 0
for line in iter(p.stdout.readline, b''):
    n = n + 1
    g = 0
    #print(line.rstrip())
    if(MAC_ADDR in line.rstrip()):
        last_seen = time.time()
        lastn = n
    if("RSSI:" in line.rstrip() and (n-lastn)<10):
        a =  line.rstrip()
        last_rssi = int(a.split("RSSI: ")[1].split("dBm")[0])
        g = 1

    if(g==1):
        print last_rssi
