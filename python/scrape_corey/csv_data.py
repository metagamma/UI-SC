#from requests_html import HTML
# 
# with open('simple.html') as html_file:
#     source = html_file.read()
#     html = HTML(html=source)
#     html.render()
# 
# match = html.find('#footer', first = True)
# print(match.html)

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

#articles = html.find('div.article')
#for article in articles:
#    headline = article.find('h2', first=True).text
#    summary = article.find('p', first=True).text
#    print(headline)
#    print(summary+'\n')

###########################################3

#import csv
#from requests_html import HTML, HTMLSession

#csv_file = open('cms_scrape.csv', 'w')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['headline', 'summary', 'video'])

#session = HTMLSession()
#r = session.get('https://coreyms.com/')


# for link in r.html.absolute_links:
# for link in r.html.links:
#   print(link)

# print(r.html)

# article = r.html.find('article', first=True)
# print(article)

#articles = r.html.find('article')

#for article in articles:
#    headline = article.find('.entry-title-link', first=True).text
 #   print(headline + "\n")

 #   summary = article.find('div.entry-content', first=True).text
#    print(summary + "\n")

    # vid_src = article.find('iframe', first=True)
    # print(vid_src.html)
    # print(vid_src.attrs['src'])

 #   try:
#        vid_src = article.find('iframe', first=True).attrs['src']
        # print(vid_src)
#        vid_id = vid_src.split('/')[4]
#        vid_id = vid_id.split('?')[0]
#        yt_link = f'https://youtube.com/watch?v={vid_id}'
#    except Exception as identifier:
#        yt_link = None

#    print(yt_link, '\n')
#    csv_writer.writerow([headline, summary, yt_link])

#csv_file.close()

import csv
from requests_html import HTML, HTMLSession

csv_file = open('mercantil_farmacias.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Nombre Farmacia', 'Razon Social', 'Rut', 'Direccion (Street Adress)', 'Direccion (Comuna)', 'Direccion (Ciudad)', 'Telefono-1', 'Telefono-2', 'Sitio Web', 'Tamaño Empresa', 'Numero de Trabajadores'])

s = HTMLSession()
r = s.get('https://www.mercantil.com/farmacias/836/')

r.html.render(timeout=20)

companies = r.html.xpath('//*[@id="list_empresas"]',first=True)

for comapany in companies.absolute_links:
    print(comapany)


csv_file.close()