# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PadakaliWord(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    explanation = Field()
    url = Field()
    date = Field()


    def __str__(self):
        return "Title : %s" % self['title']
