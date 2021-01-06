import json
import botometer


with open("config.json") as config:
    config = json.load(config)
    twitter_app_auth = {
        'consumer_key': config["consumer_key"],
        'consumer_secret': config["consumer_secret"],
        'access_token': config["access_token_key"],
        'access_token_secret': config["access_token_secret"],
    }
    rap = config["rapidapi_key"]


bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rap,
                          **twitter_app_auth)

accounts = ['@BanWhale', '@kirby1997', '@slayterchrist', "@pilscoop"]
for screen_name, result in bom.check_accounts_in(accounts):
    print(screen_name)
    print(result)