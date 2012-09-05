# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sqlite3

class PadakaliDBPipeline(object):
    def process_item(self, item, spider):
        print "I came to the pipeline for item : %s" % item
        conn = sqlite3.connect('padakalidata')
        cur = conn.cursor()
        cur.execute("insert into words(title, explanation, pub_date, url)  values(?,?,?,?)",(item['title'], item['explanation'], item['date'], item['url']))
        conn.commit()
        conn.close()
        return item
