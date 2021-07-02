
# !pip install requests
import requests
from urllib.request import urlopen
import pickle
from bs4 import BeautifulSoup
home_url = 'https://te.wikipedia.org/'
links = ['https://te.wikipedia.org/w/index.php?title=%E0%B0%AA%E0%B1%8D%E0%B0%B0%E0%B0%A4%E0%B1%8D%E0%B0%AF%E0%B1%87%E0%B0%95:%E0%B0%85%E0%B0%A8%E0%B1%8D%E0%B0%A8%E0%B0%BF%E0%B0%AA%E0%B1%87%E0%B0%9C%E0%B1%80%E0%B0%B2%E0%B1%81&from=2014+%E0%B0%86%E0%B0%82%E0%B0%A7%E0%B1%8D%E0%B0%B0%E0%B0%AA%E0%B1%8D%E0%B0%B0%E0%B0%A6%E0%B1%87%E0%B0%B6%E0%B1%8D+%E0%B0%B8%E0%B0%BE%E0%B0%B0%E0%B1%8D%E0%B0%B5%E0%B0%A4%E0%B1%8D%E0%B0%B0%E0%B0%BF%E0%B0%95+%E0%B0%8E%E0%B0%A8%E0%B1%8D%E0%B0%A8%E0%B0%BF%E0%B0%95%E0%B0%B2%E0%B1%81']

all_links = []

# Main code
prev_len = 0
for link in links:    
    counter = 0    
    while link:
        counter = counter + 1
        if (counter==4):
          break
        html_doc = ''
        with urlopen(link) as response:
            for line in response:
                line = line.decode('utf-8')
                html_doc = html_doc + line.replace('\n','')
            soup = BeautifulSoup(html_doc, 'html.parser')
            div = soup.find('div',{'class':'mw-allpages-body'})
            if div:
                anchors = div.find_all('a');
                all_links = all_links + [home_url + anchor['href'] for anchor in anchors]
                # print(len(set(all_links)))
            if prev_len == len(set(all_links)):
                break
            nav_div = soup.find('div',{'class':'mw-allpages-nav'})
            if nav_div and len(nav_div.find_all('a')) == 2:
                link = home_url + nav_div.find_all('a')[1]['href']
            prev_len = len(set(all_links))

for link in all_links:
  print(link)

print("Number of article links available: ")
print(len(all_links))

"""## Extracting text """

import requests
from bs4 import BeautifulSoup

# select which articles you want from the list

# first 280 articles give approximately 10k sentences

url_list = all_links[:280]
# print("List of articles: ")
print("Extracting data..............")
for i in url_list:
  url = i
#   print(i)
  # ping a website or portal for information
  res = requests.get(url)
  html_page = res.content

  soup = BeautifulSoup(html_page, 'html.parser')
  # Python library that is used for web scraping purposes to pull the data out of HTML and XML files
  text = soup.find_all(text=True)

  output = ''
  extractlist = [
      'p',
      'h1',
      'h2',
      'h3',
      'h4',
      'h5',
      'h6',
      'b',
      'a'
  ]

  for t in text:
      if t.parent.name in extractlist:
          output += '{} '.format(t)
    
  # print(output)
  f = open("text.txt", "a")
  f.write(output)
  f.close()
