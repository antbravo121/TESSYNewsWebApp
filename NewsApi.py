from newsapi import NewsApiClient
from NewsData import NewsData
from random import shuffle

api = NewsApiClient(api_key='e985b7fef38e4b55b6ad85c686220e82')

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

	shuffle(headlinesList)
	headlinesList.sort()

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

	headlinesList.sort()

	return headlinesList





	



