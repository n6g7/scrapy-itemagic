from context import Context
from rules import ConstRule
from rules.base import BaseRule

class Parser(object):
	"""Parser
	Fills an item given a set of rules and a source (scrapy Response or Selector)
	"""

	def __init__(self, *args):
		self.rules = [r for r in args if isinstance(r, BaseRule)]
		self.cached_describe = None

	def build(self, item, response):
		for rule in self.rules:
			item = rule.affect(item, Context(response))
		return item

	def describe(self):
		if self.cached_describe is None:
			self.cached_describe = {rule.field:rule.de.processed_value for rule in self.rules if isinstance(rule, ConstRule)}
		return self.cached_describe