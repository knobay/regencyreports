"""Get the latest from the New York Times and save to a file"""

# Import the functions needed from the regency reports library

from library.datacollector import read
from library.datacollector import tabulate
from library.datacollector import save

# Config with constants. Could be better in a separate file.
FIELDS = ('title', 'author')
FILE = './output/prototype/nyt.tsv'
TARGET = 'https://newsapi.org/v2/top-headlines?sources=the-new-york-times&apiKey=a480bf0091bb4e90bd6b24dce1eb7362'

def main():
    "run the program"
    print('Getting New York Times latest files and writing to a text file.')
    feed_data = read(TARGET)   # get list containg feed (articles + other stuff)
    json_articles = feed_data['articles']   # get list containing just json NYT articles
    tabulated_articles = tabulate(json_articles, FIELDS)
    save(tabulated_articles, 'output/prototype/nytitles.tsv')

if __name__ == "__main__":
    main()
