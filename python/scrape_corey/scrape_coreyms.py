import csv
from requests_html import HTML, HTMLSession

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video'])

session = HTMLSession()
r = session.get('https://coreyms.com/')


# for link in r.html.absolute_links:
# for link in r.html.links:
#   print(link)

# print(r.html)

# article = r.html.find('article', first=True)
# print(article)

articles = r.html.find('article')

for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    print(headline + "\n")

    summary = article.find('div.entry-content', first=True).text
    print(summary + "\n")

    # vid_src = article.find('iframe', first=True)
    # print(vid_src.html)
    # print(vid_src.attrs['src'])

    try:
        vid_src = article.find('iframe', first=True).attrs['src']
        # print(vid_src)
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as identifier:
        yt_link = None

    print(yt_link, '\n')
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()




