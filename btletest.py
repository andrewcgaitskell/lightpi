import binascii
import struct
import time
import uuid as uuidlib
from bluepy.btle import UUID, Peripheral

u = uuidlib.UUID('{19B10010-E8F2-537E-4F6C-D104768A1214}')
print u

button_uuid = UUID(u)
 
p = Peripheral("98:4F:EE:0D:16:59", "random")
 
try:
    ch = p.getCharacteristics(uuid=button_uuid)[0]
    if (ch.supportsRead()):
        while 1:
            val = binascii.b2a_hex(ch.read())
            val = binascii.unhexlify(val)
            val = struct.unpack('f', val)[0]
            print str(val)
            time.sleep(1)
 
finally:
    p.disconnect()
