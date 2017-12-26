from bluepy import btle
import time
import binascii

print "Connecting..."
dev = btle.Peripheral("98:4F:EE:0D:16:59")
print "Services..."
for svc in dev.services:
    print str(svc)

ButtonSensor = btle.UUID("19b10010-e8f2-537e-4f6c-d104768a1214")
 
ButtonService = dev.getServiceByUUID(ButtonSensor)

while True:

    uuidValue  = btle.UUID("19b10011-e8f2-537e-4f6c-d104768a1214")

    ButtonValue = ButtonService.getCharacteristics(uuidValue)[0]
    # Read the sensor
    val = ButtonValue.read()
    print "Button Value 11", binascii.b2a_hex(val)

    uuidValue  = btle.UUID("19b10012-e8f2-537e-4f6c-d104768a1214")

    ButtonValue = ButtonService.getCharacteristics(uuidValue)[0]
    # Read the sensor
    val = ButtonValue.read()
    print "Button Value 12", binascii.b2a_hex(val)


    #for ch in ButtonService.getCharacteristics():
    #     print str(ch)
