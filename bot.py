import argparse
import json
import markovify
import time
import tweepy

import keys as keys


class Bot:
    def __init__(self, model_name, max_characters=200):
        twitter_auth_keys = {
            "consumer_key": keys.API_KEY,
            "consumer_secret": keys.API_SECRET,
            "access_token": keys.ACCES_TOKEN,
            "access_token_secret": keys.ACCES_TOKEN_SECRET
        }
        auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
        )
        auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
        )
        self._api = tweepy.API(auth)

        self._model = markovify.Text.from_json(json.load(open('./{}.json'.format(model_name), 'r')))
        self._max_characters = max_characters

    def tweet_from_model(self):
        text = self._generate_from_model()
        self._tweet(text)

    def _tweet(self, text):
        return self._api.update_status(status=text)

    def _generate_from_model(self):
        return self._model.make_short_sentence(self._max_characters)


def main(args):
    bot = Bot(args.model_name, max_characters=args.max_characters)

    while True:
        print(bot._generate_from_model())
        time.sleep(args.tweet_interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the bot.')
    parser.add_argument('model_name',
                        type=str,
                        help='name of the bot to load')
    parser.add_argument('-mc',
                        '--max_characters',
                        default=200,
                        type=int,
                        help='maximun number of characters of the generated text')
    parser.add_argument('ti',
                        '--tweet_interval',
                        default=21600,
                        type=int,
                        help='interval between tweets in seconds')

    args = parser.parse_args()
    main(parser.parse_args())
