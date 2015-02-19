from base import BaseExtractor

class UrlExtractor(BaseExtractor):
	"""UrlExtractor
	Returns the url of the response
	"""
	def _extract(self, response, *args, **kwargs):
		return response.url