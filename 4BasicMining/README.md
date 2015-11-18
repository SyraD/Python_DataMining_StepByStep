# Basic Mining Scripts Tutorial
By sarahd@behaviordots

Part of the @curiositybits collective http://www.curiositybits.org/

These 'Basic Scripts' are designed to create a fundamental outline for datamining Twitter in Python that can be built on to customize or add complexity.

Video Tutorial for this Guide: COMING SOON

## Koding VM set-up
The first four steps will go through setting up a Koding VM. SKIP 1-4 if you have already completed the previous three tutorials:
*    https://github.com/SyraD/Python_DataMining_StepByStep/blob/master/1KodingVM_setup.md 
*    https://github.com/SyraD/Python_DataMining_StepByStep/blob/master/2Passwords_to_TwitterData.md
*    https://github.com/SyraD/Python_DataMining_StepByStep/blob/master/3Formulate_TwitterAPI_requests.md

The Basic Mining Script Tutorial is intended to be followed in the Koding VM environment. If you have a preferred python coding environment, you can follow the general outline but will need to take additional steps to setup a SQLite database. 
The following slides will be helpful: http://www.slideshare.net/cosmopolitanvan/curiosity-bits-tutorial-mining-twitter-user-profile-v2

## Getting Started:
Start-up the Koding VM. 
Copy and paste the following lines of code after ‘user: ~ $ ‘ into the terminal of the Koding VM.
## 1. Install pip package manager for python
http://learn.koding.com/guides/getting-started-python/

```
user: ~ $ kpm install pip

```

## 2. Install python developers
http://learn.koding.com/guides/getting-started-python/


```
user: ~ $ sudo apt-get install python-dev

```

## 3. Easy_install setup
https://pypi.python.org/pypi/setuptools

"The script will download the appropriate version and install it for you:"

```
user: ~ $ sudo su
root: wget https://bootstrap.pypa.io/ez_setup.py -O - | python
root: wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
root: wget https://bootstrap.pypa.io/ez_setup.py -O - | python - --user

```

## 4. Install libmysqlclient from python developer

```
root: apt-get install libmysqlclient-dev

```
Control + D to exit root.

## 5. Install dataset: databases for lazy people and Twython for accessing Twitter APIs in Python.
http://dataset.readthedocs.org/en/latest/quickstart.html


```
user: ~ $ sudo pip install dataset twython
```

#6. Fetch Code
Create a new folder called PyCodes 
````
user: ~/ mkdir PyCodes
````
Go into the PyCodes folder and download zip file of code. 
````
user: ~/ cd PyCodes
user: ~/ Pycodes $ wget 'https://github.com/SyraD/DataMining_Python_Scripts/archive/master.zip'
user: ~/ Pycodes $ unzip master.zip -d DownloadedCode

````
Use the folder view to navigate to the BasicMiningScripts and move out to PyCodes. 
Delete DownloadedCode folder and masterscript if you like.

#7.
Modify the Keys.py file with your keys.

#8. naviate to the folder with the code
```
user: ~/ Pycodes $ cd BasicMiningScripts

```

#9.  run the 'Run This' code

```
user: ~/ Pycodes/BasicMiningScripts $ python RunThis.py

```
You will see something similar to:
````
GRABBED:  4 statuses****
max_id VALUE USED FOR THIS GRAB--> None
returned twitter response as  <type 'dict'>  for keyword:  behaviordots
creating tweet objects from status list
working
.
..
....
........
................
[<TweetClass.Tweet instance at 0x7f9c1f6fd998>, <TweetClass.Tweet instance at 0x7f9c1f6d42d8>, <TweetClass.Tweet instance at 0x7f9c1f6d432
0>, <TweetClass.Tweet instance at 0x7f9c1f6d4368>]
Tweets in your sqlite database

````

#10. 
Install SQLite3 and developers dependencies.
````
user: ~/ sudo apt-get install sqlite3 libsqlite3-dev
````
#11. View data

In the folder view you will see a file called BasicTweet1.db.
This is our output data. To view we will open SQLite.

```
user: ~/ Pycodes/BasicMiningScripts $ sqlite3 BasicTweet1.db
sqlite> .tables
Tweet
sqlite> SELECT * FROM Tweet;
````
The data will print out. 

There are multiple viewing modes to choose from:
mode should be one of: column csv html insert line list tabs tcl
.mode column

Change mode to view clearer:
````
sqlite> .mode line
sqlite> SELECT * FROM Tweet;
````
The output will be similar to:
````
sqlite> SELECT * FROM Tweet;
           id = 1
   searchTerm = behaviordots
         text = RT @mixtrak: First post on my new science blog: learning #Git, #GitHub, and #RStudio: https://t.co/VCHu9rkpoB #ResBaz #ope
nscience
retweet_count = 6
    fav_count = 0
      tweetID = 666765847453650945
 
           id = 2
   searchTerm = behaviordots
         text = "The right to read is the right to mine". Library contracts for #scraping  https://t.co/LgXldgpsbL by @Kalendaries   https
://t.co/JNxJOm6lJU
retweet_count = 0
    fav_count = 0
      tweetID = 666763165754073090
 
           id = 3
   searchTerm = behaviordots
         text = RT @gregorysaxton: Analyzing #BigData for non-coders,  Ch. 8: Logit Regression
http://t.co/WzlN7DynQY #Python #PANDAS http://t.co/oAmf204C19
retweet_count = 2
    fav_count = 0
      tweetID = 666741840654295040
 
           id = 4
   searchTerm = behaviordots
         text = RT @CodementorIO: How to Get Your #Dev Environment Set Up Before You Finish Your Coffee https://t.co/KuhWt6rLQN #Ubuntu #L
inux https://t.co
retweet_count = 2
    fav_count = 0
      tweetID = 666663394938904576
````
