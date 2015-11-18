# Guide to Setting Up The Koding VM for Python
By sarahd@behaviordots

Part of the @curiositybits collective http://www.curiositybits.org/

##Video Tutorial for this Guide: COMING SOON
##Koding VM at: https://koding.com/

### Why Use A Koding VM?
A Koding Virtual Machine runs the Linux Ubuntu 14.04 operating system through the Amazon cloud, providing a friendly environment for coding (https://koding.com/Features). The Koding VM is used here primarily to establish a consistent environment so that following the steps below and on future tutorials @behaviordots will produce the same results 100% of the time. There is no need to modify the steps based on your home computer. Additionally, since you will essentially be working on Linux, the lessons learned through the Koding VM can be transferred to a professional-grade installed Linux system. 
A few other reasons for using Koding:
*    Experiment with root access without the risk to destroying your home computer
*     Active and supportive community
*     Real-time collaboration capabilities (http://learn.koding.com/guides/collaboration/)

## Get Started:
These steps are self-contained. Just copy and paste the following lines of code after ‘user: ~ $’ into the terminal of the Koding VM. Some of the steps will have (optional) noting additional resources. 

## 1. Install pip package manager for python
(Optional) more info available from: http://learn.koding.com/guides/getting-started-python/
```
user: ~ $ kpm install pip
```

## 2. Install python header files and a static library development tools, for building Python modules for Linux Ubuntu. 
```
user: ~ $ sudo apt-get install python-dev
```

## 3. Easy_install setup
(Optional) more info available from: https://pypi.python.org/pypi/setuptools
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



