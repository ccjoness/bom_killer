"""
Removes the Byte-order Mark (BOM) from files created in Windows.

Example:
$ python bomkill.py <NAME OF FILE>
"""
import sys

with open(sys.argv[1], mode='r', encoding='utf-8-sig') as s:
    text = s.read()

with open(sys.argv[1], mode='w', encoding='utf-8') as f:
    f.write(text)
