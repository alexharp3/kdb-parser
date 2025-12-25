import struct 

#This will allow us to work with 32 bit integers in little-endian format (entry list, block list, data) 
# this will also allow us to work woth 16 (size) bit integers in little-endian format
#Code used from this link https://blog.finxter.com/5-best-ways-to-convert-python-bytes-to-little-endian/
#b is the byte array, offset is where to read, and we will return a integer.
#we used struct unpack and <I is fo 32 bit and <H is for 16 bit
#b is the byte array, offset is where to read, and we will return a integer.
#the [0] is so we only get the integer value from the tuple that unpack returns.
def Read_32(b:bytes, offset:int) -> int:
    return struct.unpack_from('<I', b, offset)[0]

def Read_16(b:bytes, offset:int) -> int:
    return struct.unpack_from('<H', b, offset)[0]

def Read_Cstring(b:bytes, offset:int, n:int) -> str:
    raw = b[offset:offset+n].split(b'\x00',1)[0]
    return raw.decode('ascii', errors='replace')

#we have error replace so if there is a non ascii character it will be replaced and not cause an error
