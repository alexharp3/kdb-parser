#What is a KDB file? Database of passwords used by keepass password safe. 
#this is a password manager program. usually encrypted. https://fileinfo.com/extension/kdb
import argparse
from kdb_parser import parser_kdb
from clean_txt import clean_entry_text, is_printable



def main():
    parser = argparse.ArgumentParser(description="Decrypt a KDB file/extract entries")
    parser.add_argument("file", help="Path to the .kdb file")
    parser.add_argument("--key", default="4F574154", help="(default: 0x4F574154)")
    args = parser.parse_args()

    path = args.file
    initial_value = int(args.key, 16)

    with open(path, "rb") as f:
        data = f.read()
    
    entries = parser_kdb(data, initial_value)

    for name, decoded in entries:
        info = clean_entry_text(decoded)

        if not is_printable(info):
            continue
        if not name.strip():
            name = "(unamed)"
        
        print(f"{name}: {info}")

if __name__ == "__main__":
    main()
