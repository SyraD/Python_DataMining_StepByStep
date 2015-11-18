#import sys
#sys.path.insert(0, './Imports') #uncomment if using sub-folder Imports to store Keys
from Keys import * #import all variables stored in Imports/Keys.py 

from twython import Twython

twitter_auth = Twython(app_key=app_key,       #REPLACE 'APP_KEY' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
    app_secret=app_secret,
    oauth_token=oauth_token,
    oauth_token_secret=oauth_token_secret)
    