# Importing BeautifulSoup and other important imbraries
from bs4 import BeautifulSoup
import urllib.request
import re

# Url of what we need to scrape
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

# Connecting to the website using urllib

#page = urllib.request.urlopen(url)

# If we entered the wrong url then urllib will throw an error
# So we will wrap this in a try-except statement

try:
    page = urllib.request.urlopen(url)
except:
    print("An error occoured")

# Now we know that BeautifulSoup parses the page
# Parsing the html page

soup = BeautifulSoup(page, "html.parser")
#print(soup) # Gives the html code of the page *Obviously*

# Finding specific elements on the page

regex = re.compile('^tocsection-')

# .find_all method finds all the elements with that attribute
content_lis = soup.find_all('li', attrs={'class': regex})

# print(content_lis)

# Getting the text we can use the `getText` method
content = [] # List compresnion -> [li.getText().split('\n')[0] for li in content_lis]
for li in content_lis:
    content.append(li.getText().split('\n')[0])


# Getting the data from "see also" section
see_also_section = soup.find('div', attrs={'class':'div-col', 'style':'column-width: 20em;'})
see_also_soup = see_also_section.find_all('li')
# print(see_also_soup)

# Extracting the links(hrefs) and the text
see_also = []
for li in see_also_soup:
    a_tag = li.find('a', href=True, attrs={'title':True, 'class':False}) # Finds `a` tags that have title and class
    href = a_tag['href'] # Get the hr attribute
    text = a_tag.getText() # Get the text
    see_also.append([href, text]) # Appending to list see_also

# print(see_also)


######
# Saving data
######

# Saving the content section into a text file
with open('basics/saved_data/content.txt', 'w') as f:
    for i in content:
        f.write(i+"\n")

# Saving the see_also data in a csv as it has two columns(href, text)
with open('basics/saved_data/see_also.csv', 'w') as f:
    for i in see_also:
        f.write(','.join(i)+"\n")
        
