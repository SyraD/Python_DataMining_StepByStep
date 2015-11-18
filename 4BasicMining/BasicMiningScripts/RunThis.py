import dataset
from twython import Twython

from WriteToSQLite import *
from CreateTweetObjects import *
from TweetClass import *
from GetData import *

import sys
sys.path.insert(0, './Imports') #adds Imports folder to path
from Auth import twitter_auth #import all variables stored in Imports/Keys.py 


def  main(twitter_auth):
    keyword_output = get_data_search(twitter_auth, 'behaviordots', 4)
    tweet_list = []
    tweet_list = TweetObj_from_StatusList(tweet_list, keyword_output[0] , keyword_output[1]['statuses'])
    print tweet_list
    toSQL(tweet_list)
    
if __name__ == "__main__":
    main(twitter_auth)