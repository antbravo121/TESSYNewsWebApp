#data format for news
class NewsData:
	def __init__(self, author, content, description, publishedAt, source, title, url, urlToImage):
		self.author = author
		self.content = content
		self.description = description
		self.date = publishedAt.split("T")[0]
		self.time = publishedAt.split("T")[1]
		self.source = source
		self.title = title
		self.url = url
		self.urlToImage = urlToImage

	#removes the '[+# chars]'' in the content
	def contentCleaner(self):
		start = self.content.find( '[' )
		end = self.content.find( ']' )
		if start != -1 and end != -1:
			result = self.content[start:end+1]
			return self.content.replace(result, "")
		return self.content

	#used to sort news by dates
	def __eq__(self, other):
		return ((self.date, self.time) == (other.date, other.time))

	def __ne__(self, other):
		return ((self.date, self.time) != (other.date, other.time))

	def __lt__(self, other):
		return ((self.date, self.time) < (other.date, other.time))

	def __le__(self, other):
		return ((self.date, self.time) <= (other.date, other.time))

	def __gt__(self, other):
		return ((self.date, self.time) > (other.date, other.time))

	def __ge__(self, other):
		return ((self.date, self.time) >= (other.date, other.time))







