from base import MetaRule, FieldRule

class Map(FieldRule):
	def __init__(self, field, keywords, data_extractor):
		super(Map, self).__init__(field)
		if isinstance(keywords, (list, tuple)):
			self.keywords = keywords
		else:
			self.keywords = [keywords]
		self.data_extractor = data_extractor
	def accepts(self, label):
		if label is None:
			return False
		return any([(kw in label) for kw in self.keywords])
	def get_field_value(self, context):
		return self.data_extractor.extract(context)

class MapRule(MetaRule):
	rule_class = Map

	def __init__(self, elements_path, label_extractor, *args):
		super(MapRule, self).__init__(*args)
		self.elements_path = elements_path
		self.label_extractor = label_extractor

	def affect(self, item, context):
		for el in context.xpath(self.elements_path):
			label = self.label_extractor.extract(el)
			for rule in self.rules:
				if rule.accepts(label):
					item = rule.affect(item, el)
		return item