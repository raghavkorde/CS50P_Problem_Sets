import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')
try:
    n= float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

response = response['bpi']
response = response['USD']
response = response['rate_float']
cost = n * float(response)
print(f'${cost:,}')

