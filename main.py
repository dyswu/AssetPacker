# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:04:11 2024

Generate DB to store files

@author: derew
"""


import pandas as pd
import hashlib
from tkinter.filedialog import askopenfilename
import databases.py

from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
    
fileName = ""
file_df = pd.DataFrame(index = databases.file_columns)
tag_df = pd.DataFrame(index = databases.tag_columns)
package_df = pd.DataFrame(index = databases.package_columns)

#Get hash value of file
def md5(file_name):
    m = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            m.update(chunk)
        return m.hexdigest()
    
print("hello")

#Add file to database
def inputFile(path):
    #TODO
    print("Adding file to DB")
    
#Check to see if file already exists in database or not    
def checkFile(file):
    #TODO
    print("check file") 

#Create folders

#Add file to DB
def addFile():
    print("select file to add")
    path = askopenfilename()
    file_name = path.split("/")[-1]
    key = (md5(path))
    #TODO Check existing file
    #If yes -> file preview, ELSE
    #TODO Ask for tags
    #Add to existing project -> File name (new or updated)
    #Get date
    #If update -> get old id, set old next to key
    #Save changes in db
    databases.saveData()

if load:
    file_df, tag_df, package_df, fileName = databases.loadData()
    

def resetData():
    file_df = pd.DataFrame(Data = None, index = databases.file_columns)
    tag_df = pd.DataFrame(Data = None, index = databases.tag_columns)
    package_df = pd.DataFrame(Data = None, index = databases.package_columns)
    fileName = ""
 