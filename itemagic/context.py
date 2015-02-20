from scrapy.http import TextResponse

class Context(TextResponse):
	@classmethod
	def from_response(cls, response):
		kwargs = {}
		for k,v in response.__dict__.iteritems():
			if k.startswith('_'):
				if k.startswith('_cached_'):
					continue
				k = k[1:]
			kwargs[k] = v
		return cls(**kwargs)

	def xpath(self, path):
		self._cached_selector = self.selector.xpath(path)
		return self._cached_selector