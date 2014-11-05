# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 15:44:34 2014

@author: Samarth Bhargav
"""

from fabric.api import run, sudo

def aptget(command):
    sudo("apt-get {}".format(command))


# Change this to what ever install you are using
pkgmgr = aptget