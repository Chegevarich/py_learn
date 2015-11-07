import sys
from xml.etree.ElementTree import XMLParser

class MaxDepth:                     # The target object of the parser
	__news_count = 0
	maxDepth = 0
	depth = 0

	@property
	def news_count(self):
	    return self.__news_count
	
	def start(self, tag, attrib):   # Called for each opening tag.
		if tag == 'item':
			self.__news_count+=1

		self.depth += 1
		if self.depth > self.maxDepth:
			self.maxDepth = self.depth

	def end(self, tag):  
		self.depth -= 1

	def close(self):    # Called when all data has been parsed.
		return self.maxDepth

target = MaxDepth()

parser = XMLParser(target=target)

rss = open('lentaru.rss')

a = parser.feed(rss.read())

print(target.news_count)

parser.close()