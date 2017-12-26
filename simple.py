from bluepy import btle

print "Connecting..."
dev = btle.Peripheral("98:4F:EE:0D:16:59")
print "Services..."
for svc in dev.services:
    print str(svc)

ButtonSensor = btle.UUID("19b10010-e8f2-537e-4f6c-d104768a1214")
 
ButtonService = dev.getServiceByUUID(ButtonSensor)

for ch in ButtonService.getCharacteristics():
     print str(ch)
