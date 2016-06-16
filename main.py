from bs4 import BeautifulSoup
import requests
import string


print("Please enter a word to search for: ")

while True:

	inpt = str(input())

	if len(inpt) > 1:
		inptArray = inpt.split(" ")
		counter = 0
		for inplen in inptArray:
			if counter == 0:
				result = inplen
			else:
				result = result + "_" + inplen
			counter += 1	

	url = "https://de.wikipedia.org/wiki/" + result # the word you entered is added here to the link

	r = requests.get(url) # Gets the html-code of the generated link

	soup = BeautifulSoup(r.content, "html.parser") # BeautifulSoup adopts the html-code

	links = soup.find_all("p") # searches for the html tag <p>

	for link in links:
		print ("%s" %(link.text)) # prints every "p" tagged tag
	print("\n\nPlease enter the next word: ")
