from scrapy.http import TextResponse

class Context(object):

	def __init__(self, response, selector=None, paths=[]):
		self.response = response
		self.selector = selector if selector is not None else response.selector
		self.paths = paths

	def __iter__(self):
		for x in self.selector:
			yield x

	def __str__(self):
		return '<%s %r %s>' % (self.response.status, self.paths, self.selector)
	__repr__ = __str__

	@property
	def url(self):
		return self.response.url

	def xpath(self, path):
		return self.__class__(self.response, self.selector.xpath(path), paths=self.paths+[path])

	def extract(self):
		return self.selector.extract()