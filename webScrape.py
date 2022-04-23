#Project - Web Scraping
# import requests
# from bs4 import BeautifulSoup
# import pprint
#
# res = requests.get("https://news.ycombinator.com/news")
# #print(res) #Prints response code
# #print(res.text) #Prints entire html content in str format
# bsoup = BeautifulSoup(res.text, 'html.parser')
# #prints the html content
# #print(bsoup)
# #prints only body
# #print(bsoup.body)
# #prints the body content in a list format
# #print(bsoup.body.contents)
# #prints all div tags
# #print(bsoup.find_all('div'))
# #Find all <a> tags
# #print(bsoup.find_all('a'))
# #Prints the title tag
# #print(bsoup.title)
# #Prints the first <a> tag
# #print(bsoup.a)
# #Another method to find the first <a> tag
# #print(bsoup.find('a'))
# #Prints all the tags with class='score'
# #print(bsoup.select('.score'))
# #prints the specific score tag
# #print(bsoup.select('#score_31065143'))
#
# '''
# #Goal - to get the list of titles with more than 100 votes
# Go to hackernews, right click the title and click inspect -- get the variable name (titlelink)
#     right click the vote -- get the variable name (class=score)
# '''
links = bsoup.select('.titlelink')
#votes = bsoup.select('.score')
#print to get only the top most record
#votes = bsoup.select('.score')[0]
#print(votes)
subtext = bsoup.select('.subtext')

def sort_stories_by_votes(hndict):
    return sorted(hndict, key=lambda k:k['votes'], reverse=True)

def create_custom_hackernews(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        votes = subtext[idx].select('.score')
        #print(votes)
        if len(votes):
            #points = votes[0].getText()
            points = int(votes[0].getText().replace(' points', ''))
            #print(points)

            if points > 99:
                hn.append({'title': title, 'href': href, 'votes': points})
    return (sort_stories_by_votes(hn))


#Use pretty print to format the output
pprint.pprint(create_custom_hackernews(links,subtext))
