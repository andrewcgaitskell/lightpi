import binascii
import struct
import time
import uuid as uuidlib
from bluepy.btle import UUID, Peripheral

u = uuidlib.UUID(u'14128a7604d16c4f7e53f2e81000b119')

print u

button_uuid = u # UUID(u)
 
p = Peripheral("98:4F:EE:0D:16:59", "random")
 
ch = p.getCharacteristics(uuid=button_uuid)

print(ch)

p.disconnect()
