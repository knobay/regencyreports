import sys
sys.path.append('funcs')

import requests
import datacollector

# Config. Would be better in a separate file.
SOURCE = 'https://jsonplaceholder.typicode.com/users'
FIELDS = ('name', 'email', 'phone')
FILE = './output/prototype/regency.tsv'

def main():
    "Run the program"
    print("starting Regency Reports...")
    source_data = datacollector.read(SOURCE)
    tabulated_data = datacollector.tabulate(source_data, FIELDS)
    datacollector.savetsv(tabulated_data, FILE)

if __name__ == "__main__":
    main()
