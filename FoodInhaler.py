# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import ssl


print ("=====Welcome to Heeirun's Food Inhaler v.10=====")
print ("=====Choose your Dining Hall of Choice=====")
print (" 1 - Gordon's\n 2 - Rheta's\n 3 - Liz's\n 4 - Four Lakes\n 5 - Carson's\n 6 - Newell's\n")
dineHall = input("Enter - ")
#Condition where Gordon's is chosen
if dineHall is "1":
    url = "http://menus.housing.wisc.edu/menus/gordon"
    print (url)
if dineHall is "2":
    url = "http://menus.housing.wisc.edu/menus/rhetas"
    print (url)
if dineHall is "3":
    url = "http://menus.housing.wisc.edu/menus/liz" 
    print (url)
if dineHall is "4":
    url = "http://menus.housing.wisc.edu/menus/fourlakes"
    print (url)
if dineHall is "5":
    url = "http://menus.housing.wisc.edu/menus/carsons"
    print (url)
if dineHall is "6":
    url = "http://menus.housing.wisc.edu/menus/newells"
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
time = list() #Declares a list
imgTags = soup.find_all("img") #Searches for all the html tags with <img>
#print (imgTags)
for imgTag in imgTags: #Iterates through a 
    imgDicts.append(imgTag.attrs) #Adding each img tag attribute to the declared dictionary
    if len(imgTag.contents) <= 0: 
        continue
    else :
        time.append(imgTag.contents) 

        
        
#print (imgDicts)
for dict in imgDicts:
    for key,value in dict.items():
        if key == 'title':
            print (dict[key])

print (time[0][0].strip())

if not time[0][0].strip() :             
    print ("Go eat at Chipotle you health freak!")
            
#WORKS: Prints out the food availabe for the day
#UPGRADE: Make this into a method so that it can be reused.
print ("==================================FOOD AVAILABLE================================")
#driver = webdriver.Chrome()
#driver.get("http://menus.housing.wisc.edu/menus/")
#nutriUrl = "http://dining.housing.wisc.edu/NetNutrition/1"
#driver.find_element_by_xpath('//*[@id="bean-and-creamery"]/p/i').click()
ptags = soup.find_all("div", { "class" : "rest_line_indent pointer moreButton" })
ptag = ""



if ptags is []:
    ptag = ""
else :
    for ptag in ptags:
        if ptag:
            problemTag = ptag.contents[0].contents[0] #problem hidden NOT FIXED
        else:
            continue


mydivs = soup.find_all("div", { "class" : "rest_line_indent" }) #this line parse through finding the particular class in the div tag 
for food in mydivs:
    if not food:
        print ("ERROR: PROBLEM TAG IS ACCESSED") #this skips the problem tag FIXME: Need to access the drop down list from the website
    if food :
        if food is ptag:
            print (ptag.contents[0].contents[0])
        else :
            print (food.contents[0])
    else:
        print ("BIG ERROR: UNKNOWN")
    
        
       
       
print ("==================================SEPERATION================================")




#Using Selenium to click on the drop down list from down here
#PART 2 OF THE CODE: NETNUTRITION

#driver = webdriver.Chrome()
#driver.implicitly_wait(30)
#driver.get("http://dining.housing.wisc.edu/NetNutrition/1")
#nutriUrl = "http://dining.housing.wisc.edu/NetNutrition/1"
#if dineHall is "1":
#    driver.find_element_by_xpath('//*[@id="unitsPanel"]/div/table/tbody/tr[3]/td/a').click() #enter's Gordon's
 #   driver.find_element_by_xpath('//*[@id="childUnitsPanel"]/div/table/tbody/tr/td/a').click() #enter Great Greens
  #  #driver.find_element_by_xpath('//*[@id="childUnitsPanel"]/div/table/tbody/tr/td[0]/a').click() #enter Great Greens Selections







              



        
    

        
     

