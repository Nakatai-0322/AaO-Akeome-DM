# Copy and paste programming by Nakatai-0322
# Twitter: @Nakatai_0322
# GitHub: Nakatai-0322
# License: MIT License
# Completely non-guaranteed / Irresponsible coding.
import tweepy
import Config

def main():
    auth = tweepy.OAuthHandler(Config.consumer_key, Config.consumer_secret)
    auth.set_access_token(Config.access_token, Config.access_token_secret)
    api = tweepy.API(auth)
    for User in Config.toUsers:
        recipient_id = User
        result = api.send_direct_message(recipient_id=recipient_id, text=Config.message)
        print(result.id)
        print(Config.message)

if __name__ == "__main__":
    main()
