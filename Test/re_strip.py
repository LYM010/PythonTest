#! /usr/bin/env python3
# -*-UTF-8-*-
# re_strip.py

import re
def re_strip(s,t=r'\s'):
	s_format = r'^%s*|%s*$'%(t,t)
	s_re = re.compile(s_format)
	s = s_re.sub('',s)
	return s

if __name__ == '__main__':
	s = input('Enter a string: ')
	print(re_strip(s))
