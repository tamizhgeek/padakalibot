# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sqlite3
from scrapy.conf import settings

class PadakaliDBPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect(settings['DB_NAME'])
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        print "I came to the pipeline for item : %s" % item
        self.cur.execute("insert into words(title, explanation, pub_date, url)  values(?,?,?,?)",(item['title'], item['explanation'], item['date'], item['url']))
        self.conn.commit()
        return item

