import requests
import json 
import time

bryce_api_key= 'Token bb4910f9cec94810c3f792f382142798869e311a'

headers = {
    'Authorization': bryce_api_key,
    'Content-Type': 'application/json'
}

class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
    def travel(self, direction):
        print("Direction", direction)
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

    def pilfer(self):
        if len(self.currentRoom['items']) > 0:
            data={"name": "treasure"}
            res=requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', headers=headers, data=json.dumps(data)
            )

    def drop(self):
        data={"name": "treasure"}
        res=requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/', headers=headers, data=json.dumps(data)
        )
        print("-------", res.text, "DROPPING TREASURE")

    def status(self):
        res=requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', headers=headers
            )
        print("-------------------------------STATUS-------------------------------------", json.loads(res.text))
        
    def sell(self):
        data1={"name": "treasure"}
        res=requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', headers=headers, data=json.dumps(data1)
        )
        print("-------", res.text, "SELLING MY TREASURE")
        time.sleep(5)
        data2={"name": "treasure", "confirm": "yes"}
        res=requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', headers=headers, data=json.dumps(data2)
        )

    def name_change(self):
        data1={"name":"[Laird James Edgar Goodnight III]"}
        res=requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/', headers=headers, data=json.dumps(data1)
        )
        print("--------", res.text, "NAME CHANGE")
        time.sleep(35)
        data2={"name":"[Laird James Edgar Goodnight III]", "confirm": "aye"}
        res=requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/', headers=headers, data=json.dumps(data2)
        )
        print("--------", res.text, "NAME CHANGE")




        