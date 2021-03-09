import logging

import tweepy
from latimes.config import LatimesConfiguration, DEFAULT_VALUES
from latimes.latimes import convert_times

from twitter.config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class MentionsListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.user.id == self.me.id:
            return

        if not tweet.text.lower().startswith("@tzconvert"):
            return

        text = tweet.text[len("@tzconvert"):].strip()

        configuration = LatimesConfiguration.from_dict(DEFAULT_VALUES)

        reply = convert_times(
            text,
            configuration
        )

        self.api.update_status(
            status=f"@{tweet.user.screen_name} {reply}",
            in_reply_to_status_id=tweet.id,
        )

    def on_error(self, status):
        logger.error(status)


def main():
    api = create_api()
    tweets_listener = MentionsListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=["@TzConvert"])


if __name__ == "__main__":
    main()
