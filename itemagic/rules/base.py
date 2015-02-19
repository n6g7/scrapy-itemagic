class BaseRule(object):
	"""BaseRule
	Sets one of the item's attribute given a field name and an extractor.
	"""
	# Extractor class to use
	extractor = None

	def __init__(self, field, *args, **kwargs):
		self.field = field
		# If an extractor class was provided, instantiate it.
		self.de = self.extractor(*args, **kwargs) if self.extractor is not None else None

	def affect(self, item, *args, **kwargs):
		# Use the extractor if possible.
		if self.de is not None:
			item[self.field] = self.de.extract(*args, **kwargs)
			return item
		else:
			raise NotImplementedError('%r does not provide an extractor or overrides the default #affect method.' % self.__class__)