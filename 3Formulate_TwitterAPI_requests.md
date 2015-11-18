# Guide to Formulating Twitter API requests
By sarahd @behaviordots
Part of the @curiositybits collective http://www.curiositybits.org/

Video Tutorial for this Guide: XX

Koding VM at: https://koding.com/
Previous Python_DataMining_StepByStep:
*   https://github.com/SyraD/Python_DataMining_StepByStep/blob/master/1KodingVM_setup.md
*   https://github.com/SyraD/Python_DataMining_StepByStep/blob/master/2Passwords_toTwitter_Data

Copy and paste the following lines of code after user: into the terminal of the Koding VM.


Create a new file in the PyCodes folder: /home/yourUserName/PyCodes/ 
named APItests.py and paste in the below code:

````
## authenticate with Twitter via Twitter module

import sys

#adds Imports folder to 0th position of sys.path list
#temp & local to file 
sys.path.insert(0, './Imports') 
print sys.path

#import all variables stored in Imports/Keys.py 
from Keys import * 

auth = twitter.oauth.OAuth(oauth_token, oauth_token_secret,
                             app_key, app_secret)
twitter_api = twitter.Twitter(auth=auth)
print twitter_api, 'you have authentication!'

````


In the terminal, navigate to the PyCodes folder:
````
user: ~ $ cd PyCodes
```
You should see:

````
user: ~/PyCodes $  

````

Run the APItests.py python code using terminal.
````
user: ~/PyCodes $  python APItests.py
````

The code should print out something that looks like:
````
user: ~/PyCodes $ <twitter.api.Twitter object at 0x0000000009325EF8> you have authentication!
````
##Formulating requests to the Twitter API in Python with the Twitter Module 

For a FULL list of the ways to interact with the Twitter API go to:
https://dev.twitter.com/rest/public

Formulating requests in the twitter module is aligned with the twitter.com documentation format. However, the "/" changes to a ".". Then, the necessary parameters can be specified in parentheses.

Some examples:
![alt text](https://github.com/SyraD/Python_DataMining_StepByStep/blob/master/Images_storage/API_Examples.jpg "Photo")

## Testing the Examples
Open APItests.py and add these lines at the end:

````
# indicated by the screen_name or user_id parameters.
print twitter_api.statuses.user_timeline(screen_name = 'behaviordots', count = 1)

#Returns a collection of the most recent Tweets and 
#retweets posted by the authenticating user and the users they follow.
print twitter_api.statuses.home_timeline(count = 1)

#Returns the most recent tweets authored by the authenticating user 
print twitter_api.statuses.retweets_of_me(count = 1)
 
 
````
