from itemagic import extractors
import scrapy
import unittest

class TestExtractor(object):
	extractor = None
	extractor_args = None
	extract_args = None
	expected = None
	process = None

	def test_single(self):
		"""returns the first match"""
		ext = self.extractor(*self.extractor_args)
		self.assertEqual(ext.extract(self.extract_args), self.expected['single'])

	def test_multiple(self):
		"""returns list of results"""
		ext = self.extractor(*self.extractor_args, multiple=True)
		self.assertEqual(ext.extract(self.extract_args), self.expected['multiple'])

	def test_merge(self):
		"""returns concatenated results"""
		ext = self.extractor(*self.extractor_args, merge=True)
		self.assertEqual(ext.extract(self.extract_args), self.expected['merge'])

	def test_process(self):
		"""returns processed result(s)"""
		ext = self.extractor(*self.extractor_args, process=self.process)
		self.assertEqual(ext.extract(self.extract_args), self.process(self.expected['single']))

class TestConst(unittest.TestCase, TestExtractor):
	extractor = extractors.ConstExtractor
	extractor_args = [23]
	extract_args = 'random'
	expected = {
		'single': 23,
		'multiple': [23],
		'merge': 23,
	}
	process = lambda s,x: x*2

class TestUrl(unittest.TestCase, TestExtractor):
	extractor = extractors.UrlExtractor
	extractor_args = []
	extract_args = scrapy.http.Response('http://duckduckgo.com')
	expected = {
		'single': 'http://duckduckgo.com',
		'multiple': ['http://duckduckgo.com'],
		'merge': 'http://duckduckgo.com',
	}
	process = lambda s,x: x[:5]

class TestXPath(unittest.TestCase, TestExtractor):
	extractor = extractors.XPathExtractor
	extractor_args = ['//span/text()']
	extract_args = scrapy.selector.Selector(text='<html><body>Hello<span>good</span><span>bad</span></body></html>')
	expected = {
		'single': 'good',
		'multiple': ['good', 'bad'],
		'merge': 'goodbad',
	}
	process = lambda s,x: x*2

	def test_empty(self):
		ext = self.extractor('//span/a/text()', multiple=True)
		self.assertEqual(ext.extract(self.extract_args), [])

class TestTextXPath(unittest.TestCase, TestExtractor):
	extractor = extractors.XPathTextExtractor
	extractor_args = []
	extract_args = scrapy.selector.Selector(text='<html><body>Hello<span>good</span><span>bad</span></body></html>')
	expected = {
		'single': 'Hello good bad',
		'multiple': ['Hello', 'good', 'bad'],
		'merge': 'Hello good bad',
	}
	process = lambda s,x: x.replace('o', 'a')