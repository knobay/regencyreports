"""An attempt to get something by http and put it in a file."""

# You need to install something called Reqests,
# which I didn't find that easy.
# See http://docs.python-requests.org/en/master/user/install/#install"
# Hopefully this can be packaged into our program
# For some reason that feels better to me.
# I suppose you could detect the installation
# and then tell the user they need to have Requests installed.

import requests

def newsreader():
    "A function that gets the UK news from the BBC website and retuns it as a list."

    news_list = []
    news_request = requests.get('http://feeds.bbci.co.uk/news/video_and_audio/uk/rss.xml?edition=uk')
    for line in news_request.iter_lines():
        news_list.append(line)
    return news_list



def main():
    "Run the program"
    the_news = newsreader()
    print(the_news)

if __name__ == "__main__":
    main()