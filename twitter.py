from config import *
import tweepy

authenticator = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
authenticator.set_access_token(twitter_access_token, twitter_access_token_secret)
api = tweepy.API(authenticator, wait_on_rate_limit=True)


def handle_new_auction(auction_data):
    text = f"""
    An auction has started for FLOOR {auction_data['id']}!
    
    Bid at https://app.museumofcryptoart.com/floor-auction
    Learn more at https://museumofcrypto.notion.site/M-C-ROOMs-7e5ff2af1d884f0c95e48a9c091152b3
    """

    return api.update_status_with_media(text, 'images/' + str(auction_data['size']) + '.png')


def handle_new_bid(auction_data, tweet_id):
    text = f"FLOOR {auction_data['id']} has received a bid of Ξ{auction_data['amount']} from {auction_data['bidder']}\nCheck his members pass: {auction_data['memberspass']}"
    return api.update_status(status=text, in_reply_to_status_id=tweet_id)


def handle_auction_end(tweet_id):
    text = "This auction is ending soon! Bid now at https://app.museumofcryptoart.com/floor-auction"
    return api.update_status(status=text, in_reply_to_status_id=tweet_id)
