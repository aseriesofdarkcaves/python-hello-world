from pathlib import Path
from wordcloud import WordCloud, STOPWORDS

"""
Adapted from https://amueller.github.io/word_cloud/auto_examples/simple.html
"""

directory_path = str(Path.home()) + "/"
filename_noext = "a-new-hope"

# movie script of "a new hope"
# http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html
# May the lawyers deem this fair use.
# TODO: refactor to scrape data from a web-page
# TODO: Sus suggested scraping a porn script
text = open(directory_path + filename_noext + ".txt").read()

# pre-processing the text a little bit
text = text.replace("HAN", "Han")
text = text.replace("LUKE'S", "Luke")

# adding movie script specific stopwords
stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wordcloud = WordCloud(width=1920,
                      height=1080,
                      max_words=1000,
                      stopwords=stopwords,
                      margin=10,
                      random_state=1).generate(text)

wordcloud.to_file(directory_path + filename_noext + ".png")
