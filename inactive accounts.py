import json
import tweepy
from tweepy.error import RateLimitError, TweepError
import time

def limit_handled(cursor):
    while True:
        try:
            yield next(cursor)
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

with open("config.json") as config:
    config = json.load(config)
    ckey = config["consumer_key"]
    csec = config["consumer_secret"]
    akey = config["access_token_key"]
    asec = config["access_token_secret"]

auth = tweepy.OAuthHandler(ckey, csec)
auth.set_access_token(akey, asec)

api = tweepy.API(auth)

#user = api.get_user('ericscroggins6')

with open("accounts.txt") as accounts:
    for account in accounts:
        try:
            user = api.get_user(account)
            print(user.screen_name)
        except TweepError as e:

            if e.reason == "[{\'code\': 63, \'message\': \'User has been suspended.\'}]":
                print("suspended - " + account)
            elif e.reason == "[{\'code\': 50, \'message\': \'User not found.\'}]":
                print("Not found - " + account)
            else:
                print(str(e), account)




