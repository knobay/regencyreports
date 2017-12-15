"""Proof of concept program for Regency Reports"""

# Import the functions needed from the regency reports library

from library.datacollector import read
from library.datacollector import tabulate
from library.datacollector import save

# Config with constants. Could be better in a separate file.
SOURCE = 'https://jsonplaceholder.typicode.com/users'
FIELDS = ('name', 'email', 'phone')
FILE = './output/prototype/regency.tsv'

def main():
    "Run the program"
    print("starting Regency Reports...")
    source_data = read(SOURCE)
    tabulated_data = tabulate(source_data, FIELDS)
    save(tabulated_data, FILE)

if __name__ == "__main__":
    main()
