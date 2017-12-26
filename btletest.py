import binascii
import struct
import time
import uuid as uuidlib
from bluepy.btle import UUID, Peripheral

u = uuidlib.UUID('{14128a7604d16c4f7e53f2e81000b119}')
print u

button_uuid = UUID(u)
 
p = Peripheral("98:4f:ee:0d:16:59", "random")
 
try:
    ch = p.getCharacteristics(uuid=button_uuid)
    if (ch.supportsRead()):
        while 1:
            print str(val)
            time.sleep(1)
 
finally:
    p.disconnect()
