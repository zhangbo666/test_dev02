__author__ = 'zhangbo'


import requests
import json


url = 'https://api.github.com/some/endpoint'

payload = {'some':'data'}

r = requests.post(url,data=payload)

print (r.text)


# url = 'http://httpbin.org/post'
#
# payload = {"key1":"value1","key2":"value2"}
#
# r = requests.post(url,json=payload)
#
# print (r.text)
