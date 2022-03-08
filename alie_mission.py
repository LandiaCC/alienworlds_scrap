# 0xBea8302e8b0F8d4ee45f7CA9161C4A2e4f255123
from web3 import Web3, HTTPProvider
import json
import requests


def get_mission_value(mission_id):
    with open("abi_alien.json") as f:
        info_json = json.load(f)

    abi = info_json

    w3 = Web3(HTTPProvider("https://bsc-dataseed.binance.org/"))
    escrow = w3.eth.contract(address='0xBea8302e8b0F8d4ee45f7CA9161C4A2e4f255123', abi=abi)
    return escrow.functions.missions(mission_id).call()

def get_last_mission():
    with open("abi_alien.json") as f:
        info_json = json.load(f)

    abi = info_json

    w3 = Web3(HTTPProvider("https://bsc-dataseed.binance.org/"))
    escrow = w3.eth.contract(address='0xBea8302e8b0F8d4ee45f7CA9161C4A2e4f255123', abi=abi)
    return escrow.functions.missionsCount().call()



def get_info_nft(mission):
    url = 'https://ipfs.io/ipfs/' + ult_mission[9][1]
    r = requests.get(url)
    a = r.text
    return json.loads(a)

ult_mission = get_mission_value(get_last_mission()-1) 
print(get_info_nft(ult_mission))
    



