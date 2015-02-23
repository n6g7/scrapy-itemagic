from base import BaseExtractor

class ConstExtractor(BaseExtractor):
	"""ConstExtractor
	Always returns the same value.
	"""

	def __init__(self, value, **kwargs):
		super(ConstExtractor, self).__init__(**kwargs)
		self.processed_value = self.process(value)

	def __str__(self):
		return self.processed_value

	def extract(self, context):
		return [self.processed_value] if self.multiple else self.processed_value
		