# Guide to Setting Up The Koding VM for Python
By sarahd@behaviordots
Part of the @curiositybits collective http://www.curiositybits.org/

Video Tutorial for this Guide: https://youtu.be/_PqqIY_ZhkE

Koding VM at: https://koding.com/

Copy and paste the following lines of code after user: into the terminal of the Koding VM.

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



