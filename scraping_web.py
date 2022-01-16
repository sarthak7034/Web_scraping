from bs4 import BeautifulSoup as soup
import codecs
import pandas as pd

dict = {
    "Hotel_name": [],
    "Address": [],
    "stars": [],
    "Review_points": [],
    "Number_of_reviews": [],
    "Description": [],
    "Room_categories":[],
    "Alternative_hotels":[]
}
article = ''
headers = []

html = codecs.open("./task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html", "r", "utf-8")
a = html.read()
bsObj = soup(a,'html.parser')
name = bsObj.find("span", class_="fn").text.strip()
dict["Hotel_name"].append(name)
address = bsObj.find(id="hp_address_subtitle").text.strip()
dict["Address"].append(address)
star = bsObj.find("span", class_="invisible_spoken").text.strip()
dict["stars"].append(star)
review_points = bsObj.find("span", class_="average js--hp-scorecard-scoreval").text.strip()
divider = bsObj.find("span", class_="out_of").text.strip()
dict["Review_points"].append(review_points+divider)
No_review = bsObj.find("span", class_="trackit score_from_number_of_reviews").text.strip()
dict["Number_of_reviews"].append(No_review)
content = bsObj.find("div", id="summary")
# loop to remove paragraphs
for i in content.findAll('p'):
    article = article + ' ' +  i.text
dict["Description"].append(article)
Room_categories = bsObj.find("table",class_="roomstable rt_no_dates __big-buttons rt_lightbox_enabled")

for i in Room_categories.find_all('th'):
 title = i.text.replace('\n','').strip()
 headers.append(title)

mydata = pd.DataFrame(columns = headers)
# Create a for loop to fill mydata
alternative_hotels = []
for j in Room_categories.find_all('tr')[1:]:
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(mydata)
 mydata.loc[length] = row

mydata = mydata.replace('\n','', regex=True)
dict["Room_categories"].append(mydata)
hotels =bsObj.find('div', class_='tracked box sidebox')

for i in hotels.find_all('ul', class_="lastViewedList small round4"):
  for j in i.find_all('li',{'data-stage': '2'}):  
    hotels = j.find('a',class_='').text.strip()   
    dict["Alternative_hotels"].append(hotels)

print(dict)