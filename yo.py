import requests

api_key = '35d45ae0-6bc0-4782-9374-5404463fccbc'

def yo_all():
  payload = {'api_token': api_key}
  r = requests.post('http://api.justyo.co/yoall/', data=payload)

def yo_all_link(link):
  payload = {'api_token': api_key, 'link': link}
  r = requests.post('http://api.justyo.co/yoall/', data=payload)


#Just a simple link test. =D
#yo_all_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ");
