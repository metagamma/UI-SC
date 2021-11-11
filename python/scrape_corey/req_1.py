import requests

#payload_get = {'page': 2, 'count': 25}
payload = {'username': 'corey', 'password': 'testing'}

# r = requests.get('https://scx1.b-cdn.net/csz/news/800/2020/newconstrain.jpg')
# r = requests.post('https://httpbin.org/get', params=payload_get)
# r = requests.post('https://httpbin.org/post', data=payload)
r = requests.get('https://httpbin.org/basic-auth/dante/123',
                 auth=('dante', '123'))

# print(dir(r))
# print(help(r))

# print(r.text)
# print(r.content)

# with open('sample.jpg', 'wb') as f:
#    f.write(r.content)

# print(r.status_code)
# print(r.ok)
# print(r.headers)
# print(r.url)
# r_dict = r.json()
# print(r_dict['form'])
print(r.text)