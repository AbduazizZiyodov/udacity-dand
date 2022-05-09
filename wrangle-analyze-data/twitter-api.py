import rich
import json
import tweepy
import pandas as pd
from os import getenv
from tweepy import OAuthHandler
from timeit import default_timer as timer


consumer_key: str = getenv("CONSUMER_KEY")
access_token: str = getenv("ACCESS_TOKEN")
access_secret: str = getenv("ACCESS_SECRET")
consumer_secret: str = getenv("CONSUMER_SECRET")

JSON_FILE_NAME: str = "tweet_json.txt"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(
    auth,
    wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True,
    parser=tweepy.parsers.JSONParser()
)


def get_tweet_ids(filename: str) -> list:
    return pd.read_csv(filename).tweet_id.values


def fetch_twitter_data() -> None:
    count: int = 0
    fails_dict = {}
    tweet_ids = get_tweet_ids("twitter_archive_enhanced.csv")

    tweets: list = []

    for tweet_id in tweet_ids:
        count += 1
        rich.print(str("[success]")+str(count) + ": " + str(tweet_id))

        try:
            rich.print("[green] SUCCESS!")
            tweets.append(api.get_status(tweet_id))
        except tweepy.TweepError as err:
            rich.print("[red] FAIL!")
            fails_dict[tweet_id] = err
            pass

    open(JSON_FILE_NAME, 'w').write(json.dumps(tweets, indent=4))

    rich.print(f"[yellow] {fails_dict}")


if __name__ == "__main__":
    start = timer()
    fetch_twitter_data()
    rich.print(f"[cyan] {timer() - start}")
