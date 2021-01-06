import json


with open("config.json") as config:
    config = json.load(config)
    ckey = config["consumer_key"]
    csec = config["consumer_secret"]
    akey = config["access_token_key"]
    asec = config["access_token_secret"]
    wsIP = config["wsIP"]
    wsPort = config["wsPort"]
    twitacc = config["twitacc"]
    disckey = config["disckey"]