import sys

abbr = {
'NLCS': 'North London Collegiate School',
'BHA': 'Branksome Hall Asia',
'KIS': 'Korea International School',
'SJA': 'St. Johnsbury Academy'
}

print(abbr[sys.stdin.read().strip()])