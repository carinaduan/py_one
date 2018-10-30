#coding=utf-8
import requests

# r = requests.get('https://api.github.com/events')

# print r.url
# print r.text
# print r.content
# print r.json()
# print r.encoding
# print r.headers
# print r.headers['Content-Type']
# print r.headers.get('content-type')

#获取页面内容
jar = requests.cookies.RequestsCookieJar()
jar.set('JSESSIONID', 'A7419CF888087A46606D92754E59B90F', domain='admin.pptvyun.com', path='/')
url = 'http://admin.pptvyun.com/user/list'
r = requests.get(url, cookies=jar)
print r.content