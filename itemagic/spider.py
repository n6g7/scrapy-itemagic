from scrapy.contrib.spiders import CrawlSpider

class ItemagicMixin(object):
	itemagic_item_cls = None
	itemagic_parser = None

	def itemagic(self):
		return self.itemagic_item_cls()

	def parse_item(self, response):
		return self.itemagic_parser.build(self.itemagic(), response)

class ItemagicSpider(ItemagicMixin, CrawlSpider):
	pass