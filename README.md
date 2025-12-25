\# KDB Reverse Engineering (CT2018)



This project parses and decrypts a custom KeePass `.kdb` file used in the

CT2018 reverse engineering challenge.



\## Features

\- Locates entry list using file structure heuristics

\- Reconstructs block data chains

\- Decrypts data using an LFSR-based stream cipher

\- Outputs (name, decoded) entry pairs

## File Structure (High-Level)

Each entry in the KDB file consists of:
- 16 bytes: null-terminated entry name
- 4 bytes: 32-bit pointer to a block list

Block lists contain:
- 2 bytes: data size
- 4 bytes: pointer to encrypted data
- Terminated by 0xFFFFFFFF

Encrypted data blocks are concatenated and decrypted using an
LFSR-based stream cipher.


\## Usage



```bash

python main.py path\\to\\store.kdb --key 4F574154



