from extractors import XPathExtractor
from parser import Parser
from rules import ConstRule, Map, MapRule, SubPathRule, UrlRule, XPathRule

def is_list(obj):
	return isinstance(obj, (list, tuple))

def is_str(obj):
	return isinstance(obj, (str, unicode))

def parse_xpath_rule(line):
	l = len(line)

	if l == 2:
		# Basic XPath
		if is_str(line[1]):
			return XPathRule(line[0], line[1])
		# SubPath
		elif is_list(line[1]):
			sub_rules = [parse_xpath_rule(sub_rule) for sub_rule in line[1]]
			return SubPathRule(line[0], *sub_rules)
	elif l == 3:
		# Keyword XPath
		if isinstance(line[2], dict):
			return XPathRule(line[0], line[1], **line[2])
		# MapRule
		elif is_list(line[2]):
			maps = []
			for map_line in line[2]:
				len_map = len(map_line)
				if len_map == 3:
					maps.append(Map(map_line[0], map_line[1], XPathExtractor(map_line[2])))
				elif len_map == 4:
					maps.append(Map(map_line[0], map_line[1], XPathExtractor(map_line[2], **map_line[3])))
			return MapRule(line[0], XPathExtractor(line[1]), *maps)
	print 'Unknown rule : %r' % (line,)

def itemagic(const=None, url=None, xpath=None, *args):
	rules = []

	# Build const rules
	if is_list(const):
		for line in const:
			rules.append(ConstRule(line[0], line[1]))
	elif isinstance(const, dict):
		for field in const:
			rules.append(ConstRule(field, const[field]))

	# Build url rule
	if is_str(url):
		rules.append(UrlRule(url))

	# Build xpath rules
	if is_list(xpath):
		for line in xpath:
			rules.append(parse_xpath_rule(line))

	return Parser(*rules)