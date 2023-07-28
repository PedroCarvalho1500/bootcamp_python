import requests


#request_gender = requests.get(url="https://api.genderize.io?name="+name).json()
#request_age = requests.get(url="https://api.agify.io?name="+name).json()
#<h1>{{post["title"]}}</h1>
#<h2>{{post["subtitle"]}}</h2>

class Post:
    def __init__(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body
