class BaseRule(object):
	"""BaseRule
	Rule skeleton : changes an item in some way.
	"""

	def affect(self, item, context):
		raise NotImplementedError()

class MetaRule(BaseRule):
	"""MetaRule
	Rule applying sub-rules.
	"""
	rule_class = BaseRule

	def __init__(self, *args):
		self.rules = [r for r in args if isinstance(r, self.rule_class)]

	def affect(self, item, context):
		for rule in self.rules:
			item = rule.affect(item, context)
		return item

class FieldRule(BaseRule):
	"""FieldRule
	Sets the value of one of the item's fields.
	"""

	def __init__(self, field):
		self.field = field

	def affect(self, item, context):
		item[self.field] = self.get_field_value(context)
		return item

	def get_field_value(self, context):
		raise NotImplementedError('%r does not provide an extractor or overrides the default #affect method.' % self.__class__)

class ExtractorRule(FieldRule):
	# Extractor class to use
	extractor = None
	
	def __init__(self, field, *args, **kwargs):
		super(ExtractorRule, self).__init__(field)
		# If an extractor class was provided, instantiate it.
		if self.extractor is not None:
			self.de = self.extractor(*args, **kwargs)
		else:
			raise NotImplementedError('%s doesn\'t provide an extractor class.' % self.__class__)

	def get_field_value(self, context):
		return self.de.extract(context)