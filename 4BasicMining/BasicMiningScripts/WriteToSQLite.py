import dataset

#as transaction called tx, commits once all tweets inserted to tx
def toSQL(tweet_list):
    with dataset.connect('sqlite:///BasicTweet1.db') as tx:
        try:
            tx.begin()
            for tweet in tweet_list:
                tx['Tweet'].insert(tweet.table_attributes()) 
            tx.commit()
            print "Tweets in your sqlite database"
        except Exception, e:
            print "Error in uploading to sq, exception: %s" % (e)
            tx.rollback() #discard additions