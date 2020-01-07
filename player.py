import requests

jamie_api_key= 'Token 6b056b046e07f644c8a86d42fb659a70821439c2'

headers = {
    'Authorization': jamie_api_key,
    'Content-Type': 'application/json'
}

class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
    def travel(self, direction):
        print("travel")
    def init(self):
        res=requests.get(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers
        )
        print(res.text, "Here is our response")