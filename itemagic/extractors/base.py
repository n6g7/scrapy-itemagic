class BaseExtractor(object):
	"""BaseExtractor
	Interface definition.
	"""
	def __init__(self, process=None, *args, **kwargs):
		self.process = process if callable(process) else lambda x: x
	def extract(self, *args, **kwargs):
		raise NotImplementedError()