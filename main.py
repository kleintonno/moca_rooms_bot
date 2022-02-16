from ctypes import addressof
import time
import pickle

from pprint import pprint
from config import *
from twitter import *
from func import *


#load cache
try:
    auction_cache = pickle.load(open("cache", "rb"))
except:
    print("no cache file")
    auction_cache = get_data()
    pickle.dump(auction_cache, open("cache", "wb"))
try:
    auction_tweet_id = pickle.load(open("last_tweet", "rb"))
except:
    print("no tweet_id")
    auction_tweet_id = handle_new_auction(auction_cache)
    pickle.dump(auction_tweet_id, open("last_tweet", "wb"))


if __name__ == "__main__":
    while True:
        time.sleep(30)
        print("query data")
        last_auction_data = get_data()
        print("received data from subgraph")
        if last_auction_data['id'] > auction_cache['id']:
            auction_tweet_id = handle_new_auction(auction_cache)
            auction_cache = last_auction_data
            pickle.dump(auction_cache, open("cache", "wb"))
            pickle.dump(auction_tweet_id, open("last_tweet", "wb"))
            print("new auction started")




        elif last_auction_data['bid_id'] != auction_cache['bid_id']:
            auction_cache = last_auction_data
            auction_tweet_id = handle_new_bid(auction_cache, auction_tweet_id._json['id_str'])
            pickle.dump(auction_cache, open("cache", "wb"))
            pickle.dump(auction_tweet_id, open("last_tweet", "wb"))
            print("new bid")



