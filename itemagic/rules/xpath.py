from base import MetaRule, ExtractorRule
from itemagic.extractors import XPathExtractor, XPathTextExtractor

class XPathRule(ExtractorRule):
	extractor = XPathExtractor

class XPathTextRule(ExtractorRule):
	extractor = XPathTextExtractor

class SubPathRule(MetaRule):

	def __init__(self, path, *args, **kwargs):
		self.path = path
		super(SubPathRule, self).__init__(*args)

	def affect(self, item, context):
		return super(SubPathRule, self).affect(item, context.xpath(self.path))
