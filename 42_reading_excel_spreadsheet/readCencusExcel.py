#! python3
# readCencusExcel.py - Tabulates population and number of cencus tracts for each county.

import openpyxl, pprint, os

os.chdir(r'C:\Users\himan\OneDrive\Documents\Interview_Prep\My_Learning_Cognizant\atbswpython\atbswp_python_programming\42_reading_excel_spreadsheet')

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

countyData = {}


# To Do: Fill in countyData  with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row+1):
    # Each row in the spreadsheet has data for onr cencus tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exists.
    countyData.setdefault(state, {})

    # Make sure the key for this county in this state exists.

    countyData[state].setdefault(county, {'tracts':0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1

    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it. 
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')


'''
>>> import census2010
>>> census2010.allData['AK']
{'Aleutians East': {'pop': 3141, 'tracts': 1}, 'Aleutians West': {'pop': 5561, 'tracts': 2}, 'Anchorage': {'pop': 291826, 'tracts': 55}, 'Bethel': {'pop': 17013, 'tracts': 3},
'Bristol Bay': {'pop': 997, 'tracts': 1}, 'Denali': {'pop': 1826, 'tracts': 1}, 'Dillingham': {'pop': 4847, 'tracts': 2}, 'Fairbanks North Star': {'pop': 97581, 'tracts': 19},
'Haines': {'pop': 2508, 'tracts': 1}, 'Hoonah-Angoon': {'pop': 2150, 'tracts': 2}, 'Juneau': {'pop': 31275, 'tracts': 6}, 'Kenai Peninsula': {'pop': 55400, 'tracts': 13},
'Ketchikan Gateway': {'pop': 13477, 'tracts': 4}, 'Kodiak Island': {'pop': 13592, 'tracts': 5}, 'Lake and Peninsula': {'pop': 1631, 'tracts': 1}, 'Matanuska-Susitna': {'pop': 88995, 'tracts': 24},
'Nome': {'pop': 9492, 'tracts': 2}, 'North Slope': {'pop': 9430, 'tracts': 3}, 'Northwest Arctic': {'pop': 7523, 'tracts': 2}, 'Petersburg': {'pop': 3815, 'tracts': 1},
'Prince of Wales-Hyder': {'pop': 5559, 'tracts': 4}, 'Sitka': {'pop': 8881, 'tracts': 2}, 'Skagway': {'pop': 968, 'tracts': 1}, 'Southeast Fairbanks': {'pop': 7029, 'tracts': 2},
'Valdez-Cordova': {'pop': 9636, 'tracts': 3}, 'Wade Hampton': {'pop': 7459, 'tracts': 1}, 'Wrangell': {'pop': 2369, 'tracts': 1}, 'Yakutat': {'pop': 662, 'tracts': 1},
'Yukon-Koyukuk': {'pop': 5588, 'tracts': 4}}
>>> census2010.allData['AK']['Anchorage']
{'pop': 291826, 'tracts': 55}
>>> anchoragePop = census2010.allData['AK']['Anchorage']['pop']
>>> print('The 2010 population of Anchorage was ' + str(anchoragePop))
The 2010 population of Anchorage was 291826
>>> 
'''
