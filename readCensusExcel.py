#!/usr/bin/env python3
# coding:UTF-8

import openpyxl,pprint,os,logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s -%(message)s')
# logging.disable(logging.CRITICAL)

os.chdir(os.path.join('..','tmp'))

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
logging.debug(f'sheet is {sheet}')

countryData = {}

# TODO
print('Reading rows...')
for row in range(2,sheet.max_row+1):
	# Each row in the spreadsheet has data for one census tract.
	State = sheet['B'+str(row)].value
	country = sheet['C'+str(row)].value
	pop = sheet['D'+str(row)].value
	countryData.setdefault(State, {})
	countryData[State].setdefault(country,{'tracts':0,'pop':0})
	countryData[State][country]['tracts']+=1
	countryData[State][country]['pop']+=int(pop)
logging.debug('Rows had been read.')
logging.debug('countryData is ready.')

print('Writting results...')
resultFiles = open('census2010.py','w')
logging.debug(f'resultFiles is {resultFiles.name}')
resultFiles.write('allDaata = ' + pprint.pformat(countryData))
resultFiles.close()
print('Done')