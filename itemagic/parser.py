from context import Context
from rules.base import BaseRule

class Parser(object):
	"""Parser
	Fills an item given a set of rules and a source (scrapy Response or Selector)
	"""

	def __init__(self, *args):
		self.rules = [r for r in args if isinstance(r, BaseRule)]

	def build(self, item, response):
		for rule in self.rules:
			item = rule.affect(item, Context(response))
		return item