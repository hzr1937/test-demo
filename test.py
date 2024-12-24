import requests
# honey
url='https://test.tanka.ai/getusername'
url2='https://test.shanda.com/getusername'
response=requests.get(url)
print(response.text)
