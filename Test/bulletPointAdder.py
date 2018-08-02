#!/usr/bin/env python3
# -*-UTF-8-*-

import pyperclip
text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
