# Scrapy settings for padakalibot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'padakalibot'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['padakalibot.spiders']
NEWSPIDER_MODULE = 'padakalibot.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'padakalibot.pipelines.PadakaliDBPipeline'
    ]
