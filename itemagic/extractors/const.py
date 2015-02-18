from base import BaseExtractor

class ConstExtractor(BaseExtractor):
	"""ConstExtractor
	Always returns the same value.
	"""
	def __init__(self, value, *args, **kwargs):
		super(ConstExtractor, self).__init__(*args, **kwargs)
		self.value = self.process(value)
	def extract(self, *args, **kwargs):
		return self.value