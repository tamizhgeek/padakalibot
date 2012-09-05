from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from time import strptime
from padakalibot.items import PadakaliWord
from dateutil.parser import parse

class PadakaliSpider(CrawlSpider):

    name = "padakalibot"
    allowed_domains = ["padakali.com"]
    start_urls = ["http://www.padakali.com/archives"]

    rules = [
        Rule(SgmlLinkExtractor(allow=['/archive/*/*'])),
        Rule(SgmlLinkExtractor(allow=['word/*']), callback = 'parse_archives')
        ]
    
    
    def parse_archives(self, response):
        print "Parsing the link %s" % response.url
        res = HtmlXPathSelector(response)
        pw = PadakaliWord()
        pw['title'] = res.select("//div[contains(@id, 'main')]/div/h2/text()").extract()[0]
#        print res.select("//div[contains(@id, 'main')]/span[contains(@class, 'datetext')]/text()").extract()
        pw['date'] = parse(res.select("//div[contains(@id, 'main')]/span[contains(@class, 'datetext')]/text()").extract()[0].split(':')[1]).date()
        main_div = res.select("//div[contains(@id, 'main')]")
        text = ""
        for p in main_div.select('.//p[position() > 1 and position() != last()]'):
            t = p.extract()
            text += " \n " + t
        pw['explanation'] = text
        pw['url'] = response.url
        print pw
        return pw
