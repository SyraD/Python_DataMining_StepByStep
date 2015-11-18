def get_data_search(twitter_auth, search_keyword, tweets_toGather, max_id=None):
    try:
        '''
        NOTES FROM https://dev.twitter.com/docs/api/1.1/get/search/tweets 
        'count' = 'The number of tweets to return per page, up to a maximum of 100 per request. Defaults to 15.' 
         'result_type' options:
              * mixed: Include both popular and real time results in the response.
              * recent: return only the most recent results in the response
              * popular: return only the most popular results in the response.
        https://dev.twitter.com/docs/api/1.1/get/search/tweets
        '''
        twitter_dictResponse = twitter_auth.search(q=search_keyword, count = tweets_toGather, result_type = 'recent') 
        
    except Exception, e:
        print "Error reading id %s, exception: %s" % (search_keyword, e)
        return None
        
    print "GRABBED: ", len(twitter_dictResponse['statuses']), "statuses****"
    print "max_id VALUE USED FOR THIS GRAB-->", max_id
    print "returned twitter response as ", type(twitter_dictResponse)," for keyword: ", search_keyword
    return search_keyword, twitter_dictResponse