from bs4 import BeautifulSoup
import urllib
import os, csv
os.chdir("/Users/MartinShin/code/data_mining/web_crawling/")

r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = BeautifulSoup(r, "html.parser")
#print soup.prettify()[28700:30500] cleans up html  
prefix = "www.aflcio.org"

letters = soup.find_all("div", class_="ec_statements")
#print letters[0].a["href"]

lobbying = {}
for element in letters:
	# use article title as key
	lobbying[element.a.get_text()] = {}

	#store article url for future reference
	lobbying[element.a.get_text()]["link"] = prefix + element.a["href"]
	#print lobbying[element.a.get_text()]["link"]

	#store article publish date
	date = element.find(id="legalert_date").get_text()
	lobbying[element.a.get_text()]["date"] = date
	
# for item in lobbying.keys():
#     print item + ": " + "\n\t" + "link: " + lobbying[item]["link"] + "\n\t" + "date: " + lobbying[item]["date"] + "\n\n" 



with open("lobbying.csv", "w") as toWrite:
	writer = csv.writer(toWrite, delimiter = ',')
	writer.writerow(["name", "link", "date"])
	for a in lobbying.keys():
		writer.writerow([a.encode("utf-8"), lobbying[a]["link"], lobbying[a]["date"]])