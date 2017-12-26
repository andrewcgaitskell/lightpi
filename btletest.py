import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral
 
button_uuid = UUID("0x19b10012-e8f2-537e-4f6c-d104768a1214")
 
p = Peripheral("98:4F:EE:0D:16:59", "random")
 
try:
    ch = p.getCharacteristics(uuid=tbutton_uuid)[0]
    if (ch.supportsRead()):
        while 1:
            val = binascii.b2a_hex(ch.read())
            val = binascii.unhexlify(val)
            val = struct.unpack('f', val)[0]
            print str(val)
            time.sleep(1)
 
finally:
    p.disconnect()
