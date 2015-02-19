class BaseExtractor(object):
	"""BaseExtractor
	Interface definition.
	"""
	def __init__(self, process=None, multiple=False, merge=False, merge_joiner='', *args, **kwargs):
		self.process = process if callable(process) else lambda x: x
		self.multiple = multiple
		self.merge = merge
		self.merge_joiner = merge_joiner

	def extract(self, *args, **kwargs):
		res = self._extract(*args, **kwargs)
		if type(res) in (list, tuple):
			if self.multiple:
				return [self.process(x) for x in res]
			elif self.merge:
				return self.process(self.merge_joiner.join(res))
			elif len(res) > 0:
				return self.process(res[0])
			else:
				return None
		else:
			res = self.process(res)
			return [res] if self.multiple else res

	def _extract(self, *args, **kwargs):
		raise NotImplementedError('%s does not override the "_extract" method.' % self.__class__.__name__)