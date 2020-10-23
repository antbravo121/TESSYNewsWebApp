import streamlit as st
from NewsApi import homepage_headlines, search_headlines, category_headlines

def draw_block_of_news(newsObject):
	#draw the title
	if newsObject.title != None:
		st.markdown("> ## {}".format(newsObject.title))
	else:
		st.write("")

	#draw source and date
	if newsObject.source != None and newsObject.date != None:
		st.markdown("###### {} • {}".format(newsObject.source, newsObject.date))
	elif newsObject.source == None and newsObject.date != None:
		st.markdown("###### {}".format(newsObject.date))
	elif newsObject.source != None and newsObject.date == None:
		st.markdown("###### {}".format(newsObject.source))
	else:
		st.write("")

	#draw image
	if newsObject.urlToImage != None:
		st.markdown("![]({})".format(newsObject.urlToImage))
	else:
		st.write("")

	#draw description
	if newsObject.description != None:
		st.write("*{}*".format(newsObject.description))
	else:
		st.write("")

	#draw content
	if newsObject.content != None:
		st.write(newsObject.contentCleaner())
	else:
		st.write("")

	#draw link
	if newsObject.url != None:
		st.markdown("[{}]({})".format(newsObject.url, newsObject.url))
	else:
		st.write("")

	#draw seperator
	st.write("---")

def load_news(news):
	#loop through headlines and drew them on screen
	for headline in news:
		draw_block_of_news(headline)


#Initialize screen, varibles, and headlines
st.beta_set_page_config(layout="wide")
navigationName = " "
headlineList = homepage_headlines()

#Sidebar implementation
st.sidebar.write("# Welcome to TESSY News")
button1 = st.sidebar.button("Home")
button2 = st.sidebar.button("Technology")
button3 = st.sidebar.button("Entertainment")
button4 = st.sidebar.button("Sports")
user_input = st.sidebar.text_input("Search for topics below")
st.sidebar.markdown("###### Made by Anthony Bravo")


#Event Handling
if user_input != "":
	st.sidebar.write("You searched for '{}'".format(user_input))
	with st.spinner('Wait for it...'):
		headlineList = search_headlines(user_input)
	st.balloons()

if button1:
	navigationName = " "
	with st.spinner('Wait for it...'):
		headlineList = homepage_headlines()
	st.balloons()

if button2:
	navigationName = " Technology "
	with st.spinner('Wait for it...'):
		headlineList = category_headlines("technology")
	st.balloons()

if button3:
	navigationName = " Entertainment "
	with st.spinner('Wait for it...'):
		headlineList = category_headlines("entertainment")
	st.balloons()

if button4:
	navigationName = " Sports "
	with st.spinner('Wait for it...'):
		headlineList = category_headlines("sports")
	st.balloons()

st.markdown("# Top{}Headlines".format(navigationName))

#catch the exceed max news api error
try:
  load_news(headlineList)
except:
  st.markdown("# Sorry an error has occured when loading the news, try again later.")







