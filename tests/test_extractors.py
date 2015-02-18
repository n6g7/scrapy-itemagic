from itemagic import extractors
import scrapy
import unittest

class TestExtractors(unittest.TestCase):
	def test_const(self):
		val = 23
		ce = extractors.ConstExtractor(val)
		self.assertEqual(ce.extract('heyheyhey'), val)
	def test_const_process(self):
		val = 4
		ce = extractors.ConstExtractor(val, process=lambda x: x*x)
		self.assertEqual(ce.extract('lol', 42), val**2)
	def test_url(self):
		url = 'http://duckduckgo.com'
		resp = scrapy.http.Response(url)
		ue = extractors.UrlExtractor()
		self.assertEqual(ue.extract(resp), url)
	def test_url_process(self):
		url = 'http://duckduckgo.com'
		resp = scrapy.http.Response(url)
		ue = extractors.UrlExtractor(process=lambda x: x[:5])
		self.assertEqual(ue.extract(resp), url[:5])
	def test_xpath(self):
		sel = scrapy.selector.Selector(text='<html><body><span>good</span><span>bad</span></body></html>')
		xe = extractors.XPathExtractor('//span/text()', multiple=True)
		self.assertEqual(xe.extract(sel), ['good', 'bad'])
	def test_xpath_process(self):
		sel = scrapy.selector.Selector(text='<html><body><span>good</span><span>bad</span></body></html>')
		xe = extractors.XPathExtractor('//span/text()', merge=True, process=lambda x: x*2)
		self.assertEqual(xe.extract(sel), 'goodbadgoodbad')
	def test_text_xpath(self):
		sel = scrapy.selector.Selector(text='<html><body><span>good</span><span>bad</span></body></html>')
		xte = extractors.XPathTextExtractor()
		self.assertEqual(xte.extract(sel), 'good bad')
	def test_text_xpath_process(self):
		sel = scrapy.selector.Selector(text='<html><body><span>good</span><span>bad</span></body></html>')
		xte = extractors.XPathTextExtractor(process=lambda x: x.replace('o', 'a'))
		self.assertEqual(xte.extract(sel), 'gaad bad')