from newsapi import NewsApiClient
from NewsData import NewsData
from random import shuffle
from collections import Counter

api = NewsApiClient(api_key='78b9d599c4f94f8fa3afb1a5458928d6')

def homepage_headlines():
	sports_headlines = api.get_top_headlines(category="sports").get("articles")
	tech_headlines = api.get_top_headlines(category="technology").get("articles")
	ent_headlines = api.get_top_headlines(category="entertainment").get("articles")

	headlinesList = []

	#adds newsObject to list
	for headline in sports_headlines:
		headlinesList.append(NewsData(
			headline.get("author"), 
			headline.get("content"), 
			headline.get("description"), 
			headline.get("publishedAt"), 
			headline.get("source")["name"], 
			headline.get("title"), 
			headline.get("url"), 
			headline.get("urlToImage")))

	for headline in tech_headlines:
		headlinesList.append(NewsData(
			headline.get("author"), 
			headline.get("content"), 
			headline.get("description"), 
			headline.get("publishedAt"), 
			headline.get("source")["name"], 
			headline.get("title"), 
			headline.get("url"), 
			headline.get("urlToImage")))
	for headline in ent_headlines:
		headlinesList.append(NewsData(
			headline.get("author"), 
			headline.get("content"), 
			headline.get("description"), 
			headline.get("publishedAt"), 
			headline.get("source")["name"], 
			headline.get("title"), 
			headline.get("url"), 
			headline.get("urlToImage")))

	#shuffle list and sort them by date
	shuffle(headlinesList)
	headlinesList.sort()
	
	#remove repeats
	c = Counter(headline.title for headline in headlinesList)
	for indx, headline in enurmate(headlinesList):
		if c[headline.title] > 1:
			headlinesList.pop(indx)

	return headlinesList



def search_headlines(userSearch):
	sports_headlines = api.get_top_headlines(q = userSearch, category="sports").get("articles")
	tech_headlines = api.get_top_headlines(q = userSearch, category="technology").get("articles")
	ent_headlines = api.get_top_headlines(q = userSearch, category="entertainment").get("articles")

	headlinesList = []

	#adds newsObject to list
	for headline in sports_headlines:
		headlinesList.append(NewsData(
			headline.get("author"), 
			headline.get("content"), 
			headline.get("description"), 
			headline.get("publishedAt"), 
			headline.get("source")["name"], 
			headline.get("title"), 
			headline.get("url"), 
			headline.get("urlToImage")))
	for headline in tech_headlines:
		headlinesList.append(NewsData(
			headline.get("author"), 
			headline.get("content"), 
			headline.get("description"), 
			headline.get("publishedAt"), 
			headline.get("source")["name"], 
			headline.get("title"), 
			headline.get("url"), 
			headline.get("urlToImage")))
	for headline in ent_headlines:
		headlinesList.append(NewsData(
			headline.get("author"), 
			headline.get("content"), 
			headline.get("description"), 
			headline.get("publishedAt"), 
			headline.get("source")["name"], 
			headline.get("title"), 
			headline.get("url"), 
			headline.get("urlToImage")))
	#sort by date
	shuffle(headlinesList)
	headlinesList.sort()
	
	#remove repeats
	c = Counter(headline.title for headline in headlinesList)
	for indx, headline in enurmate(headlinesList):
		if c[headline.title] > 1:
			headlinesList.pop(indx)

	return headlinesList

def category_headlines(topic):
	headlines = api.get_top_headlines(category=topic).get("articles")
	headlinesList = []

	#adds newsObject to list
	for headline in headlines:
		headlinesList.append(NewsData(
			headline.get("author"), 
			headline.get("content"), 
			headline.get("description"), 
			headline.get("publishedAt"), 
			headline.get("source")["name"], 
			headline.get("title"), 
			headline.get("url"), 
			headline.get("urlToImage")))
	#sort by date
	headlinesList.sort()
	#remove repeats
	c = Counter(headline.title for headline in headlinesList)
	for indx, headline in enurmate(headlinesList):
		if c[headline.title] > 1:
			headlinesList.pop(indx)

	return headlinesList





	




