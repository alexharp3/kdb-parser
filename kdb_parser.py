from kdb_crypt import Crypt
from struct_utils import Read_32, Read_16, Read_Cstring

MAGIC = b"CT2018"
END = 0xFFFFFFFF # given to us as being the end of lists

def is_entryList(b:bytes, ptr:int) -> bool:
#checks if the entry list pointer is valid
    if ptr == END:
        return False
#We know that entry list char[16] and int32 bits for block list pointer is 4 bytes
#20 is the minimum size of an entry list, so this prevents reading out of bounds
    if ptr < 0 or ptr + 20 > len(b):
        return False 
    name_byte = b[ptr:ptr+16].split(b'\x100',1)[0]
    if name_byte:
        for c in name_byte:
            if c < 32 or c > 126:
                return False
    block_list_ptr = Read_32(b, ptr + 16)
    if block_list_ptr == END:
        return True
    return 0 <= block_list_ptr < len(b)

    
def look_for_entryList(b:bytes) ->int:
    #we know the magic is 6 bytes long 
    #we also know that the next part without padding is 32 bit which is 4 bytes 
    #if fail put greater or equal to 10 and 12
    possible_entryList = [] 
    if len(b) >= 10:
        possible_entryList.append(Read_32(b, 6))
    #sometimes c style can have padding. since 4 byte alignment is common we will check offset 8 as well
    if len(b) >= 12:
        possible_entryList.append(Read_32(b, 8))
    #no we will take both of these and apply the is_entryList function to see if they are valid
    for ptr in possible_entryList:
        if is_entryList(b, ptr):
            return ptr
    return Read_32(b, 6) #fallback if nothing is found

def parser_kdb(b:bytes, initial_value:int):
    if b[0:6] != MAGIC:
        raise ValueError("Not a KDB")
    entry_list_ptr = look_for_entryList(b)
    entries = []
    #each entry will have a character of 16 and lock list pointer of 4 bytes (32 bit)
    entry_size = 20
    # we were told ENTRY [127] so we will loop till 127
    cur = entry_list_ptr
    for _ in range(127):
        if cur + entry_size > len(b):
            break
        name = Read_Cstring(b,cur,16)
        block_list_ptr = Read_32(b,cur+16)
        cur += entry_size

        if block_list_ptr == END:
            break
        #put >= if the code messes up
        if block_list_ptr <= 0 or block_list_ptr > len(b):
            break
        

        blocks_data = bytearray()
        cur_b = block_list_ptr
        #in block there is a 32 bit data and 16 bit size. 32 is 4 bytes and 16 is 2 bytes so total of 6 bytes
        while cur_b + 6 <= len(b):
            size = Read_16(b, cur_b)
            data_ptr = Read_32(b, cur_b + 2)
            cur_b += 6
            if data_ptr == END:
                break
            if size == 0 or data_ptr < 0 or data_ptr + size > len(b):
                break
            blocks_data += b[data_ptr:data_ptr + size]

        decoded = Crypt(bytes(blocks_data), initial_value)
        entries.append((name, decoded))

    return entries





