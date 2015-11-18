## Tweet class
class Tweet:
   'Common base class for all Tweets'

   def __init__(self, search_term, tweet_json):
      self.searchTerm = search_term
      self.tweetID = tweet_json[u'id']
      self.text = tweet_json[u'text'].encode('ascii', 'ignore')
      self.retweet_count = tweet_json[u'retweet_count']
      self.fav_count = tweet_json[u'favorite_count']
      self.entities_list = tweet_json[u'entities']
      self.url_list = tweet_json[u'entities'][u'urls']
      self. hashtag_list =  tweet_json[u'entities'][u'hashtags']
      self.mentions_list = tweet_json[u'entities'][u'user_mentions']
      self.coordinates = tweet_json[u'coordinates']
        
   def display_all(self):
      print "\nsearched: ", self.searchTerm,"\nFound:", self.text, '\n     RT: ', self.retweet_count, 'Fav: ', self.fav_count 

   
   def table_attributes(self):
      return dict(searchTerm= str(self.searchTerm), tweetID = self.tweetID, text = self.text, 
                 retweet_count =self.retweet_count,fav_count = self.fav_count)
 
    ## TODO - create url, entities, hashtags, mentions, and coordinate factories
        