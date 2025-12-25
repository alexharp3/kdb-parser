
def Crypt(data: bytes, intialValue: int) -> bytes:
    S = intialValue & 0xFFFFFFFF # Initial state of the LSFR
    F = 0x87654321 # Feedback value
    result = bytearray() #empty byte array to store the result
    for byte in data:
        for _ in range(8):
            last_bit = S & 1
            if last_bit == 0:
                S = S >> 1
                S = S & 0xFFFFFFFF
            else:
                S = (S >> 1) ^ F
                S = S & 0xFFFFFFFF
        key_stream = S & 0xFF
        result.append(byte ^ key_stream)
    return bytes(result)

