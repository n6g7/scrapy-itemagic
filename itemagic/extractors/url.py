from base import BaseExtractor

class UrlExtractor(BaseExtractor):
	"""UrlExtractor
	Returns the url of the response
	"""
	def extract(self, response, *args, **kwargs):
		return self.process(response.url)