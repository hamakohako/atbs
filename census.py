#!./venv/bin/python
# Task is to calculate population statistics per county on an Excel Spreadsheet

# openpyxl is a module for working with spreadsheets like MS Excel
# pprint
import openpyxl, pprint

print('Opening workbook...')

# Loads/opens the worksheet in the current directory
wb = openpyxl.load_workbook('censuspopdata.xlsx')

# Work on the sheet named below
sheet = wb['Population by Census Tract']

# initialize a dict variable which will store the data
countyData = {}

print("Reading rows...")

# Iterate over each rows, starting with 2 since 1st row is header
for row in range(2, sheet.max_row + 1):
    # Each row has data for one census tract
    # Column B has state, and we are iterating per each row, value function is attached to return only the value.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # this makes sure that the key for this state exsits
    countyData.setdefault(state, {})
    
    # this makes sure that the key for this county exists -- otherwise the following lines
    # will result an error as the state and county does not exist yet
    # we also initialize tracts and pop to 0, then increment values on the following lines
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    
    # Each row on the sheet represents a tract, so we increment by one for each iteration
    countyData[state][county]['tracts'] += 1

    # Increase the county pop by the pop value on this census tract
    countyData[state][county]['pop'] += int(pop)

# Writing the results to a file

print('Writing results...')

# Opens a file for writing
resultFile = open('census2010.py', 'w')

# pprint.pformat fucntion produces string the is formatted as valid pythoin code
# for example, the resulting file can be imported as python module
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')


# The resulting file is basically a python file containing dictionary in a var named allData
# containing the data we iterated through and calculated above.
# This can now be used to fetch the statistics. for example:

# >>> import os

# >>> import census2010
# >>> census2010.allData['AK']['Anchorage']
# {'pop': 291826, 'tracts': 55}
# >>> anchoragePop = census2010.allData['AK']['Anchorage']['pop']
# >>> print('The 2010 population of Anchorage was ' + str(anchoragePop))
# The 2010 population of Anchorage was 291826