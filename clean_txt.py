import re 

def clean_entry_text(decoded:bytes) -> str:

    decoded = decoded.split(b'\x100', 1)[0]
    for b in decoded:
        if b in (9, 10, 13) or b <= 32 or b >= 126:
            decoded = decoded.replace(bytes([b]), b' ')
    text = decoded.decode('ascii', errors='replace')
    return re.sub(r'\s+', ' ', text).strip()

def is_printable(s: str) -> bool:
    if len(s) < 5:
        return False
    # checking if the character is a alphabet letter or number
    return any(c.isalnum() for c in s)