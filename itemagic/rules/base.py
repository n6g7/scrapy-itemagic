class BaseRule(object):
	"""BaseRule
	Rule skeleton : changes an item in some way.
	"""

	def __repr__(self, more=''):
		return '<%s%s>' % (self.__class__.__name__, more)

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

	def __init__(self, field, join=' '):
		self.field = field
		self.join = join

	def __repr__(self, more=''):
		return super(FieldRule, self).__repr__('[%s]%s' % (self.field, more))

	def affect(self, item, context):
		val = self.get_field_value(context)
		if val is not None:
			if self.field in item and item[self.field] is not None :
				item[self.field] += '%s%s' % (self.join, val)
			else:
				item[self.field] = val
		return item

	def get_field_value(self, context):
		raise NotImplementedError('%r does not provide an extractor or overrides the default #affect method.' % self.__class__)

class ExtractorRule(FieldRule):
	# Extractor class to use
	extractor = None
	
	def __init__(self, field, *args, **kwargs):
		super(ExtractorRule, self).__init__(field, kwargs.pop('join', None))
		# If an extractor class was provided, instantiate it.
		if self.extractor is not None:
			self.de = self.extractor(*args, **kwargs)
		else:
			raise NotImplementedError('%s doesn\'t provide an extractor class.' % self.__class__)

	def __repr__(self):
		extra = str(self.de)
		return super(ExtractorRule, self).__repr__(' %r' % extra if len(extra) > 0 else '')

	def get_field_value(self, context):
		return self.de.extract(context)