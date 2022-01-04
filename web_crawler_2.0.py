import requests
import lxml
from bs4 import BeautifulSoup

# Pass the URL
# Set headers to get through the ERROR 403
# Get request from the web
url = "https://rezka.ag/films/fiction/612-chelovek-iz-stali-2013.html"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
web_request = requests.get(url, headers=headers)


# Create a BeautifulSoup object and specify the parser as lxml
# Reveive the content with the help of lxml
# and gain the list of movies urls
soup = BeautifulSoup(web_request.content, 'lxml')
movies = soup.find('div', {
	'class': 'b-post__partcontent'
	}).find_all('a')


# Put all links into the variable
links = []
for link in movies:
	links.append(link['href'])


# Pass through all the links and get our data
for movie_link in links:

	# Get request
	# Reveive the content with the help of lxml
	movie_webpage = requests.get(movie_link, headers=headers)
	movie_soup = BeautifulSoup(movie_webpage.content, 'lxml')

	# Find name
	movie_name = movie_soup.find('h1', {
		'itemprop': 'name'
		})

	# Find information
	movie_information = movie_soup.find('div', {
		'class': 'b-post__description_text'
		})
	
	# Print movies without one 
	if movie_name.string.strip() != 'Чудо-женщина: 1984':
		print("Film name -> {}".format(movie_name.string.strip()))
		print("\nInformation: {}\n".format(movie_information.string.strip()))