from itemagic import extractors, rules
from itemagic.magic import magic
from itemagic.parser import Parser
import scrapy
import unittest

class TestItem(scrapy.Item):
	urlField = scrapy.Field()
	constField = scrapy.Field()
	xpathField = scrapy.Field()
	sub = scrapy.Field()
	map1 = scrapy.Field()
	map2 = scrapy.Field()

class TestParser(unittest.TestCase):
	def test_one(self):
		parser = Parser(
			rules.ConstRule('constField', 'constVal'),
			rules.SubPathRule('//span',
				rules.XPathRule('sub', './/text()'),
				rules.UrlRule('urlField')
			),
			rules.XPathRule('xpathField', '//body//text()', merge=True, merge_joiner=' '),
			rules.MapRule('//span', extractors.XPathExtractor('text()'),
				rules.Map('map1', ('well', 'good', 'enough'), extractors.XPathExtractor('text()')),
				rules.Map('map2', 'bad', extractors.XPathExtractor('text()'))
			)
		)
		resp = scrapy.http.TextResponse('http://duckduckgo.com', body='<html><body>Hello<span>good</span><span>bad</span></body></html>')
		self.assertEqual(parser.build(TestItem(), resp), {
			'urlField': 'http://duckduckgo.com',
			'constField': 'constVal',
			'xpathField': 'Hello good bad',
			'sub': 'good',
			'map1': 'good',
			'map2': 'bad'
		})

	def test_two(self):
		parser = magic(
			url='urlField',
			const=(
				('constField',	'constVal'),
			),
			xpath=(
				('//span', (
					('sub',		'.//text()'),
				)),
				('xpathField',	'//body//text()',	dict(merge=True, merge_joiner=' ')),
				('//span', 'text()', (
					('map1',	('well', 'good', 'enough'),	'text()'),
					('map2',	'bad',						'text()')
				))
			)
		)
		resp = scrapy.http.TextResponse('http://duckduckgo.com', body='<html><body>Hello<span>good</span><span>bad</span></body></html>')
		self.assertEqual(parser.build(TestItem(), resp), {
			'urlField': 'http://duckduckgo.com',
			'constField': 'constVal',
			'xpathField': 'Hello good bad',
			'sub': 'good',
			'map1': 'good',
			'map2': 'bad'
		})
