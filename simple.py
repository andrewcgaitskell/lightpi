from bluepy import btle

print "Connecting..."
dev = btle.Peripheral("98:4F:EE:0D:16:59")
print "Services..."
for svc in dev.services:
    print str(svc)
