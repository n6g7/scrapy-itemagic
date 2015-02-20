from base import BaseExtractor

class XPathExtractor(BaseExtractor):
	"""XPathExtractor
	Uses its XPath selector to extract data from an XML document.
	Handles merging (concatenation) several results and returning multiple results.
	"""
	def __init__(self, xpath, **kwargs):
		super(XPathExtractor, self).__init__(**kwargs)
		self.xpath = xpath
	def _extract(self, context):
		return context.xpath(self.xpath).extract()

class XPathTextExtractor(XPathExtractor):
	"""XPathTextExtractor
	Whole text extractor.
	"""
	def __init__(self, **kwargs):
		default = {
			'merge': True,
			'multiple': False,
			'merge_joiner': ' '
		}
		default.update(kwargs)
		super(XPathTextExtractor, self).__init__('.//text()', **default)