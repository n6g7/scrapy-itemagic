from base import BaseRule
from itemagic.extractors import XPathExtractor, XPathTextExtractor

class XPathRule(BaseRule):
	extractor = XPathExtractor

class XPathTextRule(BaseRule):
	extractor = XPathTextExtractor