import requests
import json 

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
        print("Direction inputed:", direction)
        if direction == "n":
            data={"direction": "n"}
        if direction == "s":
            data={"direction": "s"}
        if direction == "e":
            data={"direction": "e"}
        if direction == "w":
            data={"direction": "w"}
        res=requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=json.dumps(data)
        )

        nextRoom=json.loads(res.text)
        self.currentRoom=nextRoom
        print(nextRoom, "Here is our new room")

    def init(self):
        res=requests.get(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers
        )
        nextRoom=json.loads(res.text)
        self.currentRoom=nextRoom
        print(nextRoom, "Here is our response")
        