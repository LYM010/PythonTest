#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import webbrowser,sys,logging,pyperclip
logging.basicConfig(level = logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if len(sys.argv) > 1:
	address = ''.join(sys.argv[1:])
	logging.debug(f'address_argv is {address}')
else:
	address = pyperclip.paste()
	logging.debug(f'address_pyperclip is {address}')

webbrowser.open(f'http://api.map.baidu.com/geocoder?address={address}&output=html&src=test')