\# KDB Reverse Engineering (CT2018)



This project parses and decrypts a custom KeePass `.kdb` file used in the

CT2018 reverse engineering challenge.



\## Features

\- Locates entry list using file structure heuristics

\- Reconstructs block data chains

\- Decrypts data using an LFSR-based stream cipher

\- Outputs (name, decoded) entry pairs



\## Usage



```bash

python main.py path\\to\\store.kdb --key 4F574154



