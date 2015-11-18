# Guide to Gaining Access to Twitter APIs from Python
By sarahd @behaviordots
Part of the @curiositybits collective http://www.curiositybits.org/

Video Tutorial for this Guide: XX

Koding VM at: https://koding.com/
Previous Python_DataMining_StepByStep:
*   https://github.com/SyraD/Python_DataMining_StepByStep/blob/master/1.KodingVM_setup.md

Copy and paste the following lines of code after user: into the terminal of the Koding VM.

## 1. Application authentication is the first prerequisite to access Twitter data. 

Go to https://dev.twitter.com/apps or directly to https://apps.twitter.com/app/new and start an application.  

Follow Step 1 (beginning to minute 1:15) of tutorial video: https://youtu.be/StFowWalJyc, then STOP the video and come back here... okay - you can watch it if you want :)

You will need the:
* consumer key 
* consumer secret 
* access token 
* access token secret

<img src="files/Images_storage/API.jpg" width="600px">

## 2. Create a new folder called PyCodes in your KodingVM at /home/yourUserName/
## 3. Then, create a subfolder called Imports at /home/yourUserName/Imports
## Create a new document 

Paste the text below into the document and customize with your keys and secrets.
````
#REPLACE 'XX' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
app_key='XX'      
app_secret='XX'
oauth_token=XX''
oauth_token_secret='XX'

````
Save the file as Keys.py in the /home/yourUserName/Imports folder.


## 4. Import twitter module for python

```
user: ~ $ sudo pip install twitter

```

## 5. Testing path setup
Create a new file in the PyCodes folder: /home/yourUserName/PyCodes/.

Paste the below code and save it as testPath.py
 ```
import sys

#adds Imports folder to 0th position of sys.path list
#temp & local to file 
sys.path.insert(0, './Imports') 
print sys.path

#import all variables stored in Imports/Keys.py 
from Keys import * 

print app_key, app_secret, oauth_token, oauth_token_secret #variables from Imports/Keys.py 

```

In the terminal, navigate to the PyCodes folder:
````
user: ~ $ cd PyCodes
user: ~/PyCodes $  

````
Run the testPath.py python code.
````
user: ~/PyCodes $  python testPath.py
````
If the code prints out your keys and secrets. You are set up to move on! If not, you have an error in the file locations, names, or path. 

## 6. Testing authentication

Create a new file in the PyCodes folder: /home/yourUserName/PyCodes/ named
basicAuth.py and paste in the below code:

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
Run the basicAuth.py python code using terminal.
````
user: ~/PyCodes $  python basicAuth.py
````

The code should print out something that looks like:
````
user: ~/PyCodes $ <twitter.api.Twitter object at 0x0000000009325EF8> you have authentication!
````