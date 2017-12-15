"""Get the latest from the New York Times and save to a file"""

from library.datacollector import read
from library.datacollector import tabulate
from library.datacollector import save


FIELDS = ('title', 'author')
FILE = './output/prototype/nyt.tsv'
TARGET = 'https://newsapi.org/v2/top-headlines?sources=the-new-york-times&apiKey=a480bf0091bb4e90bd6b24dce1eb7362'

def main():
    "run the program"
    print('Getting New York Times latest files and writing to a text file.')
    mydata = read(TARGET)
    jsonlist = mydata['articles']
    alltitles = tabulate(jsonlist, FIELDS)
    save(alltitles, 'output/prototype/nytitles.tsv')

if __name__ == "__main__":
    main()
