from TweetClass import Tweet

def TweetObj_from_StatusList(tweet_list, search_term, status_list):
    ## create tweet object for each status and save to a list of tweets
    print "creating tweet objects from status list"
    wait_dots = '.'
    print "working\n", wait_dots
    for entry in status_list:
        wait_dots = wait_dots + wait_dots
        print wait_dots
        tweet_list.append(Tweet(search_term, entry))
    return tweet_list
#call from TweetObj_from_StatusList(keyword_output['statuses']) 

##for debugging
#for tweet in tweet_list:
#    tweet.display_all() 
