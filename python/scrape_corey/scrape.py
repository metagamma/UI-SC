from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()

match = html.find('#footer', first = True)
print(match.html)

# print(html.html)
# print(html.text)

# match = html.find('title')
# print(match)
# print(match[0])
# print(match[0].html)
# print(match[0].text)

# match = html.find('title', first=True) # same
# match = html.find('#footer', first=True)
# print(match.text)

# article = html.find('div.article', first=True)
# print(article.text)

# headline = article.find('h2', first=True)
# summary = article.find('p', first=True)
# headline = article.find('h2', first=True).text
# summary = article.find('p', first=True).text

articles = html.find('div.article')
for article in articles:
    headline = article.find('h2', first=True).text
    summary = article.find('p', first=True).text
    print(headline)
    print(summary+'\n')
