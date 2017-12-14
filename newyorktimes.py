"""Use regency reports functions to get the latest from the New York Times and save"""

import sys
sys.path.append('funcs')
import datacollector

FIELDS = ('title', 'author')
FILE = './output/prototype/nyt.tsv'
TARGET = 'https://newsapi.org/v2/top-headlines?sources=the-new-york-times&apiKey=a480bf0091bb4e90bd6b24dce1eb7362'

def main():
    "run the program"
    print('Getting New York Times latest files and writing to a text file.')
    mydata = datacollector.reader(TARGET)
    jsonlist = mydata['articles']
    alltitles = datacollector.tabulate(jsonlist, FIELDS)
    datacollector.savetsv(alltitles, 'output/prototype/nytitles.tsv')

main()
