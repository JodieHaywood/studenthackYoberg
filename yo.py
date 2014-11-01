import requests

def yo_all():
  payload = {'api_token': '35d45ae0-6bc0-4782-9374-5404463fccbc'}
  r = requests.post('http://api.justyo.co/yoall/', data=payload)

def yo_all_link(link):
  payload = {'api_token': '35d45ae0-6bc0-4782-9374-5404463fccbc', 'link': link}
  r = requests.post('http://api.justyo.co/yoall/', data=payload)


#Just a simple link test. =D
#yo_all_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ");
