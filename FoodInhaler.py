# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


print ("=====Welcome to Heeirun's Food Inhaler v.10=====")
print ("=====Choose your Dining Hall of Choice=====")
print (" 1 - Gordon's\n 2 - Rheta's\n 3 - Liz's\n 4 - Four Lakes\n 5 - Carson's\n 6 - Newell's\n")
dineHall = input("Enter - ")
#Condition where Gordon's is chosen
if dineHall is "1":
    url = "http://menus.housing.wisc.edu/menus/gordon"
    pritn (url)
if dineHall is "2":
    url = ""
    print (url)
if dineHall is "3":
    url = "http://menus.housing.wisc.edu/menus/liz" 
    print (url)
if dineHall is "4":
    url = ""
    print (url)
if dineHall is "5":
    url = ""
    print (url)
if dineHall is "6":
    url = ""
    print (url)

    
#FIX ME: Add other conditions!
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

    
#print (soup.prettify())
#print (soup.get_text)

#WORKS: Prints out the Restaurants Open 
#UPGRADE: Make this into a method so that it can be reused.
print ("==================================RESTAURANTS OPEN==============================")
imgDicts = [] #Declares a dictionary 
imgTags = soup.find_all("img") #Searches for all the html tags with <img>
#print (imgTags)
for imgTag in imgTags: #Iterates through a 
    imgDicts.append(imgTag.attrs) #Adding each img tag attribute to the declared dictionary
    
#print (imgDicts)
for dict in imgDicts:
    for key,value in dict.items():
        if key == 'title':
            print (dict[key])
            
#WORKS: Prints out the food availabe for the day
#UPGRADE: Make this into a method so that it can be reused.
print ("==================================FOOD AVAILABLE================================")


  
mydivs = soup.find_all("div", { "class" : "rest_line_indent" }) #this line parse through finding the particular class in the div tag 
for food in mydivs:
    print (food.contents[0])
       
       
print ("==================================SEPERATION================================")
print ("In Progress")
mealTimes = soup.find_all("p", {"class" : "restaurantTime rest_line_indent"})
#print ( mealTimes)
for time in mealTimes: 
    imgTime = time.contents[0]
    print ( soup.p)

        
     

