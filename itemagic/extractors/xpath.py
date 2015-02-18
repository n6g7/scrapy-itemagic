from base import BaseExtractor

class XPathExtractor(BaseExtractor):
	"""XPathExtractor
	Uses its XPath selector to extract data from an XML document.
	Handles merging (concatenation) several results and returning multiple results.
	"""
	def __init__(self, xpath, multiple=False, merge=False, merge_joiner='', *args, **kwargs):
		super(XPathExtractor, self).__init__(*args, **kwargs)
		self.xpath = xpath
		self.multiple = multiple
		self.merge = merge
		self.merge_joiner = merge_joiner
	def extract(self, context, *args, **kwargs):
		tmp = context.xpath(self.xpath).extract()
		if self.multiple:
			return [self.process(x) for x in tmp]
		elif self.merge:
			return self.process(self.merge_joiner.join(tmp))
		elif len(tmp) > 0:
			return self.process(tmp[0])
		else:
			return None

class XPathTextExtractor(XPathExtractor):
	"""XPathTextExtractor
	Whole text extractor.
	"""
	def __init__(self, *args, **kwargs):
		super(XPathTextExtractor, self).__init__('.//text()', multiple=False, merge=True, merge_joiner=' ', *args, **kwargs)