from base import BaseExtractor

class XPathExtractor(BaseExtractor):
	"""XPathExtractor
	Uses its XPath selector to extract data from an XML document.
	Handles merging (concatenation) several results and returning multiple results.
	"""
	def __init__(self, xpath, *args, **kwargs):
		super(XPathExtractor, self).__init__(*args, **kwargs)
		self.xpath = xpath
	def _extract(self, context, *args, **kwargs):
		return context.xpath(self.xpath).extract()

class XPathTextExtractor(XPathExtractor):
	"""XPathTextExtractor
	Whole text extractor.
	"""
	def __init__(self, *args, **kwargs):
		super(XPathTextExtractor, self).__init__('.//text()', multiple=False, merge=True, merge_joiner=' ', *args, **kwargs)