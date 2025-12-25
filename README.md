# KDB Reverse Engineering (CT2018)

This project reverse engineers, parses, and decrypts a custom KeePass `.kdb`
file format used in the CT2018 reverse engineering challenge.

The focus of this project is defensive binary parsing, safe pointer traversal,
and stream-cipher decryption rather than exploitation.

---

## Overview

The parser identifies structured entry lists within the binary, reconstructs
linked encrypted data blocks, and decrypts their contents using an
LFSR-based stream cipher.

The implementation emphasizes correctness, bounds checking, and resilience
against malformed data.

---

## Features

- Validates file signature and structure
- Locates the entry list using file layout heuristics
- Traverses linked block lists safely using pointer validation
- Reconstructs encrypted data across multiple blocks
- Decrypts data using an LFSR-based stream cipher
- Outputs parsed entries as `(name, decoded)` pairs

---

## File Structure (High-Level)

Each entry in the KDB file consists of:
- **16 bytes** — null-terminated entry name
- **4 bytes** — 32-bit pointer to a block list

Each block list contains:
- **2 bytes** — size of encrypted data
- **4 bytes** — pointer to encrypted data
- **0xFFFFFFFF** — sentinel value indicating end of list

Encrypted data blocks are concatenated in order and decrypted using an
LFSR-based stream cipher.

---

## Security & Robustness Considerations

- All pointers are validated before dereferencing
- Bounds checks prevent out-of-bounds memory access
- Sentinel values are used to terminate linked structures safely
- Parsing logic is defensive against malformed or unexpected input

---
## Tooling & Research
- Python 3
- Visual Studio Code
- Public documentation on KeePass KDB file structures
- LFSR stream cipher references
- AI-assisted tooling for debugging and iterative refinement

---
## Usage

```bash
python main.py path\to\store.kdb --key 4F574154

## Disclaimer
This project was created for educational and reverse engineering purposes only.
It is not intended for unauthorized access to real-world systems or data.




